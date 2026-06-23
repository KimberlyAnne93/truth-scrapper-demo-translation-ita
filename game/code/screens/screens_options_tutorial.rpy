## TUTORIAL ##########################################################
## ok.
#####################################################################
default tutorial_name = ""
default tutorial_title_text = ""
## MAIN MENU ##############################################
## setting up menu
###########################################################

## ADDED FOR DEMO ##
## Edited this to show the proper tutorial name, and also to highlight the proper button on exiting the menu.
screen game_tutorial(scroll=None, yinitial=0.0):
    on "show" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), Show("navigation_tutorial", _zorder=0), [SetVariable("tutorial_name", _("TUTORIAL")), SetVariable("tutorial_title_text", _("What do you wanna learn?"))]]
    on "replaced" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), Function(print, "run replaced")]
    on "hide" action [Hide("navigation_tutorial"), SetFocusGameMenuButton("Tutorial"), Function(print, "run hide")]
    key "mouseup_3" activate_sound renpy.random.choice(turnpage) action Return()

    style_prefix "game_tutorial"
    modal True

    frame:
        style "game_tutorial_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    controller_viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        vbox:
                            transclude

                else:

                    transclude

    label "\n[tutorial_name!t]{size=*0.5}{color=#707070}\n [tutorial_title_text!t]{/color}{/size}"
    image "transition_nextpage"



style game_tutorial_label is game_menu_label
style game_tutorial_label_text is game_menu_label_text
style game_tutorial_text is gui_text

style game_tutorial_outer_frame:
    bottom_padding 45
    top_padding 220
    background "gui/overlay/game_menu_side_big.png"

style menu_tutorial_label_text:
    size gui.label_text_size
    line_spacing 0

style game_tutorial_label:
    xpos 425
    yoffset 50
    ysize 180


## LIST ###################################################
## list of tutorial on the side
###########################################################

## ADDED FOR DEMO ##
## Made the menu exit with the page turning animation properly
## And now it also scrolls properly!
screen navigation_tutorial():

    vbox:
        style_prefix "navigation_tutorial"


        xpos gui.navigation_xpos + 200
        yalign 0.4
        xanchor 0.5
        yoffset 65
        xmaximum 250

        spacing gui.navigation_spacing -5

        if True:
            textbutton _("PLAYING"):
                default_focus 100
                action ShowMenu("menu_tutorial_play")
                activate_sound renpy.random.choice(turnpage)

            textbutton _("HISTORY"):
                action ShowMenu("menu_tutorial_history")
                activate_sound renpy.random.choice(turnpage)

            textbutton _("AUTOPLAY"):
                action ShowMenu("menu_tutorial_autoplay")
                activate_sound renpy.random.choice(turnpage)

            textbutton _("SKIPPING"):
                action ShowMenu("menu_tutorial_skip")
                activate_sound renpy.random.choice(turnpage)

            textbutton _("SAVING"):
                action ShowMenu("menu_tutorial_save")
                activate_sound renpy.random.choice(turnpage)

            textbutton _("OPTIONS"):
                action ShowMenu("menu_tutorial_options")
                activate_sound renpy.random.choice(turnpage)

            text ""
            textbutton _("BACK") action [Hide("game_tutorial"), If(main_menu, true=Return(), false=ShowMenu("history"))]

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
            action [Hide("game_tutorial"), If(main_menu, true=Return(), false=ShowMenu("history"))]

    # right click return
        key "mouseup_3" activate_sound renpy.random.choice(turnpage) action [Hide("game_tutorial"), If(main_menu, true=Return(), false=ShowMenu("history"))]

    # gamepad return
        if pad_config.is_using_controller():
            image "bbutton":
                xalign 1.0
                yalign 0.10
            key "pad_b_press" activate_sound renpy.random.choice(turnpage) action [Hide("game_tutorial"), If(main_menu, true=Return(), false=ShowMenu("history"))]

style navigation_tutorial_button is gui_button
style navigation_tutorial_button_text is gui_button_text

style navigation_tutorial_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound renpy.random.choice(menu_hover)
    activate_sound renpy.random.choice(turnpage)

## ADDED FOR DEMO ##
## Added the selected hover color to these buttons so that it's clear that they're chosen.
## It also makes them match the game menu better.
style navigation_tutorial_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    text_align 0.5
    selected_hover_color gui.selected_hover_color



## CHARACTERS ##############################################
## each tutorial has their own screen
###########################################################
style menu_tutorial_vbox:
    yoffset 70
    xsize 1200

