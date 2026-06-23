
default fakescreen_bigtitle = "MEMORIES"
default InPaCDialogue = False
default DateAndPlace = ""
define config.mouse_hide_time = None
# putting a number to the mouse hide time makes it bug out a bit jsyk
default persistent.gamepad_nav_speed = 0

default preferences.volume.music = 0.5
default preferences.volume.bg = 0.3
default preferences.volume.sfx = 0.5
default preferences.volume.ctc = 0.3

define config.has_autosave = True

################################################################################
## Trophies
################################################################################
define config.steam_appid = 3239830

#init python:
    #achievement.register("start")
    #achievement.register("end")


## BIG SCREENS ######################################################
## the frame thats always here
#####################################################################
# the frame thats there for gameplay
screen frame_page():
    use hide_mouse_screen
    layer 'frame_layer'
    add "gui/overlay/game_mainvisual.png"

#######################################
## Controller Support
#######################################
    default lerp_left_stick = LerpLeftStick(20.0)
    add lerp_left_stick


    # shortcuts mouse
    key ["K_ESCAPE", "K_MENU", "K_PAUSE", "pad_start_press", "mouseup_3"] activate_sound renpy.random.choice(turnpage) action ShowMenu('history')

    # remove the ability to use LB, X, Y and B

    key "pad_leftshoulder_press" action NullAction()
    if not renpy.get_screen("_gamepad_control"):
        key "pad_x_press" action NullAction()
        key "pad_b_press" action NullAction()
    key "pad_y_press" action NullAction()

    if not _menu:
        key pad_config.get_event("cancel") action ShowMenu()

    stick_event:
        event_type "axis"
        changed on_move_left_stick
        if leftstick_focus:
            which_stick 'right'
        else:
            which_stick stick_for_parallax
        if quick_menu:
            absorb_events True

#visuals for gamepad
    if pad_config.is_using_controller():
        if renpy.get_screen("bookUI_memories"):
            image "BookMenu/gamepadbuttons/xbox/xbox_dpad_up.png"

screen hide_mouse_screen():
    on "show" action If(pad_config.is_using_controller(), true=SetVariable("mouse_visible", False), false=SetVariable("mouse_visible", True))
    on "hide" action If(pad_config.is_using_controller(), true=SetVariable("mouse_visible", False), false=SetVariable("mouse_visible", True))
    $ mouse_visible = (pad_config.is_using_mouse() or pad_config.is_using_keyboard())
#######################################


# empty page
screen empty_page():
    add "gui/overlay/game_menu.png"

# title screen on a page. can change the text
screen newDayScreen():
    hbox:
        xalign 0.5
        yalign 0.5
        text "[NewDayScreenText!t]" size 140 xoffset -50



## OVERLAYS #########################################################
## overlays and stuff
#####################################################################

#date and place at the top right
screen dateandplace():
    hbox:
        xsize 700
        ysize 500
        xcenter 0.74
        yalign 0.16
        text "{noalt}[DateAndPlace!t]{/noalt}":
            size 35
            color "#5D855E"
            xalign 0.5

screen pointnclickbuttons():
    # done button
    imagebutton:
        id "button_done"
        idle "button_done"
        hover "button_done_hover"
        focus_mask True
        hover_sound renpy.random.choice(menu_hover_paper_random)
        activate_sound renpy.random.choice(turnpage)
        if WhichPaC == "day0_memory":
            if Day0Choice == 1:
                action Jump("Day0_Choice1Done")
            if Day0Choice == 3:
                action Jump("Day0_Choice2Done")
            if Day0Choice == 6:
                action Jump("Day0_Choice3Done")
        elif WhichPaC == "day0_dwell keycard":
            action Jump("pointnclick_day3_keycard_done")
        else:
            action None
    # top text
    vbox:
        align 0.5, 0.12
        frame:
            background Frame("gui/framewashi_green.png", gui.frame_borders, tile=gui.frame_tile)
            padding 50, 20, 50, 20
            textbutton "[pointnclickbuttons_order!t]"

