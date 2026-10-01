#!/usr/bin/env python3
"""Build data/news.json from public RSS search feeds without API keys."""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "data" / "news.json"
USER_AGENT = "PersonalWorkbench/1.0 (+https://github.com/sdwurg180507280211/personal-workbench)"
MAX_PER_CATEGORY = 6
MAX_AGE_HOURS = 72

SOURCES = {
    "财经": "财经 OR 中国经济 OR 金融市场",
    "证券": "证券 OR 证监会 OR 券商",
    "A股": "A股 OR 上证 OR 深证 OR 沪深股市",
    "宏观": "宏观经济 OR 货币政策 OR 财政政策 OR 人民银行",
    "银行": "银行业 OR 商业银行 OR 银行监管",
    "保险": "保险业 OR 保险监管 OR 保险公司",
    "投行": "投行 OR IPO OR 并购 OR 再融资",
    "国际": "全球经济 OR 美联储 OR 欧洲央行 OR 国际财经",
    "时政": "国务院 OR 全国人大 OR 政策发布 OR 时政",
    "考公": "公务员考试 OR 时事政治 OR 国考 OR 省考",
}

WHY = {
    "财经": "用于把握经济、金融市场与重要政策的日常变化。",
    "证券": "关注监管、券商与资本市场制度变化及其市场影响。",
    "A股": "跟踪A股市场的重要事件、政策和主要交易线索。",
    "宏观": "关注增长、通胀、财政与货币政策等宏观变量。",
    "银行": "跟踪银行业监管、经营与重要机构动态。",
    "保险": "跟踪保险监管、产品、机构与行业经营变化。",
    "投行": "关注IPO、并购、再融资及投行业务相关事件。",
    "国际": "关注可能影响全球资产价格与国内市场的国际事件。",
    "时政": "积累国内重要政策与公共事务事实，保留来源与时间。",
    "考公": "用于公务员考试时政积累，优先保留政策与公开事实。",
}

TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")
SOURCE_SUFFIX_RE = re.compile(r"\s+-\s+[^-]{1,45}$")


def clean_text(value: str | None) -> str:
    value = html.unescape(value or "")
    value = TAG_RE.sub(" ", value)
    return SPACE_RE.sub(" ", value).strip()


def canonical_title(title: str) -> str:
    title = SOURCE_SUFFIX_RE.sub("", clean_text(title))
    return re.sub(r"[\W_]+", "", title.lower())


def parse_date(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return datetime.now(timezone.utc)


def google_news_url(query: str) -> str:
    params = urllib.parse.urlencode({
        "q": query,
        "hl": "zh-CN",
        "gl": "CN",
        "ceid": "CN:zh-Hans",
    })
    return f"https://news.google.com/rss/search?{params}"


def fetch_xml(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def item_source(item: ET.Element, title: str) -> str:
    src = clean_text(item.findtext("source"))
    if src:
        return src
    match = re.search(r"\s+-\s+([^-]{1,45})$", title)
    return match.group(1).strip() if match else "Google News"


def make_summary(description: str, title: str) -> str:
    description = clean_text(description)
    if not description or description == title:
        return "点击查看来源报道及完整上下文。"
    if len(description) > 180:
        description = description[:177].rstrip() + "…"
    return description


def fetch_category(category: str, query: str) -> list[dict]:
    root = ET.fromstring(fetch_xml(google_news_url(query)))
    now = datetime.now(timezone.utc)
    results = []
    seen = set()
    for item in root.findall("./channel/item"):
        raw_title = clean_text(item.findtext("title"))
        if not raw_title:
            continue
        key = canonical_title(raw_title)
        if not key or key in seen:
            continue
        published = parse_date(item.findtext("pubDate"))
        age_hours = (now - published).total_seconds() / 3600
        if age_hours > MAX_AGE_HOURS:
            continue
        seen.add(key)
        title = SOURCE_SUFFIX_RE.sub("", raw_title).strip()
        link = clean_text(item.findtext("link"))
        source = item_source(item, raw_title)
        summary = make_summary(item.findtext("description") or "", title)
        results.append({
            "id": hashlib.sha1(f"{category}|{title}|{link}".encode("utf-8")).hexdigest()[:16],
            "category": category,
            "title": title,
            "summary": summary,
            "why": WHY[category],
            "source": source,
            "url": link,
            "publishedAt": published.isoformat().replace("+00:00", "Z"),
        })
        if len(results) >= MAX_PER_CATEGORY:
            break
    return results


def dedupe(items: list[dict]) -> list[dict]:
    output = []
    seen = set()
    for item in sorted(items, key=lambda x: x["publishedAt"], reverse=True):
        key = canonical_title(item["title"])
        if key in seen:
            continue
        seen.add(key)
        output.append(item)
    return output


def main() -> int:
    all_items = []
    errors = []
    for category, query in SOURCES.items():
        try:
            all_items.extend(fetch_category(category, query))
        except Exception as exc:
            errors.append(f"{category}: {exc}")
        time.sleep(0.25)

    items = dedupe(all_items)
    if not items:
        print("No news fetched; keeping existing data/news.json", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    payload = {
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "provider": "Google News RSS",
        "note": "标题、摘要与来源来自公开RSS聚合；链接可能先经过Google News跳转。",
        "errors": errors,
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} items to {OUT}")
    if errors:
        print("Partial source errors:", *errors, sep="\n- ", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
