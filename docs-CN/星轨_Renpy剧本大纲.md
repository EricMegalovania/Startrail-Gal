# 《星轨》视觉小说剧本大纲
## Ren'Py Galgame改编版

---

## 角色设定

### 主要角色
- **女鸳鸯(女主)**: 成绩优异、性格倔强、内心细腻的女生,初一遇见男鸳鸯后逐渐被他吸引
- **男鸳鸯(男主)**: 学生会副主席、年级前三、有理想抱负但不善表达感情的男生
- **喷火牛**: 男鸳鸯初中时的女友,学姐
- **老化了**: 女鸳鸯八年级时短暂喜欢的对象
- **其他配角**: 很优秀、大家好(男鸳鸯好友)、老样子等

---

## 故事结构(7章+尾声)

---

# 第一章:小小方圆(初中相遇)
**关键词**: 初遇、暗恋、青涩

## 场景1-1: 操场初见(开学第一周)
**时间**: 初一开学
**地点**: 十四中操场

### 剧情描述
女鸳鸯在操场跑完步,遇到小学认识的学姐喷火牛。学姐指着远处的男生说"那是我男朋友"。女鸳鸯眼神不好,没看清那个男生的脸,只是含糊地点头。阳光很刺眼,她不敢抬头看。

### Ren'Py脚本要点
```
scene bg playground with fade
show female_yuanyang normal at left
show hn happy at right

hn "喷火牛!你也在十四中吗?"
female_yuanyang "hi!是呀是呀!"
hn "看,那是我男朋友。"
```

### 心理独白
"刚从小学踏入初中的我,内心还无法接受这个年纪'男朋友'这种称呼...我完全不知道学姐指的是哪个男生。盛夏的阳光有点耀眼,我不敢抬头。"

---

## 场景1-2: QQ上的第一次对话
**时间**: 初一下学期
**地点**: 家中(电脑前)

### 剧情描述
男鸳鸯作为学生会副主席,在QQ上找女鸳鸯,希望她参加二中孔庙的成人礼活动。他"威逼利诱"劝说了很久,女鸳鸯虽然动心但最终因为要补寒假作业而没有答应。

### Ren'Py脚本要点
```
scene bg bedroom_night with fade
show screen phone_chat

male_yuanyangQQ "成人礼活动很有意义的,要不要来参加?"
female_yuanyangQQ "可是...那天是开学前一天啊..."
male_yuanyangQQ "就当是提前感受一下高中的氛围?"
```

### 选项系统
- [接受邀请] → 好感度+5,触发额外剧情
- [委婉拒绝] → 主线剧情,保持距离感

---

## 场景1-3: 诗文朗诵比赛(春天相识)
**时间**: 初一下学期4月末
**地点**: 学校礼堂

### 剧情描述
女鸳鸯和男鸳鸯同时被选为七八年级诗文朗诵比赛的主持人。报幕完毕,女鸳鸯拿着话筒就开始和旁边的人聊天,男鸳鸯一把按下她握住话筒的手,关闭了开关,说:"你这样,话筒会收音的。"这个专业的小动作让女鸳鸯对他印象深刻。

### CG插图建议
- CG1: 男鸳鸯按下女鸳鸯手中话筒的特写镜头(手部交叠)
- CG2: 女鸳鸯在台侧偷看男鸳鸯的侧脸剪影

### Ren'Py脚本要点
```
scene bg auditorium_stage with fade
play sound "microphone_click.wav"
show male_yuanyang serious at center

male_yuanyang "你这样,话筒会收音的。"
show female_yuanyang surprised at left
female_yuanyang_thought "这个人...专业素养好高..."
```

### 心理独白
"我连声道歉,心里却记住了这个在我看来专业素养极高的小动作。"

---

## 场景1-4: 放学后的约定(每日跑步)
**时间**: 初一下学期
**地点**: 教学楼走廊→操场

### 剧情描述
得知男鸳鸯也喜欢跑步后,女鸳鸯开始每天放学后去他教室门口等他一起跑步。男鸳鸯总是慢悠悠地收拾东西,和同学聊天。高大的男生调侃:"哟,男鸳鸯,勾搭小学妹?"女鸳鸯脸红但表面一本正经,倔强地不肯离开。

