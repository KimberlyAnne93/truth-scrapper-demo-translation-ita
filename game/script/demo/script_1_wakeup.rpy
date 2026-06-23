label script_1:

    play bg inside
    show bg outside_sky_parallax
    show cgpfar day3_wakeup
    show cgfar day3_wakeup
    call syayBG
    show bg at parallaxvertical
    "(Oh!)"

    window hide
    ## ADDED FOR DEMO ##
    ## Added new joystick thing
    show screen joystick_tutorial_v2
    pause 4.0
    "(Oh, the end of this dream woke me right up.)"
    "(What a strange dream.{w} I can't remember ever seeing a blue flower like this.)"
    "(What was I doing with it?)"
    "(What was I...)"
    "(...)"
    "(Doesn't matter.{w} Just a dream.)"
    "(I'm laying on a bed, it seems.{w} Where am I?)"
    "(Where...)"
    pause 2.0
    play sound blinkstart
    show blink start
    pause 1.0
    play sound waitasec

    "(Why...{w} Why is nothing coming to mind...?)"

    play sound happy
    b "Oh, she's awake...!"
    stop bg fadeout 2.0
    pause 1.0
    show betz d3wake
    hide transition
    show blink end
    play sound blinkend
    play music goofy
    pause 1.0

    show betz d3wake at charayay
    play sound waitasec
    b "Oh, thank the Great Artisan, mademoiselle, you're up!{w} I...{w} I thought..."
    "(\"Mah-deh-moah-zel\"...{w} \"Miss\"?)"
    "(Someone with beautiful clothes, and MASSIVE ears.{w} Who is...?)"
    play sound clothes
    show amour d3wake at appearTomiddleup
    a "Sosotte, you're {wave}awaaaaaaaaake!"
    "(And someone else, with terrible clothes, and MASSIVE muscles.{w} Do I know them...?)"
    window hide
    pause 1.5
    show blink start
    play sound blinkstart
    pause 0.5
    hide cgfar
    hide bg
    hide cgpfar
    hide henshin

    show cgfar wakeupday3
    show amour armsup e_neutral m_3 at teleportleft
    show betz aangry at teleportright

    pause 1.0
    show blink end
    play sound blinkend
    pause 0.5
    show betz at charashake
    play sound shout
    b "Don't yell, you dullard!{w} You woke up the mademoiselle!"
    a side e_surprised m_3 "What?{w} No, I didn't!{w} I'm always nice and softspoken."
    b alook "You wouldn't know what \"softspoken\" meant if it hit you in the face."
    a m_oh "Gasp...{w} You want me to punch myself?"
    play sound shout
    show betz at charashake
    b aangry e_closed m_angry "HNNNNNNGH!!!!!!"
    show amour laughing


    "(Who are those two?{w} I don't recognize them in the slightest.)"
    show betz atalk e_anger m_wide
    show amour side e_neutral m_3
    "(They called me...{w} \"Sosotte\"?{w} Is that...)"
    play sound waitasec
    "(Is that my name?)"
    show amour side e_neutral m_3
    show betz e_sneutral m_neutral
    "(My name...)"
    "(...)"
    pause 2.0
    "(Oh, I can't remember.)"
    "(If my name truly is \"Sosotte\", I can't remember it.{w} And, really, there's a lot I can't remember, either.)"
    "(I don't feel scared of that fact.{w} And the fact that I don’t feel scared of it{w} scares me even more.)"
    show betz armsides e_surprised m_wide
    show amour armsup e_surprised m_o
    play sound waitasec
    "(It's like...{w}{w=0.5} [info_narra_start]It's like I'm used to it.{w} Forgetting.[info_end])"
    "{w=1.0}(Why do I feel like I'm used to it?)"


    b armup e_sad m_neutral sweat_on "Mademoiselle, are you okay?{w} You've been staring at us for a while..."
    a side e_neutral m_3 "Of course she is.{w} She's looking at me!"
    b atalk e_ugh m_wide sweat_off "Why would she be looking at you."
    a e_frown m_eh "Well..."
    show amour callsaul e_neutral m_3 at charayay
    play sound happy
    a "Because I'm handsome, right???"
    play sound shout
    show betz aangry e_closed m_angry sweat_on at charashake
    b "STOP PLAYING AROUND!!!"

    "(Bickering, bickering...)"
    "(It feels familiar somehow, but I have other things to worry about.)"
    "(Like my forgotten memories.{w} Can they keep it down?)"
    b e_angy "And you--"
    show betz blush e_upset m_uwah_open sweat_off at charashake
    show amour armsup e_surprised m_o
    play sound waitasec
    s "Stop."
    b "Hn...?"
    a "What?{w} What is it?"
    s "...{w}{w=1}Who are you two?{w} Why are you here?"
    show betz armsides e_sadaside m_wide sweat_on
    show amour e_neutral 
    s "If we don't know each other, I'm going to have to ask you to leave.{w} I'm dealing with a lot right now, and you're giving me a headache."
    b "A-{w=0.2}Ah..."
    a m_3 "So mean, so mean!"
    b curious e_around m_neutral sweat_off "Ah, perhaps she still hasn't..."
    show amour callsaul at charayay
    play sound happy
    a "Here, here, touch your book-thing!"
    pause 0.5
    show blink start
    play sound blinkstart
    pause 0.5

    hide amour 
    hide betz
    hide cgfar
    show bg outside_grass
    show cgmid outside_grass
    show cgclose outside_grass
    play sound blinkend
    show blink end
    pause 1.0
    s "My \"book-thing\"?"
    "(Oh, a book.{w} I wonder what it--)"

    stop music fadeout 2.0

    show blink opacitymid with dissolve
    pause 0.5
    play sound henshinremembering
    show henshin remembering
    pause 2.3
    hide henshin remembering
    hide blink opacitymid  

    with dissolve
    pause 1.7
    show blink start
    play sound blinkstart
    pause 0.5
    $ save_name = _("(Day X • Time 09:42 • Cul-De-Puits)")
    $ DateAndPlace = _("Day X • Time 09:42 • Cul-De-Puits")

    hide bg
    hide cgmid
    hide cgclose
    show cgfar wakeupday3
    show amour armsup at teleportleft
    show betz armsides at teleportright  

    "(As I touch the book, memories rush forth.)"
    "(As if I am reading a book{w} filled with memories of the days I've lived through.)"
    "(In fact, that's exactly what's happening.)"
    "(This is{w=0.5} my [info_narra_start]Scrap Book[info_end].)"
    "(I remember everything I've written in it.)"
    "([info_narra_start]I remember{w=0.5} who I am.[info_end])"

    show screen bookUI_glossary_fake
    pause 0.5
    play sound menu_notif
    pause 2.0

    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide screen bookUI_glossary_fake
    $ glossary_name = _("Read Me")
    $ glossary_title_text = _("[For the empty-minded]")
    show screen menu_glossary_investigate
    $ TurnOffReturn = True


    pause 2.0
    "(I am Sosotte, member of the Truth Scrappers.{w} Every morning, I forget everything, even my name...)"
    "(...And only by touching this Saturated Item, my Scrap Book, can I remember things.)"
    pause 0.5
    $ TurnOffReturn = False
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide screen menu_glossary_investigate

    show screen bookUI_glossary

    pause 0.5
    "(I am on a case here, in the Dwell, to find out more about an incident that happened to my Truth Scrapper colleagues.)"
    "(And...){w}{w=1}{nw}"

    show blink end
    play sound blinkend
    pause 1.0
    "{w=1}(Oops.{w} We messed up a bit here, Sosotte.)"
    $ amourname = _("AMOUR")
    $ betzname = _("BETZ")
    show amour  at shake
    show betz armsides e_sadaside m_wide sweat_on at shake
    call BGshake 
    play sound shout
    "(Oh, Great Artisan, if only I could redo our meeting now that I remember!!!{w} How annoying!!!)"
    "(Oh well.{w}{w=0.5} Let's just go for it.)"

    show amour armsup e_surprised m_o at syayC
    show betz e_surprised m_wide at syayC

    call syayBG 
    play music culdepuis
    play sound happy    
    s "Um, um, hello!!!{w} Hello, it's nice to meet you!{w} You can call me Sosotte.{w} That's So-SUHT!{w} Yes, I am she!"
    s "I am from the Truth Scrappers' guild,{w} but I have even more holes in my brain than usual Truth Scrappers you might have met!{w} So, um, please take care of me!{w} o(^▽^)o"
    show amour at charayay
    play sound happy
    a callsaul e_neutral m_3 "Heh!{w} Yeah, we know!"
    b laugh_giggle "Hahah...{w} We have met before, mademoiselle."
    show screen bookUI_characters_fake
    pause 0.5
    play sound menu_notif
    pause 1.0
    $ TurnOffReturn = True
    $ character_name = _("Amour")
    $ character_title_text = _("[Red-Haired, Dull, Helpful.]")
    play sound turnpage_single
    show screen menu_character_amour
    pause 1.0
    "(Ah, that's right...{w} Amour...{w} Ah-MOO-r...)"
    pause 0.5
    pause 0.25
    $ TurnOffReturn = True
    $ character_name = _("Betz")
    $ character_title_text = _("[Knight In Shining Armor.]")
    play sound turnpage_single
    show screen menu_character_betz
    pause 1.0
    "(...And Betz, BEH-ts, was it?)"

    $ TurnOffReturn = False
    hide screen bookUI_characters_fake
    show screen bookUI_characters
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide screen menu_character_betz
    pause 1.0


    "(What gorgeous people you've found, Sosotte!{w} Good job!!!)"
    "(But, beauty isn't everything.{w} Are they useful, too?)"
    b armup e_neutral m_smile "To reiterate, I am Betz.{w} I am he and they."
    a armsup e_neutral m_3 "And I'm Amour, he and she!"
    b "We are both Path Dwellers, and we've been assigned to guide you through the Dwell for your case."
    s "Amour, and Betz!{w} Aaaah, it is so nice to see you again!{w} (;w;)"
    show amour e_surprised m_o
    show betz armsides e_surprised m_neutral sweat_off
    s "Were you two at my bedside all night?{w} That is so very kind...!"

    show amour at charayay
    "(I take Amour's hand in mine.)"
    play sound happy
    s "Thank you for guarding my sleep!{w} I'm ever so grateful...!{w} *looks up at Amour with stars in my eyes...!*{w} (*w*)"
    a m_3 "Wow!{w} We're holding hands!"
    s "A-{w=0.2}Ah, is that okay?{w} I...{w} I'm feeling so overwhelmed, and you make me feel so safe already..."
    a e_neutral m_3 "Huh!"
    a callsaul "Yeah, don't worry!{w} I, Amour, will protect you from everything that is too scary, I promise!"
    "(Hook, line and sinker.{w} This one is easily manipulated, good to know...)"
    "(Verdict: Useful.)"
    b atalk e_anger m_wide "I wouldn't expect this one to be able to protect you from anything."
    "(Ah, is the other one feeling left out?{w} Time to butter up our other sleep guardian, right, Sosotte?)"
    show betz atalk e_sneutral m_neutral
    show amour armsup
    show amour side
    s "*turns to look at Betz with wet eyes...*{w} Oh, gentle Betz...{w} Y-{w=0.2}You are the one who rescued me, yes?{w} I-{w=0.2}I am deeply in your debt...!"
    show betz armsides e_surprised m_wide
    s "You're like...{w} You're like a knight!{w} A knight in charming armor!{w} o(^▽^)o{w} *clasps my hands together like a supplicant in front of their deity!*"
    b e_neutral m_neutral_s "..."
    play sound shiny
    b e_fakesmile m_fakesmile_oend stars_on "Hahaha, thank you for your kind words, mademoiselle.{w} I truly do not deserve them."
    "(Woah.{w} That smile feels like the kind of smile you would give an annoying customer...)"
    play sound shock
    show amour laughing at shake
    show betz at shake
    call BGshake
    "(I feel like my attack got repelled...!!!)"
    "(Verdict: To be determined...)"
    show amour armsup
    b curious e_around m_neutral "That aside...{w} Do you remember why you're here...?"
    s "Ah, yes!{w} I am here for a case..."
    show screen bookUI_mystery_fake
    pause 0.5
    play sound menu_notif
    pause 2.5

    $ VisibleDayPageMystery = 1
    $ TurnOffReturn = True
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    show amour armsup
    show screen book_mystery
    pause 1
    s "Three of my colleagues from the Truth Scrapper guild have been attacked by someone, here in the mines of the Dwell...{w} And I'm here to find out why!!!"
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    $ VisibleDayPageMystery = 2
    pause 1
    "(I wonder what this weird drawing is, though...)"
    pause 0.5
    $ TurnOffReturn = False
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide screen book_mystery
    hide screen bookUI_mystery_fake

    show screen bookUI_mystery
    pause 0.5

    b armup e_sad m_neutral sweat_on "Y-{w=0.2}Yes, but..."
    show amour at charayay
    play sound happy
    a callsaul "But, but, do you remember why you're HERE here?"
    s "Here?{w} You mean, in this room?{w} Um, no...{w} (;A;)"
    play sound shout
    show amour e_angry at charashake
    play sound shout
    show betz armsides e_sadaside m_wide sweat_on
    a "You got attacked too~~~!!!"
    show amour at shake
    show betz at shake
    call BGshake
    play sound shout
    s "HUH?!?!?!"
    a armsup e_neutral m_3 "You got attacked yesterday, too!{w} By the Hazard, just like your coworkers!"
    s "Th-{w=0.2}The Hazard?!{w} That sounds so scary~!{w} What is it?{w} *shakes in fright!*"
    b curious e_sad "The monster of the Dwell, or so we believe..."
    b armup e_sad sweat_on "Th-{w=0.2}The three of us got separated yesterday, and we lost you in the mines.{w} When we found you, a couple hours later, you were out cold..."
    a e_surprised m_o "It was after the Dwell closed for the day!{w} That's when the Hazard attacks people!"
    s "A monster..."
    "(Hm...)"
    $ VisibleDayPageMystery = 2
    $ TurnOffReturn = True
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    show screen book_mystery
    pause 1
    s "I-{w=0.2}Is this it, perhaps?"
    play sound happy
    a "That sure is it!!!"
    pause 0.5
    $ TurnOffReturn = False
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide screen book_mystery
    pause 0.5
    b hiding "Ngh...{w} The fact that you were attacked, even though we were supposed to guide you..."
    b "The fault lies with me.{w} Please, accept my deepest apologies."
    "(So Betz says it is their fault...{w} Where was Amour, I wonder?)"
    show betz armsides e_sadaside m_wide
    s "Oh, i-{w=0.2}it's alright...{w} I don't remember it, after all, so I forgive you completely!{w} (^w^)"
    a side e_neutral m_3 "Yeah, Betz, Sosotte forgives you!"
    b alook "The fault also lies with you, dullard.{w} If only you didn't go off on your own, the mademoiselle wouldn't have been in this situation."
    a lookup "...{w}Sorry Sosotte..."
    play sound shout
    show betz at charashake
    b aangry e_angy "Muttered apologies just won't cut it, Amour!!!"
    show amour callsaul e_angry m_3 at charayay
    play sound happy
    a "SOOOOORRYYYYYYYYY SOSOOOOOOOOOOOOOOOOOOOTTE!!!"
    show betz at charashake
    play sound shout
    b e_closed "YELLING THEM WON'T CUT IT EITHER!!!!"

    show amour side
    show betz atalk e_anger
    "(Amour and Betz...)"
    "(So we have met them before.)"
    "(Sosotte...{w} What happened to us, yesterday?{w} What did you write down?)"
    show screen bookUI_memories_fake
    $ TurnOffReturn = True

    pause 0.5
    play sound menu_notif
    pause 2.0

    $ fakememoryscreen_title = _("THE DWELL • DAY X-1")
    $ fakememory1 = _("{color=B06531}• Met Amour.{/color}")
    $ fakememory2 = _("{color=5597A9}• Met Betz.{/color}")
    $ fakememory3 = _("{color=6B883C}• Nothing else interesting happened.{/color}")
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    show screen book_reminders_cutscene
    show screen fakeMemory1
    show screen fakeMemory2
    show screen fakeMemory3
    pause 1.0

    "(...{w}That's pretty sparse.{w} Nothing about how we feel about them, or even about how the day went...)"
    "(Let's write a little more for today, shall we?)"
    play sound turnpage_single
    show transition_nextpage onlayer overlay

    #########################
    ## Point and Click Memory
    #########################
    #SETUP FOR PACS
    $ WhichPaC = "day0_memory"
    #$ TurnOffReturn = True
    default Day0Choice = 0
    show screen day0_book_reminders

    pause 1.
    "(Hm...{w} What am I noticing about my environment, today...)"

    pause 0.5
    label Day0_Choice1Start:
        $ Day0Choice = 1
        $ pointnclickbuttons_order = _("Choose what to remember.")
        $ MemoryTextForSpot1 = _("{color=6B883C}• Hospital smells like antiseptic. Ew...{image=smell}{/color}")
        $ MemoryTextForSpot2 = _("{color=6B883C}• Those painkillers did nothing. My head hurts...{image=str}{/color}")
        $ MemoryTextForSpot3 = _("{color=B06531}• Amour is interesting.{image=amourstat}{/color}")
    play sound write
    show screen day0_Memory1 with wiperight
    pause 0.3
    $ renpy.choice_for_skipping()
    # Don't show screens in the 'overlay' layer
    show screen pointnclickbuttons with dissolve
    show screen clickindicator_day0
    hide screen pointnclickbuttons #so its not doubled up

    label Day0_CallScreen_Choice1():
        show screen pointnclickbuttons
        call screen day0_Memory1

    #create loop here. so the callstack doesn't go higher and higher
    if Day0Choice == 1:
        jump Day0_CallScreen_Choice1
    else:
        pass


    label Day0_Choice1Done():
        show screen day0_Memory1
        # When we are done with our choice, hide the point and click buttons.
        hide screen pointnclickbuttons
        hide screen clickindicator_day0
        $ Day0Choice += 1
        $ D0C1Text = MemoryTextForSpot1
        if D0C1Text == _("{color=6B883C}• Hospital smells like antiseptic. Ew...{image=smell}{/color}"):
            $ temptext = _("{image=smell}smell")
        elif D0C1Text == _("{color=6B883C}• I can see some hospital books about all kinds of medical subjects.{image=sight}{/color}"):
            $ temptext = _("{image=sight}see")
        elif D0C1Text == _("{color=6B883C}• I can hear hospital machines nearby. Beep beep...{image=hearing}{/color}"):
            $ temptext = _("{image=hearing}hear")
        "{w=0.5}(Is this what I want to remember?{w} What I can [info_narra_start][temptext!t][info_end]?){w}{nw}"
        $ _history = False

        menu:
            "(Is this what I want to remember? What I can [info_narra_start][temptext!t][info_end]?){fast}"
            "(Yes.)":
                $ _history = True
                $ Day0Choice = 2
                $ D0C1Text = MemoryTextForSpot1
                if D0C1Text == _("{color=6B883C}• Hospital smells like antiseptic. Ew...{image=smell}{/color}"):
                    $ stats_smell = True
                    $ MemoryNumberForSpot1 = 1
                    "{w=1}(It sure does smell like antiseptic.{w} It's putting me on edge, quite honestly...)"
                    "(But I think it's a good idea to pay attention to [info_narra_start]things we can smell, Sosotte.[info_end]{w} Memories are linked to smells, aren't they...?)"

                if D0C1Text == _("{color=6B883C}• I can see some hospital books about all kinds of medical subjects.{image=sight}{/color}"):
                    $ stats_sight = True
                    $ MemoryNumberForSpot1 = 2
                    "{w=1}(There sure are some books over here.{w} Books about anatomy, biology...)"
                    "(I think it's a good idea to pay attention to [info_narra_start]things we can see, Sosotte.[info_end])"
                    "(We might not remember the things we see later, but that doesn't mean we should ignore them, right...?)" 

                if D0C1Text == _("{color=6B883C}• I can hear hospital machines nearby. Beep beep...{image=hearing}{/color}"):
                    $ stats_hearing = True
                    $ MemoryNumberForSpot1 = 3
                    "{w=1}(It's true, Sosotte!{w} I only noticed it now.)"
                    "(I suppose hearing this sound is good news.{w} No one's dying today, heh.)"
                    "(I think it's a good idea to pay attention to [info_narra_start]things we can hear, Sosotte.[info_end]{w} Certain sounds can help unlock memories, don't they...?)"

            "(No.)":
                $ _history = True
                "(Let's think about it a bit more, Sosotte!!!{w} This is important!!!)"
                $ Day0Choice -= 1
                jump Day0_CallScreen_Choice1
            
    
    window hide
    pause 2.0
    "(Let's see.{w} What else do I feel?)"
         

    pause 0.5
    $ Day0Choice = 3
    $ Day0Reroll = 1
    play sound write
    show screen day0_Memory2 with wiperight
    pause 0.5
    $ renpy.choice_for_skipping()
    show screen pointnclickbuttons with dissolve
    hide screen pointnclickbuttons #so its not doubled up


    label Day0_CallScreen_Choice2():
        show screen pointnclickbuttons
        call screen day0_Memory2

    if Day0Choice == 3:
        jump Day0_CallScreen_Choice2
    else:
        pass

    label Day0_Choice2Done():
        show screen day0_Memory2
        hide screen pointnclickbuttons
        $ Day0Choice += 1
        $ D0C2Text = MemoryTextForSpot2

        if D0C2Text == _("{color=6B883C}• Those painkillers did nothing. My head hurts...{image=str}{/color}"):
            $ temptext = _("{image=str}To listen to my body, see what it knows that my brain doesn't?")

        if D0C2Text == _("{color=6B883C}• There's a crossword puzzle on the table. I wonder if I could solve it...{image=int}{/color}"):
            $ temptext = _("{image=int}To keep my brain stimulated, so I can keep myself safe?")

        if D0C2Text == _("{color=6B883C}• People in the hallway seem happy.{image=psy}{/color}"):
            $ temptext = _("{image=psy}To pay attention to people around me, how they think?")

        "{w=0.5}(Is this what I want to remember?)"
        "([info_narra_start][temptext!t][info_end]){w}{nw}"
        $ _history = False

        menu:
            "([info_narra_start][temptext!t][info_end]){fast}"
            "(Yes.)":
                $ _history = True
                if D0C2Text == _("{color=6B883C}• Those painkillers did nothing. My head hurts...{image=str}{/color}"):
                    $ stats_str = True
                    $ MemoryNumberForSpot2 = 4
                    "{w=1}(It really does hurt.{w} Maybe I fell down when I got attacked?)"
                    "([info_narra_start]...Instead of only counting on our memories, we could rely on our body.{w} See what it remembers, or reacts to.[info_end])"

                if D0C2Text == _("{color=6B883C}• There's a crossword puzzle on the table. I wonder if I could solve it...{image=int}{/color}"):
                    $ stats_int = True
                    $ MemoryNumberForSpot2 = 5
                    "{w=1}(With my memory being how it is, solving it would be hard, but possible, I think...)"
                    "([info_narra_start]Paying attention to small details, and making sure to use our brain...{w} That's important, Sosotte.[info_end])" id Day0_Choice2Done_43cd1685

                if D0C2Text == _("{color=6B883C}• People in the hallway seem happy.{image=psy}{/color}"):
                    $ stats_psy = True
                    $ MemoryNumberForSpot2 = 6
                    "{w=1}(This must be a nice hospital...{w} No one seems too sad or upset.)"
                    "([info_narra_start]Paying attention to the reactions of people around us is important, Sosotte.[info_end])"

                window hide
                pause 2.0
            "(No.)":
                $ _history = True
                "(Let's think about it a bit more, Sosotte!!!{w} This is important!!!)"
                $ Day0Choice -= 1
                jump Day0_CallScreen_Choice2

    "(And, finally...)"

    pause 0.5
    $ Day0Choice = 6
    $ Day0Reroll = 1
    play sound write
    show screen day0_Memory3 with wiperight
    pause 0.5
    $ renpy.choice_for_skipping()
    show screen pointnclickbuttons with dissolve
    hide screen pointnclickbuttons #so its not doubled up


    label Day0_CallScreen_Choice3():
        show screen pointnclickbuttons
        call screen day0_Memory3


    if Day0Choice == 6:
        jump Day0_CallScreen_Choice3
    else:
        pass


    label Day0_Choice3Done():
        show screen day0_Memory3
        hide screen pointnclickbuttons
        $ Day0Choice += 1
        $ D0C3Text = MemoryTextForSpot3

        if D0C3Text == _("{color=B06531}• Amour is interesting.{image=amourstat}{/color}"):
            $ temptext = _("{image=amourstat}How interesting I find Amour?")

        if D0C3Text == _("{color=5597A9}• Betz is interesting.{image=betzstat}{/color}"):
            $ temptext = _("{image=betzstat}How interesting I find Betz?")


        "{w=0.5}(Is this what I want to remember?)"
        "([info_narra_start][temptext!t][info_end]){w}{nw}"
        $ _history = False

        menu:
            "([info_narra_start][temptext!t][info_end]){fast}"
            "(Yes.)":
                $ _history = True
                if D0C3Text == _("{color=B06531}• Amour is interesting.{image=amourstat}{/color}"):
                    $ stats_amour = True
                    $ MemoryNumberForSpot3 = 7
                    "{w=1}(Amour...)"
                    "(She seems laidback...{w} But also seems to be kind of a troublemaker, too.{w} He's been riling Betz up a bunch, today.)"
                    "(And she just looks so ripped...{w} Heh, I wouldn't mind a hug or two.)"
                if D0C3Text == _("{color=5597A9}• Betz is interesting.{image=betzstat}{/color}"):
                    $ stats_betz = True
                    $ MemoryNumberForSpot3 = 8
                    "{w=1}(Betz...)"
                    "(He seems to want to help us on our case, Sosotte.)"
                    "(And seems so noble, too...{w} And easy to fluster!{w} How cute!)"
                    "(And the way they're dressed...{w} What a handsome person!)"          
                window hide
                pause 2.0
            "(No.)":
                $ _history = True
                "(Let's think about it a bit more, Sosotte!!!{w} This is important!!!)"
                $ Day0Choice -= 1
                jump Day0_CallScreen_Choice3


    pause 1.0

    "(Hm...{w} What I want to remember is...)"
    if stats_sight:
        "(To pay attention to what I can [info_narra_start]{image=sight}see[info_end]...)"
    if stats_smell:
        "(To pay attention to what I can [info_narra_start]{image=smell}smell[info_end]...)"
    if stats_hearing:
        "(To pay attention to what I can [info_narra_start]{image=hearing}hear[info_end]...)"

    if stats_str:
        "(...To [info_narra_start]{image=str}what my body tells me[info_end]...)"
    if stats_int:
        "(...To [info_narra_start]{image=int}use my brain[info_end]...)"
    if stats_psy:
        "(...On [info_narra_start]{image=psy}analysing the people around me[info_end]...)"

    if stats_amour:
        "(...And on the lovely [info_narra_start]{image=amourstat}Amour[info_end].)"
    if stats_betz:
        "(...And on the smart [info_narra_start]{image=betzstat}Betz[info_end].)"


    "(Is this what I want us to remember in the future?){w}{nw}"
    $ _history = False
    menu:
        "(Is this what I want us to remember in the future?){fast}"
        "(Yes.)":
            $ _history = True
            jump statsdone
        "(Let's think about it a bit more...)":
            $ _history = True
            "(No, that's not right.{w} Let's think about that more...)"
            $ stats_sight = False
            $ stats_smell = False
            $ stats_hearing = False
            $ stats_str = False
            $ stats_int = False
            $ stats_psy = False
            $ stats_amour = False
            $ stats_betz = False
            hide screen day0_Memory1 with dissolve
            hide screen day0_Memory2 with dissolve
            hide screen day0_Memory3 with dissolve

            pause 0.5
            $ InPaCDialogue = False
            jump Day0_Choice1Start

    label statsdone:
        pause 0.5
        "(Yes, that should be good!)"

    "(Hmmm...{w} Ordinarily, I might have time to change my mind about these later on, but I have a feeling I'll be too busy today...)"
    "(...So this will have to do for now, Sosotte!)"

    hide screen day0_book_reminders
    hide screen day0_Memory1
    hide screen day0_Memory2
    hide screen day0_Memory3

    hide screen book_reminders_cutscene
    hide screen fakeMemory1
    hide screen fakeMemory2
    hide screen fakeMemory3
    hide screen pointnclickbuttons
    $renpy.hide_screen("pointnclickbuttons", layer="front")
    hide screen bookUI_memories_fake
    show screen bookUI_memories
    $ TurnOffReturn = False

    play sound turnpage_single
    show transition_nextpage onlayer overlay
    pause 2.0

    "(My memories, the case, people I've met, and my glossary...)"
    "([info_narra_start]I can check those at any time by interacting with the bookmarks on the right of my Scrap Book.[info_end])"
    "(...)"
    if stats_betz:
        "{image=betzstat}(After writing all this, I cannot help but look at Betz...)"
        play sound stats
        if stats_sight:
            play sound stats
            "{image=sight}(Betz's skin looks perfect.{w} So smooth...)"
        if stats_smell:
            play sound stats
            "{image=smell}(Betz's perfume...{w} Fig, and maybe some base notes of cedar?{w} It makes me want to inhale deeply.)"
        if stats_hearing:
            play sound stats
            "{image=hearing}(Betz's voice...{w} It was soft and quiet.{w} Something about it makes my heart tighten.)"
        "(And...)"
        play sound stats     
        if stats_psy:
            "{image=psy}(He's so easy to rattle...{w} What a fun person.)"
        if stats_int:
            "{image=int}(Betz seems to be the smartest out of the two.{w} I should listen to what he has to say...)"
        if stats_str:
            "{image=str}(...Betz seem thin, but I'm willing to bet this is all lean muscle.)"  

    if stats_amour:
        "{image=amourstat}(After writing all this, I cannot help but look at Amour...)"   
        play sound stats     
        if stats_sight:
            "{image=sight}(What strange hair Amour has!{w} It looks covered in hair gel!)"
        if stats_smell:
            "{image=smell}(Amour smells like lemons, and rocks after rain.{w} I wish I was making that up, Sosotte.{w} What soap does she use?!)"
        if stats_hearing:
            "{image=hearing}(Amour has a booming, but somewhat mellow voice.{w} Smooth...)" 
        "(And...)"
        play sound stats     
        if stats_psy:
            "{image=psy}(He really has been smiling this whole time...{w} Enjoying our presence, or...?)"
        if stats_int:
            "{image=int}(...Mmh.{w} He acts in a childish way, but I'm not sure he's as stupid as he appears.)"
        if stats_str:
            "{image=str}(She definitely looks like someone who lifts!!!{w} Don't underestimate her!!!{w} Use her for your own means!!!)"  

    pause 1.0
    play sound happy
    show betz e_sneutral
    show amour armsup
    s "Alright!{w} Um, s-{w=0.2}so, do either of you remember what we should do...?"
    b curious e_around "We were trying to get deeper into the Dwell.{w} Yesterday, you had a theory that we could find more clues about how your colleagues were attacked by going farther down..."
    a side "We didn't get to see more yesterday, after all!"
    b e_sad "But, you did get attacked yesterday, mademoiselle, so we could--"
    s "So, we should go back to the Dwell?{w} Sounds good to me!"
    show betz armsides e_sad m_wide
    a armsup e_surprised m_3 "Heh!{w} Not scared of the Dwell, Sosotte?"
    "(Not really.)"
    s "W-{w=0.2}Will you two not protect me...?{w} (;_;){w} *starts shaking like a frightened bird...!*"
    play sound happy
    show betz at charayay
    b blush e_upset sweat_on air_on "We will!{w} We absolutely will!!!"
    play sound happy
    show amour at charayay
    a callsaul e_neutral m_3 "Yeah!{w} Of course we will!"
    s "O-{w=0.2}Okay...{w} Then I don't mind heading back there, if you two are with me!{w} \\(^w^)/"
    show betz cough
    a armsup "Okay!"
    b armup e_neutral m_smile "Let us go back to the Dwell, then.{w} We'll have to go through the city, and take a Cara Van down..."
    stop music fadeout 2.0
    pause 2.0
    hide cgfar
    hide amour
    hide betz
    return
