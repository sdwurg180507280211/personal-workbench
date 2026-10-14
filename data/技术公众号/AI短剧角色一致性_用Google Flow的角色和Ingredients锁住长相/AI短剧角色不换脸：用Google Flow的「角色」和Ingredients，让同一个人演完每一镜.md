# AI短剧角色不换脸：用Google Flow的「角色」和Ingredients，让同一个人演完每一镜

上一篇讲了怎么把剧本拆成镜头表，并且在每一镜里原样重复角色卡。照做之后，你会发现画面确实“像”了，但还不够：第一镜里的老人戴圆框眼镜，到第五镜眼镜变成了方的，风衣的灰色也深了一号。**只靠文字描述，视频模型每一次都在重新“想象”这个人。**

解决办法是给模型看图。这篇讲 Google 的 AI 影片制作工具 Flow 里的两个功能：**Ingredients（参考素材）** 和 **Characters（角色）**。前者让你把角色、道具、场景的图片作为参考塞进每一次生成；后者把角色的图片、名字和声音打包成一个可以反复调用的“演员”。看完你能做到：准备好一张合格的角色参考图，在 Flow 里建好一个原创角色，然后让它连续出演几个镜头。

## Ingredients 和「角色」是从哪来的

Flow 是 Google 在 2025 年 5 月的 I/O 大会上推出的，前身是 Google Labs 的实验项目 VideoFX。它的定位从一开始就不是“生成一段好看的视频”，而是**做电影**：把 Google 的视频模型 Veo、图像模型和 Gemini 放进同一个工作台，让创作者管理素材、生成镜头、再在 Scenebuilder 里把镜头排成一场戏。

既然是做电影，就绕不开同一个问题：**一部片子里，同一个角色要在几十个镜头里长得一样。** 所以 Flow 上线时就带着 Ingredients 这个设计：角色、物件、画面风格都可以做成一个可复用的“配料”，或用图像模型生成，或自己上传，生成视频时把它们作为参考加进去。

这个功能的演进，基本就是“参考能锁住的东西越来越多”的过程：

- **2025 年 6 月**：Google 发布的 Flow 上手技巧里写明，Ingredients to Video 当时只能配合 Veo 2 使用，最新的 Veo 3 还用不了。早期的参考图功能只管画面，不管声音。
- **2025 年 10 月**：Veo 3.1 上线，Google 第一次给 Ingredients to Video、首尾帧和延长视频这几项功能加上了声音。参考图生成的镜头，终于可以带对白和环境音了。
- **2026 年的 I/O**：Google 推出 Gemini Omni 模型家族，第一款 Gemini Omni Flash 接入了 Flow。它能同时吃进图片、视频、文字和声音作为参考，声音参考先从**人声**开始支持。
- **现在**：Flow 帮助中心里多了「角色」功能，把一到两张外观图和一个声音绑定成一个角色，官方的说法是角色的脸、服装和声音在多次生成里保持一致，不用每次重新上传同样的图片。

这条路线留下了一个今天仍然要面对的包袱：**不同模型对参考图的支持程度不一样。** 后面讲动手步骤时会专门说清楚哪个模型能用、能生成多长。

## 四种锁角色的办法，比一比

![四种锁定角色的做法对比：纯文字角色卡、首帧图、Ingredients 参考图、Flow 角色，比较锁住什么、灵活程度、能否带声音](imgs/01-four-methods.png)

在多镜头里保持角色一致，现在常见的做法有四种。把它们放在一起比，是因为新手往往从第一种开始，然后一路往后试，最好先知道每一步换来了什么、又付出了什么。

| | 纯文字角色卡 | 首帧图（图生视频） | Ingredients 参考图 | Flow「角色」 |
|---|---|---|---|---|
| 锁住什么 | 只有文字描述，模型每次重新想象 | 第一帧的画面，包括角色、场景和构图 | 角色、物件、场景或风格的外观 | 角色的外观和声音，打包在一起 |
| 灵活程度 | 最高，但最容易跑偏 | 最低，构图基本被首帧定死 | 高，同一张参考图可以放进不同场景和动作 | 高，在提示词里 @ 名字即可 |
| 能否带固定声音 | 不能 | 不能 | 配合 Omni Flash 可加人声参考 | 角色自带声音 |
| 能否换到别的工具 | 能，文字到哪都能用 | 能，图片到哪都能用 | 参考图本身能带走 | 角色是 Flow 项目里的素材 |
| 适合 | 前期试方向 | 需要精确控制某一镜的构图 | 角色要在不同场景里出现 | 要拍系列、角色反复出场 |