男鸳鸯穿着白色校服和西裤跑步的模样,慢慢渗入女鸳鸯心里。直至后来,每当看到他正装出现,她的心都会猛地一缩。

### CG插图建议
- CG3: 男鸳鸯白色校服+西裤在操场跑步的背影(夕阳剪影)
- CG4: 女鸳鸯站在教室门口等待的落寞身影

### Ren'Py脚本要点
```
scene bg classroom_after_school with fade
show male_yuanyang normal at right
show classmate tease at center

classmate "哟,男鸳鸯,勾搭小学妹?"
female_yuanyang_thought "我把不好意思的脸红硬生生憋进心里..."

scene bg playground_sunset with dissolve
show male_yuanyang running at right with moveinright
female_yuanyang_thought "他穿着白色校服和西裤的模样,慢慢渗入我心里。"
```

### 情感系统
- 好感度可视化: 心跳动画效果
- 倔强值指标: 影响后续选项

---

## 场景1-5: 年级第一的执念
**时间**: 初一下学期段考
**地点**: 考场→成绩公布

### 剧情描述
女鸳鸯偶然发现男鸳鸯之前和喷火牛的说说,得知学姐成绩平平(年级200多名)。"复仇"之心蠢蠢欲动:"让他和那成绩平平的女生谈恋爱去吧,我要变得更好——至少比你现在要好。"男鸳鸯最好的成绩是年级第三。

段考成绩公布,女鸳鸯考了初中阶段第一个年级第一。这个年级第一,只是因为他。

### Ren'Py脚本要点
```
scene bg exam_room with fade
play music "determination.mp3"

female_yuanyang_thought "让他和那成绩平平的女生谈恋爱去吧..."
female_yuanyang_thought "我要变得更好——至少比你现在要好!"

scene bg school_hallway with fade
show screen score_board
narrator "女鸳鸯 - 年级第一"

female_yuanyang_thought "这件事,我在很久以后才在他面前承认。"
female_yuanyang_thought "当时的年一,只是因为他。"
```

### 成就系统
解锁成就: "因你而优秀"

---

# 第二章:启天之星(暧昧升温)
**关键词**: 暧昧、争吵、成长

## 场景2-1: 辩论赛的深夜讨论
**时间**: 初二
**地点**: 学校食堂→QQ聊天

### 剧情描述
女鸳鸯要参加辩论赛,向男鸳鸯请教。男鸳鸯答应借八年级政治课本,并主动找她跑步边跑边讲辩论内容。有一次在食堂吃饭,女鸳鸯问:"我这样跟你吃饭,喷火牛会有意见吗?"男鸳鸯嗦着粉说:"她不知道。"

### CG插图建议
- CG5: 食堂对坐吃饭的场景(暖光灯下)
- CG6: 夜跑时两人的剪影(星空背景)

### Ren'Py脚本要点
```
scene bg canteen_evening with fade
show male_yuanyang eating at right
show female_yuanyang normal at left

female_yuanyang "我这样跟你吃饭,喷火牛会有意见吗?"
show male_yuanyang casual
male_yuanyang "她不知道。" with hpunch

female_yuanyang_thought "他一边嗦着粉,一边含糊不清地说..."
```

### 心理独白
"我内心已经承认自己喜欢上他了,但谁都不说,只是在自己的课桌里贴上小字条:'每天和41123跑步!'"

---

## 场景2-2: 生存手册项目(夏日协作)
**时间**: 初一升初二暑假
**地点**: 各自家中(远程合作)

### 剧情描述
男鸳鸯拉女鸳鸯入伙做《生存手册》。两人都很有主见,意见相左就开始争论。女鸳鸯从没因为他是学长而"屈服"。后来打电话咨询政教处才得知,这个"任务"并非老师布置,而是由男鸳鸯本人牵头创办的。女鸳鸯逐渐触碰到了他的内心:热情如火,坚如磐石,拥有天海一般宽广的情怀。

### Ren'Py脚本要点
```
scene bg bedroom_day with fade
play sound "phone_call.wav"

female_yuanyang "我觉得这个设计不太合理..."
male_yuanyang "但是从实用性角度来说..."
female_yuanyang "可是美观也很重要啊!"

narrator "后来得知,这个项目是他自己主动发起的..."
female_yuanyang_thought "我逐渐触碰到了他的内心..."
```

