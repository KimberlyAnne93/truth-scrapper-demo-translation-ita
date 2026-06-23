## Train ######################################################
## point and click section
################################################################
default pointnclick_day0_dream_check = 0
default pointnclick_day0_flower_click = False
#bring back to the start, with stuff setup for it
label pointnclick_day0_dream_reset:
    if pointnclick_day0_dream_check == 4:
        jump pointnclick_day0_dream_continue
    else:
        show screen pointnclickbuttonhelp with dissolve
        $ IsPaCDisabled = False # Disable skipping during the pac section
        call screen pointnclick_day0_dream onlayer front

image day0_dream_1_flower_click:
    "images/PaC/PaC Day 0 Dream/cgfar day0_dream_2_flower_click1.png"
    pause 0.75
    "images/PaC/PaC Day 0 Dream/cgfar day0_dream_2_flower_click2.png"
    pause 0.75
    repeat

#image small_outline = Window(Transform(Placeholder(), crop=(0.0, 0.08, 1.0, 0.4)), style='empty', padding=(25, 25))
screen pointnclick_day0_dream():
    use prevent_skipping()

    if not IsPaCDisabled:
        # if not picked before, it makes noise and can be clicked:
        if pointnclick_day0_dream_check == 0:
            add "images/PaC/PaC Day 0 Dream/cgpfar day0_dream_1_BG.png"
            imagebutton:
                idle "cgpfar day0_dream_1_flower_idle"
                hover "cgpfar day0_dream_1_flower_hover"
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                action Jump("pointnclick_day0_dream_advance")
            if pointnclick_day0_flower_click:
                add "day0_dream_1_flower_click"

        if pointnclick_day0_dream_check == 1:
            add "images/PaC/PaC Day 0 Dream/cgfar day0_dream_2_BG.png"
            imagebutton:
                idle "cgfar day0_dream_2_flower"
                hover At('cgfar day0_dream_2_flower', outline_transform(5, "#ffffff"))
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                action Jump("pointnclick_day0_dream_advance")

        if pointnclick_day0_dream_check == 2:
            add "images/PaC/PaC Day 0 Dream/cgmid day0_dream_3_BG.png"
            imagebutton:
                idle "cgmid day0_dream_3_flower"
                hover At('cgmid day0_dream_3_flower', outline_transform(5, "#ffffff"))
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                action Jump("pointnclick_day0_dream_advance")

        if pointnclick_day0_dream_check == 3:
            add "images/PaC/PaC Day 0 Dream/cgfar day0_dream_4_BG.png"
            add "images/PaC/PaC Day 0 Dream/cgmid day0_dream_4_hand.png"
            imagebutton:
                idle "cgmid day0_dream_4_flower"
                hover At('cgmid day0_dream_4_flower', outline_transform(10, "#ffffff"))
                focus_mask True
                hover_sound renpy.random.choice(pac_hover)
                activate_sound renpy.random.choice(pac_click)
                action Jump("pointnclick_day0_dream_continue")

#####################################################################

label pointnclick_day0_dream_advance:
    show screen pointnclick_day0_dream onlayer front
    $ IsPaCDisabled = True
    pause 1.5
    $ pointnclick_day0_dream_check += 1
    if pointnclick_day0_dream_check == 1:
        $ pointnclickbuttons_order = _("I want to forget.")
    elif pointnclick_day0_dream_check == 2:
        $ pointnclickbuttons_order = _("Now, Saturate.")
    elif pointnclick_day0_dream_check == 3:
        $ pointnclickbuttons_order = _("We can do this, together.")
    pause 1.5
    jump pointnclick_day0_dream_reset


