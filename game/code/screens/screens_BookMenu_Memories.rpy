## REMINDERS MENU ###################################################
## reminders menu. the bane of my existence. this is for what it looks like
#####################################################################

#####
# IF THE MEMORIES ARENT CENTERED: its the click indicator.
#####
default IsPaCDisabledStored = False

screen book_reminders_choices():
    default IsPaCDisabledStored = IsPaCDisabled
    use hide_mouse_screen
    style_prefix "memoriesfull"
 
    vbox:
        xalign 0.5
        yoffset 20
        ################### MEMORIES
        if VisibleDayPageMemory == 0:
            vbox:
                style "memoryvbox"
                textbutton _("{color=B06531}• Met Amour.{/color}") action None style "memorybox" text_style "memoriesboxtext"

            vbox:
                style "memoryvbox"
                textbutton _("{color=5597A9}• Met Betz.{/color}") action None style "memorybox" text_style "memoriesboxtext"

            vbox:
                style "memoryvbox"
                textbutton _("{color=6B883C}• Nothing else interesting happened.{/color}") action None style "memorybox" text_style "memoriesboxtext"

        elif CurrentDay == VisibleDayPageMemory: #can be changed

            #choice text number +1 must be in here and not in the whichmemoryisgonnaappear label. wont work otherwise
            hbox:
                style "memoryvbox"
                textbutton "[D0C1Text!t]" action None style "memorybox" text_style "memoriesboxtext"

            hbox:
                style "memoryvbox"
                textbutton "[D0C2Text!t]" action None style "memorybox" text_style "memoriesboxtext"

            hbox:
                style "memoryvbox"
                textbutton "[D0C3Text!t]" action None style "memorybox" text_style "memoriesboxtext"


## ADDED FOR DEMO ## 
## Fixed IsPaCDisabled being set to the wrong value
screen book_reminders():
    default IsPaCDisabledStored = IsPaCDisabled

    on "show" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), SetVariable("IsPaCDisabled", True)]
    on "replaced" action [Show("screen_transition_nextpage_noreturn", _zorder = 100)]
    on "hide" action SetVariable("IsPaCDisabled", IsPaCDisabledStored)

    use game_menu_no_navi(_("Memories")):
    #edit it in General>>> screen game_menu_no_navi

        style_prefix "memories"

        vbox:
            xsize 1550
            ysize 500
            if VisibleDayPageMemory == 0:
                text _("THE DWELL • DAY X-1") xoffset 30 size 70
            else:
                text _("THE DWELL • DAY X") xoffset 30 size 70

            use book_reminders_choices
    
        ######################## ARROWS
        ###CAN GO -1 DAY
        if VisibleDayPageMemory != 0 and TurnOffReturn == False:
            imagebutton:
                xpos 80
                ypos 550
                idle "BookMenu/arrow_left_idle.png"
                hover "left_arrow_hover"
                hover_sound renpy.random.choice(menu_hover_random)
                activate_sound renpy.random.choice(turnpage)
                keyboard_focus None
                action [SetVariable("VisibleDayPageMemory", VisibleDayPageMemory - 1), SetVariable("ClickingOnChoice", False)], Jump("RecallMemoryPageText")

            if pad_config.is_using_controller():
                image "BookMenu/gamepadbuttons/xbox/xbox_lb.png"
                key "pad_leftshoulder_press" action [SetVariable("VisibleDayPageMemory", VisibleDayPageMemory - 1), SetVariable("ClickingOnChoice", False)], Jump("RecallMemoryPageText")

            #CAN GO +1 DAY
        if VisibleDayPageMemory < CurrentDay and TurnOffReturn == False:
            imagebutton:
                xpos 1300
                ypos 550
                idle "BookMenu/arrow_right_idle.png"
                hover "right_arrow_hover"
                hover_sound renpy.random.choice(menu_hover_random)
                activate_sound renpy.random.choice(turnpage)
                keyboard_focus None
                action [SetVariable("VisibleDayPageMemory", VisibleDayPageMemory + 1), SetVariable("ClickingOnChoice", False)], Jump("RecallMemoryPageText")

            if pad_config.is_using_controller():
                image "BookMenu/gamepadbuttons/xbox/xbox_rb.png"
                key "pad_rightshoulder_press" action [SetVariable("VisibleDayPageMemory", VisibleDayPageMemory + 1), SetVariable("ClickingOnChoice", False)], Jump("RecallMemoryPageText")


# LB AND RB BUTTONS AND GAMEPAD

    if TurnOffReturn == False:
        if VisibleDayPageMemory != 0:
            if pad_config.is_using_controller():
                image "BookMenu/gamepadbuttons/xbox/xbox_lb.png":
                    yoffset -80
                key "pad_leftshoulder_press" action [SetVariable("VisibleDayPageMemory", VisibleDayPageMemory - 1), SetVariable("ClickingOnChoice", False)], Jump("RecallMemoryPageText")

        if VisibleDayPageMemory < CurrentDay:
            if pad_config.is_using_controller():
                image "BookMenu/gamepadbuttons/xbox/xbox_rb.png":
                    yoffset -80
                key "pad_rightshoulder_press" action [SetVariable("VisibleDayPageMemory", VisibleDayPageMemory + 1), SetVariable("ClickingOnChoice", False)], Jump("RecallMemoryPageText")


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
            image "bbutton":
                xalign 1.0
                yalign 0.10
            key "pad_b_press" activate_sound renpy.random.choice(turnpage) action [SetVariable("IsPaCDisabled", IsPaCDisabledStored), ShowMenu("screen_transition_previouspage")]
    ##################

    # page turn at the bottom because it needs to be in front of everything
    if not ClickingOnChoice:
        image "transition_nextpage"

style memories_button:
    size_group "memories"
    xalign 0.5

style memoryvbox:
    yalign 0.5
    xalign 0.5
    ysize 160
    xsize 1300
    box_wrap True

style memorybox:
    yalign 0.5
    xalign 0.5
    hover_background Frame("gui/framewashi.png", 63, 59, 86, 58) padding (50, 15, 50, 15)

style memoriesboxtext:
    size 60
    text_align 0.5

    # #make them the same color so its not weird
    # color gui.insensitive_color
    # selected_color gui.idle_color

    # hover_color gui.hover_color
    # selected_hover_color gui.hover_color
    