---

## 场景2-3: 若即若离的八年级
**时间**: 初二整年
**地点**: 教室走廊、操场等

### 剧情描述
整个八年级是"带着暧昧的平淡"。男鸳鸯和喷火牛分分合合,女鸳鸯"丧失理智般"喜欢上了老化了。起哄的人把焦点转移,两人反而相处得更自然。

男鸳鸯经常直接走进女鸳鸯班里,还没抬头就听到他的声音。规律是:若某天放学突然来找,第二天他必有重大考试。

### Ren'Py脚本要点
```
scene bg classroom_afternoon with fade
play sound "footsteps.wav"
show male_yuanyang happy at center with moveinleft

classmate1 "哟,来找女鸳鸯?"
show female_yuanyang embarrassed at left
female_yuanyang_thought "又来了..."

male_yuanyang "明天考试,想找你借笔记看看。"
female_yuanyang_thought "果然...这个规律屡试不爽。"
```

---

## 场景2-4: 考前的陪伴(中考倒计时)
**时间**: 初三中考前
**地点**: 男鸳鸯教室→小区门口

### 剧情描述
在男鸳鸯三次模拟考前一天,他必定下来找女鸳鸯。很晚的时候,女鸳鸯陪他走回教室收拾东西,看他把物理实验盒拎回家。教室里只有两个人,没开灯。女鸳鸯站在他身后,脑海里蹦出:"我可以抱抱你吗?作为朋友。"但最终话到嘴边变成:"收拾好了没,走吧。"

女鸳鸯慢慢陪他走,从教室到小区门口,再折回学校。

### CG插图建议
- **CG7(关键场景)**: 黑暗教室里,女鸳鸯站在男鸳鸯身后的剪影(月光透过窗户)
- CG8: 小区门口道别的背影(路灯下)

### Ren'Py脚本要点
```
scene bg classroom_night with fade
play music "melancholy.mp3"
show male_yuanyang packing at right
show female_yuanyang standing at left

female_yuanyang_thought "我可以抱抱你吗?作为朋友。"
female_yuanyang_thought "......"
female_yuanyang "收拾好了没,走吧。"

scene bg school_gate_night with fade
narrator "她陪他走到小区门口,再折回学校。"
```

### 选项系统(回忆模式)
- [说出真心话] → 触发BE线(过早表白)
- [继续沉默] → 主线继续

---

## 场景2-5: 跳绳与物理分析(趣味日常)
**时间**: 初三冬末春初
**地点**: 教室走廊

### 剧情描述
临近中考,男鸳鸯带着很优秀、大家好来找女鸳鸯。女鸳鸯在走廊跳绳,三个男生站在她面前用物理知识分析"为什么跳绳打到人会痛"。跳完一组,女鸳鸯挑眉似笑非笑,做出要甩绳子的样子:"你要不要自己试试跳绳打人为什么痛?"

### Ren'Py脚本要点
```
scene bg hallway_day with fade
play sound "rope_jumping.wav"
show female_yuanyang jumping at center
show male_yuanyang thinking at right
show friends at left

friends "从动能转化的角度来说..."
male_yuanyang "还有撞击面积的因素..."

show female_yuanyang smirk
female_yuanyang "你要不要自己试试跳绳打人为什么痛?"
show male_yuanyang panic
```

---

## 场景2-6: 启天跨年夜(初次约会)
**时间**: 跨年夜
**地点**: 二中启天楼

### 剧情描述
男鸳鸯送给女鸳鸯二中启天跨年的票。跨年夜那晚,两人一起参加活动。(可设计为小游戏/互动环节)

### Ren'Py脚本要点
```
scene bg qitian_night with fade
play music "celebration.mp3"
show fireworks animation

narrator "这是我们第一次单独出来参加活动。"
female_yuanyang_thought "他今晚穿着正装...心跳得好快。"
```

### Mini Game
- 跨年倒计时互动
- 烟花许愿选项

---

# 第三章:沅芷澧兰(高中恋爱)
**关键词**: 表白、甜蜜、分歧初现

## 场景3-1: 凤岭之巅的告白
**时间**: 初三升高一暑假
**地点**: 凤岭儿童公园顶层平台(夜晚)

