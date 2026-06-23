################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################
#drop shadow to all dialogue
define gui.dialogue_text_outlines = [ (0, "#B3AEA4", 2, 2) ]


define config.mouse = { }
define config.mouse['default'] = [ ( "gui/button/cursor_idle.png", 11, 31) ]
define config.mouse['button'] = [ ( "gui/button/cursor_menu.png", 11, 31) ]

#############remove mouse rollback
#define config.rollback_enabled = False

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize 38
    left_bar Frame("gui/bar/left.png", 6, 6, 6, 6, tile=False)
    right_bar Frame("gui/bar/right.png", 6, 6, 6, 6, tile=False)

style vbar:
    xsize 38
    top_bar Frame("gui/bar/top.png", 6, 6, 6, 6, tile=False)
    bottom_bar Frame("gui/bar/bottom.png", 6, 6, 6, 6, tile=False)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

# A variant of the vertical scrollbar that looks like it's always focused
# this is to emulate the look of a focused scrollbar
style vscrollbar_vp_focused:
    take vscrollbar
    thumb Frame("gui/scrollbar/vertical_hover_thumb.png", 6, 6, 6, 6, tile=False)

style slider:
    ysize 38
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize 38
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding (6, 6, 6, 6)
    background Frame("gui/frame.png", 6, 6, 6, 6, tile=False)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    # ctc SOUND!!!!!!!!!!!
    # if not config.skipping and what: ##This keeps the sound from playing when the dialogue is being skipped.
    #     on 'hide' action Play('sound', menu_hover) ## This plays the sound whenever the window is hidden.

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

        use quick_menu


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0, yoffset=40)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

## ADDED FOR DEMO ##
## Adjusted the default_focus so it takes priority.
## Also, fixed the SetFocus() not having the layer name.
screen choice(items):
    style_prefix "choice"
    # Setting default focus to this.
    default selection = 0
    hbox at Appear_ZoomOvershoot:
        for i in range(len(items)):
            if len(items) == 3:
                if i == 0:
                    textbutton items[i].caption id "but_1" default_focus 1000 action items[i].action at rotateleft
                if i == 1:
                    textbutton items[i].caption id "but_2"action items[i].action at rotatemiddle
                if i == 2:
                    textbutton items[i].caption id "but_3" action items[i].action at rotateright

            elif len(items) == 2:
                if i == 0:
                    textbutton items[i].caption id "but_1" default_focus 1000 action items[i].action at rotatemiddle
                if i == 1:
                    textbutton items[i].caption id "but_2" action items[i].action at rotateright
            else:
                textbutton items[i].caption default_focus 1000 action items[i].action
    # Ignore up/down focus.
    if len(items) == 3:
        focused_on "but_1" key "focus_right" action SetFocus("choice", "but_2", layer="say_layer")
        focused_on "but_2" key "focus_left" action SetFocus("choice", "but_1", layer="say_layer")
        focused_on "but_2" key "focus_right" action SetFocus("choice", "but_3", layer="say_layer")
        focused_on "but_3" key "focus_left" action SetFocus("choice", "but_2", layer="say_layer")
    elif len(items) == 2:
        focused_on "but_1" key "focus_right" action SetFocus("choice", "but_2", layer="say_layer")
        focused_on "but_1" key "focus_left" action NullAction()

        focused_on "but_2" key "focus_left" action SetFocus("choice", "but_1", layer="say_layer")
        focused_on "but_2" key "focus_right" action NullAction()
        
    key "focus_up" action NullAction()
    key "focus_down" action NullAction()


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_hbox:
    xalign 0.5
    yalign 0.87
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(turnpage)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    idle_color '#BFBFBF'


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