**为什么选 Ingredients 和「角色」**：首帧图虽然最“稳”，但它锁死的是整个画面，你想让同一个人从便利店走到街上，就得为每个场景单独做一张首帧图。参考图只锁人，场景和动作交给提示词，一张图能用在很多镜头里。「角色」再往前走一步，把声音也绑上，拍对白戏时，同一个角色不会这一镜是低沉的嗓音、下一镜变成清亮的。

**为什么有人放弃它**：一是门槛，Flow 需要订阅 Google AI 套餐，而且只在部分国家和地区开放；二是模型限制，用参考图生成时能选的模型和时长都比纯文字少；三是角色存在 Flow 项目里，如果后期要换到别的视频工具，带得走的只有你自己准备的那几张参考图。**所以不管用不用 Flow，参考图都值得自己保存一份。**

## 动手前，先确认三件事

**第一，你能不能用。** 按 Flow 帮助中心的说明，使用 Flow 需要同时满足：年满 18 岁并完成年龄验证；人在 Flow 支持的国家或地区；订阅 Google AI Plus、Pro 或 Ultra 套餐，或者使用符合条件的 Google Workspace 企业和教育版套餐。支持地区的名单里有香港、澳门和台湾，**中国大陆不在名单内**。官方还特别说明，VPN 不能让不支持地区的用户获得使用权限。

> **先查地区，再买套餐。** Flow 并不是在所有能订阅 Google AI Pro 的地区都开放，官方帮助中心建议购买前先核对 Flow 支持地区列表。另外，部分功能还有额外的地区限制，比如“头像”（Avatar）功能在欧洲经济区、英国和瑞士不可用。

**第二，积分怎么扣。** Flow 生成内容要消耗 Flow 积分。帮助中心写明每天有 50 个积分，Plus、Pro、Ultra 订阅用户每月还会额外获得一批积分，数量随套餐递增；当日没用完的每日积分不会累积到第二天，每月的积分也不会结转。

和本篇相关的几档消耗（按帮助中心当前页面，单位是“每次生成”）：

| 模型 | 能否用参考图 | 参考图生成的时长 | 每次生成消耗 |
|---|---|---|---|
| Veo 3.1 Lite | 能 | 只能 8 秒 | 非 Ultra 订阅 10，Ultra 订阅 5 |
| Veo 3.1 Fast | 能 | 只能 8 秒 | 非 Ultra 订阅 20，Ultra 订阅 10 |
| Veo 3.1 Quality | 不能 | — | — |
| Gemini Omni Flash（720p） | 能 | 4、6、8、10 秒 | 4 秒 7，6 秒 10，8 秒 12，10 秒 15 |
| Gemini Omni Flash（360p） | 能 | 4、6、8、10 秒 | 4 秒 4，6 秒 5，8 秒 6，10 秒 7 |

> **积分按“每次生成”算，不是按“每次点击”算。** 帮助中心特别说明，一次请求可能生成两段视频，就要扣两次积分。如果你在设置里选了多个输出，消耗会成倍增加。官方也提醒积分规则随时可能调整，生成前在提示框右上角的设置里看一眼当前模型和最新消耗。失败的生成不扣积分。

**第三，用中文还是英文写提示词。** Flow 支持包括简体和繁体中文在内的多种界面语言，但帮助中心明确建议用**英文提示词**以获得最好的效果。下面的示例都给英文版，附上中文意思，方便你照着改。

## 第一步：准备一张合格的角色参考图

![合格与不合格的角色参考图对比：左边是纯色背景、全身正面、服装清晰的原创角色线稿；右边是背景杂乱、多人同框、半身被遮挡的反例，各自标注要点](imgs/02-reference-image.png)

参考图决定了模型“认识”的这个角色长什么样，这一步花的功夫最值。Flow 帮助中心给的建议归纳起来就三条：