### 剧情描述
这是整个故事最关键的转折点。女鸳鸯和男鸳鸯约在凤岭儿童公园见面。天色渐暗,两人来到顶层平台。男鸳鸯带着前所未有的认真和坚定,说出那句:"我喜欢你,我们在一起吧。"

### CG插图建议
- **CG9(重要!!)**: 凤岭之巅告白场景 - 夜空繁星,男鸳鸯认真的表情,女鸳鸯震惊的眼神
- **CG10**: 拥抱/牵手的特写(可做H-scene过渡)

### Ren'Py脚本要点
```
scene bg fengling_top_night with fade
play music "confession.mp3"
show male_yuanyang serious at right
show female_yuanyang surprised at left

male_yuanyang "女鸳鸯。"
female_yuanyang "嗯?"
male_yuanyang "我喜欢你。我们在一起吧。"

show female_yuanyang shocked
female_yuanyang_thought "!!!"
female_yuanyang_thought "女生的直觉不会有错...但当他真的说出来的时候..."

menu:
    "我...我也喜欢你":
        $ relationship = "together"
        jump together_route
    
    "我需要时间考虑":
        $ relationship = "pending"
        jump thinking_route
```

### 情感系统触发
- 解锁成就: "凤岭之约"
- BGM切换为专属恋爱主题曲
- 开启恋爱模式UI

---

## 场景3-2: 确认关系后的甜蜜
**时间**: 高一
**地点**: 学校、约会地点

### 剧情描述
在一起后的甜蜜时光。两人在学校小心翼翼地维持着公开的秘密,偶尔的眼神交流、放学后的约会、深夜的QQ聊天。

### 片段集锦
- 图书馆一起自习
- 操场跑步(回忆初见)
- 第一次牵手
- 节日礼物交换

### Ren'Py脚本要点
```
scene bg library with fade
show male_yuanyang reading at right
show female_yuanyang studying at left

narrator "我们在同一张桌子上学习,脚在桌子下轻轻碰触。"

scene bg playground_sunset with dissolve
narrator "一起跑步时,他会放慢速度等我。"

scene bg street_evening with fade
narrator "放学后,我们牵着手在小巷里散步。"
```

### (成人向场景暗示)
**首次亲吻场景**
```
scene bg park_bench_night with fade
show female_yuanyang shy at left
show male_yuanyang gentle at right

male_yuanyang "可以吗?"
female_yuanyang "...嗯。"

scene black with fade
play sound "heartbeat.wav"
narrator "他的唇轻轻覆上来..."

[渐入黑屏,配以心跳音效]
[选择是否观看详细CG]
```

---

## 场景3-3: 生日惊喜(甜蜜高光)
**时间**: 男鸳鸯生日
**地点**: 男鸳鸯家/餐厅

### 剧情描述
女鸳鸯精心准备生日惊喜。这是两人感情的高光时刻之一。

### Ren'Py脚本要点
```
scene bg restaurant with fade
show female_yuanyang excited at left
show male_yuanyang surprised at right

female_yuanyang "生日快乐!"
male_yuanyang "你怎么...这么用心..."
female_yuanyang "因为你值得啊。"

show male_yuanyang touched
male_yuanyang_thought "我何德何能...拥有这样的女孩。"
```

---

## 场景3-4: 矛盾初现(沟通问题)
**时间**: 高一下学期
**地点**: QQ聊天/电话

### 剧情描述
男鸳鸯开始不回消息,或回复很官方。女鸳鸯需要频繁的交流和情感确认,而男鸳鸯觉得"感情稳定"就不需要太多表达。矛盾开始累积。

### Ren'Py脚本要点
```
scene bg bedroom_night with fade
show screen phone_chat

female_yuanyangQQ "你在忙吗?"
female_yuanyangQQ "怎么不回消息?"
[等待30秒]
female_yuanyangQQ "......"

narrator "一小时后"
male_yuanyangQQ "在做作业,怎么了?"

female_yuanyang_thought "只是...想和你说说话..."
```

### 情感系统
- 幸福度开始下降
- 矛盾值开始累积

---

## 场景3-5: 首次争吵
**时间**: 高二
**地点**: 电话/见面

### 剧情描述
因为回消息频率问题,两人发生首次激烈争吵。女鸳鸯哭着挂断电话,男鸳鸯站在原地不知所措。

