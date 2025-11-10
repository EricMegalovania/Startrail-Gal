# 星轨 - Ren'Py Script Example
# 示例场景实现代码

##############################################
# 角色定义 (characters.rpy)
##############################################

# 主要角色
define y = Character("女鸳鸯", color="#FFB6C1", image="female_yuanyang")
define k = Character("男鸳鸯", color="#4169E1", image="male_yuanyang")

# 配角
define hn = Character("喷火牛", color="#DDA0DD")
define hl = Character("老化了", color="#98FB98")
define classmate = Character("同学", color="#D3D3D3")
define narrator = Character(None)

# 旁白模式
define nvl_narrator = Character(None, kind=nvl)

##############################################
# 图像定义 (images.rpy)
##############################################

# 背景
image bg playground = "images/bg/playground.jpg"
image bg classroom = "images/bg/classroom.jpg"
image bg fengling_night = "images/bg/fengling_night.jpg"
image bg airplane = "images/bg/airplane_cabin.jpg"

# 角色立绘
image female_yuanyang normal = "images/characters/female_yuanyang_normal.png"
image female_yuanyang happy = "images/characters/female_yuanyang_happy.png"
image female_yuanyang sad = "images/characters/female_yuanyang_sad.png"
image female_yuanyang shy = "images/characters/female_yuanyang_shy.png"
image female_yuanyang angry = "images/characters/female_yuanyang_angry.png"
image female_yuanyang crying = "images/characters/female_yuanyang_crying.png"

image male_yuanyang normal = "images/characters/male_yuanyang_normal.png"
image male_yuanyang happy = "images/characters/male_yuanyang_happy.png"
image male_yuanyang serious = "images/characters/male_yuanyang_serious.png"
image male_yuanyang shy = "images/characters/male_yuanyang_shy.png"

# CG图
image cg_first_meeting = "images/cg/cg01_first_meeting.jpg"
image cg_confession = "images/cg/cg09_confession.jpg"
image cg_reunion = "images/cg/cg15_reunion.jpg"
image cg_ending = "images/cg/cg17_ending.jpg"

##############################################
# 变量定义 (variables.rpy)
##############################################

default affection = 0  # 好感度 (0-100)
default conflict_level = 0  # 矛盾等级 (0-100)
default relationship_status = "strangers"  # 关系状态
default player_name = "玩家"  # 玩家名字(如果需要自定义)

# 剧情标记
default met_first_time = False
default confession_accepted = False
default broke_up = False
default reunited = False

# 选项记录
default choices_made = []

##############################################
# 音乐定义 (audio.rpy)
##############################################

# 背景音乐
define audio.bgm_daily = "audio/music/daily_life.mp3"
define audio.bgm_romantic = "audio/music/romantic.mp3"
define audio.bgm_tension = "audio/music/tension.mp3"
define audio.bgm_sadness = "audio/music/sadness.mp3"
define audio.bgm_confession = "audio/music/confession.mp3"
define audio.bgm_reunion = "audio/music/reunion.mp3"

# 音效
define audio.sfx_heartbeat = "audio/sfx/heartbeat.wav"
define audio.sfx_phone_ring = "audio/sfx/phone_ring.wav"
define audio.sfx_message = "audio/sfx/message_notification.wav"

##############################################
# 主脚本开始 (script.rpy)
##############################################

label start:
    
    # 显示标题画面
    scene black
    with fade
    
    show text "星轨\n————\n八年等待的爱情故事" with dissolve
    pause 3.0
    hide text with dissolve
    
    # 序章引入
    nvl clear
    nvl_narrator "从2023年暑假就计划着写这一本书..."
    nvl_narrator "而和你的再次相遇重新点燃了我用文字记录表达的热情。"
    nvl_narrator "因为人会遗忘..."
    nvl_narrator "走过太远的路需要在地图上被标注,追寻过意义太深的幸福需要在文字里被提醒。"
    nvl clear
    
    # 跳转到第一章
    jump chapter_1
    