## ADDED FOR DEMO ##
## Fixed focus issues for quick menu so that it doesn't go crazy once you scroll / repeat inputs.
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if pad_config.is_using_controller():
        image "BookMenu/gamepadbuttons/xbox/xbox_dpad_left.png"

    if current_dpad_menu == "quick" and not renpy.get_screen("confirm"):
        key ["pad_dpup_press", "pad_dpdown_press", "pad_b_press"] action [ClearDisplayFocus(), SetVariable("current_dpad_menu", None)]

    if quick_menu:
        if not renpy.get_screen("confirm"):
            if current_dpad_menu == None:
                if not renpy.get_screen("bookUI_memories") and not renpy.get_screen("bookUI_glossary"):
                    key ["repeat_pad_dpup_press", "repeat_pad_dpdown_press", "pad_dpup_press", "pad_dpdown_press"] action NullAction()

                if not renpy.get_screen("choice"):
                    key "pad_dpleft_press" action [SetFocus("say", "quick_history", "say_layer"), SetVariable("current_dpad_menu", "quick"), SetVariable("v_cursor_enabled", False)]
                    key "pad_dpright_press" action [SetFocus("say", "quick_history", "say_layer"), SetVariable("current_dpad_menu", "quick"), SetVariable("v_cursor_enabled", False)]
            focused_on "quick_history" key "pad_dpleft_press" action SetFocus("say", "quick_options", "say_layer")
            focused_on "quick_options" key "pad_dpright_press" action SetFocus("say", "quick_history", "say_layer")


        hbox:
            xalign 0.5
            yalign 0.5
            xoffset 580
            yoffset 150
            $ tooltip = GetTooltip()
            if tooltip:
                frame:
                    background Frame("gui/framewashi_green_quickmenu.png")
                    padding 30, 20, 30, 20
                    text "{color=FFFFFF}{size=*0.7}[tooltip!t]{/size}{/color}"
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.5
            xoffset 450
            yoffset 230

            imagebutton:
                id "quick_history"
                idle "gui/button/quickmenu_history_idle.png"
                hover "quickmenu_history_hover"
                hover_sound renpy.random.choice(dialogue_hover_random)
                activate_sound renpy.random.choice(turnpage)
                action ShowMenu('history')
                tooltip _("HISTORY")
                keyboard_focus True

            imagebutton:
                id "quick_auto"
                idle "gui/button/quickmenu_auto_idle.png"
                hover "quickmenu_auto_hover"
                selected_idle "gui/button/quickmenu_auto_idle_playing.png"
                selected_hover "quickmenu_auto_hover_playing"
                hover_sound renpy.random.choice(dialogue_hover_random)
                activate_sound renpy.random.choice(turnpage)
                action Preference("auto-forward", "toggle")
                tooltip _("AUTOPLAY")
                keyboard_focus True

            imagebutton:
                id "quick_skip"
                idle "gui/button/quickmenu_skip_idle.png"
                hover "quickmenu_skip_hover"
                insensitive "gui/button/quickmenu_skip_disabled.png"
                hover_sound renpy.random.choice(dialogue_hover_random)
                activate_sound renpy.random.choice(turnpage)
                action CustomSkip(confirm=True)
                #alternate Skip(fast=True, confirm=True)
                tooltip _("SKIP")
                #keyboard_focus True
            imagebutton:
                id "quick_save"
                idle "gui/button/quickmenu_save_idle.png"
                hover "quickmenu_save_hover"
                hover_sound renpy.random.choice(dialogue_hover_random)
                activate_sound renpy.random.choice(turnpage)
                action ShowMenu('save')
                tooltip _("SAVE")
                keyboard_focus True
            imagebutton:
                id "quick_options"
                idle "gui/button/quickmenu_options_idle.png"
                hover "quickmenu_options_hover"
                hover_sound renpy.random.choice(dialogue_hover_random)
                activate_sound renpy.random.choice(turnpage)
                action ShowMenu('preferences')
                tooltip _("OPTIONS")
                keyboard_focus True


# confirm they want to skip
screen confirmskip():
    add "gui/overlay/game_mainvisual.png"
    # Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Start skipping text?\n(You can stop skipping by pressing any button.)"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150
                textbutton _("Yes") action CustomSkip()
                textbutton _("No") action Return()

    ## Right-click and escape answer "no".
    key "game_menu" action Return()


default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