### Ren'Py脚本要点
```
scene bg bedroom_night with fade
play sound "phone_call.wav"

female_yuanyang "你为什么就不能多花点时间陪我聊聊天?!"
male_yuanyang "我...我有在忙正事..."
female_yuanyang "所以和我说话就不是正事了?!"
male_yuanyang "我不是这个意思..."

play sound "phone_hangup.wav"
scene black with fade

male_yuanyang_thought "我...做错了什么?"
```

---

# 第四章:凤岭之巅(回忆与现实交织)
**关键词**: 反思、成长、大学分离

## 场景4-1: 大学的分离
**时间**: 高三毕业→大一
**地点**: 不同城市

### 剧情描述
女鸳鸯在北京上大学,男鸳鸯在武汉。异地恋让问题更加凸显。女鸳鸯需要频繁联系,男鸳鸯却忙于社团和学业。

### Ren'Py脚本要点
```
scene bg university_beijing with fade
show female_yuanyang lonely at center

female_yuanyang_thought "他已经两天没回我消息了..."
female_yuanyang_thought "我在北京,他在武汉...我们的距离越来越远。"

scene bg university_wuhan with dissolve
show male_yuanyang busy at center

male_yuanyang_thought "又有社团活动...等忙完再回她吧。"
```

---

## 场景4-2: 矛盾的爆发(争吵加剧)
**时间**: 大一
**地点**: 视频通话

### 剧情描述
频繁的争吵让两人都疲惫不堪。男鸳鸯说出"没把你放在很重要的位置是正确的决定",这句话成为压垮女鸳鸯的最后一根稻草。

### Ren'Py脚本要点
```
scene bg video_call with fade
show male_yuanyang tired at right
show female_yuanyang angry at left

male_yuanyang "我每天给你发表情,都落下了课程..."
female_yuanyang "所以你是在怪我?!"
male_yuanyang "我只是说...没把你放在很重要的位置是正确的决定。"

show female_yuanyang hurt
female_yuanyang_thought "......他竟然说出这种话。"
female_yuanyang "我明白了。"
```

---

## 场景4-3: 分手决定(痛苦抉择)
**时间**: 大一
**地点**: 女鸳鸯宿舍

### 剧情描述
女鸳鸯写下分手信。她承认自己犯过错,但也认为这段感情已经只剩痛苦。"我累了,不想和你再生气吵架。"

### CG插图建议
- **CG11**: 女鸳鸯在深夜写信的背影(泪痕)
- CG12: 男鸳鸯收到信息后呆坐的侧脸

### Ren'Py脚本要点
```
scene bg dorm_night with fade
play music "sadness.mp3"
show female_yuanyang crying at center

female_yuanyang_thought "我要写下来...把一切都说清楚。"
narrator "她打开电脑,开始敲打键盘。"

[显示分手信部分内容]
narrator "到最后这段感情给我只剩下了痛苦。"
narrator "我真的累了,不想和你再生气吵架。"

scene black with fade
narrator "发送。"
```

### 情感系统
- 关系状态: 分手
- 解锁成就: "繁花落幕"

---

# 第五章:潮起潮落(分手后的迷茫)
**关键词**: 疗伤、新恋情、反思

## 场景5-1: 分手后的空白期
**时间**: 大一下学期
**地点**: 北京

### 剧情描述
分手后,女鸳鸯试图让自己忙起来。参加社团、努力学习、认识新朋友。但夜深人静时,还是会想起男鸳鸯。

### Ren'Py脚本要点
```
scene bg university_campus with fade
show female_yuanyang smile_fake at center

narrator "她在朋友面前笑得很开心..."
scene bg dorm_night with dissolve
show female_yuanyang crying at center
narrator "但回到宿舍,眼泪止不住。"

female_yuanyang_thought "六年...就这样结束了。"
```

---

## 场景5-2: 新的开始?(第二任)
**时间**: 大一下学期
**地点**: 大学

### 剧情描述
女鸳鸯遇到新的男生,开始新恋情。但她很快发现,自己无法像爱男鸳鸯一样爱任何人。

### Ren'Py脚本要点
```
scene bg cafe with fade
show female_yuanyang normal at left
show new_boyfriend at right

new_bf "你在想什么?"
female_yuanyang "没...没什么。"
female_yuanyang_thought "可是我脑海里想的...还是男鸳鸯。"
```

