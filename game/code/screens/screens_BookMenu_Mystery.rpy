## SETUP ###################################################
## variables and stuff
#####################################################################
default VisibleDayPageMystery = 2
default GotNewCase = False
# play sound menu_notif

default MysteryMaxPage = 2

## MYSTERY MENU ###################################################
## the text is also here
#####################################################################
## ADDED FOR DEMO ##
## Fixed the IsPaCDisabled being set to false always. now it sets it to the appropriate value always.
screen book_mystery():
    default IsPaCDisabledStored = IsPaCDisabled

    on "show" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), SetVariable("IsPaCDisabled", True)]
    on "replaced" action [Show("screen_transition_nextpage_noreturn", _zorder = 100)]
    on "hide" action SetVariable("IsPaCDisabled", IsPaCDisabledStored)
    
    use hide_mouse_screen
    use game_menu_no_navi(_("CASE")):
    #edit it in General>>> screen game_menu_no_navi

        style_prefix "mystery"

        vbox:
            xsize 1550
            ysize 500

            if VisibleDayPageMystery == 3:
                text _("THE DWELL • DAY X") xoffset 30 size 70
            if VisibleDayPageMystery == 1 or VisibleDayPageMystery == 2:
                text _("THE DWELL • DAY X-1") xoffset 30 size 70


            ################### MYSTERIES
            vbox:
                style_prefix "mystery_hints"

                if VisibleDayPageMystery == 1:

                    text _("• Throughout the last few months, three Truth Scrappers were sent to research the Dwell.")

                    text _("• Went to research the city's culture, and its high Item Saturation Rate.")
                    
                    text _("• All got attacked.")

                    text _("• I was sent to find out who targeted them, and why.")


                elif VisibleDayPageMystery == 2:
                    image "images/BookMenu/Doodles/casemenu_monster.png":
                        xpos -220
                        ypos -400



        ######################## ARROWS
        ###CAN GO -1 DAY
        if TurnOffReturn == False:
            if VisibleDayPageMystery != 1:
                imagebutton:
                    xpos 80
                    ypos 630
                    idle "BookMenu/arrow_left_idle.png"
                    hover "left_arrow_hover"
                    hover_sound renpy.random.choice(menu_hover_random)
                    activate_sound renpy.random.choice(turnpage)
                    keyboard_focus None
                    action [SetVariable("VisibleDayPageMystery", VisibleDayPageMystery - 1)], Jump("RecallMysteryPageText")

                if pad_config.is_using_controller():
                    image "BookMenu/gamepadbuttons/xbox/xbox_lb.png"
                    key "pad_leftshoulder_press" action [SetVariable("VisibleDayPageMystery", VisibleDayPageMystery - 1)], Jump("RecallMysteryPageText")

            if VisibleDayPageMystery < MysteryMaxPage:
                imagebutton:
                    xpos 1300
                    ypos 630
                    idle "BookMenu/arrow_right_idle.png"
                    hover "right_arrow_hover"
                    hover_sound renpy.random.choice(menu_hover_random)
                    activate_sound renpy.random.choice(turnpage)
                    keyboard_focus None
                    action [SetVariable("VisibleDayPageMystery", VisibleDayPageMystery + 1)], Jump("RecallMysteryPageText")

# LB AND RB BUTTONS AND GAMEPAD

    if TurnOffReturn == False:
        if VisibleDayPageMystery != 1:
            if pad_config.is_using_controller():
                image "BookMenu/gamepadbuttons/xbox/xbox_lb.png"
                key "pad_leftshoulder_press" action [SetVariable("VisibleDayPageMystery", VisibleDayPageMystery - 1)], Jump("RecallMysteryPageText")

        if VisibleDayPageMystery < MysteryMaxPage:
            if pad_config.is_using_controller():
                image "BookMenu/gamepadbuttons/xbox/xbox_rb.png"
                key "pad_rightshoulder_press" action [SetVariable("VisibleDayPageMystery", VisibleDayPageMystery + 1)], Jump("RecallMysteryPageText")
    ##################
    # ALL THE CANCELS
    ##################
    # visual arrow return
    if TurnOffReturn == False:
        imagebutton:
            xalign 1.0
            yalign 0.10
            xoffset -10
            yoffset 50
            idle "BookMenu/tab_return_idle.png"
            hover "tab_return_hover"
            hover_sound renpy.random.choice(menu_cancel)
            activate_sound renpy.random.choice(turnpage)
            #at Appear_ZoomOvershoot
            keyboard_focus None
            action [SetVariable("IsPaCDisabled", IsPaCDisabledStored), ShowMenu("screen_transition_previouspage")]

    # right click return
        key "mouseup_3" activate_sound renpy.random.choice(turnpage) action [SetVariable("IsPaCDisabled", IsPaCDisabledStored), ShowMenu("screen_transition_previouspage")]

    # gamepad return
        if pad_config.is_using_controller():
            image "bbutton"
            key "pad_b_press" activate_sound renpy.random.choice(turnpage) action [SetVariable("IsPaCDisabled", IsPaCDisabledStored), ShowMenu("screen_transition_previouspage")]
    ##################

    # page turn at the bottom because it needs to be in front of everything
    image "transition_nextpage"

style mystery_outer_frame:
    bottom_padding 43
    top_padding 220
    background "gui/overlay/game_menu_side_big.png"

style mystery_hints_text:
    xalign 0.5
    yalign 0.0
    size 45
    text_align 0.5

    #make them the same color so its not weird
    color gui.insensitive_color

label RecallMysteryPageText():
    #so screen doesn't disappear
    call screen book_mystery

    return