##############################################
# 第一章:小小方圆
##############################################

label chapter_1:
    
    # 章节标题
    scene black
    with fade
    show text "第一章\n小小方圆" with dissolve
    pause 2.0
    hide text with dissolve
    
    # 场景1-1: 操场初见
    scene bg playground
    with fade
    play music bgm_daily fadein 2.0
    
    narrator "2019年,初一开学第一周"
    narrator "那是我第一次见到他,虽然当时我还不知道。"
    
    show female_yuanyang normal at left with dissolve
    show hn happy at right with dissolve
    
    hn "喷火牛!你也在十四中吗?"
    
    y "hi!是呀是呀!"
    
    hn "看,那是我男朋友。"
    
    show female_yuanyang surprised at left
    
    $ met_first_time = True
    
    y "{i}(刚从小学踏入初中的我,内心还无法接受'男朋友'这种称呼...){/i}"
    y "{i}(而且我完全不知道学姐指的是哪个男生...){/i}"
    
    narrator "盛夏的阳光有点耀眼,她不敢抬头。"
    narrator "在他坦坦荡荡地表白之前,她面对他,内心都缩在一个阴暗的角落。"
    
    hide hn with dissolve
    show female_yuanyang shy at center with move
    
    y "{i}(是缘分吗?){/i}"
    
    # 场景1-3: 诗文朗诵比赛
    scene bg auditorium
    with fade
    
    narrator "初一下学期,四月末"
    narrator "学校举行诗文朗诵比赛,我和他同时被选为主持人。"
    
    show female_yuanyang normal at left with dissolve
    show male_yuanyang normal at right with dissolve
    
    narrator "报幕结束后..."
    
    k "你这样,话筒会收音的。"
    
    play sound sfx_heartbeat
    show female_yuanyang surprised at left with vpunch
    
    y "{i}(他一把按下我握住话筒的手...){/i}"
    y "{i}(这个专业素养极高的小动作...){/i}"
    
    show female_yuanyang shy at left
    
    # CG显示
    scene cg_microphone with dissolve
    pause 2.0
    
    scene bg auditorium with dissolve
    show female_yuanyang shy at left
    show male_yuanyang normal at right
    
    y "{i}(我...好像记住他了。){/i}"
    
    # 好感度增加
    $ affection += 5
    
    k "后来得知你也喜欢跑步,一起跑吧?"
    
    menu:
        "好啊,每天一起跑步!":
            $ affection += 10
            $ choices_made.append("agreed_running")
            jump running_together
            
        "我再考虑考虑...":
            $ affection += 3
            jump running_hesitate
    
label running_together:
    
    scene bg playground
    with fade
    play music bgm_romantic fadein 2.0
    
    narrator "从那天起,她开始每天放学后去他教室门口等他。"
    
    show female_yuanyang normal at center with dissolve
    
    y "{i}(他穿着白色校服和西裤跑步的模样...){/i}"
    y "{i}(慢慢渗入我心里。){/i}"
    
    # CG: 白衬衫跑步
    scene cg_white_shirt_running with dissolve
    play sound sfx_heartbeat
    pause 3.0
    
    scene bg playground with dissolve
    
    narrator "直至现在,每当看到他正装出现,她的心都会猛地一缩。"
    
    jump chapter_1_continue

label running_hesitate:
    
    scene bg playground
    with fade
    
    narrator "虽然她嘴上说考虑,但还是忍不住每天去看他跑步。"
    
    jump chapter_1_continue