---

## 场景5-3: 无法遗忘
**时间**: 大二
**地点**: 各地

### 剧情描述
女鸳鸯和第二任也分手了。她意识到:"我再也不可能像爱男鸳鸯一样爱上任何人。"她跟所有人反复提到的都是男鸳鸯的故事。

### Ren'Py脚本要点
```
scene bg therapy_room with fade
narrator "我和每一个人讲起我和你共同成长的青春。"
narrator "我用你的模样写出我理想对象的模板。"

female_yuanyang_thought "我已经永久地在心里给他划了一片自留地。"
```

---

# 第六章:翻山越岭(各自成长)
**关键词**: 蜕变、成熟、重逢

## 场景6-1: 两年后的成长
**时间**: 分手一年半后
**地点**: 武汉/北京

### 剧情描述
男鸳鸯在这段时间内有了巨大改变。他学会了沟通,学会了表达,不再是那个不回消息的男孩。女鸳鸯也在独立和成长,但心里始终有个位置属于男鸳鸯。

### Ren'Py脚本要点
```
scene bg wuhan_university with fade
show male_yuanyang mature at center

male_yuanyang_thought "我终于明白,感情需要经营。"
male_yuanyang_thought "我终于明白,她需要的不是物质,而是陪伴。"

scene bg beijing_university with dissolve
show female_yuanyang independent at center

female_yuanyang_thought "我可以一个人很好...但还是会想起他。"
```

---

## 场景6-2: 偶然的联系
**时间**: 2025年夏
**地点**: 社交软件

### 剧情描述
男鸳鸯主动联系女鸳鸯。从日常寒暄开始,慢慢恢复交流。

### Ren'Py脚本要点
```
scene bg bedroom_day with fade
show screen phone_notification
play sound "message.wav"

female_yuanyang_thought "是他...?"
male_yuanyangQQ "最近怎么样?"

menu:
    "回复他":
        female_yuanyangQQ "还好,你呢?"
    "不理会":
        narrator "但她还是忍不住点开了聊天框..."
```

---

## 场景6-3: 重新了解彼此
**时间**: 2025年夏末
**地点**: 线上交流

### 剧情描述
两人开始频繁聊天。女鸳鸯发现男鸳鸯真的变了——他变得主动,变得会聊天,变得懂得表达情感。

### Ren'Py脚本要点
```
scene bg chat_montage with fade
narrator "他们开始每天聊天..."
narrator "从日常琐事,到人生思考..."
narrator "她发现,他真的变了。"

female_yuanyang_thought "他...是我熟悉的他,但又不完全是。"
female_yuanyang_thought "他成长了。"
```

---

# 第七章:回到原点(复合之路)
**关键词**: 表白、决定、承诺

## 场景7-1: 再次告白(关键转折)
**时间**: 2025年夏
**地点**: 线上/见面

### 剧情描述
男鸳鸯再次表白:"我一直喜欢你啊,你不会不知道吧。分手以后我还没有喜欢过别人。"

女鸳鸯震惊又感动。她开始思考:"我还喜欢他吗?我们还有可能吗?"

### CG插图建议
- **CG13(重要)**: 男鸳鸯认真表白的特写
- **CG14**: 女鸳鸯流泪的侧脸

### Ren'Py脚本要点
```
scene bg video_call with fade
show male_yuanyang serious at right
show female_yuanyang shocked at left

male_yuanyang "我一直喜欢你啊,你不会不知道吧。"
show female_yuanyang crying
female_yuanyang "你..."
male_yuanyang "分手以后我还没有喜欢过别人。"

female_yuanyang_thought "他说的是真的..."
female_yuanyang_thought "他...一直在等我。"
```

---

## 场景7-2: 内心挣扎(思考篇)
**时间**: 表白后数天
**地点**: 女鸳鸯宿舍

### 剧情描述
女鸳鸯陷入巨大的内心挣扎。她列出"执念"和"问题"两部分(对应原文附录二)。

### 执念部分
- 他塑造了半个我
- 我的择偶标准就是按他的样子写的
- 我再也不可能像爱他一样爱任何人
- 我无法全身心地爱除了他以外的第二个人