- **主体放在纯色或已抠好的背景上。** 官方原话是，角色或产品参考最好用纯色或分割好的背景。背景里的杂物，模型可能会当成角色的一部分一起“记住”。
- **一张图只放一个主体。** 场景和风格参考里也不要出现多余的人物，除非这就是你想要的效果。
- **几张参考图的整体观感要统一。** 角色图是写实风，场景图却是动漫风，模型很难把它们融合在一起。

在官方建议之外，从短剧的实际需要出发，我还建议：

- **用正面、全身、光线均匀的图。** 短剧里角色会走、会坐、会转身，一张能看清服装全貌的全身图，比一张漂亮的半身特写更有用。
- **把标志性物件画进去。** 上一篇角色卡里写的“一盒白色包装的热牛奶”“圆框眼镜”，最好都出现在参考图上。
- **参考图直接在 Flow 里生成。** Flow 内置了 Nano Banana 系列图像模型，可以用你的角色卡文字先生成一张角色图，满意了再用它做参考。这样角色从一开始就是 AI 原创的。

用来生成角色参考图的提示词可以这样写，把角色卡的内容换成你自己的：

```text
Full-body front view of an original character standing straight, plain light gray background, even soft lighting, realistic film style.
A slim man in his seventies, short gray-white hair, round wire-rimmed glasses, wearing a knee-length gray trench coat, dark trousers and black cloth shoes, holding a small white carton of hot milk in his right hand.
```

（意思：原创角色的全身正面站姿，浅灰色纯色背景，柔和均匀的光线，写实电影风格；角色是七十岁左右的清瘦老人，花白短发，戴圆框金属眼镜，穿及膝灰色风衣、深色长裤、黑色布鞋，右手拿着一小盒白色包装的热牛奶。）

> **参考图只用原创或你有权使用的形象。** 不要拿明星、网红或身边人的照片当角色参考，也不要用动漫、影视剧里已有的角色。Flow 在所有地区都不支持生成知名人物的视频，并对上传的人物照片设有保护措施；更重要的是，用别人的脸做短剧本身就有侵权风险。想让自己出镜，Flow 有专门的“头像”功能，需要本人在手机上完成采集，和角色是两回事。

## 第二步：在 Flow 里建一个角色

![Flow「角色」的组成示意：一到两张外观图、角色名、声音三部分打包成一个角色卡片，右侧多条箭头指向镜头 1、镜头 2、镜头 3，标注“提示词里 @ 名字调用”](imgs/03-character-bundle.png)

参考图准备好之后，按 Flow 帮助中心的步骤建角色：

1. 打开 Flow，进入一个已有项目或新建项目。
2. 在左侧点 **Characters**（角色）。已经有角色的话，点 **New Character** 新建。
3. 在提示框里详细描述这个角色，然后**上传或生成一到两张**展示角色外观的图片。一个角色至少要有一张图才能使用。
4. 点生成。
5. 给角色起个名字，再点 **Select a voice** 选一个声音（可以用预设声音，也可以创建自定义声音），点 **Add to Character** 加到角色上。
6. 需要的话补充角色信息，最后点右上角的 **Done**。

几个细节值得注意：

- **名字起得短、好打、不重复。** 后面在提示词里要用 @ 加名字调用它，比如把老人叫 `OldMan_Milk`，把店员叫 `Xiaohe`。
- **自定义声音是在预设声音上“调”出来的**，不是克隆某个真人的声音。帮助中心的流程是：选一个基础声音，起名，再用一句话描述你想要的变化，比如“声音略沙哑、语速慢”，可以先输入一小段台词试听 8 秒样音，满意了点 **Sync** 再保存。
- 角色建在哪个项目里，就在哪个项目的 Characters 里编辑和删除。**一部短剧的所有镜头，最好放在同一个项目里做。**

## 第三步：在镜头里调用角色和参考图

现在拿出上一篇的镜头表，一镜一镜地生成。调用方式有两种，按需要选。

**方式一：直接 @ 角色。** 在提示框里输入 @ 加角色名，然后描述这个角色在这一镜里做什么。官方示例是 `@CaptainZoro walking through a futuristic city`（@CaptainZoro 穿过一座未来城市）。用在示例故事的第 2 镜：