label chapter_1_continue:
    
    # 场景1-5: 年级第一的执念
    scene bg classroom
    with fade
    play music bgm_tension fadein 2.0
    
    narrator "某天,她偶然翻到他的说说..."
    narrator "发现了他和喷火牛的照片。"
    
    show female_yuanyang angry at center with dissolve
    
    y "{i}(原来...他有女朋友了...){/i}"
    y "{i}(而且她成绩很一般...年级200多名...){/i}"
    
    show female_yuanyang serious at center
    
    y "{i}(让他和那成绩平平的女生谈恋爱去吧!){/i}"
    y "{i}(我要变得更好——至少比你现在要好!){/i}"
    
    # 好感度转化为动力
    $ affection += 15
    
    narrator "他最好的成绩是年级第三。"
    narrator "而她,要超过他。"
    
    # 段考场景
    scene bg exam_room
    with fade
    play music bgm_daily
    
    narrator "初一下学期段考..."
    
    # 模拟考试过程(可添加小游戏)
    narrator "她拼尽全力答题。"
    
    scene bg school_hallway
    with fade
    
    narrator "成绩公布那天——"
    
    show text "女鸳鸯\n年级第一" with dissolve
    pause 3.0
    hide text with dissolve
    
    show female_yuanyang happy at center with dissolve
    
    y "{i}(我做到了...){/i}"
    y "{i}(这个年级第一,只是因为他。){/i}"
    
    # 第一章结束
    scene black with fade
    
    narrator "她不知道的是,这个年级第一,会成为他们故事的开始..."
    
    # 成就解锁
    $ persistent.achievement_grade1 = True
    show text "成就解锁:因你而优秀" with dissolve
    pause 2.0
    hide text with dissolve
    
    # 跳转到第二章
    jump chapter_2

##############################################
# 第二章:启天之星
##############################################

label chapter_2:
    
    scene black
    with fade
    show text "第二章\n启天之星" with dissolve
    pause 2.0
    hide text with dissolve
    
    # 场景2-1: 辩论赛合作
    scene bg canteen
    with fade
    play music bgm_daily
    
    narrator "初二,他们的互动越来越多。"
    
    show female_yuanyang normal at left with dissolve
    show male_yuanyang normal at right with dissolve
    
    k "辩论赛的主题是网络利弊,我把八年级政治书借你。"
    
    show female_yuanyang happy at left
    
    y "谢谢!我会好好准备的!"
    
    narrator "他们开始每天一起跑步,一起讨论辩论内容。"
    narrator "有时甚至会在食堂一起吃饭。"
    
    show female_yuanyang shy at left
    
    y "我这样跟你吃饭...喷火牛会有意见吗?"
    
    show male_yuanyang casual at right
    
    k "她不知道。"
    
    play sound sfx_heartbeat
    show female_yuanyang surprised at left with vpunch
    
    y "{i}(他说'她不知道'...){/i}"
    y "{i}(不是'她不会介意',而是'她不知道'...){/i}"
    
    $ affection += 10
    
    # CG: 食堂对坐
    scene cg_canteen_together with dissolve
    pause 3.0
    
    scene bg canteen with dissolve
    
    y "{i}(我内心已经承认自己喜欢上他了...){/i}"
    y "{i}(但谁都不说。){/i}"
    
    # 过渡到启天跨年
    scene bg qitian_building
    with fade
    play music bgm_romantic
    
    narrator "跨年夜,他送给她启天跨年的票。"
    
    show female_yuanyang happy at left with dissolve
    show male_yuanyang happy at right with dissolve
    
    k "要一起去吗?"
    
    menu:
        "当然!我很期待!":
            $ affection += 15
            $ choices_made.append("attend_qitian")
            jump qitian_event
            
        "我...我要考虑一下...":
            $ affection += 5
            jump qitian_hesitate

label qitian_event:
    
    scene bg qitian_night
    with fade
    play music bgm_celebration
    
    narrator "跨年夜,他们一起参加了活动。"
    narrator "烟花在夜空中绽放。"
    
    show fireworks animation
    
    show female_yuanyang happy at left with dissolve
    show male_yuanyang happy at right with dissolve
    
    y "{i}(他今晚穿着正装...){/i}"
    play sound sfx_heartbeat
    y "{i}(心跳得好快...){/i}"
    
    k "新年快乐!"
    
    y "新年快乐!"
    
    narrator "那一刻,她几乎以为会有什么发生..."
    narrator "但他只是微笑着看向烟花。"
    
    $ affection += 20
    
    jump chapter_2_continue