### 问题部分
- 他还是原来那个他吗?
- 分手的原因解决了吗?
- 我还喜欢他吗?
- 三观是否契合?

### Ren'Py脚本要点
```
scene bg dorm_night with fade
show female_yuanyang thinking at center

female_yuanyang_thought "我需要理性分析..."
narrator "[显示思考清单]"

female_yuanyang_thought "但当我问自己..."
female_yuanyang_thought "我越问越觉得不可替代的就是他本人。"
show female_yuanyang crying
female_yuanyang_thought "我真的哭了...我真的是在爱他整个人。"
```

---

## 场景7-3: 复合决定(高潮)
**时间**: 思考后的某天
**地点**: 视频/见面

### 剧情描述
女鸳鸯做出决定。"我愿意再一次相信,再试一次。我没有后路,只能相信,只能面对,只能解决所有问题。"

### CG插图建议
- **CG15(关键!!)**: 复合时的拥抱(可设计H-scene过渡)
- **CG16**: 两人牵手的特写(对应初恋时的牵手形成呼应)

### Ren'Py脚本要点
```
scene bg meeting_place with fade
play music "reunion.mp3"
show male_yuanyang nervous at right
show female_yuanyang determined at left

male_yuanyang "你...考虑得怎么样?"
female_yuanyang "我想通了。"
show male_yuanyang hopeful
female_yuanyang "我愿意...再试一次。"

show male_yuanyang happy
male_yuanyang "真的?!"
female_yuanyang "我没有后路...只能相信你。"
female_yuanyang "只能面对,只能解决所有问题。"

scene cg_reunion_hug with fade
narrator "他紧紧抱住她..."
narrator "这一次,不会再放手。"
```

### 成就系统
- 解锁成就: "回到原点"
- 解锁成就: "八年等待"
- 解锁True End路线

---

## 场景7-4: 复合宣言(情感升华)
**时间**: 复合当天
**地点**: 深夜对话

### 剧情描述
两人深夜长谈,说出彼此的心声(对应原文"复合那天"的对话)。

### 经典台词
```
male_yuanyang "我的一半是你赋予的。"
female_yuanyang "我再也不会像爱他一样爱上别人了。"
male_yuanyang "爱是最大的理由,压倒所有。"
female_yuanyang "用了两个月来思考自己到底喜欢什么样的人,用了两个小时来决定和他复合。"
```

### Ren'Py脚本要点
```
scene bg night_call with fade
play music "promise.mp3"

male_yuanyang "我的一半是你赋予的。"
show female_yuanyang touched
female_yuanyang "我也是...你塑造了我三观里最重要的部分。"

male_yuanyang "那么这一次,一辈子好吗?"
female_yuanyang "一辈子。"

scene black with fade
narrator "事与愿违,爱是最大的理由,压倒所有。"
```

---

# 尾声:时间的见证
**关键词**: 未来、承诺、祝福

## 场景尾声-1: 复合后的幸福
**时间**: 复合后
**地点**: 各种日常场景

### 剧情描述
两人重新在一起后的甜蜜日常。这一次,他们更加珍惜彼此。

### 片段蒙太奇
- 一起旅行
- 一起学习
- 视频聊天到深夜
- 节日纪念日

### Ren'Py脚本要点
```
scene bg travel_montage with fade
narrator "他们一起去了很多地方..."

scene bg video_call_happy with dissolve
narrator "即使异地,也每天视频..."

scene bg anniversary with fade
narrator "每一个纪念日都认真庆祝..."
```

---

## 场景尾声-2: 飞机上的完稿(原文后记)
**时间**: 2025年10月5日
**地点**: 上海飞往柳州的航班上

### 剧情描述
女鸳鸯在飞机上完成这本书。男鸳鸯睡在她肩膀上,她看着他,回忆这八年的一切。

### CG插图建议
- **CG17(结局CG)**: 飞机上,男鸳鸯睡在女鸳鸯肩上,女鸳鸯看着电脑屏幕微笑

### Ren'Py脚本要点
```
scene bg airplane_cabin with fade
play music "epilogue.mp3"
show male_yuanyang sleeping at right
show female_yuanyang writing at left

female_yuanyang_thought "我们现在坐在从上海浦东飞往柳州白莲的航班上。"
female_yuanyang_thought "你睡得很香..."
narrator "她看着他,眼里满是温柔。"

female_yuanyang_thought "我从未如此清醒地疯狂:"
female_yuanyang_thought "我要和你度过我的漫漫余生。"
```