```text
Medium shot, eye level, the camera slowly follows. @OldMan_Milk pushes open the glass door of a small convenience store late at night and walks to the warmer shelf next to the fridge, picking up a carton of hot milk. Cold white fluorescent lighting, realistic film style, vertical 9:16.
Sound: a single electronic door chime, a faint hum from the fridge.
```

（意思：中景，平视，镜头缓慢跟随。@OldMan_Milk 深夜推开一家小便利店的玻璃门，走到冰柜旁的保温柜前，拿起一盒热牛奶。冷白色灯管照明，写实电影风格，竖屏 9:16。声音：电子门铃响一声，冰柜轻微的嗡嗡声。）

**方式二：用 Ingredients 加参考图。** 当你需要的不只是角色，还有固定的道具或场景时，用这种方式。步骤是：在提示框里点模型名称，选 **Video**，再选 **Ingredients**，然后把参考图拖进来，或者输入 @ 按名称搜索项目里已有的素材，或者点提示框下方的 **Add** 上传。官方给的例子很能说明问题：素材是“一个女人、一盏熔岩灯、一条起雾的街道”，提示词写成“那个女人，躯干是熔岩灯，走在起雾的街道上”。**提示词的任务，是告诉模型每一张参考图在这一镜里扮演什么。**

比如第 4 镜，你可以把老人的角色图和一张便利店门口长椅的场景图都作为参考：

```text
Wide shot through the glass door of the convenience store. The old man from the character reference places the carton of hot milk on the wooden bench shown in the location reference, then turns and walks away into the dark street. Realistic film style, vertical 9:16.
Sound: soft night wind.
```

（意思：透过便利店玻璃门的全景。角色参考图里的老人把热牛奶放在场景参考图里的那张木长椅上，然后转身走进昏暗的街道。写实电影风格，竖屏 9:16。声音：轻柔的夜风。）

写这类提示词时，记住帮助中心的另一条建议：**文字要和参考图互相补充，不要互相矛盾。** 参考图里老人穿灰色风衣，提示词就别写“穿着黑色大衣”；参考图里是木长椅，提示词就别写“金属长椅”。冲突的指令只会让模型左右为难。

如果这一镜有对白，还可以加声音参考：模型选 **Omni Flash**，在 Ingredients 下点 **Add** 再选 **Voices**，选好声音后在提示词里用 `@Voice: 声音名` 引用。帮助中心说明，要在多个片段里保持同一个角色的声音，就加一个单人声音参考；声音参考只能用在使用了 Ingredients 的生成里，其他生成方式会报错。用「角色」功能时，声音已经绑在角色上了。

## 第四步：把几个镜头串成一场戏

![多镜头制作流程：先用 360p 草稿试动作 → 挑出满意的一条 → 换 720p 正式生成 → 暂停在合适的画面保存为图片 → 作为下一镜的参考或首帧 → 在 Scenebuilder 里排序和修剪](imgs/04-multi-shot-flow.png)

单个镜头做出来之后，要把它们接成一场戏。Flow 里有几个功能正好对应这个环节：

- **先用 360p 试，再出 720p。** Gemini Omni Flash 有 360p 草稿档，消耗是 720p 的一半左右。一个镜头的动作和构图对不对，360p 已经看得出来，确认之后再用 720p 正式生成。帮助中心还写明，Pro 和 Ultra 订阅用户可以把 360p 的结果免费放大到 720p。
- **把满意的画面存成图片。** 打开一段视频，暂停在想要的那一帧，点 **Save frame**，这一帧就会存进项目，可以当作后续生成的参考素材、首帧或尾帧。上一镜的结尾画面拿来做下一镜的参考，衔接会顺很多。
- **在 Scenebuilder 里排戏。** 把多个片段按顺序放进 Scenebuilder，调整顺序、拖动两端的把手修剪每段的开头和结尾，预览整场，最后下载。

即使用了参考图和角色，**生成结果仍然有随机性**，不会每一条都完全一致。比较务实的做法是：每个镜头多生成几条，从里面挑角色最像、动作最对的那条；看到明显跑偏的，按下面这几条排查：