label qitian_hesitate:
    
    narrator "她最终还是没有去..."
    narrator "但心里还是会想,如果去了会怎样。"
    
    $ conflict_level += 5
    
    jump chapter_2_continue

label chapter_2_continue:
    
    # 场景2-4: 考前陪伴
    scene bg classroom_night
    with fade
    play music bgm_melancholy
    
    narrator "初三,中考前夕。"
    narrator "在他考试前一天,她总会陪他收拾东西。"
    
    show female_yuanyang normal at left with dissolve
    
    narrator "教室里只有两个人,没有开灯。"
    narrator "她站在他身后。"
    
    show male_yuanyang packing at right with dissolve
    
    y "{i}(我可以抱抱你吗?){/i}"
    y "{i}(作为朋友...){/i}"
    
    menu:
        "说出口":
            jump embrace_scene
            
        "憋回去":
            jump silent_walk

label embrace_scene:
    
    y "那个...我可以...抱抱你吗?"
    
    show male_yuanyang surprised at right
    
    k "诶?"
    
    y "就...作为朋友!给你鼓励!"
    
    show male_yuanyang shy at right
    
    k "...好。"
    
    # CG或特殊效果
    scene black with dissolve
    play sound sfx_heartbeat
    
    narrator "她轻轻抱住了他..."
    narrator "她能感觉到他的心跳..."
    
    $ affection += 25
    $ choices_made.append("embraced")
    
    scene bg classroom_night with dissolve
    
    jump walk_home_together

label silent_walk:
    
    y "收拾好了没,走吧。"
    
    show male_yuanyang normal at right
    
    k "嗯,走吧。"
    
    $ conflict_level += 3
    
    jump walk_home_together

label walk_home_together:
    
    scene bg school_gate_night
    with fade
    
    narrator "她陪他走到小区门口。"
    
    show female_yuanyang normal at left with dissolve
    show male_yuanyang normal at right with dissolve
    
    k "谢谢你陪我。"
    
    show female_yuanyang shy at left
    
    y "加油,考试!"
    
    k "嗯。"
    
    narrator "他转身离开..."
    narrator "她站在原地,看着他的背影。"
    
    hide male_yuanyang with dissolve
    show female_yuanyang sad at center with move
    
    y "{i}(我喜欢你...){/i}"
    y "{i}(可是我不敢说。){/i}"
    
    # 第二章结束
    scene black with fade
    
    narrator "中考结束后,便是暑假..."
    narrator "一切,将在那个夏天改变。"
    
    jump chapter_3

##############################################
# 第三章:沅芷澧兰(告白篇)
##############################################

label chapter_3:
    
    scene black
    with fade
    show text "第三章\n沅芷澧兰" with dissolve
    pause 2.0
    hide text with dissolve
    
    # 关键场景: 凤岭之巅告白
    narrator "初三升高一,暑假。"
    narrator "他约她在凤岭儿童公园见面。"
    
    scene bg fengling_entrance
    with fade
    play music bgm_romantic
    
    show female_yuanyang normal at center with dissolve
    
    y "{i}(他说有重要的事要说...){/i}"
    y "{i}(会是什么呢?){/i}"
    
    show male_yuanyang normal at right with moveinright
    
    k "来了?"
    
    show female_yuanyang happy at left with move
    
    y "嗯!什么重要的事?"
    
    k "跟我来。"
    
    # 走到顶层平台
    scene bg fengling_top_day
    with fade
    
    narrator "他们来到了凤岭的顶层平台。"
    narrator "天色渐暗,夕阳染红了天空。"
    
    show female_yuanyang normal at left with dissolve
    show male_yuanyang serious at right with dissolve
    
    k "女鸳鸯。"
    
    show female_yuanyang surprised at left
    
    y "嗯?"
    
    # 关键时刻
    play music bgm_confession
    scene cg_confession with dissolve
    play sound sfx_heartbeat
    
    k "我喜欢你。"
    k "我们在一起吧。"
    
    pause 3.0
    
    scene bg fengling_top_night with dissolve
    show female_yuanyang shocked at left
    show male_yuanyang nervous at right
    
    y "你...你说什么?"
    
    show male_yuanyang serious at right
    
    k "我说,我喜欢你。"
    k "从很久以前就喜欢了。"
    
    play sound sfx_heartbeat
    show female_yuanyang crying at left with vpunch
    
    y "{i}(他...他真的说了...){/i}"
    y "{i}(女生的直觉不会有错...){/i}"
    
    # 重要选择
    menu confession_choice:
        "我也喜欢你!":
            jump accept_confession
            
        "我...需要时间考虑...":
            jump consider_confession