screen pointnclickbuttonhelp():
    vbox:
        align 0.5, 0.12
        frame:
            background Frame("gui/framewashi_green.png", gui.frame_borders, tile=gui.frame_tile)
            padding 50, 20, 50, 20
            textbutton "[pointnclickbuttons_order!t]"

screen casemenu_monster():
    add "images/BookMenu/Doodles/casemenu_monster.png"

## MEMORY SCREEN CUSTCENE ############################################################
## memory screen cutscene + memories. they just appear they're not interactable!!!
######################################################################################
screen book_reminders_cutscene():
    use game_menu_no_navi_no_return(_("[fakescreen_bigtitle!t]")):
        style_prefix "memories"
        vbox:
            xsize 1550
            ysize 500
            text "[fakememoryscreen_title!t]" xoffset 30 size 70

screen fakeMemory1():
    vbox:
        style "memoryvbox_fake"
        yoffset -150
        textbutton "[fakememory1!t]" action None style "memorybox_fake" text_style "memoriesboxtext_fake"

screen fakeMemory2():
    vbox:
        style "memoryvbox_fake"
        yoffset -150+145
        textbutton "[fakememory2!t]" action None style "memorybox_fake" text_style "memoriesboxtext_fake"

screen fakeMemory3():
    vbox:
        style "memoryvbox_fake"
        yoffset -150+145+145
        textbutton "[fakememory3!t]" action None style "memorybox_fake" text_style "memoriesboxtext_fake"



screen fakeCase():
    vbox:
        style_prefix "mystery_hints"
        text "[fakememory1!t]"

style memoryvbox_fake:
    xmaximum 1500
    ymaximum 160
    #xoffset 150
    #yoffset 225

    yalign 0.5
    xalign 0.5
    #ysize 160
    #xsize 1500
    xoffset -25

style memorybox_fake:
    yalign 0.5

style memoriesboxtext_fake:
    xalign 0.5
    size 60
    text_align 0.5

## CASE SCREEN CUSTCENE ############################################################
## case screen cutscene
######################################################################################
screen book_mystery_cutscene():
    use game_menu_no_navi(_("CASE")):
    #edit it in General>>> screen game_menu_no_navi

        style_prefix "mystery"

        vbox:
            xsize 1550
            ysize 500
            text "[fakememoryscreen_title!t]" xoffset 30 size 70

screen fakeCase1():
    vbox:
        style "mystery_hints_vbox"
        style_prefix "mystery_hints"
        yoffset -150
        text "[fakememory1!t]"

style mystery_hints_vbox:
    xmaximum 1500
    ymaximum 160

    yalign 0.5
    xalign 0.5
    xoffset -25

style mystery_hints_text:
    xalign 0.5
    size 50
    text_align 0.5
    color gui.insensitive_color

## BOOK BUTTON ######################################################
## calls the book buttons
#####################################################################
label hidealltabs:
    hide screen bookUI_memories
    hide screen bookUI_mystery
    hide screen bookUI_characters
    hide screen bookUI_glossary
    with dissolve
    return

label hidealltabs_nodissolve:
    hide screen bookUI_memories
    hide screen bookUI_mystery
    hide screen bookUI_characters
    hide screen bookUI_glossary
    return

label showalltabs:
    show screen bookUI_memories
    show screen bookUI_mystery
    show screen bookUI_characters
    show screen bookUI_glossary
    with dissolve
    return

