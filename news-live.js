(function () {
  var liveNewsMeta = { status: 'loading', generatedAt: '', provider: '', note: '' };

  function fmtWhen(value) {
    if (!value) return '';
    var d = new Date(value);
    if (Number.isNaN(d.getTime())) return '';
    var now = new Date();
    var sameDay = d.toDateString() === now.toDateString();
    return new Intl.DateTimeFormat('zh-CN', sameDay
      ? { hour: '2-digit', minute: '2-digit', hour12: false }
      : { month: 'numeric', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false }
    ).format(d);
  }

  function normalize(item, index) {
    return {
      id: item.id || ('live-' + index),
      category: item.category || '财经',
      title: item.title || '未命名报道',
      summary: item.summary || '点击查看来源报道及完整上下文。',
      why: item.why || '用于补充今日信息判断。',
      source: item.source || '公开来源',
      url: item.url || '',
      time: fmtWhen(item.publishedAt),
      publishedAt: item.publishedAt || ''
    };
  }

  function statusLine() {
    if (liveNewsMeta.status === 'live') {
      return '实时数据 · 更新于 ' + fmtWhen(liveNewsMeta.generatedAt) + ' · ' + liveNewsMeta.provider;
    }
    if (liveNewsMeta.status === 'error') return '实时源暂不可用 · 已降级到缓存/演示数据';
    return '正在加载真实新闻…';
  }

  function card(n, compact) {
    var link = n.url ? '<a class="news-source-link" href="' + esc(n.url) + '" target="_blank" rel="noopener noreferrer">查看报道 ↗</a>' : '';
    if (compact) {
      return '<div class="brief"><div class="row small"><span><span class="tag blue">' + esc(n.category) + '</span> ' + esc(n.source) + '</span><span>' + esc(n.time) + '</span></div><b>' + esc(n.title) + '</b><span class="muted">' + esc(n.summary) + '</span><div class="news-actions">' + link + '</div></div>';
    }
    return '<article class="card news"><div class="row small"><span><span class="tag blue">' + esc(n.category) + '</span> ' + esc(n.source) + '</span><span>' + esc(n.time) + '</span></div><h3>' + esc(n.title) + '</h3><p>' + esc(n.summary) + '</p><div class="why"><b>为什么关注：</b>' + esc(n.why) + '</div><div class="news-actions">' + link + '</div></article>';
  }

  var originalToday = today;
  today = function () {
    var html = originalToday();
    var demo = '<small class="muted">演示数据</small>';
    html = html.replace(demo, '<small class="muted">' + esc(statusLine()) + '</small>');
    return html;
  };

  intelligence = function () {
    var cats = ['全部','AI国内','AI国际','财经','证券','A股','宏观','银行','保险','投行','国际','时政','考公'];
    var news = s.cat === '全部' ? s.news : s.news.filter(function (n) { return n.category === s.cat; });
    var notice = liveNewsMeta.status === 'live'
      ? '<b>真实新闻已接入。</b> ' + esc(statusLine()) + '。AI 情报与原有新闻流合并展示，并保留来源链接。'
      : '<b>实时新闻暂未加载。</b> 当前显示缓存或演示内容；任务、目标等其他功能不受影响。';
    return head('每日情报','不是无限新闻流，而是快速知道今天值得关注什么。','')
      + '<div class="seg">' + cats.map(function (c) { return '<button data-cat="' + c + '" class="' + (s.cat === c ? 'active' : '') + '">' + c + '</button>'; }).join('') + '</div>'
      + '<div class="card" style="margin-bottom:15px"><div class="insight">' + notice + '</div></div>'
      + '<div class="grid newsgrid">' + (news.length ? news.map(function (n) { return card(n, false); }).join('') : empty('这个分类今天还没有抓取到内容')) + '</div>';
  };

  var style = document.createElement('style');
  style.textContent = '.news-actions{display:flex;justify-content:flex-end;margin-top:9px}.news-source-link{color:var(--p);text-decoration:none;font-size:12px;font-weight:600}.news-source-link:hover{text-decoration:underline}';
  document.head.appendChild(style);

  function getJson(url, optional) {
    return fetch(url + '?ts=' + Date.now(), { cache: 'no-store' })
      .then(function (response) {
        if (!response.ok) {
          if (optional) return { items: [] };
          throw new Error('HTTP ' + response.status);
        }
        return response.json();
      })
      .catch(function (err) {
        if (optional) return { items: [] };
        throw err;
      });
  }

  Promise.all([
    getJson('data/news.json', false),
    getJson('data/ai-news.json', true)
  ])
    .then(function (payloads) {
      var basePayload = payloads[0] || {};
      var aiPayload = payloads[1] || {};
      var baseItems = Array.isArray(basePayload.items) ? basePayload.items : [];
      var aiItems = Array.isArray(aiPayload.items) ? aiPayload.items : [];
      var allItems = aiItems.concat(baseItems);

      if (!allItems.length) throw new Error('empty news');

      liveNewsMeta = {
        status: 'live',
        generatedAt: aiPayload.generatedAt || basePayload.generatedAt || '',
        provider: [aiItems.length ? (aiPayload.provider || 'ChatGPT AI Daily Intel') : '', basePayload.provider || 'RSS'].filter(Boolean).join(' + '),
        note: aiPayload.note || basePayload.note || ''
      };
      s.news = allItems.map(normalize);
      render();
    })
    .catch(function () {
      liveNewsMeta.status = 'error';
      render();
    });
}());