label accept_confession:
    
    show female_yuanyang happy at left
    
    y "我也喜欢你!"
    y "从初一就喜欢了!"
    
    show male_yuanyang happy at right
    
    k "真的?!"
    
    y "真的!"
    
    # 拥抱CG
    scene cg_first_embrace with dissolve
    play sound sfx_heartbeat
    
    narrator "他紧紧抱住了她..."
    narrator "星空下,两颗心终于靠在一起。"
    
    $ affection = 100
    $ relationship_status = "together"
    $ confession_accepted = True
    
    # 成就解锁
    $ persistent.achievement_confession = True
    show text "成就解锁:凤岭之约" with dissolve
    pause 2.0
    hide text with dissolve
    
    scene bg fengling_top_night with dissolve
    show female_yuanyang shy at left
    show male_yuanyang happy at right
    
    k "那么...我们现在是..."
    
    y "...男女朋友?"
    
    k "嗯!"
    
    narrator "那天夜晚的星空,她永远不会忘记。"
    
    jump dating_period

label consider_confession:
    
    show female_yuanyang shy at left
    
    y "对不起...我需要时间考虑..."
    
    show male_yuanyang sad at right
    
    k "...我明白。我会等你的答案。"
    
    $ affection += 10
    $ conflict_level += 10
    
    narrator "她心里其实已经有了答案..."
    narrator "只是还不敢相信这是真的。"
    
    # 几天后
    scene bg phone_chat
    with fade
    
    narrator "几天后,她主动联系了他..."
    
    y "那个...关于那天的事..."
    k "嗯?"
    y "我想通了。"
    y "我愿意和你在一起。"
    
    $ relationship_status = "together"
    $ confession_accepted = True
    
    jump dating_period

label dating_period:
    
    # 恋爱期片段
    scene black with fade
    
    narrator "他们在一起了..."
    narrator "甜蜜的高中恋爱时光开始了。"
    
    # 蒙太奇场景
    scene bg library with fade
    play music bgm_daily
    narrator "一起在图书馆学习..."
    
    scene bg playground_sunset with fade
    narrator "一起在操场跑步..."
    
    scene bg cafe with fade
    narrator "一起去咖啡馆约会..."
    
    # 亲密场景(可选)
    if persistent.adult_content_enabled:
        jump first_kiss_scene
    else:
        jump chapter_3_end

label first_kiss_scene:
    
    scene bg park_bench_night
    with fade
    play music bgm_romantic
    
    show female_yuanyang shy at left with dissolve
    show male_yuanyang gentle at right with dissolve
    
    narrator "某个夜晚,他们坐在公园的长椅上..."
    
    k "那个..."
    
    show female_yuanyang surprised at left
    
    k "我可以...吻你吗?"
    
    play sound sfx_heartbeat
    show female_yuanyang shy at left with vpunch
    
    y "...嗯。"
    
    menu:
        "观看详细场景":
            scene cg_first_kiss with dissolve
            play sound sfx_heartbeat
            pause 3.0
            $ affection += 10
            
        "跳过":
            scene black with fade
            pause 1.0
    
    scene bg park_bench_night with dissolve
    
    narrator "那是她的初吻..."
    narrator "也是他的。"
    
    jump chapter_3_end

