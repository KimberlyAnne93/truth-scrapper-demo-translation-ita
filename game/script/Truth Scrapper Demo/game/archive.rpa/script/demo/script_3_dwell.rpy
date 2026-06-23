label script_3:
    $ save_name = _("(Day X • Time 13:32 • Dwell, Floor 1)")
    $ DateAndPlace = _("Day X • Time 13:32 • Dwell, Floor 1")
    $ renpy.force_autosave(take_screenshot=True, block=False)

    play sound turnpage_single
    stop bg
    show transition_nextpage onlayer overlay

    show cgpfar dwell_mine_entrance
    show cgfar dwell_mine_entrance_empty
    show cgmid dwell_mine_entrance_day1
    show cgclose dwell_mine_entrance
    pause 0.5
    play music dwell

    pause 2.0
    "(We arrive in the Dwell.)"
    if stats_sight:
        play sound stats
        "{image=sight}(The walls of this mine are covered in a Saturated Thread of some kind.{w} They're all different colors, spun by different hands.)"
    if stats_smell:
        play sound stats
        "{image=smell}(It smells strange, like citrus and mildew.{w} Something about it makes me feel faint.{w} Am I allergic?)"
    if stats_hearing:
        play sound stats
        "{image=hearing}(For a mine, they sure aren't mining very heavily.{w} Probably because it's a day off...?)"
    pause 1.0


    hide amour
    hide betz
    hide cgpfar
    hide cgfar
    hide cgmid
    hide cgclose
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    show blink black
    pause 1.0
    "(We walk for a while, passing many rooms...)"
    "(Without Amour and Betz guiding me, I'm not sure I would be able to find my way around.)"
    pause 1.0
    show cgfar dwell_day1_door
    show cgmidback dwell_day1_door
    show cgmid dwell_day1_door_door
    "(The tunnels continue endlessly, and they guide me through a path only they can see, until...)"
    pause 1.0
    a "Aaand this is the way to the lower floor!"
    s "Ah, but..."
    pause 1.0
    show blink end
    play sound blinkend
    window hide
    pause 2.0
    s "{w=0.5}...{w}I-{w=0.2}Isn't the way forward blocked?{w} (>x<);"
    show amour armsup e_neutral m_3 at appearTorightup
    show betz armsides at appearToleftup
    a "Yeah!{w} Every floor has one of those big locked doors.{w} But they're pretty easy to open!"
    a "All you need is to Saturate a Key Card!"
    "(Saturate...)"
    "(With a Saturation Ritual, we can Saturate normal objects, and give them magical powers.)"
    "(My Scrap Book, which allows me to record and instantly remember what I wrote down in it without reading it, is one such item.)"
    "(So, to open this door, we need to Saturate a Key Card...)"
    b curious e_sad "You can make one easily.{w} U-{w=0.2}Um..."
    pause 0.5
    show blink start
    play sound blinkstart
    pause 1.0
    hide amour
    hide betz
    show cgback day3supplies
    show cgmid day3suppliesbetz
    show cgclose day3suppliesbetz
    show blink end
    play sound blinkend
    pause 2
    b "I have some supplies for you to Saturate your Key Card..."
    b "I noticed you like putting eyes on your Saturated Items.{w} Like your hat, and your ribbon...{w} I hope it's not too presumptuous."
    s "Oh!{w} This is lovely...{w} Thank you so much, Betz!{w} *looks very grateful!*"
    a "I made some too!"
    pause 0.5
    show blink start
    play sound blinkstart
    pause 1.0
    hide cgback
    show cgmid day3suppliesamour
    show cgclose day3suppliesamour

    show blink end
    play sound blinkend
    pause 2
    a "Some eyes and ribbons!{w} For you!{w} Too!!!"
    s "Waaah!{w} Th-{w=0.2}Thank you, Amour!{w} *looks very grateful, but in a totally different way!*"
    pause 0.5
    show blink start
    play sound blinkstart
    pause 2.0
    hide cgmid
    hide cgclose

    show cgfar dwell_day1_door
    show cgmidback dwell_day1_door
    show cgmid dwell_day1_door_door

    show blink end
    play sound blinkend
    show amour armsup e_neutral m_3 at appearTorightup
    show betz armsides at appearToleftup
    hide cgback
    pause 1
    s "Alright!{w} I shall start making this Key Card!"
    b armup m_smile "Of course.{w} Amour and I will take a look around, to make sure it's safe, while you Saturate it..."
    stop music fadeout 2.0
    pause 1.0






    #########################
    ## Point and Click KeyCard
    #########################
    pause .5
    show blink start
    play sound blinkstart
    pause .5
    hide amour
    hide cgfar
    hide cgmidback
    hide cgmid
    hide amour
    hide betz

    $ WhichPaC = "day0_dwell keycard"
    $ pointnclickbuttons_order = _("Prepare the Key Card.")
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    pause .5
    show blink end
    play sound blinkend
    play music saturate_dwell

    show screen pointnclick_day3_keycard onlayer front
    pause 3.0
    "(I crouch down, getting ready to Saturate.)"
    if stats_hearing:
        play sound stats
        "{image=hearing}(I hear Amour and Betz bicker, their voices getting fainter as they walk away.)"
    "(The dull Key Card quietly waits for me to make art.)"
    "(Alright...{w} Let's start this Saturating Ritual.)"
    "(First, clap my hands three times, as if dusting them off.)"
    play sound singleclap
    pause 0.3
    play sound singleclap
    pause 0.3
    play sound singleclap
    pause 1.0
    "(And now...)"
    "(Saturated Items are peculiar beings.)"
    "(If there's one thing I found out during my research, it's that they seem to love being touched and handled with bare hands.)"
    if stats_int:
        play sound stats
        "{image=int}(Mid Artisans would say it's so the Item can \"feel your soul\", or some nonsense like that.)"
    if stats_psy:
        play sound stats
        "{image=psy}(Something about feeling closer to your creation, or something...)"
    "(I have gloves on, though, so...)"
    play sound clothes
    show pacclose day1_keycard_hands_1 with dissolve
    pause 0.5
    "{w=0.5}(Let me remove my gloves...)"
    play sound clothes
    show pacclose day1_keycard_hands_2 with dissolve
    pause 0.5
    stop music fadeout 5.0
    "{w=0.5}(So I can give it what it...)"
    window hide
    pause 2.0
    play bg heartbeat fadein 4.0
    show pacclose day1_keycard_hands_3 with dissolve
    pause 3.0
    "{w=2}({cps=*.1}...{/cps})"
    "({cps=*.25}...{/cps})"
    "({cps=*.25}...{w} I have scars here.{/cps})"
    pause 2.0
    "({cps=*.25}I{w} did notice{w} that my hands felt tight.{w} Difficult to move.{/cps})"
    if stats_str:
        pause 2.0
        play sound stats
        "{image=str}({cps=*.25}My body feels frozen, the more I look at them.{/cps})"
    if stats_int:
        pause 2.0
        play sound stats
        "{image=int}({cps=*.25}I've never written anything about those in my Scrap Book.{/cps})"
    if stats_sight:
        pause 2.0
        play sound stats
        "{image=sight}({cps=*.25}Those scars look old.{w} Years old.{/cps})"
    pause 2.0
    "({cps=*.25}...{/cps})"
    pause 4.0
    play sound clothes
    show pacclose day1_keycard_hands_2
    stop bg
    play music saturate_dwell
    "(Oh well!{w} Not gonna ruin our day, Sosotte!)"
    hide pacclose with dissolve
    pause 2.0
    "{w=0.5}(Alright.{w} Time to start this Saturation Ritual in earnest.)"
    "(First, let's say the words!)"
    s "Key Card, do this for me.{w} I want to open this locked door."
    pause 2.0
    "(After this...{w} Mmh...)"
    "(Let's just have fun and make this Key Card truly mine!)"
    $ renpy.choice_for_skipping()

    show blink start
    play sound blinkstart
    pause 1.0
    show blink end
    play sound blinkend
    $ IsPaCDisabled = False
    $ InPaCDialogue = False
    show screen pointnclickbuttons
    call screen pointnclick_day3_keycard onlayer front

    # all happens in the specific PaC file.

    #when finished the whole thing:
    label pointnclick_day3_keycard_continue():
    pause 1.5
    hide screen pointnclickbuttonhelp
    $renpy.hide_screen("pointnclick_day3_keycard", layer="front")

    show cgfar dwell_day1_door
    show cgmidback dwell_day1_door
    show cgmid dwell_day1_door_door
    show betz armsides at teleportright
    show amour armsup at teleportleft
    pause 2.0
    play music dwell
    show blink end
    play sound blinkend

    pause 0.5
    s "All done!"
    show betz e_smile m_smile
    a callsaul "Let me see, let me see!"
    play sound happy
    show amour at charayay
    a callsaul "Aw, it's a cute Key Card!{w} Very cute, Sosotte, very cute!"
    b "It looks lovely, mademoiselle."
    a "I like the eyes on it!{w} Same as your hat!{w} Cute!"
    a armsup "I usually just drop some paint on them and call it a day.{w} You went above and beyond!"
    call BGshake from _call_BGshake_22
    show betz aangry sweat_on m_angry e_angy at shake
    show amour at shake
    play sound shock
    b "WHAT?"
    s "J-{w=0.2}Just dropping some paint?!"
    a side "Yeah!{w} Just dropping paint works fine, you know?"
    b atalk e_ugh sweat_on "{cps=*.2}...{/cps}"
    s "{cps=*.2}...{/cps}"
    show amour armsup
    show betz e_sworried
    s "W-{w=0.2}Well, that aside...{w} We can open that door, now."

    #stop music fadeout 3.0
    window hide
    hide amour
    hide betz
    with dissolve
    pause 1.5
    play sound openkeycarddoor
    show cgmid dwell_day1_door_dooropen
    call BGshake from _call_BGshake_23

    pause 1.0

    show blink white with dissolve

    pause 2.0

    hide cgmid dwell_day1_door_door
    show cgmid dwell_day1_door_nodoor
    hide blink white with dissolve

    pause 2.5

    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide cgfar dwell_day1_door
    hide cgmidback dwell_day1_door
    hide cgmid dwell_day1_door_door
    hide cgpfar

    return