## ADDED FOR DEMO ##
## Made it so that the history button is the default focus for pause/regular navigation
## And the start button is the default focus for the main menu
## This to avoid weird controller bugs
screen navigation():
    use hide_mouse_screen
    zorder 1

    ## Show this only if we're not in the tutorial.
    showif renpy.get_screen("navigation_tutorial") == None:
        vbox:
            style_prefix "navigation"


            #change navi depending on if youre on the main menu or a normal menu
            if renpy.get_screen("main_menu"):
                yalign 0.5
                yoffset 170
                xcenter 930
                #xoffset 880
                #yoffset 30

            else:
                xpos gui.navigation_xpos + 200
                yalign 0.5
                xanchor 0.5
                yoffset 65
                xmaximum 250

            spacing gui.navigation_spacing-5

            #change which options appear depending on main menu or normal menu
            if renpy.get_screen("main_menu"):

                textbutton _("START") action Start() text_style "mainmenubuttons":
                    default_focus True

                textbutton _("LOAD") action ShowMenu("load") text_style "mainmenubuttons"

                textbutton _("TUTORIAL") action [ShowMenu("game_tutorial"), SetVariable("persistent.tutocheck", True)] text_style "mainmenubuttons"

                textbutton _("OPTIONS") action ShowMenu("preferences") text_style "mainmenubuttons"

                # if not renpy.variant("console"):
                #     textbutton _("ACCESSIBILITY") action Show("_accessibility") text_style "mainmenubuttons"

                #textbutton "image tools for baby adrienne" action ShowMenu("image_tools")

                if renpy.variant("pc"):

                    ## The quit button is banned on iOS and unnecessary on Android and
                    ## Web.
                    textbutton _("QUIT") action Quit(confirm=not main_menu) text_style "mainmenubuttons"

            else:

                if main_menu:
                    textbutton _("START") action Start()

                if not main_menu:
                    textbutton _("HISTORY") action ShowMenu("history") id "history_mb":
                        if renpy.get_screen("history"):
                            default_focus True

                    textbutton _("SAVE") action ShowMenu("save") id "save_mb"

                textbutton _("LOAD") action ShowMenu("load") id "load_mb"

                textbutton _("OPTIONS") action ShowMenu("preferences") id "options_mb"

                textbutton _("TUTORIAL") action ShowMenu("game_tutorial") id "tutorial_mb"

                textbutton _("ABOUT") action ShowMenu("about") id "about_mb"

                text ""

                textbutton _("BACK TO{p}GAME") action [Return()] id "back_game_mb"

                if not main_menu:

                    textbutton _("BACK TO{p}MAIN MENU") action MainMenu() id "back_mm_mb"

                if renpy.variant("pc"):

                    ## The quit button is banned on iOS and unnecessary on Android and
                    ## Web.
                    textbutton _("QUIT") action Quit(confirm=not main_menu) id "quit_mb"

        if renpy.get_screen("main_menu"):
            vbox:
                style_prefix "version"
                yalign 0.948
                xalign 0.88

                text "VERSION [config.version]"

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style sigmar:
    font "SigmarOne.otf"
translate japanese style sigmar:
    font "和風ぽっぷ.ttf"

style mainmenubuttons:
    size 45
    color "#FFD632"
    hover_color "#E6E4DE"
    xalign 0.5
    outlines [ (absolute(5), "#1B2D07", absolute(0), absolute(0)) ]
    line_leading -25
    font "SigmarOne.otf"

translate japanese style mainmenubuttons:
    font "和風ぽっぷ.ttf"

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound renpy.random.choice(menu_hover)
    activate_sound renpy.random.choice(turnpage)

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    text_align 0.5 layout 'nobreak'
    selected_hover_color gui.selected_hover_color
translate japanese style navigation_button_text:
    first_indent 0

style version_text:
    size 17
    color "#3D6944"

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

init python:
    import pygame
    import math


    class TrackCursor(renpy.Displayable):

        def __init__(self, child, paramod, **kwargs):

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0
            self.actual_x = 0
            self.actual_y = 0

            self.paramod = paramod
            self.last_st = 0



        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)
            minimum_speed = 0.5
            maximum_speed = 3
            speed = 1 + minimum_speed
            mouse_distance_x = min(maximum_speed, max(minimum_speed, (self.x - self.actual_x)))
            mouse_distance_y = (self.y - self.actual_y)
            if self.x is not None:
                st_change = st - self.last_st

                self.last_st = st
                self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x) * speed * (st_change )) * self.paramod)
                self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y) * speed * (st_change)) * self.paramod)


                if mouse_distance_y <= minimum_speed:
                    mouse_distance_y = minimum_speed
                elif mouse_distance_y >= maximum_speed:
                    mouse_distance_y = maximum_speed

                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.actual_x, self.actual_y))



            renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            mousefocus = pygame.mouse.get_focused()
            if hover:

                if (x != self.x) or (y != self.y) or click:
                    self.x = -x /self.paramod
                    self.y = -y /self.paramod