label chapter_3_end:
    
    scene black with fade
    
    narrator "甜蜜的高一过去了..."
    narrator "但幸福的背后,裂痕正在悄悄生长..."
    
    # 跳转到第四章(矛盾篇)
    jump chapter_4

##############################################
# 第四章:凤岭之巅(回忆与矛盾)
##############################################

label chapter_4:
    
    scene black
    with fade
    show text "第四章\n凤岭之巅" with dissolve
    pause 2.0
    hide text with dissolve
    
    # 矛盾开始
    scene bg bedroom_night
    with fade
    play music bgm_tension
    
    narrator "高二,矛盾开始出现。"
    
    show female_yuanyang sad at center with dissolve
    
    y "{i}(他开始不回消息了...){/i}"
    y "{i}(有时候要等很久才回复...){/i}"
    
    # QQ聊天界面
    scene bg phone_chat
    with fade
    
    show screen qq_chat:
        text "你在忙吗?" xalign 0.8 yalign 0.3
        text "..." xalign 0.8 yalign 0.4
        text "怎么不回消息?" xalign 0.8 yalign 0.5
    
    narrator "一小时后..."
    
    show screen qq_chat:
        text "在做作业,怎么了?" xalign 0.2 yalign 0.6
    
    $ conflict_level += 10
    
    # 首次争吵
    scene bg bedroom_night with fade
    play music bgm_sadness
    
    show female_yuanyang angry at center with dissolve
    
    y "{i}(我只是...想和你说说话...){/i}"
    y "{i}(为什么就这么难?){/i}"
    
    # 电话场景
    play sound sfx_phone_ring
    
    narrator "她打电话给他..."
    
    y "你为什么就不能多花点时间陪我聊聊天?!"
    k "我...我有在忙正事..."
    y "所以和我说话就不是正事了?!"
    k "我不是这个意思..."
    
    play sound "phone_hangup.wav"
    
    scene black with fade
    
    narrator "她挂断了电话。"
    
    $ conflict_level += 20
    
    # 继续积累矛盾...
    # (此处省略部分矛盾场景,直接跳到大学分离)
    
    # 大学分离
    scene bg train_station
    with fade
    play music bgm_sadness
    
    narrator "高三毕业,他们考上了不同的大学。"
    narrator "她在北京,他在武汉。"
    
    show female_yuanyang sad at left with dissolve
    show male_yuanyang sad at right with dissolve
    
    y "要...好好照顾自己。"
    
    k "你也是。"
    
    narrator "异地恋开始了。"
    
    # 异地矛盾
    scene bg dorm_night
    with fade
    
    narrator "大一,矛盾愈演愈烈..."
    
    show female_yuanyang crying at center with dissolve
    
    y "{i}(他已经三天没回我消息了...){/i}"
    y "{i}(我们的距离...越来越远...){/i}"
    
    $ conflict_level += 30
    
    # 关键争吵
    scene bg video_call
    with fade
    play music bgm_tension
    
    show female_yuanyang angry at left with dissolve
    show male_yuanyang tired at right with dissolve
    
    k "我每天给你发表情,都落下了课程..."
    
    show female_yuanyang shocked at left with vpunch
    
    y "所以你是在怪我?!"
    
    k "...没把你放在很重要的位置是正确的决定。"
    
    play sound sfx_heartbeat
    show female_yuanyang hurt at left with hpunch
    
    y "{i}(他...竟然说出这种话...){/i}"
    
    $ conflict_level += 50
    
    menu:
        "继续争吵":
            jump big_fight
            
        "冷静下来":
            jump calm_down_moment

