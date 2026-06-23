image trailer = Movie(size=(1920, 1080), loop=False, play="images/trailer.webm")

label script_4:
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    $ save_name = _("(Day 1 • Time 16:52 • Dwell, Floor 2)")
    $ DateAndPlace = _("Day 1 • Time 16:52 • Dwell, Floor 2")


    show cgfar dwell_day1_hallway
    show cgmid dwell_day1_hallway

    pause 2.0
    show amour armsup e_surprised m_o at appearTorightup
    show betz armsides e_surprised m_wide at appearToleftup
    play sound happy
    a "Oh!{w} I recognize that place!{w} That's where we found Sosotte yesterday, yeah?"
    b "Ah...{w} Indeed it is."
    s "So...{w} Th-{w=0.2}This is where I was attacked?{w} Th-{w=0.2}That's so scary!{w} (>w<)"
    s "And yet, both of you went to my rescue...{w} I-{w=0.2}I am ever so grateful for your help!{w} *bows cutely in thanks!*"
    a e_angry m_o "..."
    b curious e_sad "..."
    "(...{w}Did I say something wrong?)"
    if stats_str:
        play sound stats
        "{image=str}(I feel my shoulders tighten.)"
    if stats_psy:
        play sound stats
        "{image=psy}(They both are looking at me like you'd look at a bad liar.{w} I'm busted, aren't I...)"
    "(I tilt my head to the side questioningly.)"
    play sound waitasec
    s "(0w0)?"
    b e_sad m_neutral sweat_off "Hm...{w} Mademoiselle...{w} I wanted to ask this whole time, but..."
    play sound happy
    a callsaul e_neutral m_o "Why are you back to that today, Sosotte?{w} The cutesy-wutesy voice?"
    a e_angry m_buh "The \"uwah im sho cute im sho nice teehee oowoo\" voice!"
    play sound waitasec
    s "Huh?"
    "(Did you not act this way with them yesterday, Sosotte?{w} Huh?!?{w} How did we act, then?!)"
    s "Wh-{w=0.2}What do you mean, that's how I always talk!{w} (>︿<)"
    show betz curious e_sad
    show amour e_neutral
    s "I-{w=0.2}I'm sorry if I seem annoying...{w} B-{w=0.2}But that's just who I am!{w} (;︿;){w} *looks so cute and small!*"
    a "{cps=*0.1}..."
    b "{cps=*0.1}..."
    show amour at charayay
    play sound happy
    a armsup "No it's not~!"
    b armup e_sad m_realsmile "...It really isn't, mademoiselle."
    call BGshake
    show amour at shake
    show betz at shake
    play sound shout
    "(Urgh...)"
    a "Yeah!{w} When we met you yesterday, we saw through the cute act immediately!!!"
    "(What in the...)"
    "(Urgh, I can only assume you dropped the cute façade, Sosotte.{w} Alright...)"
    s "...{w}Okay, fine, I'll act normal!{w} Urgh..."
    show betz armsides e_smile m_smile
    show amour laughing
    call BGshake
    show amour at shake
    show betz at shake
    play sound shout
    s "I can't believe you let me keep the act up for a whole day!!!{w} How rude!!!"
    b "Hah..."
    a "Heheheh!{w} Sorry, sorry!"
    s "Urgh...{w} Please bear with me for a bit, alright?{w} I have to readjust..."
    s "...{w}How...{w} How did I act with you two?"
    a armsup e_neutral m_3 "You were mean!{w} It was fun!"
    show amour at shake
    show betz at shake
    call BGshake from _call_BGshake_75
    play sound shock
    s "HUH?!?"
    b laugh_giggle "You were somewhat...{w} Playful, yes."
    a callsaul e_angry m_3 "You were so~~~ mean!{w} You told me, um..."
    a lookup "\"I would never lower myself as to remember your name, you shattered soul.{w}{nw}"
    show amour armsup
    extend " Hohohoho~!\""
    call BGshake
    show amour at shake
    show betz at shake
    play sound shout
    s "I-{w=0.2}I said that?!{w} That's--"
    b armsides e_asad m_smile "Not in so many words.{w} Amour is exaggerating."
    b e_smile m_smile "...But you did tease us quite a bit.{w} You didn't say this to her, but you did say something similar..." id script_4_61a05d13
    b curious e_around m_smile "You did tend to say what you were thinking.{w} I thought your honesty and playfulness was quite refreshing, to be honest."
    "(...Oh, so whatever we thought, sounds like we said aloud, no matter how terrible it was.)"
    "(Sosotte, did we decide they were worth acting this way with?{w} This early?!)"
    "(You must've really liked spending time with them, for you to do that, Sosotte...)"
    "(...)"
    show betz armsides e_smile m_smile
    "(How nice...{w} That we had this experience with them, Sosotte.)"
    "(Both the Sosotte of yesterday, and the Sosotte of today...{w} Got to meet them.)"
    "(...{w}{w=1}I won't tell you anything about this either, Sosotte of tomorrow.{w} Please forgive me.)"
    "(Let me keep the two of them a secret for a little while longer.)"
    s "...{w}So, I said mean things to you both..."
    call syayBG
    show amour at syayC
    show betz at syayC
    play sound happy
    show betz e_surprised m_wide
    show amour e_surprised m_oend
    s "But it sounds like I didn't say anything false, did I?{w} (^v^){w} *grins evil-y!*"
    a laughing "HAH, that’s our Sosotte!"
    b laugh_giggle "Heh.{w} It's nice to meet you again."
    a armsup e_neutral m_3 "Heheh!{w} Alright, then!"
    a "Let's keep going!{w} We still have this whole new floor to explore!"
    pause 2.0


    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide betz
    hide amour
    hide cgfar
    hide cgmid
    show cgfar dwell_day1_end
    show cgmidback dwell_day1_end
    pause 3.0
    show amour armsup e_neutral m_3 at appearTorightup
    show betz armsides e_smile m_smile at appearToleftup
    s "Alright!{w} Now, we can...{w}{nw}"
    show betz blush e_upset m_uwah sweat_on
    play sound fall
    pause 0.5
    show blink start

    extend " WARGH!"
    hide amour
    hide betz
    play sound shout
    b "M-{w=0.2}Mademoiselle!!!"
    play sound happy
    a "Hahaha!!!{w} Sosotte, you tripped on nothing!!!"

    if stats_amour:
        s "{image=amourstat}Urgh...{w} Amour, help me up, will you?"
        a "Hahah, okay!"
        pause 1.0
        show amour meetingamour at cg_meetingamour_immediate_bg
        show blink end
        play sound blinkend
        pause 2.0
        a "Heh!{w} You fell so hard!{w} That was funny, you should do that again."
        s "I'm not going to fall over again for your amusement."
        a "Awww!{w} Not even a little?"
        s "How can I fall a little?"
        a "I don't know!{w} We can find out!"
        s "Heh...{w} Let's not."
        a "Okaaaaaay!"

    if stats_betz:
        s "{image=betzstat}Urgh...{w} Betz, help me up, will you?"
        b "Of course...{w} Hold on a second."
        pause 1.0
        show betz meetingbetz at cg_meetingbetz_move_betz
        show blink end
        play sound blinkend
        pause 2.0
        b "You didn't get hurt, did you?"
        s "No, I'm alright...{w} Just tripped on my own feet, I guess."
        b "Oh.{w} Well, I'm glad you're alright.{w} Let me help you to your feet..."


    pause 1.0
    show blink start
    play sound blinkstart
    pause 2.0
    hide amour
    hide betz
    show blink end
    play sound clothes

    show amour callsaul at appearTorightup
    show betz armup at appearToleftup
    pause 1.0
    a "Did you really trip on nothing?"
    s "I suppose so."
    show amour at charayay
    play sound happy
    show betz e_sadclosed
    a "Cute!{w} That was cute!{w} You--"
    show amour e_surprised m_o
    stop music
    play bg bgdwell_empty
    show betz at shake
    b alook "Hold on."
    b m_neutral_s"{cps=*0.1}...{w}{w=2}{nw}"
    b curious e_sad m_neutral "I-{w=0.2}I thought I heard something, but..."
    hide betz
    hide amour
    with dissolve
    pause 1.0
    s "...{w}Could it be the thing that attacked me...{w} The Hazard?"
    pause 2.0
    show betz armsides e_frown m_wide at appearTomiddleup
    b "...Could be."
    b armsides e_frown m_wide "Please stay here, mademoiselle, while I investigate."
    s "Alright...{w} Be careful, okay?"
    b "Of course."
    play sound walkingdwell
    hide betz with dissolve
    pause 3.0
    s "...{w} I hope Betz will be alright.{w} What do you think, Amour?"
    pause 2.0
    s "...{w}{w=1}Amour?"
    "(Where did Amour go?){nw}"
    stop bg
    play sound rocksound
    extend ""
    pause 0.5
    $ save_name = _("(Day 1 • Time 17:00 • Dwell, Floor 2)")
    $ DateAndPlace = _("Day 1 • Time 17:00 • Dwell, Floor 2")
    play music spooky
    call BGshake from _call_BGshake_29
    play sound scare
    "(What was that noise?!)"
    "({cps=*0.1}...)"
    $ renpy.choice_for_skipping()
    $ InPaCDialogue = False
    $ IsPaCDisabled = False
    $ pointnclickbuttons_order = _("Look around.")
    show screen pointnclickbuttonhelp with dissolve
    hide cgclose bookdown
    show cgmidback
    call screen pointnclick_day1_endday onlayer front

    label pointnclick_day1_endday_continue():
    play soundloop runningdwellloop
    show blink start
    play sound blinkstart
    pause 0.5
    hide screen pointnclickbuttonhelp
    $renpy.hide_screen("pointnclick_day1_endday", layer="front")
    hide cgclose bookdown
    hide cgmid
    pause 1.0
    "(What was that{w=0.2} what was that{w=0.2} {shake}what was THAAAAAAAAAAAAAT!!!!!!!!{/shake})"
    if stats_sight:
        play sound stats
        "{image=sight}({shake}W-{w=0.2}What kind of monster is that!!!{w} It has teeth!!!{w} Sharp teeth!!!{/shake})"
    if stats_smell:
        play sound stats
        "{image=smell}({shake}The smell of citrus around me is overpowering!!!{/shake})"
    if stats_hearing:
        play sound stats
        "{image=hearing}(I don't hear it coming after me, {shake}but that doesn't mean I should stop!!!{/shake})"
    if stats_str:
        play sound stats
        "{image=str}(Running like this...{w} Why does it feel so familiar...?!?)"
    pause 1.0
    "({shake}OK OK OK OK just run, keep running, and calm down.{/shake})"
    pause 0.5
    "({shake}You have your Scrap Book, Sosotte, and a pen in your hand.{w} Just keep running.{/shake})"

    "(I take a few running steps, but, quicker than I can see--)"
    stop bg
    stop soundloop
    show blink end
    play sound monstercatch
    show cgfar day2hazard
    show cgmid day2hazard
    show cgclose day2hazard
    pause 1.0
    "(It catches up to me--)"
    "(And{w=0.5} I--)"
    stop music fadeout 3.0
    show cgpclose white at slowdissolve
    "(Forget{w} everything.)"
    pause 3.0

    hide cgfar
    hide cgmid
    hide cgclose
    hide cgpclose
    hide cgmidback
    hide cgback
    call hidealltabs_nodissolve
    hide screen dateandplace
    hide screen frame_page onlayer frame_layer

    pause 1.0

    $ renpy.movie_cutscene("images/trailer.webm")

    #show trailer

    pause 0.5


    python:
        if stats_amour:
            feniks_stat_manager.set_stat_true('pickedamour')
            achievement.grant("amour")
            achievement.sync()
        if stats_betz:
            feniks_stat_manager.set_stat_true('pickedbetz')
            achievement.grant("betz")
            achievement.sync()



    python:
        if stats_sight:
            achievement.grant("sight")
            feniks_stat_manager.set_stat_true('pickedsight')
            achievement.sync()
        if stats_smell:
            feniks_stat_manager.set_stat_true('pickedsmell')
            achievement.grant("smell")
            achievement.sync()
        if stats_hearing:
            feniks_stat_manager.set_stat_true('pickedhearing')
            achievement.grant("hear")
            achievement.sync()

    python:
        if stats_str:
            feniks_stat_manager.set_stat_true('pickedstr')
            achievement.grant("str")
            achievement.sync()
        if stats_int:
            feniks_stat_manager.set_stat_true('pickedint')
            achievement.grant("int")
            achievement.sync()
        if stats_psy:
            feniks_stat_manager.set_stat_true('pickedpsy')
            achievement.grant("psy")
            achievement.sync()

    if achievement.steam:
        ## Push steam stats
        $ achievement.steam.store_stats()

    if stats_amour:
        $ persistent.stats_amour_end = True
    if stats_betz:
        $ persistent.stats_betz_end = True

    if stats_sight:
        $ persistent.stats_sight_end = True
    if stats_smell:
        $ persistent.stats_smell_end = True
    if stats_hearing:
        $ persistent.stats_hearing_end = True

    if stats_str:
        $ persistent.stats_str_end = True
    if stats_int:
        $ persistent.stats_int_end = True
    if stats_psy:
        $ persistent.stats_psy_end = True

    python:
        if persistent.stats_amour_end and persistent.stats_betz_end and persistent.stats_sight_end and persistent.stats_smell_end and persistent.stats_str_end and persistent.stats_betz_end and persistent.stats_int_end and persistent.stats_psy_end:
            achievement.grant("complete")
            achievement.sync()

    play music culdepuis
    show screen frame_page
    show bg 1920x1080
    show cgpfar 1920x1080
    show cgfar 1920x1080
    show cgmidback 1920x1080
    show cgclose 1920x1080
    with dissolve
    $ leftstick_focus = True
    call screen wishlist
    $ leftstick_focus = False

    return

