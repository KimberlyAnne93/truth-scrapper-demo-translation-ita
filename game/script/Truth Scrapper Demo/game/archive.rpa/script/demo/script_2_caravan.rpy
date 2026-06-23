label script_2:


    play sound turnpage_single
    show transition_nextpage onlayer overlay
    play music betz
    play bg city

    show cgfar city_trainstation_nobetz
    show cgpfar city_trainstation
    show cgmid city_trainstation
    pause 2.0
    "(We exit the hospital I was in, and arrive in a busy street.)"
    s "So...{w} Th-{w=0.2}this is the city of Cul-De-Puits?{w} \"Koo-deh-poo-ee\"?"
    show amour armsup e_neutral m_3 at appearTorightup
    show betz armsides e_smile m_smile at appearToleftup
    a "Yes!{w} It's the city on the walls of the sinkhole, and the Dwell is at the very bottom!"
    s "What a beautiful place..."
    if stats_smell:
        play sound stats
        "{image=smell}(There are so many lovely smells.{w} Grilled food, flowers for sale, and a slight smell of hot metal.{w} From a nearby shop, maybe?)"
    if stats_sight:
        play sound stats
        "{image=sight}(There are so many shops related to Saturated Items.{w} I've lost count of the number of shops selling paint, thread, or weird little beads.)"
    if stats_hearing:
        play sound stats
        "{image=hearing}(The city is noisy, but it's...{w} Reassuring noises.{w} People chatting with friends, shopkeepers trying to bring customers in.{w} People of all ages and sizes, walking around.)"

    "(So peaceful...{w} And my colleagues got attacked here, in such an idyllic place?)"
    b curious e_around "Hm...{w} Should we get lunch for the road, maybe?"
    a callsaul "Yeah!{w} We might spend the whole day in the Dwell!"
    show betz armsides e_smile m_smile
    a armsup "Wait for us here, Sosotte!{w} We'll be right back!"
    play sound runningcity
    show amour at zoomsaway
    stop music fadeout 2.0
    pause 0.5
    s "Ah...!"
    b "See you soon, mademoiselle."
    play sound walkingcity
    hide betz with dissolve
    pause 2.0
    "(...{w}They both left so quickly.)"
    "(So they'll buy us food, Sosotte?{w} How kind of them.)"
    pause 2.0
    play sound waitasec
    if stats_str:
        play sound stats
        "{image=str}(I feel the hair on the back of my neck raise.)"
    if stats_sight:
        play sound stats
        "{image=sight}(...{w}There's a group over there...)"
    if stats_psy:
        play sound stats
        "{image=psy}(I feel like I'm being stared at.)"
    "(Let me look around for a second...)"

    pause 1.5
    show bm pose at appearTomiddleup
    pause 0.1
    show bb pose at appearTomiddleup
    pause 0.1
    show bv pose at appearTomiddleup
    pause 3.0

    $ bbname = _("MINE DWELLER? (THIN)")
    $ bmname = _("MINE DWELLER? (BROAD)")
    $ bvname = _("PATH DWELLER?")

    bb "..."
    bm "..."
    bv "..."
    "(...Those three are staring daggers into me...)"
    "(We probably know them, Sosotte, but how?{w} Did we meet them yesterday?)"

    pause 0.25
    $ TurnOffReturn = True
    $ character_name = _("KALE")
    $ character_title_text = _("[Betz Brigade Member.]")
    play sound turnpage_single
    show screen menu_character_kale
    pause 1.0

    "(...Ah.{w} Seems like we have.{w} I wonder what happened...)"

    pause 0.5
    $ TurnOffReturn = False
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide screen menu_character_kale
    pause 1.0

    $ GotNewCharacter = True
    $ DayxNewCharacters = True
    play sound menu_notif

    "(Let's just cutely wave back.)"
    show bb at charayay
    play sound shout

    show bb m_anger e_anger
    show bv e_serious
    bb "...!!!"
    "(...That made them angrier.{w} Oops...)"
    pause 1.0
    play sound walkingcity
    hide bb
    hide bv
    hide bm
    with dissolve
    pause 1.0
    "(...{w}They left.)"
    pause 2.0
    show amour callsaul e_neutral m_3 at appearTorightup
    show betz armsides e_smile m_smile at appearToleftup
    play music amour
    stop bg fadeout 2.0
    a "We're back, Sosotte!{w} Here's your lunch!"
    s "Thank you..."
    b armup e_sad sweat_on m_neutral "...{w}Something wrong, mademoiselle?"
    show amour e_surprised m_o
    s "U-{w=0.2}Um...{w} Some people over there were glaring at me..."
    b alook"Is that so?{w} ...Ah."
    a armsup "Oh, them!"
    b "..."
    play sound shiny
    b armsides e_fakesmile m_fakesmile stars_on "Don't worry about it, mademoiselle.{w} Everything is all good."
    if stats_int:
        play sound stats
        "{image=int}(Both of them knew immediately who I was talking about.)"
    show amour laughing
    b "You had a bit of an altercation with them yesterday...{w} But it's all resolved, now.{w} Pay them no mind."
    "(What in the shattering hells happened yesterday...?)"
    if stats_psy:
        play sound stats
        "{image=psy}(For even gentle-looking Betz to react so coldly to them, sounds like whatever happened wasn't pretty...)"
    "(But whatever happened, I must've won.{w} Betz seems firmly on my side, here, heh.)"
    show amour armsup e_surprised m_o at shake
    show betz e_surprised m_wide stars_off at shake
    call BGshake
    play sound happy
    s "Really?!?{w} B-{w=0.2}But I'm so scared...!!!{w} They just looked so mad at me...{w} *glances at the trio, and then away, as if their mere stare is enough to hurt me...*"
    show betz blush air_on m_uwah_open at shake
    b "A-Ah, mademoiselle...{w} Please, don't..."
    a e_angry m_o "...{w}Hm..."
    a "I got some almonds..."
    show amour at charayay
    play sound happy
    a callsaul m_3 "So, what if we threw some almonds at them?"
    show betz aangry e_angy at charashake
    play sound shout
    b "WH--!!!"
    play sound happy
    "(HAH!{w} Yeah, that sounds fun...)"
    show amour m_o
    s "N-{w=0.2}No, it's alright, Amour...{w} What if...{w} What if some of them are allergic?{w} I..."
    a "...You're right..."
    a e_angry m_3 "We should throw peanuts instead.{w} WAY more chances to give them a flare up."
    show betz aangry e_closed at charashake
    play sound shout
    b "AMOUR!!!"
    s "Pft...{w} Heheh..."
    play sound waitasec
    a armsup e_surprised m_oend "!"
    "(Ah, Amour noticed I laughed.)"
    show betz e_sangy m_hmf
    s "Th-{w=0.2}That's so mean, Amour!{w} We, we shouldn't do that..."
    show betz blush air_on m_uwah_open at shake
    play sound happy
    s "...If we have to give them a flare up, I think grinding those peanuts into dust and blowing it their way should do the trick, right?{w} o(>w< )o"
    s "A-{w=0.2}Ah, I mean...!{w} *goes back to being a gentle kind little flower of a girl!*"
    play sound happy
    a laughing "Heheheh!{w} Yeah, yeah, exactly!"
    b armup e_mocking m_smile "P-{w=0.2}Please don't joke about bringing people to the hospital, you two..."
    if stats_hearing:
        play sound stats
        "{image=hearing}(Betz's voice is shaking...{w} Despite what he's saying, I think he found it funny.)"
    if stats_sight:
        play sound stats
        "{image=sight}(I see you smile, Betz!{w} You found it funny!)"
    if stats_psy:
        play sound stats
        "{image=psy}(The looks they're both giving me...{w} I think I may have blown my cover, but I just couldn't resist.)"
    a callsaul "Oh, oh, the Cara Van is here!"



    pause 0.5
    hide amour
    hide betz
    with dissolve
    play sound trainarrive
    show cgmidback city_trainstation_train at trainarrives
    pause 5.0
    stop music fadeout 2.0
    pause 2.0

    play sound turnpage_single
    show transition_nextpage onlayer overlay



    $ save_name = _("(Day X • Time 12:14 • Cara Van)")
    $ DateAndPlace = _("Day X • Time 12:14 • Cara Van")
    $ renpy.force_autosave(take_screenshot=True, block=False)

    play sound turnpage_single
    play bg bgtrain
    play music train
    show transition_nextpage onlayer overlay
    hide cgfar
    hide cgpfar
    hide cgmid
    hide cgmidback

    show cgpfar city_train_inside at train_rattle
    show cgfar city_train_inside at train_rattleslow
    show cgclose city_train_inside
    pause 3.0

    "(We enter the Cara Van, a Saturated vehicle heading towards the Dwell.)"
    "(Amour and Betz sit down on opposite sides of the vehicle...{w} So I put myself in the middle, and observe.)"
    pause 2.0
    "{w=1}(The railway leads down, deep into the sinkhole.)"
    "(There's a couple Cara Vans in front of us, and I can also see a couple other railways in the distance, all leading down as well.)"
    "(The Dwell must be traveled through a lot.)"
    pause 2.0
    "(The Cara Van we're on rocks back and forth.{w} I hope I won't get nauseous...)"
    if stats_smell:
        play sound stats
        "{image=smell}(...For a vehicle used daily, though, it smells surprisingly clean.)"
        "(It even smells a bit like...{w} Lavender?)"
    if stats_sight:
        play sound stats
        "{image=sight}(...Those Cara Van designs are lovely, though.{w} The teal color they've chosen is very nice.)"
        "(And that symbol, on the back of it...{w} A teal circle, with white lines coming out of the center...)"
        "(Perhaps it is the Cara Van's logo?{w} Or maybe even the city's?)"
    if stats_hearing:
        play sound stats
        "{image=hearing}(...The sound of the Cara Van on the tracks is surprisingly soothing, though.{w} What a nice journey.{w} I can easily imagine people napping while on their way to the Dwell.)"
    "(And that view...{w} As if we're descending into the center of the earth...)"
    "(How often do people take this beautiful, unsettling path?)"
    "(How quickly does it stop becoming a special experience, and start becoming routine?)"
    pause 2.0
    "(Our guides...{w} Amour, and Betz...)"
    "(Amour is looking out the window, not paying attention to anything else.{w} And Betz has their eyes closed, probably resting until we arrive.)"
    "(Heheh...)"
    pause 1.0

    if stats_amour:
        show blink start
        play sound blinkstart
        pause 2.0
        show cgpfar at train_sidecamera
        show cgfar at train_sidecamera
        show cgclose at train_sidecamerastatic
        show amour trainback at train_sidecamerastaticamour
        show blink end
        play sound blinkend
        $ shakeoffsetXnumber = 45
        pause 1.0

        "{image=amourstat}(Hm.{w} We like Amour best, right?)"
        pause 2.0
        "([info_narra_start]We have some time to look at our guide now[info_end], don’t we, Sosotte?)"

        #########################
        ## Point and Click Train
        #########################
        $ WhichPaC = "day1_train"
        $ pointnclickbuttons_order = _("Look at Amour.")
        $ InPaCDialogue = False
        $ IsPaCDisabled = False
        $ renpy.choice_for_skipping()
        show amour trainback_nooutline with dissolve
        show screen pointnclickbuttonhelp with dissolve
        call screen pointnclick_day1_trainamour onlayer front with dissolve

        # all happens in the specific PaC file.

        #when finished the whole thing:
        label pointnclick_day1_trainamour_continue():
        hide screen pointnclickbuttonhelp
        $renpy.hide_screen("pointnclick_day1_trainamour", layer="front")


        #DONE:
        pause 3.0
        show amour trainfront with dissolve
        pause 1.0
        a "{w=0.5}...{w}So?"
        s "Mmh?"
        a "So, so?{w} What do you think, Sosotte?{w} Am I handsome?"
        a "You've been looking at me for a bit now!"
        "(Ah, I suppose I wasn't being very subtle...)"
        if stats_str:
            play sound stats
            "{image=str}(I really was almost undressing her with my eyes.{w} Teehee, oopsies.)"
        play sound happy
        s "O-{w=0.2}Oh!{w} I'm sorry to stare...{w} Y-{w=0.2}You're just very nice to look at!{w} (>///<){w} *avoids your gaze shyly...*"
        a "HA!!!{w} So I AM handsome?"
        "(Fishing for compliments, are we?{w} Embarassing, Amour.)"
        s "I-{w=0.2}I--!!!{w} *fidgets fidgets!*"
        a "Heheheheheheh!"
        "(Amour just laughs.)"
        $ GotNewCharacter = True
        $ DayxAmourVain = True
        $ characters_update_amour = " •"
        play sound menu_notif
        "(We can definitely add \"vain\" to Amour's profile, Sosotte...)"
        "(...{w}Heh!)"
        "(What an interesting person we have found, Sosotte!)"

    if stats_betz:
        show blink start
        play sound blinkstart
        pause 2.0
        hide cgpfar
        hide cgfar
        hide cgclose

        show cgpfar day2_city_train_inside at train_rattle_x
        show cgfar day2_city_train_inside at train_rattleslow_x
        show cgclose day2_city_train_inside
        hide cgmid
        show betz trainfront rest
        show blink end
        play sound blinkend
        pause 0.5
        "{image=betzstat}(Hm.{w} We like Betz best, right?)"
        pause 2.0
        "([info_narra_start]We have some time to look at our guide now[info_end], don’t we, Sosotte?)"

        #########################
        ## Point and Click Train
        #########################
        $ WhichPaC = "day2_train"
        $ pointnclickbuttons_order = _("Look at Betz.")
        $ InPaCDialogue = False
        $ IsPaCDisabled = False
        $ renpy.choice_for_skipping()
        show screen pointnclickbuttonhelp with dissolve
        show betz trainfront_nooutline with dissolve
        call screen pointnclick_day2_trainbetz onlayer front with dissolve

        # all happens in the specific PaC file.

        #when finished the whole thing:
        label pointnclick_day2_trainbetz_continue():
        hide screen pointnclickbuttonhelp
        $renpy.hide_screen("pointnclick_day2_trainbetz", layer="front")

        b "..."
        s "..."
        b "........."
        pause 0.5
        show betz trainfront e_neutral m_neutral with dissolve
        pause 2.0
        b "Stop...{w} looking at me...{w} Please...."
        if stats_str:
            play sound stats
            "{image=str}(I feel myself smile.)"
        s "O-{w=0.2}Oh!{w} I'm sorry for staring...{w} Y-{w=0.2}You're just a very pretty person!"
        s "Did I make you uncomfortable?{w} I'm sorry...{w} (>//<)...{w} *tears my gaze away from your beauty...*"
        b "N-{w=0.2}No, it's...{w} It's alright, I'm just not used to..."
        "(To being looked at?{w} Cute.)"
        "(...{w}Wow, he really is blushing.)"
        "(...{w}Heh!)"
        "(What an interesting person we have found, Sosotte!)"
    stop music fadeout 2.0
    stop bg fadeout 2.0
    pause 3.0
    hide cgpfar
    hide cgfar
    hide cgclose
    hide cgmid
    hide amour
    hide betz

    return