default persistent.tutocheck = False

## ADDED FOR DEMO ##
## Used "on show" action so that the navigation screen was registered properly,
## and it would show in the options menu.
screen main_menu():
    ## This ensures that any other menu screen is replaced.
    on "show" action Show("navigation")
    tag menu

    default x_dir = 0
    default y_dir = 0

    key "pad_rightx_pos" action SetScreenVariable('x_dir',(persistent.gamepad_nav_speed+120))
    key "pad_rightx_neg" action SetScreenVariable('x_dir',-(persistent.gamepad_nav_speed+120))
    key "pad_righty_pos" action SetScreenVariable('y_dir',(persistent.gamepad_nav_speed+120))
    key "pad_righty_neg" action SetScreenVariable('y_dir',-(persistent.gamepad_nav_speed+120))
    key "pad_rightx_zero" action SetScreenVariable('x_dir',0)
    key "pad_righty_zero" action SetScreenVariable('y_dir',0)

    add "gui/thoughtbubble.png":
        id "thought"
    # add TrackCursor("gui/title/main_title_5.png", 30)
    # add TrackCursor("gui/title/main_title_4.png", 26)
    # add TrackCursor("gui/title/main_title_3.png", 15)
    # add TrackCursor("gui/title/main_title_2.png", 20)


    add "gui/title/main_title_1.png"
    default lerp_right_stick = LerpRightStick(20.0)
    add lerp_right_stick

    if not persistent.tutocheck:
        imagebutton:
            xpos 1370
            ypos 670
            idle "tutocheck"
            hover At("tutocheck", outline_transform(5, "#ffffff"))
            action [ShowMenu("game_tutorial"), SetVariable("persistent.tutocheck", True)]

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"
    if x_dir or y_dir:
        timer 0.02 repeat True action [SetVariable("right_stick_x", MoveRightStick(x_dir, y_dir)[0]), SetVariable("right_stick_y", MoveRightStick(x_dir, y_dir)[1])]


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

## ADDED FOR DEMO ##
## Restored some edits I had made to this before, mainly to preserve page transitions + the PaC state.
## As a note, don't set IsPaCDisabled to False, instead, set it back to what it was before by having the line "default IsPaCDisabledStored = IsPaCDisabled" at the top.
## This way your PaC won't get weirdly overriden.

## Also, fixed the navigation screen not showing properly.

screen game_menu(title="History", scroll=None, yinitial=0.0, no_transition=False):
    default IsPaCDisabledStored = IsPaCDisabled

    on "show" action [If(not no_transition, Show("screen_transition_nextpage_noreturn", _zorder = 100)), SetVariable("is_in_menu", True), Show("navigation"), Function(hide_mouse_based_on_state), SetVariable("current_dpad_menu", None)]
    on "replace" action [If(renpy.get_screen("navigation") == None, true=Show("navigation")), If(not no_transition, Show("screen_transition_nextpage_noreturn", _zorder = 100)), If(not no_transition, SetFocusGameMenuButton(title))]
    on "hide" action [SetVariable("is_in_menu", False)]

    style_prefix "game_menu"

    if title == "History": #add these 2 lines
        add "gui/overlay/game_menu_history.png"
        add "gui/superoverlay/history.png"
    elif title == "Save": #add these 2 lines
        add gui.game_menu_background_side
        add "gui/superoverlay/save.png"
    elif title == "Load": #add these 2 lines
        add gui.game_menu_background_side
        add "gui/superoverlay/load.png"
    elif title == "Options": #add these 2 lines
        add gui.game_menu_background_side
        add "gui/superoverlay/options.png"
    elif title == "About": #add these 2 lines
        add gui.game_menu_background_side
        add "gui/superoverlay/about.png"
    else:
        add gui.game_menu_background_side
    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    side 'c r':
                        viewport:
                            id "history_vp"
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True
                            vbox:
                                transclude

                        controller_vbar value YScrollValue("history_vp") style 'vscrollbar' keyboard_focus True

                elif scroll == "vpgrid":

                    vpgrid:
                        id "history_vp"
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                elif scroll == "controller":
                    side 'c r':
                        # MAURI SAYS: If you want to make it so that focusing on the viewport (not the bar) scrolls it,
                        # you can use 'controller_viewport' instead of 'viewport' and uncomment the stuff I wrote.
                        # This lets you smoothly scroll, however,
                        controller_viewport:
                            focus_scroll True
                            absorb_events False
                            yinitial yinitial
                            id "history_vp"
                            mousewheel True draggable True pagekeys True
                            which_stick "both"
                            scrollbars 'vertical'
                            trap_focus('right')

                            vbox:
                                transclude

                        controller_vbar:
                            id "history_bar"
                            value YScrollValueSelected("history_vp", "history_bar")
                            keyboard_focus False
                else:
                    transclude

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
            action [SetVariable("IsPaCDisabled", IsPaCDisabledStored), Show("screen_transition_previouspage")]

    # gamepad return
        if pad_config.is_using_controller():
            image "bbutton"
            key "pad_b_press" action [SetVariable("IsPaCDisabled", IsPaCDisabledStored), Show("screen_transition_previouspage")]
    ##################

    label title
    key ["mouseup_3", "pad_start_press", "K_ESCAPE"] activate_sound renpy.random.choice(turnpage) action [SetVariable("IsPaCDisabled", IsPaCDisabledStored), Show("screen_transition_previouspage")]

    if not no_transition:
        image "transition_nextpage"


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 220

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    right_margin 30
    top_margin 30
    bottom_margin 90