## ADDED FOR DEMO ##
## Cleared display focus properly when B or Left is pressed.
screen bookUI_memories():
    if current_dpad_menu == None:
        key "pad_dpup_press" action [SetBookUIFocus("menu_glossary", 1), SetVariable("current_dpad_menu", "book"), SetVariable("v_cursor_enabled", False)] capture False
        key "pad_dpdown_press" action [SetBookUIFocus("menu_glossary", 1), SetVariable("current_dpad_menu", "book"), SetVariable("v_cursor_enabled", False)] capture False

    if current_dpad_menu == "book":
        key "pad_dpdown_press" action SetBookUIFocus(current_book_highlight, 1)
        key "pad_dpup_press" action SetBookUIFocus(current_book_highlight, -1)
        key ["pad_dpleft_press", "pad_b_press"] action [ClearDisplayFocus(), SetVariable("current_dpad_menu", None)]
        key "pad_dpright_press" action NullAction()
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -20
        yoffset 50
        idle "BookMenu/tab_1_idle.png"
        hover "tab_1_hover"
        tooltip _("MEMORIES")
        at Appear_ZoomOvershoot
        if not TurnOffReturn:
            hover_sound renpy.random.choice(dialogue_hover_random)
            activate_sound renpy.random.choice(turnpage)
            keyboard_focus None
            action [SetVariable("GotNewChoice", False), SetVariable("ClickingOnChoice", False), SetVariable("VisibleDayPageMemory", CurrentDay), SetVariable("WhichChoiceWasClicked", 0)], ShowMenu("book_reminders")
            id "menu_memories"
    if GotNewChoice:
        imagebutton:
            xalign 0.95
            yalign 0.0
            xoffset 80
            yoffset 90
            at Appear_ZoomOvershoot
            idle "book_newMemory_idle"
            action None

screen bookUI_mystery():
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -20
        yoffset 300
        idle "BookMenu/tab_2_idle.png"
        hover "tab_2_hover"
        tooltip _("CASE")
        at Appear_ZoomOvershoot
        if not TurnOffReturn:
            hover_sound renpy.random.choice(dialogue_hover_random)
            activate_sound renpy.random.choice(turnpage)
            keyboard_focus None
            id "menu_mystery"
            action [SetVariable("GotNewCase", False), SetVariable("VisibleDayPageMystery", MysteryMaxPage)], ShowMenu("book_mystery")

    if GotNewCase:
        imagebutton:
            xalign 0.95
            yalign 0.0
            xoffset 80
            yoffset 350
            at Appear_ZoomOvershoot
            idle "book_newMystery_idle"
            action None

screen bookUI_characters():
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -30
        yoffset 480
        idle "BookMenu/tab_3_idle.png"
        hover "tab_3_hover"
        tooltip _("CHARACTERS")
        at Appear_ZoomOvershoot
        if not TurnOffReturn:
            hover_sound renpy.random.choice(dialogue_hover_random)
            activate_sound renpy.random.choice(turnpage)
            keyboard_focus None
            id "menu_characters"
            action [SetVariable("GotNewCharacter", False), SetVariable("character_name", "Sosotte"), SetVariable("character_title_text", "[You, Me, Her, Us. The Person In The Mirror.]")], ShowMenu("menu_character_sosotte")
    if GotNewCharacter:
        imagebutton:
            xalign 0.95
            yalign 0.0
            xoffset 80
            yoffset 520
            at Appear_ZoomOvershoot
            idle "book_newCharacter_idle"
            action None