############### amour

#####################################################################

label pointnclick_day1_trainamour_arms:
    show screen pointnclick_day1_trainamour onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(Artisan alive, she is SO JACKED.)"
    "(…{w}Stop looking, Sosotte!{w} Look elsewhere!{w} Right now!!!{w} (>///<){w} Heh.)"
    if stats_str:
        play sound stats
        "{image=str}(He IS very buff, though.{w} I suppose being a Path Dweller is hard work...)"
    ####################################################
    $ trainamour_arms_picked = True
    jump pointnclick_day1_trainamour_reset


label pointnclick_day1_trainamour_cloak:
    show screen pointnclick_day1_trainamour onlayer front
    $ IsPaCDisabled = True

    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(This cloak…{w} Could it be the Path Dwellers' Guild Item?{w} It feels tightly Saturated.)"
    "(Path Dwellers must explore the Dwell, right…?{w} So it probably must have some Protection Core, maybe even a Location Core in case they get lost…)"
    if stats_int:
        play sound stats
        "{image=int}(Did she not add any other Cores?{w} It doesn't strike me as very useful.)"
    "(Still, his is…{w} Pretty simple, isn't it?)"
    if stats_sight:
        play sound stats
        "{image=sight}(It's pretty dirty, too...{w} Does he know you're supposed to wash it every so often?)"
    if stats_smell:
        play sound stats
        "{image=smell}(It smells a little, too...{w} Does he know you're supposed to wash it every so often?)"
    ####################################################
    $ trainamour_cloak_picked = True
    jump pointnclick_day1_trainamour_reset


label pointnclick_day1_trainamour_clothes:
    show screen pointnclick_day1_trainamour onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(I have to be honest, Amour doesn’t seem to have a single shred of fashion sense.)"
    "(Is this perhaps just the usual Path Dweller uniform…{w} With no customizations whatsoever?!?)"
    "(Dull clothes, no personality, and not even a glimpse of any Saturated Jewelry.)"
    "(That cloak looks to be the only Saturated Item Amour owns…{w} How strange.{w} Even a child would have more.)"
    if stats_psy:
        play sound stats
        "{image=psy}(People with very little Saturated Items are usually ostracized, seen as people with no imagination, no drive…{w} Is it a choice for her, or…?)"
    ####################################################
    $ trainamour_clothes_picked = True
    jump pointnclick_day1_trainamour_reset


label pointnclick_day1_trainamour_hair:
    show screen pointnclick_day1_trainamour onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(What thick hair!{w} It must be a pain to brush.{w} Must be why she doesn’t seem to do it very often, huh?)"
    "(…{w}{w=0.5}That was a little mean.{w} Let's not say that out loud.)"
    "(It is a lovely red color, though.{w} Did she dye it, or is it natural?)"
    ####################################################
    $ trainamour_hair_picked = True
    jump pointnclick_day1_trainamour_reset



label pointnclick_day1_trainamour_face:
    show screen pointnclick_day1_trainamour onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(Still…{w} Even if she doesn't have much fashion sense, she has agreed to guide me into the Dwell.)"
    "(Getting to the Dwell is my first priority, and it would've been harder without someone to guide me.)"
    "(Not that she seems very smart.)"
    "(But, mmh…{w} It's true that she doesn't seem to know much about anything, and yet she doesn't strike me as someone with no intelligence.{w} Just with no interest.)"
    "(Just someone who walks to the beat of her own drum.)"
    "(Interesting...)"

    ####################################################
    $ trainamour_face_picked = True
    jump pointnclick_day1_trainamour_reset


## Train ######################################################
## point and click section
################################################################

default trainamour_arms_picked = False
default trainamour_cloak_picked = False
default trainamour_clothes_picked = False
default trainamour_face_picked = False
default trainamour_hair_picked = False

#bring back to the start, with stuff setup for it
label pointnclick_day1_trainamour_reset:
    $ InPaCDialogue = False
    if trainamour_arms_picked and trainamour_cloak_picked and trainamour_clothes_picked and trainamour_face_picked and trainamour_hair_picked:
        jump pointnclick_day1_trainamour_continue
    else:
        $ renpy.choice_for_skipping()
        show screen pointnclickbuttonhelp with dissolve
        $ IsPaCDisabled = False
        call screen pointnclick_day1_trainamour onlayer front

#image small_outline = Window(Transform(Placeholder(), crop=(0.0, 0.08, 1.0, 0.4)), style='empty', padding=(25, 25))
screen pointnclick_day1_trainamour():
    use prevent_skipping()
    viewport:
        #yoffset -100
        xoffset 44
        if not IsPaCDisabled and not InPaCDialogue:
            # if not picked before, it makes noise and can be clicked:

            if not trainamour_hair_picked:
                imagebutton:
                    idle "amour train_hotspot_hair"
                    hover At('amour train_hotspot_hair', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(pac_hover)
                    activate_sound renpy.random.choice(pac_click)
                    action Jump("pointnclick_day1_trainamour_hair")

            if not trainamour_cloak_picked:
                imagebutton:
                    idle "amour train_hotspot_cloak"
                    hover At('amour train_hotspot_cloak', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(pac_hover)
                    activate_sound renpy.random.choice(pac_click)
                    action Jump("pointnclick_day1_trainamour_cloak")

            if not trainamour_clothes_picked:
                imagebutton:
                    idle "amour train_hotspot_clothes"
                    hover At('amour train_hotspot_clothes', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(pac_hover)
                    activate_sound renpy.random.choice(pac_click)
                    action Jump("pointnclick_day1_trainamour_clothes")

            if not trainamour_arms_picked:
                imagebutton:
                    idle "amour train_hotspot_arms"
                    hover At('amour train_hotspot_arms', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(pac_hover)
                    activate_sound renpy.random.choice(pac_click)
                    action Jump("pointnclick_day1_trainamour_arms")

            if trainamour_arms_picked and trainamour_cloak_picked and trainamour_clothes_picked and trainamour_hair_picked:
                imagebutton:
                    idle "amour train_hotspot_face"
                    hover At('amour train_hotspot_face', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(pac_hover)
                    activate_sound renpy.random.choice(pac_click)
                    action Jump("pointnclick_day1_trainamour_face")


#####################################################################

## FACE ######################################################
## portraits and stuff
################################################################

##################################################
### Body
##################################################

image amour trainback:
    "images/Backgrounds/02_city_train_inside/amour_trainback.png"

image amour trainback_nooutline:
    "images/Backgrounds/02_city_train_inside/amour_trainbacknooutline.png"


layeredimage amour trainfront:
    group body auto: #amour_armsup_body
        attribute base default

    group eyes: #amour_armsup_eyes_neutral
        attribute e_neutral default:
            "amour_trainfront_eyes_neutral"


    group mouth: #amour_armsup_mouth_neutral
        attribute m_3 default:
            "amour_trainfront_mouth_3"
        attribute m_3_s:
            "images/Backgrounds/02_city_train_inside/amour_trainfront_mouth_3_S.png"

##################################################
### Eyes
##################################################

image amour_trainfront_eyes_neutral:
    "images/Backgrounds/02_city_train_inside/amour_trainfront_body_eyes_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Backgrounds/02_city_train_inside/amour_trainfront_body_eyes_C.png"
    0.1
    "images/Backgrounds/02_city_train_inside/amour_trainfront_body_eyes_OC.png"
    .1
    repeat

##################################################
### Mouth
##################################################

image amour_trainfront_mouth_3_talking:
        "images/Backgrounds/02_city_train_inside/amour_trainfront_mouth_3_TA.png" #for ah sound
        pause 0.15
        "images/Backgrounds/02_city_train_inside/amour_trainfront_mouth_3_S.png" #for closed mouth
        pause 0.15
        "images/Backgrounds/02_city_train_inside/amour_trainfront_mouth_3_TO.png" #for oh sound
        pause 0.15
        "images/Backgrounds/02_city_train_inside/amour_trainfront_mouth_3_S.png"
        pause 0.15
        repeat

image amour_trainfront_mouth_3 = ConditionSwitch(
    "amourLipflapping", "amour_trainfront_mouth_3_talking",
    "True", "images/Backgrounds/02_city_train_inside/amour_trainfront_mouth_3_S.png")

######################## betz

## Train ######################################################
## point and click section
################################################################
#####################################################################

label pointnclick_day2_trainbetz_cloak:
    show screen pointnclick_day2_trainbetz onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(A purple cloak, with blue fabric lining the inside...{w} It shimmers softly under the sunlight.)"
    "(I believe this is the Guild Item for Path Dwellers.)"
    "(It seems old, but well maintained.{w} Betz must've been working for the Path Dwellers for a long time...)"
    if stats_smell:
        play sound stats
        "{image=smell}(Smells lovely, too.{w} Is that...{w} Pear...?)"
    ####################################################
    $ trainbetz_cloak_picked = True
    jump pointnclick_day2_trainbetz_reset


label pointnclick_day2_trainbetz_earring:
    show screen pointnclick_day2_trainbetz onlayer front
    $ IsPaCDisabled = True

    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(What a lovely earring.{w} Glass.{w} Cerulean blue.)"
    "(...No, it is not actually pure blue!{w} There seems to be something blue in it, giving it its color.)"
    "(What could it be...{w} I can't see it from here.)"
    "(And it's Saturated...{w} I wonder what Core it's made out of.)"
    if stats_int:
        play sound stats
        "{image=int}(Usually, people Saturate earrings with either Communication Cores, or Glamour Cores, so...?)" id pointnclick_day2_trainbetz_earring_50222104
    if stats_sight:
        play sound stats
        "{image=sight}(Honestly, if I had to guess?{w} Glamour Core.{w} Their skin is just too perfect, and has that barely noticeable shimmer...)"
    if stats_psy:
        play sound stats
        "{image=psy}(It's shiny and polished...{w} Somehow, I get the feeling that this is a well loved Item.)"
    ####################################################
    $ trainbetz_earring_picked = True
    jump pointnclick_day2_trainbetz_reset


label pointnclick_day2_trainbetz_clothes:
    show screen pointnclick_day2_trainbetz onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(Tight fitting clothes.{w} They follow Betz's curves well.)"
    "(Heh.{w} As if.{w} Betz is just flat everywhere.)"
    "(...{w}Betz does have a very established sense of style.{w} Quite dashing, to be honest.)"
    if stats_str:
        play sound stats
        "{image=str}(Covered from head to toe.{w} Their face is the only part of their body uncovered.)"
        "(Are they prudish, or...?)"
    ####################################################
    $ trainbetz_clothes_picked = True
    jump pointnclick_day2_trainbetz_reset


label pointnclick_day2_trainbetz_thread:
    show screen pointnclick_day2_trainbetz onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(Betz seems to be surrounded in some kind of thread...)"
    "(I first thought it was some kind of harness, but the thread looks too thin for that.)"
    "(There's also a wisp of it, always flowing around them, as if alive...{w} Has to be Saturated in some way.)"
    "(Either way: very kinky.{w} Easy to restrain.{w} I approve.{w} *nods.*)"
    ####################################################
    $ trainbetz_thread_picked = True
    jump pointnclick_day2_trainbetz_reset



label pointnclick_day2_trainbetz_face:
    show screen pointnclick_day2_trainbetz onlayer front
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    ####################################################
    # DIALOGUE
    ####################################################
    hide screen pointnclickbuttonhelp with dissolve
    "(Betz...{w} He's agreed to be my Guide, and to accompany me to the Dwell.)"
    "(Why would he help me, though?)"
    "(Out of duty?{w} I don't feel like that's the only reason.)"
    if stats_psy:
        play sound stats
        "{image=psy}(Maybe a sense of...{w} Guilt?)"
    "(Whatever the reason is, he has been kind, and helpful.)"
    "(He's interesting, too.{w} I first saw him as kind of emotionless, but that only seems to be a façade.{w} They're a lot easier to rattle than I thought.)"
    "(Interesting...)"

    ####################################################
    $ trainbetz_face_picked = True
    jump pointnclick_day2_trainbetz_reset

#####################################################################

default trainbetz_face_picked = False
default trainbetz_cloak_picked = False
default trainbetz_earring_picked = False
default trainbetz_clothes_picked = False
default trainbetz_thread_picked = False

#bring back to the start, with stuff setup for it
label pointnclick_day2_trainbetz_reset:
    $ InPaCDialogue = False
    if trainbetz_face_picked and trainbetz_cloak_picked and trainbetz_earring_picked and trainbetz_clothes_picked and trainbetz_thread_picked:
        jump pointnclick_day2_trainbetz_continue
    else:
        if trainbetz_cloak_picked and trainbetz_earring_picked and trainbetz_clothes_picked and trainbetz_thread_picked:
            pause 0.5
            show betz trainfront_nooutline_blush with dissolve
        $ renpy.choice_for_skipping()
        show screen pointnclickbuttonhelp with dissolve
        $ IsPaCDisabled = False
        call screen pointnclick_day2_trainbetz onlayer front

#image small_outline = Window(Transform(Placeholder(), crop=(0.0, 0.08, 1.0, 0.4)), style='empty', padding=(25, 25))
screen pointnclick_day2_trainbetz():
    use prevent_skipping()
    viewport:
        if not IsPaCDisabled and not InPaCDialogue:
            # if not picked before, it makes noise and can be clicked:

            if not trainbetz_thread_picked:
                imagebutton:
                    idle "betz train_hotspot_thread"
                    hover At('betz train_hotspot_thread', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)
                    action Jump("pointnclick_day2_trainbetz_thread")

            if not trainbetz_cloak_picked:
                imagebutton:
                    idle "betz train_hotspot_cloak"
                    hover At('betz train_hotspot_cloak', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)
                    action Jump("pointnclick_day2_trainbetz_cloak")

            if not trainbetz_clothes_picked:
                imagebutton:
                    idle "betz train_hotspot_clothes"
                    hover At('betz train_hotspot_clothes', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)
                    action Jump("pointnclick_day2_trainbetz_clothes")

            imagebutton:
                if trainbetz_cloak_picked and trainbetz_earring_picked and trainbetz_clothes_picked and trainbetz_thread_picked:
                    idle "betz train_hotspot_face_blush"
                    hover At('betz train_hotspot_face_blush', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)
                    action Jump("pointnclick_day2_trainbetz_face")
                else:
                    idle "betz train_hotspot_face_rest"

            if not trainbetz_earring_picked:
                imagebutton:
                    idle "betz train_hotspot_earring"
                    hover At('betz train_hotspot_earring', outline_transform(10, "#ffffff"))
                    focus_mask True
                    hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)
                    action Jump("pointnclick_day2_trainbetz_earring")
            else:
                image "betz train_hotspot_earring"

########################################################################################################

## FACE ######################################################
## portraits and stuff
################################################################

##################################################
### Body
##################################################
image betz trainfront_nooutline:
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_body_base_noutline.png"
image betz trainfront_nooutline_blush:
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_body_base_noutlineblush.png"


layeredimage betz trainfront:
    group body auto: #betz_armsup_body
        attribute base default:
            "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_body_base.png"

    group eyes: #betz_armsup_eyes_neutral
        attribute e_neutral default:
            "betz_trainfront_eyes_neutral"
        attribute rest:
            "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_rest.png"
        attribute e_alright:
            "betz_trainfront_eyes_alright"
        attribute e_worried:
            "betz_trainfront_eyes_worried"
        attribute e_side:
            "betz_trainfront_eyes_side"

    group mouth: #betz_armsup_mouth_neutral
        attribute m_neutral default:
            "betz_trainfront_mouth_neutral"
        attribute m_neutral_s:
            "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_S.png"

        attribute rest:
            null

        attribute m_smile:
            "betz_trainfront_mouth_smile"
        attribute m_smile_s:
            "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_smile_S.png"

    group sweat: #betz_armsup_mouth_neutral
        attribute sweat_on:
            "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_sweat_on.png"
        attribute sweat_off default:
            null

# ##################################################
# ### Eyes
# ##################################################

image betz_trainfront_eyes_neutral:
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_neutral_C.png"
    0.1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_neutral_OC.png"
    .1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_neutral_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    repeat

image betz_trainfront_eyes_side:
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_side_C.png"
    0.1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_side_OC.png"
    .1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_side_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    repeat

image betz_trainfront_eyes_worried:
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_worried_C.png"
    0.1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_worried_OC.png"
    .1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_worried_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    repeat

image betz_trainfront_eyes_alright:
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_alright_C.png"
    0.1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_alright_OC.png"
    .1
    "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_eyes_alright_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    repeat
# ##################################################
# ### Mouth
# ##################################################

image betz_trainfront_mouth_neutral_talking:
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_TA.png" #for ah sound
        pause 0.15
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_S.png" #for closed mouth
        pause 0.15
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_TO.png" #for oh sound
        pause 0.15
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_S.png"
        pause 0.15
        repeat

image betz_trainfront_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_trainfront_mouth_neutral_talking",
    "True", "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_S.png")

image betz_trainfront_mouth_smile_talking:
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_TA.png" #for ah sound
        pause 0.15
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_smile_S.png" #for closed mouth
        pause 0.15
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_neutral_TO.png" #for oh sound
        pause 0.15
        "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_smile_S.png"
        pause 0.15
        repeat

image betz_trainfront_mouth_smile = ConditionSwitch(
    "betzLipflapping", "betz_trainfront_mouth_smile_talking",
    "True", "images/Backgrounds/11_city_train_inside_betz/betz_trainfront_mouth_smile_S.png")