---

## 场景尾声-3: 未来的承诺(结局)
**时间**: 未来展望
**地点**: 幻想场景

### 剧情描述
女鸳鸯在心中默念未来的承诺——领证时要说的话,结婚时要说的话。

### CG插图建议
- **CG18(完美结局)**: 婚礼场景(幻想)/领证照(幻想)
- CG19: 两人在星空下的背影(呼应"星轨"标题)

### Ren'Py脚本要点
```
scene white_fade with fade
play music "future.mp3"

female_yuanyang_thought "时间啊时间,请做这对恋人的护佑神..."
female_yuanyang_thought "让我在领证的时候写下:"
narrator "'我终于嫁给了我十三岁就喜欢上的男孩。'"

scene bg wedding_fantasy with fade
female_yuanyang_thought "让我在结婚的时候写下:"
narrator "'和你的一切是我生命中的奇迹,我的祷告终于有了回音。'"

scene bg starry_sky with fade
show silhouette_couple at center
narrator "八年的星轨,终于交汇。"
narrator "这一次,永不分离。"

scene black with fade
show text "THE END - True End Achieved" with dissolve
play music "credits.mp3"
```

### 结局评价系统
- **True End**: "永恒的星轨" (复合+美满未来)
- **Good End**: "各自精彩" (分手但成长)
- **Bad End**: "错过一生" (未能解决矛盾)

---

# 额外内容建议

## 回忆录系统
解锁条件: 完成主线后
内容: 可重新体验关键场景,查看所有CG

## 角色语音
- 关键场景配音
- 经典台词语音回放

## 书信系统
解锁原文中的六封书信内容,作为额外剧情

## 成就系统
- "初见之缘" - 完成第一章
- "因你而优秀" - 取得年级第一
- "凤岭之约" - 首次告白成功
- "繁花落幕" - 经历分手
- "八年等待" - 完成全部章节
- "永恒星轨" - 达成True End
- "完美收藏家" - 收集所有CG

## 迷你游戏
- 跑步小游戏(操场跑圈)
- 辩论赛答题
- 考试系统(影响剧情走向)

---

## 成人内容场景建议(18+)

### 亲密场景1: 高一确认关系后
**场景**: 男鸳鸯家中
**CG**: 初吻→拥抱→抚摸(可选详细程度)

### 亲密场景2: 高二纪念日
**场景**: 酒店/家中
**CG**: 第一次(温馨浪漫向)

### 亲密场景3: 大学暑假相聚
**场景**: 女鸳鸯宿舍/酒店
**CG**: 异地重逢的激情

### 亲密场景4: 复合后
**场景**: 旅行途中
**CG**: 成熟的爱(激情+温情)

所有成人场景设置:
- 可选跳过
- 可选详细程度(暗示/部分/完整)
- 配合音效和特殊效果
- 注重情感表达而非纯粹色情

---

## Ren'Py技术要点

### 角色定义
```python
define y = Character("女鸳鸯", color="#FFB6C1")
define k = Character("男鸳鸯", color="#4169E1")
define narrator = Character(None, kind=nvl)
```

### 变量系统
```python
default affection = 0  # 好感度
default conflict = 0  # 矛盾值
default relationship_status = "strangers"  # 关系状态
```

### 分支系统
根据玩家选择影响:
- 好感度积累
- 矛盾处理方式
- 最终结局走向

### 音乐配置
- BGM: 日常、紧张、浪漫、悲伤、欢快等多种主题
- SE: 脚步声、电话铃声、心跳声等

### 特效建议
- 回忆闪回特效
- 心跳特效(心动时刻)
- 时间流逝效果
- 天气变化效果

---

## 总结

这个改编剧本保留了原作的核心情感线和关键情节,适合制作成多结局的视觉小说。建议制作时长约8-12小时,包含:
- 主线剧情7章
- 18+可选内容4段
- CG总数: 建议19张(含变体可达30+)
- 结局: 3种主要结局+若干BE
- 额外系统: 回忆录、成就、书信等

整体风格:青春、纯爱、治愈,带有淡淡忧伤但最终圆满的基调。
