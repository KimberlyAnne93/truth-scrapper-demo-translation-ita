

label pointnclick_day1_endday_event:
    show cgclose bookdown
    # can't use the other PaC buttons
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    $ pointnclick_day1_endday_CHECK += 1
    ####################################################
    # DIALOGUE
    ####################################################
    if pointnclick_day1_endday_CHECK == 1:
        s "{w=0.5}Hello?{w} Amour?"
        window hide
        pause 2.0
        "{w=1}({cps=*.1}...{/cps}{w}Nothing here.)"

    ####################################################
    if pointnclick_day1_endday_CHECK == 2:
        s "{w=0.5}Betz?{w} Is that you?"
        window hide
        pause 3.0
        "{w=1}({cps=*.1}...{/cps})"
        "(Silence.)"
        "(Great.{w} Amazing.)"
        pause 2.0
        "(In my pocket,{w} I adjust the grip I have around my pen, nib ready to stab.)"

    ####################################################
    if pointnclick_day1_endday_CHECK == 3:
        s "I-{w=0.5}If you're both trying to scare me, it's not working!!!{w} (-︿-);;;;;"
        window hide
        pause 4.0
        "{w=1}(I tighten my grip.)"

    ####################################################
    if pointnclick_day1_endday_CHECK == 4:
        show cgmid dwell_day1_end_outline
        pause 0.7
        call BGshake from _call_BGshake_30
        play sound scare
        play music pursuit
        s "What THE--{w=1.0}{nw}"
    ####################################################
    if pointnclick_day1_endday_CHECK < 4:
        pause 1.0
        show blink start
        play sound blinkstart
        pause 1.0
        show blink end
        play sound blinkend
        # back to showing the screen:
    jump pointnclick_day1_endday_reset

## MONSTER ######################################################
## point and click section
################################################################
default pointnclick_day1_endday_CHECK = 0

#bring back to the start, with stuff setup for it
label pointnclick_day1_endday_reset:
    $ InPaCDialogue = False
    if pointnclick_day1_endday_CHECK == 4:
        jump pointnclick_day1_endday_continue
    else:
        $ renpy.choice_for_skipping()
        $ IsPaCDisabled = False
        call screen pointnclick_day1_endday onlayer front

screen pointnclick_day1_endday():
    use prevent_skipping()

    if pointnclick_day1_endday_CHECK == 0:
        if not IsPaCDisabled and not InPaCDialogue:
            # if not picked before, it makes noise and can be clicked:
            imagebutton:
                idle "pac dwell_day1_end_1"
                hover "pac dwell_day1_end_1_outline"
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                action Jump("pointnclick_day1_endday_event")

    if pointnclick_day1_endday_CHECK == 1:
        if not IsPaCDisabled and not InPaCDialogue:
            # if not picked before, it makes noise and can be clicked:
            imagebutton:
                idle "pac dwell_day1_end_3"
                hover "pac dwell_day1_end_3_outline"
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                action Jump("pointnclick_day1_endday_event")

    if pointnclick_day1_endday_CHECK == 2:
        if not IsPaCDisabled and not InPaCDialogue:
            imagebutton:
                idle "pac dwell_day1_end_2"
                hover "pac dwell_day1_end_2_outline"
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                action Jump("pointnclick_day1_endday_event")

    if pointnclick_day1_endday_CHECK == 3:
        if not IsPaCDisabled and not InPaCDialogue:
            imagebutton:
                idle "cgmid dwell_day1_end"
                hover "cgmid dwell_day1_end_outline"
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                hovered Jump("pointnclick_day1_endday_event")
                action Null()
