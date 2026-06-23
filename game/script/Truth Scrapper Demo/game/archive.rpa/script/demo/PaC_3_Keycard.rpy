## KeyCard ######################################################
## KeyCard point and click section
################################################################
default day3_keycard_eye = 0
default day3_keycard_ribbon = 0
default day3_keycard_paint = 0
default day3_keycard_color = False
default day3_keycard_carved = True
default day3_keycard_betz = False
default day3_keycard_amour = False

#bring back to the start, with stuff setup for it
label pointnclick_day3_keycard_reset:
    $ IsPaCDisabled = False
    $ InPaCDialogue = False
    $ renpy.choice_for_skipping()
    show screen pointnclickbuttons
    call screen pointnclick_day3_keycard onlayer front



screen pointnclick_day3_keycard():
    use prevent_skipping()

    # full image of the thing. BACK -> FRONT
    add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_table.png"

    # black and white
    if not day3_keycard_color:
        add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_base_NC.png"

        if day3_keycard_paint == 1:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_paint_1_NC.png"
        if day3_keycard_paint == 2:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_paint_2_NC.png"

        if day3_keycard_ribbon == 1:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_ribbon_1_NC.png"
        if day3_keycard_ribbon == 2:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_ribbon_2_NC.png"

        if day3_keycard_eye == 1:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_eye_1_NC.png"
        if day3_keycard_eye == 2:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_eye_2_NC.png"



    # color
    else:
        if day3_keycard_amour:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_base_CA.png"
        if day3_keycard_betz:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_base_CB.png"

        if day3_keycard_paint == 1:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_paint_1_C.png"
        if day3_keycard_paint == 2:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_paint_2_C.png"

        if day3_keycard_ribbon == 1:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_ribbon_1_C.png"
        if day3_keycard_ribbon == 2:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_ribbon_2_C.png"

        if day3_keycard_eye == 1:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_eye_1_C.png"
        if day3_keycard_eye == 2:
            add "images/PaC/PaC Day 3 Key Card/pacclose day3_keycard_custom_eye_2_C.png"




# imagebuttons here!
    imagebutton:
        idle "pacclose day3_keycard_selectable_eye"
        focus_mask True
        if not IsPaCDisabled and not InPaCDialogue:
            hover At('pacclose day3_keycard_selectable_eye', outline_transform(5, "#ffffff"))
            hover_sound renpy.random.choice(custo_hover_random)
            activate_sound renpy.random.choice(custo_confirm_random)
            action Jump("pointnclick_day3_keycard_eye")
        else:
            action None

    imagebutton:
        idle "pacclose day3_keycard_selectable_paint"
        focus_mask True
        if not IsPaCDisabled and not InPaCDialogue:
            hover At('pacclose day3_keycard_selectable_paint', outline_transform(5, "#ffffff"))
            hover_sound renpy.random.choice(custo_hover_random)
            activate_sound renpy.random.choice(custo_confirm_random)
            action Jump("pointnclick_day3_keycard_paint")
        else:
            action None

    imagebutton:
        idle "pacclose day3_keycard_selectable_ribbon"
        focus_mask True
        if not IsPaCDisabled and not InPaCDialogue:
            hover At('pacclose day3_keycard_selectable_ribbon', outline_transform(5, "#ffffff"))
            hover_sound renpy.random.choice(custo_hover_random)
            activate_sound renpy.random.choice(custo_confirm_random)
            action Jump("pointnclick_day3_keycard_ribbon")
        else:
            action None

## buttons ###########################################
## buttons hell
######################################################

label pointnclick_day3_keycard_eye:
    #math
    $ day3_keycard_eye += 1
    if day3_keycard_eye == 3:
        $ day3_keycard_eye = 0
    call pointnclick_day1_keycard_firsttime
    # back to showing the screen:
    jump pointnclick_day3_keycard_reset


label pointnclick_day3_keycard_ribbon:

    $ day3_keycard_ribbon += 1
    if day3_keycard_ribbon == 3:
        $ day3_keycard_ribbon = 0
    call pointnclick_day1_keycard_firsttime
    jump pointnclick_day3_keycard_reset


label pointnclick_day3_keycard_paint:

    $ day3_keycard_paint += 1
    if day3_keycard_paint == 3:
        $ day3_keycard_paint = 0
    call pointnclick_day1_keycard_firsttime
    jump pointnclick_day3_keycard_reset

## ALL DONE ###########################################
## ok
######################################################
default keycard_firsttime = False

label pointnclick_day1_keycard_firsttime:
    if not keycard_firsttime:

        show screen pointnclick_day3_keycard onlayer front
        $ IsPaCDisabled = True
        $ InPaCDialogue = True
        pause 1.0
        hide screen pointnclickbuttons
        "(Mmh, this looks nice, but...)"
        "(I think I have a couple more ideas in me.{w} [info_narra_start]I can use this again and try something else with it[info_end]...)"
        $ keycard_firsttime = True
        $ InPaCDialogue = False
    return


label pointnclick_day3_keycard_done:
    $ IsPaCDisabled = True
    $ InPaCDialogue = True
    show screen pointnclick_day3_keycard onlayer front
    hide screen pointnclickbuttons

    if day3_keycard_eye == 0 or day3_keycard_ribbon == 0 or day3_keycard_paint == 0:
        "(...)"
        "(Sosotte, we didn't add any Supplies.{w} [info_narra_start]Let's add at least one of each[info_end] and Saturate this thing, okay?)"
        jump pointnclick_day3_keycard_reset
    else:
        "{w=0.5}(Am I truly done with this?){w}{nw}"
        $ _history = False

        menu:
            "(Am I truly done with this?){fast}"
            "(Yes.)":
                $ _history = True
                window hide
                pause 1.0
                s "There we go!"
                s "\"Key Card, do this for me, that’s what I want!!!\""

                if day3_keycard_eye == 1:
                    if day3_keycard_ribbon == 1 or day3_keycard_paint == 1:
                        $ day3_keycard_amour = True
                    else:
                        $ day3_keycard_betz = True
                else:
                    if day3_keycard_ribbon == 2 or day3_keycard_paint == 2:
                        $ day3_keycard_betz = True
                    else:
                        $ day3_keycard_amour = True

                pause 0.5
                ###############
                #the henshin.
                ###############
                play sound henshinsaturate
                show henshin keycard_start
                pause 0.7
                $ day3_keycard_color = True
                show henshin keycard_end
                pause 0.6
                ###############
                pause 2.0
                "(All done!)"
                hide screen pointnclickbuttons with dissolve
                show blink start
                play sound blinkstart
                pause 0.5
                stop music fadeout 2.0

                #TO HIDE SCREEN ON NON-DEFAULT LAYER:
                $renpy.hide_screen("pointnclick_day3_keycard", layer="front")
                $ InPaCDialogue = False
                jump pointnclick_day3_keycard_continue

            "(No.)":
                $ _history = True
                "(Let's try something else...)"
                $ InPaCDialogue = False
                jump pointnclick_day3_keycard_reset



#####################################################################