## ADDED FOR DEMO ##
## Cleared display focus properly when pressing B or left
screen bookUI_glossary():
    # This is the first screen that pops up and that we can interact with, so if the memories are not available then show this.
    if renpy.get_screen("bookUI_memories") == None:
        if current_dpad_menu == None:
            key "pad_dpup_press" action [SetBookUIFocus("menu_glossary", 1), SetVariable("current_dpad_menu", "book"), SetVariable("v_cursor_enabled", False)]
            key "pad_dpdown_press" action [SetBookUIFocus("menu_glossary", 1), SetVariable("current_dpad_menu", "book"), SetVariable("v_cursor_enabled", False)]

        if current_dpad_menu == "book":
            key "pad_dpdown_press" action SetBookUIFocus(current_book_highlight, 1)
            key "pad_dpup_press" action SetBookUIFocus(current_book_highlight, -1)
            key ["pad_dpleft_press", "pad_b_press"] action [ClearDisplayFocus(), SetVariable("current_dpad_menu", None)]
            key "pad_dpright_press" action NullAction()
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -20
        yoffset 680
        idle "BookMenu/tab_4_idle.png"
        hover "tab_4_hover"
        tooltip _("GLOSSARY")
        at Appear_ZoomOvershoot
        if not TurnOffReturn:
            hover_sound renpy.random.choice(dialogue_hover_random)
            activate_sound renpy.random.choice(turnpage)
            keyboard_focus None
            id "menu_glossary"
            action [SetVariable("GotNewGlossary", False), SetVariable("glossary_name", ""), SetVariable("glossary_title_text", "")], ShowMenu("book_glossary")
    if GotNewGlossary:
        imagebutton:
            xalign 0.95
            yalign 0.0
            xoffset 80
            yoffset 750
            at Appear_ZoomOvershoot
            idle "book_newGlossary_idle"
            action None
# Fake screens

screen bookUI_memories_fake():
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -20
        yoffset 50
        idle "BookMenu/tab_1_idle.png"
        hover "tab_1_hover"
        at Appear_ZoomOvershoot
        action None
        id "menu_memories"

screen bookUI_mystery_fake():
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -50
        yoffset 300
        idle "BookMenu/tab_2_idle.png"
        hover "tab_2_hover"
        at Appear_ZoomOvershoot
        action None
        id "menu_mystery"

screen bookUI_characters_fake():
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -40
        yoffset 480
        idle "BookMenu/tab_3_idle.png"
        hover "tab_3_hover"
        at Appear_ZoomOvershoot
        action None
        id "menu_characters"

screen bookUI_glossary_fake():
    imagebutton:
        xalign 1.0
        yalign 0.10
        xoffset -20
        yoffset 680
        idle "BookMenu/tab_4_idle.png"
        hover "tab_4_hover"
        at Appear_ZoomOvershoot
        action None
        id "menu_glossary"

screen wishlist():
    style_prefix "wishlist"
    imagebutton:
        idle "CGs/wishlist/buttonwishlist.png"
        hover At("CGs/wishlist/buttonwishlist.png", outline_transform(5, "#ffffff"))
        pos (239-12, 600-14) keyboard_focus_insets (0, 20, 0, 20)
        at Appear_ZoomOvershoot
        focus_mask True default_focus 10
        hover_sound renpy.random.choice(menu_cancel)
        activate_sound renpy.random.choice(turnpage)
        action OpenURL("https://store.steampowered.com/app/3239830/Truth_Scrapper/")

    imagebutton:
        idle "CGs/wishlist/buttonnewsletter.png"
        hover At("CGs/wishlist/buttonnewsletter.png", outline_transform(5, "#ffffff"))
        pos (239-17, 737-15) keyboard_focus_insets (0, 20, 0, 20)
        at Appear_ZoomOvershoot
        focus_mask True
        hover_sound renpy.random.choice(menu_cancel)
        activate_sound renpy.random.choice(turnpage)
        action OpenURL("https://buttondown.com/insertdisc5")


    add "CGs/wishlist/logo.png":
        at Appear_ZoomOvershoot

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
        id 'w_return'
        keyboard_focus None
        action Return()
    frame:
        background Frame("gui/framewashi_green.png")
        padding 30, 20, 30, 20
        xalign 0.8
        yalign 0.9
        text _("Thank you for playing the Truth Scrapper demo!\nWhy not play again with different memories...?")
        at Appear_ZoomOvershoot

    key pad_config.get_event("cancel") action SetFocus("wishlist", 'w_return')

style wishlist_text:
    textalign 0.5

screen joystick_tuto():
    add "joystickanim":
        xoffset 100
        yoffset 70
        at Appear_ZoomOvershoot