style game_menu_viewport:
    xsize 1250

style game_menu_vscrollbar:
    unscrollable gui.unscrollable


style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 175
    yoffset 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
    font "SigmarOne.otf"

translate japanese style game_menu_label_text:
    font "和風ぽっぷ.ttf"

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Game Menu NO NAVI screen ############################################################
##
## Game Menu screen, but without the navigation
screen game_menu_no_navi(title, scroll=None, yinitial=0.0):
    default IsPaCDisabledStored = IsPaCDisabled

    style_prefix "game_menu"

    add gui.game_menu_background

    if title == "CASE": #add these 2 lines
        add "gui/superoverlay/case.png"
    elif title == "Memories" and CurrentDay == VisibleDayPageMemory:
        pass
    elif title == "Memories" and VisibleDayPageMemory == 0:
        add "gui/superoverlay/memories_0.png"
#GLOSSARY is in its own file

    frame:
        style "game_menu_outer_frame_no_navi"

        hbox:

            frame:
                style "game_menu_content_frame_no_navi"
                transclude

    #tab 4


    label title


style game_menu_outer_frame_no_navi is empty
style game_menu_content_frame_no_navi is empty
style game_menu_viewport_no_navi is gui_viewport
style game_menu_side_no_navi is gui_side

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_no_navi_outer_frame:
        background "gui/overlay/game_menu.png"

style game_menu_no_navi_noline_outer_frame:
        background "gui/overlay/game_menu_noline.png"

style game_menu_content_frame_no_navi:
    xmaximum 1550
    ymaximum 700
    xoffset 150
    yoffset 225

style game_menu_viewport_no_navi:
    xsize 1380
    xalign 0.5

style game_menu_label:
    xpos 175
    yoffset 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button_no_navi:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

## Game Menu NO NAVI AND NO RETURNscreen ############################################################
##
## Game Menu screen, but without the navigation

