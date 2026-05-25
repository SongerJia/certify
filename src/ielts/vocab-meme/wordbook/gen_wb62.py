#!/usr/bin/env python
"""Generate wordbook-62.md with 180 IELTS word cards"""

import json

# Reference meanings from ielts4000_raw
with open(r'E:\certify\src\ielts\vocab-meme\wordbook\_wd62_ref.json', encoding='utf-8') as f:
    ref = json.load(f)

# Complete word data: phonetics, Chinese meanings, memes, examples
words_data = [
    ("tremble", "/ˈtrembl/", "v. 颤抖/发抖/战栗",
     "「穿伯」—— 穿伯伯的大鞋走路，抖个不停 😨",
     "Her voice began to <b>tremble</b> as she gave the speech."),

    ("trench", "/trentʃ/", "n. 沟渠/战壕/海沟",
     "「蠢吃」—— 蠢人掉进了战壕吃土 🕳️",
     "Soldiers dug deep <b>trenches</b> for protection during the battle."),

    ("tribe", "/traɪb/", "n. 部落/族群",
     "「踹步」—— 部落人踹着步子跳战舞 🏕️",
     "The <b>tribe</b> has lived in this region for thousands of years."),

    ("tribute", "/ˈtrɪbjuːt/", "n. 贡品/颂词/致敬",
     "「吹比特」—— 吹捧比特的贡献，致敬 💐",
     "The concert was a fitting <b>tribute</b> to the late musician."),

    ("trick", "/trɪk/", "n. 诡计/把戏 v. 欺骗",
     "「吹壳」—— 吹破了壳的骗局 🃏",
     "He used a clever <b>trick</b> to solve the puzzle."),

    ("trickle", "/ˈtrɪkl/", "v. 滴/淌/慢慢流动",
     "「吹口」—— 水从破口处一滴一滴流淌 💧",
     "Water began to <b>trickle</b> through the cracked ceiling."),

    ("trifle", "/ˈtraɪfl/", "n. 小事/琐事/微不足道的东西",
     "「踹否」—— 踹一脚否？这点小事不值得 🫢",
     "Don't waste time worrying about such a <b>trifle</b>."),

    ("trim", "/trɪm/", "v. 修剪/削减 adj. 整齐的",
     "「吹木」—— 风把树枝吹歪，需要修剪 ✂️",
     "I need to <b>trim</b> the hedges before the party."),

    ("triple", "/ˈtrɪpl/", "adj. 三倍的/三重的 v. 增至三倍",
     "「吹破」—— 吹破了，三倍多 🤯",
     "The company's profits have <b>tripled</b> in the last year."),

    ("triumph", "/ˈtraɪʌmf/", "n. 胜利/成功/喜悦",
     "「踹俺服」—— 踹了俺，服了，他胜利了 🏆",
     "Winning the championship was a moment of great <b>triumph</b>."),

    ("tropic", "/ˈtrɒpɪk/", "n. 热带/回归线",
     "「戳匹克」—— 戳破匹克的防晒霜，在热带 🌴",
     "Coconut palms grow abundantly in the <b>tropics</b>."),

    ("troublesome", "/ˈtrʌblsəm/", "adj. 麻烦的/令人烦恼的",
     "「抓包桑」—— 抓住一包桑心的麻烦事 😫",
     "The new software has some <b>troublesome</b> bugs."),

    ("trumpet", "/ˈtrʌmpɪt/", "n. 小号/喇叭 v. 吹嘘",
     "「川皮特」—— 川普皮特吹小号 🎺",
     "The jazz band opened with a soaring <b>trumpet</b> solo."),

    ("trunk", "/trʌŋk/", "n. 树干/象鼻/行李箱",
     "「创可」—— 创可贴贴在大象鼻子上 🐘",
     "The elephant used its <b>trunk</b> to pick up the fruit."),

    ("tub", "/tʌb/", "n. 盆/桶/浴缸",
     "「踏布」—— 脚踏布放进桶里 🛁",
     "She filled the <b>tub</b> with warm water for a relaxing bath."),

    ("tube", "/tjuːb/", "n. 管子/地铁/软管",
     "「休布」—— 休整布线，管子都排好了 📺",
     "He takes the <b>tube</b> to work every morning."),

    ("tuck", "/tʌk/", "v. 塞进/把...掖好/卷起",
     "「它壳」—— 把它塞进壳里 🐢",
     "She <b>tucked</b> the blanket around her sleeping child."),

    ("tug", "/tʌɡ/", "v. 用力拉/拖拽 n. 拖船",
     "「塔哥」—— 塔哥用力拖着船 🚢",
     "The child <b>tugged</b> at her mother's sleeve to get attention."),

    ("tumble", "/ˈtʌmbl/", "v. 摔倒/倒塌/暴跌",
     "「贪伯」—— 贪心的伯伯走路摔倒了 🤸",
     "Oil prices <b>tumbled</b> sharply on the news."),

    ("tumult", "/ˈtjuːmʌlt/", "n. 骚动/喧哗/混乱",
     "「休骂特」—— 休息时骂得特别凶，一片喧哗 😤",
     "The announcement caused a <b>tumult</b> among the protesters."),

    ("turmoil", "/ˈtɜːmɔɪl/", "n. 混乱/动荡/骚乱",
     "「特猫油」—— 特猫油洒了一地，一片混乱 🌀",
     "The country has been in political <b>turmoil</b> for months."),

    ("tutor", "/ˈtjuːtə/", "n. 导师/家庭教师 v. 辅导",
     "「休特」—— 休息时特地辅导你 📚",
     "She works as a private <b>tutor</b> for high school students."),

    ("twig", "/twɪɡ/", "n. 小树枝/嫩枝",
     "「推个」—— 推个小树枝过去 🌿",
     "A bird perched on a slender <b>twig</b> near the window."),

    ("twilight", "/ˈtwaɪlaɪt/", "n. 黄昏/暮光/衰退期",
     "「踹来特」—— 踹来特别的光，是暮光 🌅",
     "The garden looks magical in the soft <b>twilight</b>."),

    ("twinkle", "/ˈtwɪŋkl/", "v. 闪烁/闪耀/眨眼",
     "「推可」—— 推一推，就可以闪烁 ✨",
     "Stars began to <b>twinkle</b> in the evening sky."),

    ("twist", "/twɪst/", "v. 扭曲/旋转/蜿蜒",
     "「推死特」—— 推进去死特别的扭曲角度 🧬",
     "The plot of the movie has an unexpected <b>twist</b>."),

    ("typhoon", "/taɪˈfuːn/", "n. 台风",
     "「台风」—— 直接就是台风 🌀",
     "The <b>typhoon</b> caused widespread damage along the coast."),

    ("typical", "/ˈtɪpɪkl/", "adj. 典型的/有代表性的",
     "「踢皮扣」—— 踢皮扣是典型的犯规动作 🏷️",
     "This is a <b>typical</b> example of Gothic architecture."),

    ("tyrant", "/ˈtaɪrənt/", "n. 暴君/专制者",
     "「抬润特」—— 把人抬起来滋润，这是暴君 😈",
     "The people rose up against the cruel <b>tyrant</b>."),

    ("tyre", "/ˈtaɪə/", "n. 轮胎",
     "「胎尔」—— 胎尔就是轮胎 🛞",
     "He had to change a flat <b>tyre</b> on the highway."),

    ("ugly", "/ˈʌɡli/", "adj. 丑陋的/难看的",
     "「阿格力」—— 阿格力的长相真是难看 👹",
     "The building is an <b>ugly</b> concrete block from the 1960s."),

    ("ultrasonic", "/ˌʌltrəˈsɒnɪk/", "adj. 超声波的",
     "「奥特说尼克」—— 奥特曼用超声波和尼克对话 🔊",
     "Dentists use <b>ultrasonic</b> tools to clean teeth."),

    ("ultraviolet", "/ˌʌltrəˈvaɪələt/", "adj. 紫外线的 n. 紫外线",
     "「奥特唯乐特」—— 奥特曼唯独乐特紫外线 ☀️",
     "Sunscreen protects your skin from <b>ultraviolet</b> radiation."),

    ("unbearable", "/ʌnˈbeərəbl/", "adj. 无法忍受的/难以承受的",
     "「按贝尔若伯」—— 按着贝尔犹如伯伯，无法忍受 😣",
     "The pain became almost <b>unbearable</b> after the surgery."),

    ("unconscious", "/ʌnˈkɒnʃəs/", "adj. 无意识的/失去知觉的",
     "「俺看射死」—— 俺看到射箭死的人失去知觉 💫",
     "She was knocked <b>unconscious</b> in the accident."),

    ("uncover", "/ʌnˈkʌvə/", "v. 揭开/揭露/发现",
     "「俺卡我」—— 俺卡住了我，揭开盖子 🔎",
     "The investigation helped to <b>uncover</b> widespread fraud."),

    ("underestimate", "/ˌʌndərˈestɪmeɪt/", "v. 低估/轻视",
     "「俺的儿爱死提妹」—— 俺的儿子低估了提妹的能力 📉",
     "Never <b>underestimate</b> the power of a determined person."),

    ("underground", "/ˌʌndəˈɡraʊnd/", "adj. 地下的 n. 地铁 adv. 在地下",
     "「俺的哥让的」—— 俺的哥让的地铁很便利 🚇",
     "The city has an extensive <b>underground</b> railway system."),

    ("underline", "/ˌʌndəˈlaɪn/", "v. 在...下划线/强调",
     "「俺的来」—— 俺的来强调一下 ✍️",
     "The report <b>underlines</b> the need for urgent action."),

    ("underlying", "/ˌʌndəˈlaɪɪŋ/", "adj. 潜在的/根本的/在下面的",
     "「俺的来影」—— 俺的影子是潜在的 🌊",
     "The <b>underlying</b> cause of the problem has not been addressed."),

    ("underneath", "/ˌʌndəˈniːθ/", "prep./adv. 在...下面/在底下",
     "「俺的尼斯」—— 俺的尼斯湖在下面 🏞️",
     "She found the key hidden <b>underneath</b> the mat."),

    ("undertaking", "/ˌʌndəˈteɪkɪŋ/", "n. 事业/任务/承诺",
     "「俺的特king」—— 俺的特大king事业 🏗️",
     "Building the bridge was a massive <b>undertaking</b>."),

    ("undo", "/ʌnˈduː/", "v. 解开/取消/破坏",
     "「俺堵」—— 俺堵住了，解开它 🔓",
     "Some mistakes are impossible to <b>undo</b>."),

    ("undoubtedly", "/ʌnˈdaʊtɪdli/", "adv. 毫无疑问地/肯定地",
     "「俺道提得里」—— 俺说这道题肯定对 ✅",
     "This is <b>undoubtedly</b> the best film I have seen this year."),

    ("undue", "/ˌʌnˈdjuː/", "adj. 过度的/不适当的",
     "「俺丢」—— 俺丢人，过度了 🤦",
     "The judge warned against <b>undue</b> influence on the jury."),

    ("uneasy", "/ʌnˈiːzi/", "adj. 不安的/担心的/不自在的",
     "「俺椅子」—— 俺坐在椅子上感到不安 🪑",
     "She felt <b>uneasy</b> walking home alone at night."),

    ("unequivocal", "/ˌʌnɪˈkwɪvəkl/", "adj. 明确的/不含糊的",
     "「安泥亏我可」—— 安泥亏了我可以明确说 📣",
     "The report's conclusion was <b>unequivocal</b> in its condemnation."),

    ("unfair", "/ʌnˈfeə/", "adj. 不公平的/不合理的",
     "「俺飞儿」—— 俺飞了儿子，不公平 ⚖️",
     "He felt the referee's decision was deeply <b>unfair</b>."),

    ("unfortunately", "/ʌnˈfɔːtʃənətli/", "adv. 不幸地/遗憾地",
     "「俺佛车那特丽」—— 俺佛车那特丽，不幸 😞",
     "<b>Unfortunately</b>, we arrived too late to catch the train."),

    ("unity", "/ˈjuːnəti/", "n. 团结/统一/和谐",
     "「邮拿提」—— 邮件拿来提团结 🤝",
     "The team showed great <b>unity</b> in the face of adversity."),

    ("universe", "/ˈjuːnɪvɜːs/", "n. 宇宙/世界/领域",
     "「邮你窝丝」—— 邮给你的窝丝遍布宇宙 🌌",
     "Scientists continue to explore the mysteries of the <b>universe</b>."),

    ("unlikely", "/ʌnˈlaɪkli/", "adj. 不太可能的/未必的",
     "「俺来可丽」—— 俺来可以美丽？不太可能 🤷",
     "It is <b>unlikely</b> that the project will be completed on schedule."),

    ("unload", "/ʌnˈləʊd/", "v. 卸货/卸载/倾吐",
     "「俺楼的」—— 俺楼的东西要卸货 🚛",
     "Workers began to <b>unload</b> the cargo from the ship."),

    ("unravel", "/ʌnˈrævl/", "v. 解开/澄清/崩溃",
     "「俺绕福」—— 俺绕开烦恼，解开谜团 🧶",
     "Detectives worked to <b>unravel</b> the mystery of the missing painting."),

    ("unsatisfactory", "/ˌʌnsætɪsˈfæktəri/", "adj. 不满意的/不充分的",
     "「按塞提斯发个特瑞」—— 按塞提斯发个特长，不满意 😕",
     "The quality of the work was deemed <b>unsatisfactory</b>."),

    ("unstable", "/ʌnˈsteɪbl/", "adj. 不稳定的/易变的",
     "「俺死待伯」—— 俺死待伯伯，状态不稳定 🎢",
     "The political situation remains highly <b>unstable</b>."),

    ("unwarranted", "/ʌnˈwɒrəntɪd/", "adj. 无根据的/不必要的",
     "「俺窝润体的」—— 俺窝里润体的说法是无根据的 ❌",
     "The criticism was completely <b>unwarranted</b>."),

    ("uphold", "/ʌpˈhəʊld/", "v. 支持/维护/维持",
     "「阿婆吼的」—— 阿婆吼的声音，支持你 🙌",
     "Judges must <b>uphold</b> the law regardless of personal feelings."),

    ("upright", "/ˈʌpraɪt/", "adj./adv. 直立的/正直的",
     "「阿婆来特」—— 阿婆站着特别直立 🧍",
     "The <b>upright</b> freezer fits perfectly in the corner."),

    ("upset", "/ʌpˈset/", "v./adj. 使烦恼/不安的/打翻",
     "「阿婆塞特」—— 阿婆被塞了特别的烦心事 😢",
     "The bad news really <b>upset</b> the whole family."),

    ("urge", "/ɜːdʒ/", "v. 敦促/力劝/强烈要求 n. 冲动",
     "「鹅只」—— 鹅只催促你快走 🦢",
     "I strongly <b>urge</b> you to reconsider your decision."),

    ("urgent", "/ˈɜːdʒənt/", "adj. 紧急的/急迫的",
     "「鹅拯特」—— 鹅拯救特别紧急 🚨",
     "There is an <b>urgent</b> need for blood donors."),

    ("utility", "/juːˈtɪləti/", "n. 公用事业/实用/效用",
     "「邮踢了提」—— 邮局踢了提公用事业 ⚡",
     "Gas and electricity are essential <b>utilities</b>."),

    ("utilization", "/ˌjuːtɪlaɪˈzeɪʃn/", "n. 利用/使用",
     "「邮踢来贼神」—— 邮局踢来的贼神利用 🔧",
     "Better <b>utilization</b> of existing resources should be the priority."),

    ("utmost", "/ˈʌtməʊst/", "adj./n. 最大的/极度的/极限",
     "「阿特某斯特」—— 阿特某斯特的最大努力 💪",
     "I have the <b>utmost</b> respect for her dedication."),

    ("utterance", "/ˈʌtərəns/", "n. 话语/发言/表达",
     "「阿特润斯」—— 阿特润斯的话语 🗣️",
     "His every <b>utterance</b> was carefully analyzed by the media."),

    ("vacation", "/vəˈkeɪʃn/", "n. 假期/休假",
     "「威剋神」—— 威力剋了神，去度假 🏖️",
     "We spent our summer <b>vacation</b> at the beach."),

    ("vaccinate", "/ˈvæksɪneɪt/", "v. 给...接种疫苗",
     "「外可西内特」—— 外面可西内特打疫苗 💉",
     "Health workers are trying to <b>vaccinate</b> all children."),

    ("vacuum", "/ˈvækjuːm/", "n. 真空/真空吸尘器 v. 用吸尘器打扫",
     "「外可有木」—— 外面可有一块木头？吸一下 🧹",
     "She uses a cordless <b>vacuum</b> to clean the floors."),

    ("validate", "/ˈvælɪdeɪt/", "v. 验证/证实/使生效",
     "「外里得特」—— 外面里面都得特别验证 ✅",
     "We need more data to <b>validate</b> this hypothesis."),

    ("valley", "/ˈvæli/", "n. 山谷/流域",
     "「外里」—— 外面里面的山谷 🏔️",
     "The river winds through a beautiful green <b>valley</b>."),

    ("valve", "/vælv/", "n. 阀门/瓣膜",
     "「外吾」—— 外面的阀门由我来控制 🔧",
     "A safety <b>valve</b> prevents the pressure from building up."),

    ("vanguard", "/ˈvænɡɑːd/", "n. 先锋/先驱/先头部队",
     "「万嘎的」—— 万匹大车嘎嘎的先锋队 🚩",
     "The company has always been at the <b>vanguard</b> of technology."),

    ("vanish", "/ˈvænɪʃ/", "v. 消失/突然不见",
     "「外你失」—— 外面你失去了踪影，消失了 🫥",
     "The magician made the rabbit <b>vanish</b> into thin air."),

    ("vanity", "/ˈvænəti/", "n. 虚荣/自负/空虚",
     "「外拿提」—— 外人拿着提包炫耀，真是虚荣 💄",
     "Her excessive <b>vanity</b> made it difficult to be her friend."),

    ("vapor", "/ˈveɪpə/", "n. 蒸汽/水汽",
     "「威婆」—— 威猛的婆婆泡澡冒蒸汽 ♨️",
     "Thick <b>vapor</b> rose from the hot springs."),

    ("variance", "/ˈveəriəns/", "n. 差异/变化/不一致",
     "「外俄恩斯」—— 外面和俄国的恩斯有差异 📊",
     "There is significant <b>variance</b> between the two test results."),

    ("variant", "/ˈveəriənt/", "n. 变体/变种/不同形式",
     "「外俄恩特」—— 外面俄国恩特的变体 🧬",
     "A new <b>variant</b> of the virus has been detected."),

    ("variation", "/ˌveəriˈeɪʃn/", "n. 变化/变异/变体",
     "「外瑞诶神」—— 外面瑞的诶神有变异 🔄",
     "There is considerable <b>variation</b> in temperature across the region."),

    ("varied", "/ˈveərid/", "adj. 各种各样的/多变的",
     "「外瑞的」—— 外面的瑞士的，各种各样的 🎨",
     "The course content is <b>varied</b> and keeps students engaged."),

    ("variety", "/vəˈraɪəti/", "n. 多样性/种类/变化",
     "「我莱提」—— 我的莱提有各种种类 🌈",
     "The supermarket offers a wide <b>variety</b> of fresh produce."),

    ("various", "/ˈveəriəs/", "adj. 各种的/不同的",
     "「外瑞俄斯」—— 外面的瑞士和俄国各种都有 📦",
     "She has lived in <b>various</b> countries around the world."),

    ("varnish", "/ˈvɑːnɪʃ/", "n. 清漆/光泽 v. 给...上漆",
     "「挖你洗」—— 挖出来的漆给你洗，清漆 🖌️",
     "Apply a coat of <b>varnish</b> to protect the wooden surface."),

    ("vault", "/vɔːlt/", "n. 金库/地下室/拱顶 v. 跳跃",
     "「窝特」—— 窝特别的大金库 🏦",
     "The precious documents are stored in a secure <b>vault</b>."),

    ("vegetable", "/ˈvedʒtəbl/", "n. 蔬菜/植物人",
     "「歪只特伯」—— 歪只特别伯伯爱吃蔬菜 🥬",
     "Eat more <b>vegetables</b> to maintain a healthy diet."),

    ("veil", "/veɪl/", "n. 面纱/遮盖物 v. 遮掩",
     "「威哦」—— 威严哦，面纱遮住了 👰",
     "The bride wore a delicate lace <b>veil</b>."),

    ("vein", "/veɪn/", "n. 静脉/叶脉/矿脉/风格",
     "「胃嗯」—— 胃嗯，静脉在流动 🩸",
     "The doctor inserted the needle into a <b>vein</b> in her arm."),

    ("velocity", "/vɪˈlɒsəti/", "n. 速度/速率",
     "「为拉瑟提」—— 为了拉瑟提的速度 🚀",
     "The car can reach a maximum <b>velocity</b> of 200 kph."),

    ("ventilate", "/ˈventɪleɪt/", "v. 通风/公开讨论",
     "「文提累特」—— 文章提到累了就通风 💨",
     "Please <b>ventilate</b> the room by opening all the windows."),

    ("ventilation", "/ˌventɪˈleɪʃn/", "n. 通风/通风设备",
     "「文提累神」—— 文章提到累了神气通风 🌬️",
     "The basement has poor <b>ventilation</b> and smells musty."),

    ("verge", "/vɜːdʒ/", "n. 边缘/临界点 v. 接近",
     "「窝之」—— 窝之边缘 ⚠️",
     "The country is on the <b>verge</b> of an economic crisis."),

    ("verse", "/vɜːs/", "n. 诗/韵文/节",
     "「我斯」—— 我的诗斯文 📜",
     "The poet recited a beautiful <b>verse</b> about nature."),

    ("vertical", "/ˈvɜːtɪkl/", "adj. 垂直的/直立的",
     "「我体扣」—— 我的身体扣着垂直站 📏",
     "The cliff face rose almost <b>vertical</b> from the sea."),

    ("vested", "/ˈvestɪd/", "adj. 既定的/既得的",
     "「外斯体的」—— 外面斯文体的既定利益 📜",
     "All parties have a <b>vested</b> interest in the project's success."),

    ("vex", "/veks/", "v. 使烦恼/使恼怒",
     "「外克斯」—— 外面克斯惹人烦恼 😤",
     "The constant delays began to <b>vex</b> the manager."),

    ("vibrate", "/vaɪˈbreɪt/", "v. 振动/颤动/摇摆",
     "「歪不锐特」—— 歪着的不能是锐特的，会振动 📳",
     "The phone began to <b>vibrate</b> silently in her pocket."),

    ("vibration", "/vaɪˈbreɪʃn/", "n. 振动/颤动/共鸣",
     "「歪不瑞神」—— 歪着的不能瑞神，振动太大 🎵",
     "Strong <b>vibrations</b> from the drilling shook the building."),

    ("vice", "/vaɪs/", "n. 恶习/缺点/副的",
     "「外死」—— 外面的死都是恶习 🚫",
     "Gambling was his only <b>vice</b>."),

    ("vicinity", "/vɪˈsɪnəti/", "n. 附近/邻近/周围",
     "「为西拿提」—— 为了西边拿提子在附近 📍",
     "There is no hospital in the immediate <b>vicinity</b>."),

    ("vicious", "/ˈvɪʃəs/", "adj. 恶毒的/凶猛的/剧烈的",
     "「为射死」—— 为了射死真是恶毒 🐍",
     "The dog launched a <b>vicious</b> attack on the intruder."),

    ("victorious", "/vɪkˈtɔːriəs/", "adj. 胜利的/得胜的",
     "「维克特瑞斯」—— 维克的特别瑞斯胜利了 🥇",
     "The <b>victorious</b> team celebrated with champagne."),

    ("victory", "/ˈvɪktəri/", "n. 胜利/成功",
     "「维克特瑞」—— 维克特瑞取得胜利 🏆",
     "The election was a landslide <b>victory</b> for the party."),

    ("vigilant", "/ˈvɪdʒɪlənt/", "adj. 警惕的/警觉的",
     "「为之冷特」—— 为了之冷静特别警惕 👀",
     "Security guards must remain <b>vigilant</b> at all times."),

    ("vigorous", "/ˈvɪɡərəs/", "adj. 精力充沛的/强有力的",
     "「为哥弱死」—— 为了哥弱死是不可能的，精力充沛 💪",
     "The CEO launched a <b>vigorous</b> defense of the company's policies."),

    ("vine", "/vaɪn/", "n. 藤/葡萄藤/攀援植物",
     "「外恩」—— 外面的恩赐是葡萄藤 🍇",
     "Grapes hung heavily from the <b>vine</b>."),

    ("violence", "/ˈvaɪələns/", "n. 暴力/暴行/激烈",
     "「外俄冷斯」—— 外面的俄国冷斯暴力 🚫",
     "The government condemned the use of <b>violence</b> against civilians."),

    ("violent", "/ˈvaɪələnt/", "adj. 暴力的/猛烈的/剧烈的",
     "「外俄冷特」—— 外面俄国的冷特暴力 ⚔️",
     "The region has experienced <b>violent</b> storms recently."),

    ("violin", "/ˌvaɪəˈlɪn/", "n. 小提琴",
     "「外俄林」—— 外面的俄国林子里拉小提琴 🎻",
     "She has been playing the <b>violin</b> since she was six."),

    ("virtually", "/ˈvɜːtʃuəli/", "adv. 几乎/实质上/虚拟地",
     "「我去俄里」—— 我去俄国里的几乎 💻",
     "The company <b>virtually</b> dominates the smartphone market."),

    ("virus", "/ˈvaɪrəs/", "n. 病毒/电脑病毒",
     "「外若死」—— 外面如果死了，是病毒 🦠",
     "A computer <b>virus</b> infected thousands of devices overnight."),

    ("viscous", "/ˈvɪskəs/", "adj. 黏稠的/黏性的",
     "「为斯科死」—— 为了斯科死黏稠的 🍯",
     "The <b>viscous</b> liquid flowed slowly out of the container."),

    ("vocation", "/vəʊˈkeɪʃn/", "n. 职业/天职/使命感",
     "「偶剋神」—— 偶剋了神，这是我的使命 💼",
     "Teaching has always been her true <b>vocation</b>."),

    ("vogue", "/vəʊɡ/", "n. 时尚/流行/风行",
     "「呕哥」—— 呕了哥还这么时尚 👗",
     "Minimalism is back in <b>vogue</b> this season."),

    ("void", "/vɔɪd/", "n. 空虚/空白/无效 adj. 空的",
     "「我的」—— 我的世界一片空白 🕳️",
     "The contract was declared null and <b>void</b>."),

    ("volatile", "/ˈvɒlətaɪl/", "adj. 不稳定的/易挥发的/反复无常的",
     "「窝了太哦」—— 窝了太哦，情绪不稳定 🎢",
     "The stock market has been highly <b>volatile</b> this week."),

    ("volley", "/ˈvɒli/", "n. 截击/齐射/连发",
     "「我里」—— 我里面的连发球 🎾",
     "The tennis player returned with a sharp <b>volley</b>."),

    ("voltage", "/ˈvəʊltɪdʒ/", "n. 电压/伏特数",
     "「偶踢只」—— 偶尔踢一只，电压过高 ⚡",
     "Check the <b>voltage</b> before plugging in the appliance."),

    ("vote", "/vəʊt/", "v./n. 投票/选举/表决",
     "「偶特」—— 偶特别要投票 🗳️",
     "Every citizen has the right to <b>vote</b>."),

    ("voter", "/ˈvəʊtə/", "n. 投票者/选举人",
     "「偶特」—— 偶特就是投票人 👤",
     "The candidate appealed to young <b>voters</b>."),

    ("voucher", "/ˈvaʊtʃə/", "n. 优惠券/代金券/凭证",
     "「我扯」—— 我扯了一张优惠券 🎫",
     "You can redeem this <b>voucher</b> at any of our stores."),

    ("vow", "/vaʊ/", "n./v. 誓言/发誓/郑重宣告",
     "「我」—— 我发誓！🤞",
     "They exchanged wedding <b>vows</b> in a beautiful garden."),

    ("vowel", "/ˈvaʊəl/", "n. 元音",
     "「我哦」—— 我哦，都是元音 🔤",
     "English has five basic <b>vowels</b>: a, e, i, o, u."),

    ("voyage", "/ˈvɔɪɪdʒ/", "n./v. 航行/航海/旅行",
     "「我一只」—— 我一只船去航行 ⛵",
     "The <b>voyage</b> across the Atlantic took three weeks."),

    ("vulgar", "/ˈvʌlɡə/", "adj. 粗俗的/庸俗的/普通的",
     "「挖哥」—— 挖哥说话很粗俗 😒",
     "His <b>vulgar</b> language shocked everyone at the dinner party."),

    ("wade", "/weɪd/", "v. 涉水/艰难前行",
     "「威的」—— 威严地涉水前行 🌊",
     "We had to <b>wade</b> through the flooded street."),

    ("wag", "/wæɡ/", "v. 摇摆/摇动 n. 爱说笑的人",
     "「外哥」—— 外面的哥摇着尾巴 🐕",
     "The dog <b>wagged</b> its tail happily."),

    ("wagon", "/ˈwæɡən/", "n. 马车/货车/旅行车",
     "「外根」—— 外面的根在马车里 🛒",
     "Pioneers traveled west in covered <b>wagons</b>."),

    ("waist", "/weɪst/", "n. 腰部/腰围",
     "「威斯特」—— 威斯特的腰很细 👖",
     "She wore a belt around her <b>waist</b>."),

    ("waive", "/weɪv/", "v. 放弃/免除/搁置",
     "「威舞」—— 威严地舞动，放弃了权利 📋",
     "The bank agreed to <b>waive</b> the late payment fee."),

    ("wake", "/weɪk/", "v. 醒来/唤醒 n. 尾迹/守灵",
     "「威客」—— 威客醒来就工作 ☀️",
     "I usually <b>wake</b> up at six in the morning."),

    ("walnut", "/ˈwɔːlnʌt/", "n. 核桃/胡桃木",
     "「窝拿特」—— 窝里拿的特别核桃 🥜",
     "The table is made of solid <b>walnut</b> wood."),

    ("wander", "/ˈwɒndə/", "v. 漫步/闲逛/走神",
     "「忘的」—— 忘记目的地，到处闲逛 🚶",
     "We spent the afternoon <b>wandering</b> through the old town."),

    ("wardrobe", "/ˈwɔːdrəʊb/", "n. 衣柜/全部衣物",
     "「窝的肉布」—— 窝里的肉布放进衣柜 👔",
     "She donated half her <b>wardrobe</b> to charity."),

    ("ware", "/weə/", "n. 商品/制品/器皿",
     "「外耳」—— 外面的耳朵要买商品 🛍️",
     "Stallholders displayed their ceramic <b>ware</b> at the fair."),

    ("warehouse", "/ˈweəhaʊs/", "n. 仓库/货栈",
     "「外耳耗死」—— 外面耳朵都耗死在仓库里 🏭",
     "The goods are stored in a large <b>warehouse</b> near the port."),

    ("warfare", "/ˈwɔːfeə/", "n. 战争/冲突/斗争",
     "「我飞儿」—— 我飞到儿子那里，战争 ⚔️",
     "Modern <b>warfare</b> relies heavily on technology."),

    ("warrior", "/ˈwɒriə/", "n. 战士/勇士/斗士",
     "「我瑞儿」—— 我的瑞儿是勇士 🛡️",
     "The ancient <b>warrior</b> was buried with his sword and shield."),

    ("waterproof", "/ˈwɔːtəpruːf/", "adj./n. 防水的/雨衣",
     "「窝特普入夫」—— 窝特别普入的防水夫 ☔",
     "You need a <b>waterproof</b> jacket for the hike."),

    ("waver", "/ˈweɪvə/", "v. 摇摆/动摇/犹豫",
     "「威我」—— 威严的我也会动摇 🎭",
     "Her determination never <b>wavered</b> despite the difficulties."),

    ("wax", "/wæks/", "n. 蜡 v. 上蜡/增大",
     "「外克斯」—— 外面克斯打蜡 🕯️",
     "The floor has been freshly <b>waxed</b> and polished."),

    ("weather", "/ˈweðə/", "n. 天气 v. 经受住/风雨侵蚀",
     "「外则」—— 外面的法则看天气 🌤️",
     "The company has <b>weathered</b> several economic storms."),

    ("weave", "/wiːv/", "v. 编织/编排/迂回行进",
     "「威武」—— 威武地编织 🧶",
     "She learned to <b>weave</b> baskets from palm leaves."),

    ("weaver", "/ˈwiːvə/", "n. 织布工/编织者",
     "「威我」—— 威严的我就是织布工 🕸️",
     "The <b>weaver</b> spent hours creating the intricate pattern."),

    ("web", "/web/", "n. 网/网络/蛛网",
     "「外部」—— 外部的网 🌐",
     "A spider spun its <b>web</b> across the doorway."),

    ("wedding", "/ˈwedɪŋ/", "n. 婚礼/结婚庆典",
     "「外顶」—— 外公的顶上婚礼 👰",
     "The <b>wedding</b> ceremony was held in a beautiful church."),

    ("wedge", "/wedʒ/", "n. 楔子/三角块 v. 楔入/挤入",
     "「外只」—— 外面的一只楔子 📐",
     "She used a <b>wedge</b> to keep the door open."),

    ("weed", "/wiːd/", "n. 杂草/野草 v. 除草",
     "「微的」—— 微小的杂草 🌿",
     "I need to pull the <b>weeds</b> out of the vegetable garden."),

    ("weld", "/weld/", "v. 焊接/结合/团结",
     "「外的」—— 外边的焊接在一起 🔧",
     "The two pieces of metal were <b>welded</b> together."),

    ("whilst", "/waɪlst/", "conj. 当...时/然而",
     "「外尔斯特」—— 外面的尔斯特别，然而 🔄",
     "He listened to music <b>whilst</b> driving to work."),

    ("whip", "/wɪp/", "n. 鞭子 v. 鞭打/搅打",
     "「微普」—— 微小的普打就是鞭策 🥚",
     "She <b>whipped</b> the cream until it formed soft peaks."),

    ("whirl", "/wɜːl/", "v./n. 旋转/回旋/眩晕",
     "「窝」—— 窝旋转起来 🌀",
     "The dancer began to <b>whirl</b> across the stage."),

    ("whisper", "/ˈwɪspə/", "v./n. 低语/耳语/悄悄话",
     "「微斯婆」—— 微小的斯婆婆在耳语 🤫",
     "She leaned over to <b>whisper</b> something in his ear."),

    ("whistle", "/ˈwɪsl/", "n. 哨子/口哨 v. 吹口哨",
     "「微搜」—— 微小搜索后用哨子吹 🎶",
     "The referee blew his <b>whistle</b> to stop the game."),

    ("wholesaler", "/ˈhəʊlseɪlə/", "n. 批发商",
     "「吼塞了」—— 吼一声就塞了，批发商 🏪",
     "The <b>wholesaler</b> supplies goods to retailers across the region."),

    ("wholesome", "/ˈhəʊlsəm/", "adj. 有益健康的/有益的",
     "「吼桑」—— 吼桑椹，有益健康 🥗",
     "Children need <b>wholesome</b> food and plenty of exercise."),

    ("wicked", "/ˈwɪkɪd/", "adj. 邪恶的/淘气的/恶劣的",
     "「微剋的」—— 微小的剋人，真是邪恶 😈",
     "The witch in the story is truly <b>wicked</b>."),

    ("width", "/wɪdθ/", "n. 宽度/广度",
     "「微的死」—— 微小的死宽度 📏",
     "The room measures five meters in <b>width</b>."),

    ("wilderness", "/ˈwɪldənəs/", "n. 荒野/荒原/荒凉之地",
     "「微的妮死」—— 微小的妮子死在荒野 🏜️",
     "The cabin was deep in the <b>wilderness</b>, miles from civilization."),

    ("willow", "/ˈwɪləʊ/", "n. 柳树/柳木",
     "「微楼」—— 微小楼边的柳树 🌿",
     "The <b>willow</b> trees bent gracefully over the river."),

    ("winding", "/ˈwaɪndɪŋ/", "adj. 蜿蜒的/曲折的",
     "「外顶」—— 外面的顶蜿蜒曲折 🛤️",
     "We drove along a <b>winding</b> mountain road."),

    ("wisdom", "/ˈwɪzdəm/", "n. 智慧/才智/明智",
     "「微自的姆」—— 微小的自己的姆妈有智慧 🦉",
     "With age comes <b>wisdom</b> and experience."),

    ("wit", "/wɪt/", "n. 机智/风趣/才智",
     "「微特」—— 微小的特别机智 🤓",
     "He is known for his sharp <b>wit</b> and sense of humor."),

    ("withdrawal", "/wɪðˈdrɔːəl/", "n. 撤回/退出/取款/戒毒",
     "「微卓了」—— 微小的卓越撤退了 ⬅️",
     "He made a <b>withdrawal</b> of $500 from his account."),

    ("wither", "/ˈwɪðə/", "v. 枯萎/凋谢/衰弱",
     "「微则」—— 微小的法则，枯萎 🥀",
     "The flowers began to <b>wither</b> in the hot sun."),

    ("withhold", "/wɪðˈhəʊld/", "v. 扣留/拒绝给予/隐瞒",
     "「微着吼的」—— 微着吼着扣留 🤐",
     "The company decided to <b>withhold</b> payment until the work was complete."),

    ("woe", "/wəʊ/", "n. 悲痛/灾难/苦恼",
     "「我」—— 我的悲痛 😢",
     "She told her friend all her <b>woes</b>."),

    ("woods", "/wʊdz/", "n. 树林/森林",
     "「物的子」—— 物的子树，树林 🌲",
     "They went for a walk in the <b>woods</b>."),

    ("wool", "/wʊl/", "n. 羊毛/毛线/毛料",
     "「物」—— 物就是羊毛 🐑",
     "This sweater is made of pure <b>wool</b>."),

    ("wording", "/ˈwɜːdɪŋ/", "n. 措辞/用词/表达方式",
     "「我顶」—— 我的措辞要顶用 ✍️",
     "The <b>wording</b> of the contract needs to be more precise."),

    ("worst", "/wɜːst/", "adj./n. 最坏的/最差的 v. 击败",
     "「我死特」—— 我的死特别糟糕 👎",
     "That was the <b>worst</b> movie I have ever seen."),

    ("wrap", "/ræp/", "v. 包裹/缠绕/用...包",
     "「瑞普」—— 瑞普把礼物包起来 🎁",
     "She carefully <b>wrapped</b> the gift in shiny paper."),

    ("wrench", "/rentʃ/", "n. 扳手/扭伤/痛苦 v. 猛扭",
     "「软吃」—— 软的东西吃了扭伤 🔧",
     "He used a <b>wrench</b> to tighten the bolts."),

    ("wrestle", "/ˈresl/", "v. 摔跤/搏斗/全力应付",
     "「瑞搜」—— 瑞搜了摔跤 🤼",
     "She had to <b>wrestle</b> with a difficult decision."),

    ("wretched", "/ˈretʃɪd/", "adj. 可怜的/悲惨的/恶劣的",
     "「瑞切的」—— 瑞切的可悲 😞",
     "The refugees lived in <b>wretched</b> conditions."),

    ("wring", "/rɪŋ/", "v. 拧/绞/榨取",
     "「瑞嗯」—— 瑞嗯，拧一拧 👋",
     "She <b>wrung</b> out the wet towel."),

    ("wrist", "/rɪst/", "n. 手腕/腕关节",
     "「瑞斯特」—— 瑞斯特扭伤了手腕 ⌚",
     "He broke his <b>wrist</b> during the football game."),

    ("yard", "/jɑːd/", "n. 院子/码(长度单位)/场地",
     "「丫的」—— 丫的院子 🏡",
     "The children were playing in the back <b>yard</b>."),

    ("yawn", "/jɔːn/", "v./n. 打哈欠/裂开",
     "「涌」—— 涌出哈欠 🥱",
     "She tried to stifle a <b>yawn</b> during the meeting."),

    ("yeast", "/jiːst/", "n. 酵母/发酵剂",
     "「衣斯特」—— 衣服斯特需要酵母 🍞",
     "Add some <b>yeast</b> to make the bread rise."),

    ("yolk", "/jəʊk/", "n. 蛋黄/羊毛油脂",
     "「有客」—— 有客人来了，吃点蛋黄 🥚",
     "Separate the egg <b>yolk</b> from the white carefully."),
]


def gen_card(idx, word, phonetic, meaning, meme, example):
    return f'''<div class="vm-word-card">
  <div class="vm-num">#{idx}</div>
  <div class="vm-head"><span class="vm-word">{word}</span><span class="vm-phonetic">{phonetic}</span></div>
  <div class="vm-meaning">{meaning}</div>
  <span class="vm-meme-label vm-label-xieyin">谐音</span>
  <div class="vm-meme">{meme}</div>
  <div class="vm-example">{example}</div>
</div>'''


# Generate the full markdown
lines = []
lines.append("---")
lines.append("title: 单词本_62")
lines.append("---")
lines.append("")
lines.append('<div class="vm-word-cards">')
lines.append("")

base_num = 6101
for i, (word, phonetic, meaning, meme, example) in enumerate(words_data):
    idx = base_num + i
    card = gen_card(idx, word, phonetic, meaning, meme, example)
    lines.append(card)
    lines.append("")

lines.append("</div>")

content = "\n".join(lines)

output_path = r"E:\certify\src\ielts\vocab-meme\wordbook\wordbook-62.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {output_path} with {len(words_data)} word cards (#{base_num} - #{base_num + len(words_data) - 1})")