- **参考图背景是否干净？** 背景杂乱时，模型可能把背景元素当成角色特征。
- **提示词有没有和参考图打架？** 尤其是服装颜色、发型、配饰。
- **一镜里是不是塞了太多东西？** 参考素材越多、动作越复杂，模型越难兼顾，必要时把一镜拆成两镜。
- **几张参考图风格是否统一？** 写实的人放进卡通的场景，结果往往两边都不像。
- **模型选对了吗？** 选了不支持参考图的模型时，Flow 会提示你，或者自动切换到兼容的模型，生成前在设置里确认一下当前模型。

## 下载和发布前，知道这两件事

**水印。** Flow 用 Veo、Omni 或 Nano Banana 生成的所有内容都带有不可见的 SynthID 数字水印，用来标识这是 AI 生成的内容，官方要求不得篡改或移除。你还可以在头像下拉菜单里打开“可见水印”开关，给图片和视频加上肉眼可见的水印。至于国内平台发布短剧时还要做哪些 AI 生成内容标识，下一篇单独讲。

**能不能商用。** Flow 帮助中心对这个问题的回答是：以 Google 服务条款为准，并引用了条款里的原话，部分服务允许你生成原创内容，Google 不会主张这些内容的所有权。同时，生成内容必须遵守 Google 的生成式 AI 禁止使用政策。打算商用之前，建议把服务条款和禁止使用政策完整读一遍。

## 写在最后

如果你只想记住一个顺序：**先做一张干净的原创角色图，再建角色，最后在每一镜里 @ 它。** 参考图这一步做扎实了，后面每个镜头都在同一张“脸”上做文章，比反复改文字描述省心得多。今晚就可以先从一张浅灰背景的全身角色图开始，它不只在 Flow 里能用，换到别的工具同样是你最有用的素材。

## 参考资料

<div class="sources">
<p>Google Flow 帮助中心：<a href="https://support.google.com/flow/answer/16353333?hl=en">Get started with Google Flow</a>（使用条件、浏览器、水印、商用说明）、<a href="https://support.google.com/flow/answer/16353334?hl=en">Create videos in Google Flow</a>（Ingredients、@ 角色、声音参考、最佳实践）、<a href="https://support.google.com/flow/answer/16935308?hl=en">Manage your Google Flow projects, assets &amp; collections</a>（创建和管理角色、下载、SynthID 说明）、<a href="https://support.google.com/flow/answer/16935718?hl=en">Edit videos &amp; build scenes in Google Flow</a>（保存画面、Scenebuilder）、<a href="https://support.google.com/flow/answer/16352836?hl=en">Learn about Google Flow models &amp; supported features</a>（各模型支持的功能和时长）、<a href="https://support.google.com/flow/answer/16526234?hl=en">Manage your Google Flow credits</a>（积分规则与每次生成消耗）、<a href="https://support.google.com/flow/answer/16353544?hl=en">Where you can use Google Flow</a>（支持的语言、国家和地区、功能地区限制）、<a href="https://support.google.com/flow/answer/17102997?hl=en">Create &amp; use your avatar in Google Flow</a>。</p>
<p>Google 官方博客：<a href="https://blog.google/technology/ai/google-flow-veo-ai-filmmaking-tool/">Meet Flow: AI-powered filmmaking with Veo 3</a>（2025 年 5 月）、<a href="https://blog.google/technology/ai/flow-video-tips/">5 tips for getting started with Flow</a>（2025 年 6 月）、<a href="https://blog.google/technology/ai/veo-updates-flow/">Introducing Veo 3.1 and advanced capabilities in Flow</a>（2025 年 10 月）、<a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/">Introducing Gemini Omni</a>。</p>
<p>政策：<a href="https://policies.google.com/terms/generative-ai/use-policy">Google 生成式 AI 禁止使用政策</a>、<a href="https://policies.google.com/terms">Google 服务条款</a>。</p>
<p>资料核对于 2026 年 10 月 15 日。文中步骤来自官方文档，写作时未实际操作；按钮名称沿用帮助中心的英文写法，实际界面以当前版本为准。Flow 的套餐、积分消耗、模型和支持地区更新频繁，以官方页面为准。示例角色和提示词均为原创，不承诺生成效果；AI 生成结果有随机性，不保证每个镜头角色完全一致。配图为示意图，不是产品界面截图。</p>
</div>