screen menu_tutorial_play():
    modal True

    tag game_tutorial
    use game_tutorial(_("play")):

        style_prefix "menu_tutorial"

        vbox:
            text _("• This visual novel doesn't require much. [info_narra_start]Just click to advance the story[info_end]!")

            text _("\n• You know you can click when you see a triangle symbol at the [info_narra_start]bottom right of the dialogue screen[info_end].")
            image "images/BookMenu/Tutorial/tutorial_play_ctc.png":
                xalign 0.5

            text _("\n• At the top right of the dialogue screen, you'll find the [info_narra_start]quick menu[info_end].")
            image "images/BookMenu/Tutorial/tutorial_play_quickmenu.png":
                xalign 0.5

            text _("\n• [info_narra_start]Hovering over the icons[info_end] will tell you what they do.")

    on "replace" action [SetVariable("tutorial_name", _("PLAYING THE GAME")), SetVariable("tutorial_title_text", _("Just click, baby!"))]

screen menu_tutorial_history():
    modal True

    tag game_tutorial
    use game_tutorial(_("history")):

        style_prefix "menu_tutorial"

        vbox:
            text _("• Missed a line of dialogue? You can click the [info_narra_start]HISTORY[info_end] button in the quickmenu at any time, and read previous lines!")
            image "images/BookMenu/Tutorial/tutorial_history.png":
                xalign 0.5

    on "replace" action [SetVariable("tutorial_name", _("HISTORY")), SetVariable("tutorial_title_text", _("Um, LINE?!?!"))]


screen menu_tutorial_save():
    modal True

    tag game_tutorial
    use game_tutorial(_("save")):

        style_prefix "menu_tutorial"

        vbox:
            text _("• Want to take a break? [info_narra_start]You can SAVE your progress at any time by clicking the SAVE button in the quickmenu![info_end]")
            image "images/BookMenu/Tutorial/tutorial_save_save.png":
                xalign 0.5

            text _("\n• Once you save your game, you can [info_narra_start]LOAD[info_end] your save in the [info_narra_start]LOAD screen[info_end] and pick up where you left off.")

            text _("\n• This game has [info_narra_start]multiple endings[info_end] depending on your choices throughout the story, so [info_narra_start]save early, save often![info_end]")

    on "replace" action [SetVariable("tutorial_name", _("SAVING/LOADING")), SetVariable("tutorial_title_text", _("Record your progress!"))]

screen menu_tutorial_autoplay():
    modal True

    tag game_tutorial
    use game_tutorial(_("autoplay")):

        style_prefix "menu_tutorial"

        vbox:
            text _("• Don't want to keep clicking? You can click the [info_narra_start]AUTOPLAY[info_end] button in the quickmenu at any time, and watch the dialogue come in automatically!")
            image "images/BookMenu/Tutorial/tutorial_auto_button.png":
                xalign 0.5

            text _("\n• To stop AUTOPLAY, you can just [info_narra_start]click the AUTOPLAY button again[info_end].")

            text _("\n• If the AUTOPLAY goes by too quickly or slowly, you can [info_narra_start]change its speed[info_end] in the OPTIONS menu.")
            image "images/BookMenu/Tutorial/tutorial_auto_speed.png":
                xalign 0.5

    on "replace" action [SetVariable("tutorial_name", _("AUTOPLAY")), SetVariable("tutorial_title_text", _("Look ma, no hands!"))]

screen menu_tutorial_skip():
    modal True

    tag game_tutorial
    use game_tutorial(_("skip")):

        style_prefix "menu_tutorial"

        vbox:
            text _("• Have you seen this before? You can skip quickly through the story by pressing the [info_narra_start]SKIP[info_end] button in the quickmenu!")
            image "images/BookMenu/Tutorial/tutorial_skip_button.png":
                xalign 0.5

            text _("\n• To stop skipping, you can just [info_narra_start]click anywhere[info_end].")

            text _("\n• If, for some reason, you want to [info_narra_start]skip text you've never seen before[info_end], you can toggle [info_narra_start]\"Skip Unseen Text\"[info_end] in the OPTIONS menu.")
            image "images/BookMenu/Tutorial/tutorial_skip_unseen.png":
                xalign 0.5

    on "replace" action [SetVariable("tutorial_name", _("SKIPPING")), SetVariable("tutorial_title_text", _("Nyoom~~~"))]

screen menu_tutorial_options():
    modal True

    tag game_tutorial
    use game_tutorial(_("options")):

        style_prefix "menu_tutorial"

        vbox:
            text _("• Want to [info_narra_start]skip unseen text[info_end]? Want to [info_narra_start]change the speed[info_end] at which the text appears? Want to remove [info_narra_start]shaky camera moves[info_end]? This, and way more, are available in the [info_narra_start]OPTIONS menu[info_end]!")
            image "images/BookMenu/Tutorial/tutorial_options_button.png":
                xalign 0.5

            text _("\n• You can find more accessibility options in the Options' [info_narra_start]Accessibility menu[info_end], including a font override, high contrast text, and way more!")
            image "images/BookMenu/Tutorial/tutorial_options_access.png":
                xalign 0.5

    on "replace" action [SetVariable("tutorial_name", _("OPTIONS")), SetVariable("tutorial_title_text", _("Customize your experience!"))]