label big_fight:
    
    y "你知道你在说什么吗?!"
    y "我为你付出了那么多,你就这样对我?!"
    
    show male_yuanyang angry at right
    
    k "我也很累!你就不能理解我吗?!"
    
    $ conflict_level += 20
    
    jump breakup_decision

label calm_down_moment:
    
    y "...我们冷静一下吧。"
    
    show male_yuanyang sad at right
    
    k "...对不起。"
    
    $ conflict_level += 5
    
    narrator "但冷静并不能解决根本问题..."
    
    jump breakup_decision

label breakup_decision:
    
    # 分手场景
    scene bg dorm_night
    with fade
    play music bgm_sadness
    
    show female_yuanyang crying at center with dissolve
    
    narrator "她开始写分手信..."
    
    y "{i}(我累了...){/i}"
    y "{i}(我不想再这样下去了...){/i}"
    
    # 显示分手信片段
    scene bg letter with fade
    
    narrator "\"到最后这段感情给我只剩下了痛苦。\""
    narrator "\"我真的累了,不想和你再生气吵架。\""
    narrator "\"谢谢你,出现在我的青春里。\""
    
    scene bg dorm_night with dissolve
    
    show female_yuanyang crying at center
    
    y "{i}(发送...){/i}"
    
    $ broke_up = True
    $ relationship_status = "broken_up"
    
    # 成就解锁
    $ persistent.achievement_breakup = True
    show text "成就解锁:繁花落幕" with dissolve
    pause 2.0
    hide text with dissolve
    
    scene black with fade
    
    narrator "六年的感情,就这样结束了..."
    
    # 跳转到第五章
    jump chapter_5

##############################################
# (此处省略第五章部分内容,直接跳到复合)
##############################################

label chapter_7_reunion:
    
    # 第七章:回到原点
    scene black
    with fade
    show text "第七章\n回到原点" with dissolve
    pause 2.0
    hide text with dissolve
    
    # 再次告白
    scene bg video_call
    with fade
    play music bgm_confession
    
    narrator "分手一年半后..."
    narrator "他主动联系了她。"
    
    show female_yuanyang surprised at left with dissolve
    show male_yuanyang serious at right with dissolve
    
    k "我一直喜欢你啊,你不会不知道吧。"
    
    show female_yuanyang shocked at left with vpunch
    play sound sfx_heartbeat
    
    y "你..."
    
    k "分手以后我还没有喜欢过别人。"
    k "我想...再试一次。"
    
    show female_yuanyang crying at left
    
    y "{i}(他...一直在等我...){/i}"
    
    narrator "她陷入了沉思..."
    
    # 思考片段
    scene bg dorm_night with fade
    
    show female_yuanyang thinking at center with dissolve
    
    y "{i}(我还喜欢他吗?){/i}"
    y "{i}(我们还有可能吗?){/i}"
    
    narrator "她开始列出执念和问题..."
    
    # 显示思考清单
    show screen thinking_list:
        text "执念:" xalign 0.2 yalign 0.3
        text "• 他塑造了半个我" xalign 0.25 yalign 0.35
        text "• 我的择偶标准就是他" xalign 0.25 yalign 0.4
        text "• 我无法爱上其他人" xalign 0.25 yalign 0.45
        
        text "问题:" xalign 0.6 yalign 0.3
        text "• 他变了吗?" xalign 0.65 yalign 0.35
        text "• 矛盾解决了吗?" xalign 0.65 yalign 0.4
        text "• 我还爱他吗?" xalign 0.65 yalign 0.45
    
    pause 3.0
    hide screen thinking_list
    
    show female_yuanyang crying at center
    
    y "{i}(我越问越觉得...){/i}"
    y "{i}(不可替代的就是他本人...){/i}"
    y "{i}(我真的...还在爱他整个人...){/i}"
    
    # 做出决定
    scene bg video_call with fade
    play music bgm_reunion
    
    show female_yuanyang determined at left with dissolve
    show male_yuanyang hopeful at right with dissolve
    
    k "你...考虑得怎么样?"
    
    y "我想通了。"
    
    show male_yuanyang nervous at right
    
    y "我愿意...再试一次。"
    y "这一次,不会再放手。"
    
    show male_yuanyang happy at right
    
    k "真的?!"
    
    y "我没有后路...只能相信你。"
    y "只能面对,只能解决所有问题。"
    
    # 复合CG
    scene cg_reunion_hug with dissolve
    play sound sfx_heartbeat
    
    narrator "他们终于...回到了彼此身边。"
    narrator "八年的等待,终于有了回音。"
    
    $ reunited = True
    $ relationship_status = "reunited"
    $ affection = 100
    
    # 成就解锁
    $ persistent.achievement_reunion = True
    show text "成就解锁:回到原点" with dissolve
    pause 2.0
    hide text with dissolve
    
    $ persistent.achievement_true_end = True
    show text "成就解锁:八年等待" with dissolve
    pause 2.0
    hide text with dissolve
    
    # 跳转到结局
    jump true_ending