screen game_menu_no_navi_no_return(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"
    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame_no_navi"

        hbox:

            frame:
                style "game_menu_content_frame_no_navi"
                transclude

    label title


style game_menu_outer_frame_no_navi is empty
style game_menu_content_frame_no_navi is empty
style game_menu_viewport_no_navi is gui_viewport
style game_menu_side_no_navi is gui_side

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_no_navi_outer_frame:
        background "gui/overlay/game_menu.png"

style game_menu_no_navi_noline_outer_frame:
        background "gui/overlay/game_menu_noline.png"

style game_menu_content_frame_no_navi:
    xmaximum 1550
    ymaximum 700
    xoffset 150
    yoffset 225

style game_menu_viewport_no_navi:
    xsize 1380
    xalign 0.5

style game_menu_label:
    xpos 175
    yoffset 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button_no_navi:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"
        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("PAGE {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:
            xoffset -100
            yoffset -70

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                yoffset -30
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5
                yoffset 15

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:

                        if renpy.get_screen("load") and not FileLoadable(slot):
                            action NullAction()
                        else:
                            action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5 yoffset 35

                        text FileTime(slot, format=_("{#file_time}%m/%d/%Y - %H:%M"), empty=_("Day ??? • ??:??")):
                            style "slot_time_text"
                            yoffset 35

                        text FileSaveName(slot):
                            style "slot_name_text"
                            yoffset 35

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                yoffset 130

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                            yoffset -10
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5

    if pad_config.is_using_controller():
        image "BookMenu/gamepadbuttons/xbox/xbox_lbrb_save.png"

        key "pad_leftshoulder_press" action FilePagePrevious()

        key "pad_rightshoulder_press" action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color
    selected_hover_color gui.selected_hover_color

style page_button:
    properties gui.button_properties("page_button")
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(menu_confirm)

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(menu_confirm)

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

image xbox_lb = Crop((324, 941, 108, 70), "BookMenu/gamepadbuttons/xbox/xbox_lb.png")
image xbox_rb = Crop((1406, 940, 110, 77), "BookMenu/gamepadbuttons/xbox/xbox_rb.png")
screen preferences_header(no_transition=False):

    use game_menu(_("Options"), scroll="none", no_transition=no_transition):
        vbox:
            xsize 1270
            null height 170
            transclude

    hbox:
        style_prefix 'pref_header'
        if pad_config.is_using_controller():
            add "xbox_lb"
        else:
            null width 108
        textbutton _("GAME") action ShowMenu("preferences", no_transition=True)
        textbutton _("VIDEO") action ShowMenu("preferences_video", no_transition=True)
        textbutton _("AUDIO") action ShowMenu("preferences_audio", no_transition=True)
        textbutton _("CONTROLS") action ShowMenu("preferences_help", no_transition=True)
        textbutton _("SYSTEM") action ShowMenu("preferences_system", no_transition=True)
        if pad_config.is_using_controller():
            add "xbox_rb"
        else:
            null width 110

    if renpy.get_screen("preferences"):
        key "pad_leftshoulder_press" action ShowMenu("preferences_system", no_transition=True)
        key "pad_rightshoulder_press" action ShowMenu("preferences_video", no_transition=True)
    elif renpy.get_screen("preferences_video"):
        key "pad_leftshoulder_press" action ShowMenu("preferences", no_transition=True)
        key "pad_rightshoulder_press" action ShowMenu("preferences_audio", no_transition=True)
    elif renpy.get_screen("preferences_audio"):
        key "pad_leftshoulder_press" action ShowMenu("preferences_video", no_transition=True)
        key "pad_rightshoulder_press" action ShowMenu("preferences_help", no_transition=True)
    elif renpy.get_screen("preferences_help"):
        key "pad_leftshoulder_press" action ShowMenu("preferences_audio", no_transition=True)
        key "pad_rightshoulder_press" action ShowMenu("preferences_system", no_transition=True)
    elif renpy.get_screen("preferences_system"):
        key "pad_leftshoulder_press" action ShowMenu("preferences_help", no_transition=True)
        key "pad_rightshoulder_press" action ShowMenu("preferences", no_transition=True)


style pref_header_hbox:
    xcenter 1920//2+100
    ypos 285
    spacing 2
style pref_header_button:
    ## Replace these + the size with the image you need
    background "gui/framewashi_green_quickmenu_select.png"
    hover_background "gui/framewashi_green_quickmenu_hover.png"
    selected_background "gui/framewashi_green_quickmenu_selected.png"
    xysize (215, 96)
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(menu_confirm)

style pref_header_button_text:
    align (0.5, 0.5)
    color "#FFF"
    selected_color "#FFF"
    idle_color "#BFBFBF"

screen preferences(no_transition=False):
    tag menu
    style_prefix "preferences"

    use preferences_header(no_transition=no_transition):
        hbox:
            xalign 0.5
            yoffset -10
            text _("Adjust your gameplay experience.")

        hbox:
            xalign 0.5 spacing 50
            vbox:
                xsize 500
                style_prefix "slider"

                label _("Text Speed")

                bar value Preference("text speed")

                label _("Autoplay Speed")

                bar value Preference("auto-forward time") bar_invert True
                null height 10
                text _("{size=*0.7}{color=757575}Adjusts the time auto-play takes to go to the next line.{/color}{/size}")

                # null height gui.pref_spacing

                # textbutton _("Punctuation Pauses"):
                #     action ToggleVariable("persistent.autopunctuation", true_value=True, false_value=False)
                #     style "mute_all_button"

            vbox:
                xsize 500
                style_prefix "check"
                label _("Skip")
                textbutton _("Skip Unseen Text") action Preference("skip", "toggle") default_focus True
                null height 10
                text _("{size=*0.7}{color=757575}If checked, pressing \"SKIP\" will skip all dialogue, including unseen dialogue.{/color}{/size}")

                null height 10

                textbutton _("Skip Pauses") action InvertSelected(ToggleField(persistent, "hard_pauses"))
                null height 10
                text _("{size=*0.7}{color=757575}If checked, Cool Dramatic Pauses(tm) can be skipped.{/color}{/size}")


                #textbutton _("After Choices") action Preference("after choices", "toggle")
                #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))





screen preferences_video(no_transition=False):
    tag menu
    style_prefix "preferences"

    use preferences_header(no_transition=no_transition):
        hbox:
            xalign 0.5
            yoffset -10
            text _("Adjust the display settings.")
        hbox:
            xalign 0.5
            if renpy.variant("pc") or renpy.variant("web"):

                vbox:
                    xsize 500
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window") default_focus True
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            vbox:
                xsize 500
                vbox:
                    style_prefix "check"
                    label _("Camera")
                    textbutton _("Mouse Parallax") action ToggleVariable("persistent.parallaxOn", true_value=True, false_value=False)
                    null height 10
                    text _("{size=*0.7}{color=757575}If checked, moving the mouse/stick moves the camera.{/color}{/size}")

screen preferences_audio(no_transition=False):
    tag menu
    style_prefix "preferences"

    use preferences_header(no_transition=no_transition):
        hbox:
            xalign 0.5
            yoffset -10
            text _("Adjust the volume.")
        hbox:
            xalign 0.5 spacing 100
            vbox:
                xsize 500
                style_prefix 'slider'
                if config.has_music:
                    label _("Music Volume")

                    hbox:
                        bar value Preference("music volume") default_focus True

                    label _("Background Volume")

                    hbox:
                        bar value Preference("bg volume")


            vbox:
                xsize 500
                style_prefix 'slider'

                if config.has_sound:

                    label _("Sound Effects Volume")

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

                label _("\"Dialogue\" Volume")

                hbox:
                    bar value Preference("ctc volume")

                    if config.sample_sound:
                        textbutton _("Test") action Play("ctc", config.sample_sound)

                null height gui.pref_spacing
        vbox:
            xalign 0.5
            yoffset 30
            textbutton _("Mute All"):
                action Preference("all mute", "toggle")
                style "mute_all_button"



screen preferences_help(no_transition=False):
    tag menu
    style_prefix "preferences"

    default device = "keyboard" if not pad_config.is_using_controller() else "gamepad"

    use preferences_header(no_transition=no_transition):

        style_prefix "help"
        hbox:
            xalign 0.5
            yoffset -10
            if pad_config.is_using_controller():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad"):
                    sensitive device != 'gamepad'
                textbutton _("Calibrate Gamepad") action Hide("game_tutorial"), GamepadCalibrate()
            else:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

        hbox:
            xalign 0.5 spacing 30
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    vbox:
        xsize 500
        hbox:
            label _("Enter")
            text _("Confirm, Advance dialogue.")

        hbox:
            label _("Space")
            text _("Advance dialogue.")

        hbox:
            label _("Escape")
            text _("Open the Game menu.")

        hbox:
            label _("Ctrl/Tab")
            text _("Skip dialogue.")

    vbox:
        xsize 500
        hbox:
            label _("H")
            text _("Hide the dialogue box.")

        hbox:
            label "S"
            text _("Take a screenshot.")

        hbox:
            label "V"
            text _("Toggle assistive self-voicing.")

        hbox:
            label "Shift+A"
            text _("Open the accessibility menu.")





screen mouse_help():
    style_prefix "helpbig"
    vbox:
        xsize 500
        hbox:
            label _("Left Click")
            text _("Confirm, Advance dialogue.")

        hbox:
            label _("Middle Click")
            text _("Hide the dialogue box.")

        hbox:
            label _("Right Click")
            text _("Open the History menu, Cancel.")



screen gamepad_help():

    vbox:
        xsize 500
        hbox:
            label _("A")
            text _("Confirm, Advance dialogue.")

        hbox:
            label _("B")
            text _("Cancel, Return.")

        hbox:
            label _("Analog Sticks")
            text _("Move the cursor or camera.")

        hbox:
            label _("Up/Down")
            text _("Toggle through Book Menu Options.")

    vbox:
        xsize 500
        hbox:
            label _("Left/Right")
            text _("Toggle through Dialogue Menu Options.")

        hbox:
            label _("Right Trigger")
            text _("Toggle skipping dialogue.")

        hbox:
            label _("Share")
            text _("Take a screenshot.")

        hbox:
            label _("Start")
            text _("Open the History menu.")


screen preferences_system(no_transition=False):
    tag menu
    style_prefix "preferences"

    use preferences_header(no_transition=no_transition):
        hbox:
            xalign 0.5
            yoffset -10
            text _("Adjust the system settings.")

        hbox:
            xalign 0.5 spacing 100
            vbox:
                xsize 500
                style_prefix "radio"
                label _("Language")
                textbutton _("English"):
                    default_focus 2
                    action Language(None)
                textbutton _("{font=natumemozi.ttf}日本語{/font}"):
                    default_focus 1
                    action Language("japanese")
                textbutton _("Français"):
                    action Language("french")
                textbutton _("Italiano"):
                    action Language("italian")
                
            vbox:
                xsize 500
                label _("More")
                if not renpy.variant("console"):
                    textbutton _("Accessibility Menu") action Show("_accessibility")
                    null height 10
                    text _("{size=*0.7}{color=757575}Includes options for self-voicing, font override, high contrast text...{/color}{/size}")

        hbox:
            xalign 0.5
            textbutton _("Credits") action Show("credits_menu")



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style help_button:
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(menu_confirm)


style pref_vbox:
    xsize 380

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(turnpage)

style preferences_button:
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(turnpage)

style radio_button_text:
    properties gui.button_text_properties("radio_button")


style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(menu_confirm)

style check_button_text:
    properties gui.button_text_properties("check_button")
    selected_hover_color gui.selected_hover_color

style slider_slider:
    xsize 475
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(menu_confirm)

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
    hover_sound renpy.random.choice(menu_hover_paper_random)
    activate_sound renpy.random.choice(menu_confirm)

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 500


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu

    on "show" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), SetVariable("IsPaCDisabledStored", IsPaCDisabled), SetVariable("IsPaCDisabled", True)]
    on "replaced" action [Show("screen_transition_nextpage_noreturn", _zorder = 100)]
    on "hide" action SetVariable("IsPaCDisabled", IsPaCDisabledStored)

    ## Avoid predicting this screen, as it can be very large.
    predict False

    #
    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "controller"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:
            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True
                    # xoffset 100


                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "histcolor" in h.who_args:
                            text_color h.who_args["histcolor"]
                        elif "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("...")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    # xoffset -170
    xsize 1250
    # xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    xoffset -0

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.



    # hbox:
    #     label _("Y/Top Button")
    #     text _("Hides the user interface.")




style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 120
    right_padding 30

style helpbig_label:
    xsize 120
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

### ADDED FOR DEMO ###
### Made yes the default focus for this screen.
screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action default_focus 2000 id 'confirm'
                textbutton _("No") action no_action id 'cancel'

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

    focused_on "confirm" key "focus_left" action NullAction()
    focused_on "cancel" key "focus_right" action NullAction()
    key ["focus_up", "focus_down"] action NullAction()



style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    image "skip":
        xalign 0.85
        yalign 0.25
    # frame:

    #     hbox:
    #         spacing 9

    #         #text _("Skipping")

    #         text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat



## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        if not renpy.get_screen("confirm"):
            key "pad_dpleft_press" action SetFocus("quick_menu", "back")
            focused_on "back" key "pad_dpright_press" action SetFocus("quick_menu", "skip")
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") id "back" action Rollback()
            textbutton _("Skip") id "skip" action CustomSkip(confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