##############################################
# True Ending
##############################################

label true_ending:
    
    # 飞机上的场景
    scene bg airplane
    with fade
    play music bgm_epilogue fadein 3.0
    
    narrator "2025年10月5日"
    narrator "上海飞往柳州的航班上..."
    
    show female_yuanyang writing at left with dissolve
    show male_yuanyang sleeping at right with dissolve
    
    narrator "他睡在她的肩膀上,她看着电脑屏幕。"
    narrator "她在写下这个故事的结尾..."
    
    # CG: 飞机上的场景
    scene cg_airplane_ending with dissolve
    pause 3.0
    
    scene bg airplane with dissolve
    show female_yuanyang writing at left
    
    y "{i}(我从未如此清醒地疯狂:){/i}"
    y "{i}(我要和你度过我的漫漫余生。){/i}"
    
    narrator "她在心中默念..."
    
    # 未来展望
    scene white_fade with fade
    
    y "{i}(时间啊时间,请做这对恋人的护佑神...){/i}"
    y "{i}(让我在领证的时候写下:){/i}"
    
    narrator "\"我终于嫁给了我十三岁就喜欢上的男孩。\""
    
    # 幻想场景: 领证
    scene cg_marriage_license with dissolve
    pause 3.0
    
    scene white_fade with dissolve
    
    y "{i}(让我在结婚的时候写下:){/i}"
    
    narrator "\"和你的一切是我生命中的奇迹,我的祷告终于有了回音。\""
    
    # 幻想场景: 婚礼
    scene cg_wedding with dissolve
    pause 3.0
    
    # 最终画面
    scene bg starry_sky with fade
    play music bgm_ending fadein 2.0
    
    show text "八年的星轨" with dissolve
    pause 2.0
    show text "终于交汇" with dissolve at truecenter
    pause 2.0
    show text "这一次,永不分离" with dissolve at truecenter
    pause 3.0
    
    # 剪影画面
    scene cg_silhouette_starry with dissolve
    pause 5.0
    
    scene black with fade
    
    # 结局文字
    centered "{size=+10}TRUE END{/size}\n\n\"永恒的星轨\"\n\n\n事与愿违\n爱是最大的理由\n压倒所有"
    
    pause 5.0
    
    # 制作组名单
    scene black
    show text "制作组\n\n原作: 女鸳鸯\n改编: [你的名字]\n程序: Ren'Py\n音乐: [音乐来源]\n\n感谢游玩!" with dissolve
    pause 5.0
    
    return

##############################################
# 其他辅助标签
##############################################

# 设置菜单
label preferences:
    # 这里可以添加设置选项
    return

# 成就查看
label achievements:
    # 显示已解锁的成就
    return

# 回忆录
label gallery:
    # CG回顾
    return
