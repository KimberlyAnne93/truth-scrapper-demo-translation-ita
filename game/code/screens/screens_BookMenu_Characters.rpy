## CHARACTERS ##########################################################
## main and secondary characters
#####################################################################
default character_name = "Sosotte"
default character_title_text = "[You, me, her, us. The person in the mirror.]"
default GotNewCharacter = False

default DayxNewCharacters = False

default DayxAmourVain = False


default characters_update_amour = " •"

default characters_update_kale = " •"
default characters_update_julienne = " •"
default characters_update_iris = " •"


## MAIN MENU ##############################################
## setting up menu
###########################################################
screen book_characters(scroll=None, yinitial=0.0):
    #default IsPaCDisabledStored = IsPaCDisabled

    on "show" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), Show("navigation_characters", _zorder=0), SetVariable("IsPaCDisabledStored", IsPaCDisabled), SetVariable("IsPaCDisabled", True)]
    on "replaced" action [Show("screen_transition_nextpage_noreturn", _zorder = 100)]
    on "hide" action [Hide("navigation_characters"), SetVariable("IsPaCDisabled", IsPaCDisabledStored)]


    use hide_mouse_screen
    modal True
    style_prefix "book_characters"

    frame:
        style "book_characters_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                else:

                    transclude
    label "\n[character_name!t]{size=*0.5}{color=#707070}\n [character_title_text!t]{/color}{/size}"


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
            action [ShowMenu("screen_transition_previouspage")]

    # right click return
        key "mouseup_3" activate_sound renpy.random.choice(turnpage) action [ShowMenu("screen_transition_previouspage")]

    # gamepad return
        if pad_config.is_using_controller():
            image "bbutton"
            key "pad_b_press" activate_sound renpy.random.choice(turnpage) action [ShowMenu("screen_transition_previouspage")]
    ##################



style book_characters_label is game_menu_label
style book_characters_label_text is game_menu_label_text
style book_characters_text is gui_text

style book_characters_outer_frame:
    bottom_padding 45
    top_padding 220
    background "gui/overlay/game_menu_side_big.png"

style menu_character_label_text:
    size gui.label_text_size
    line_spacing 0

style book_characters_label:
    xpos 425
    yoffset 50
    ysize 180


### ADDED FOR DEMO ###
### Added bumper button focus actions and made Sosotte be the default focus

## LIST ###################################################
## list of characters on the side
###########################################################
init python:
    def get_glossary_character_list():
        """
        A function which returns a list of the screens to cycle through
        in the character menu.
        """
        ret = [ ]
        if TurnOffReturn == False:
            ret.append("menu_character_sosotte")
            ret.append("menu_character_amour")
            ret.append("menu_character_betz")
            if DayxNewCharacters:
                ret.append("menu_character_kale")
                ret.append("menu_character_julienne")
                ret.append("menu_character_iris")
        return ret


screen navigation_characters():

    default character_list = get_glossary_character_list()

    if TurnOffReturn == False:
        if pad_config.is_using_controller():
            image "BookMenu/gamepadbuttons/xbox/xbox_lbrb_chara.png"
        if character_list:
            key ["pad_leftshoulder_press"] action ShowNextScreen(character_list, -1, "navigation_characters", "characters_navi_id")
            key ["pad_rightshoulder_press"] action ShowNextScreen(character_list, 1, "navigation_characters", "characters_navi_id")


    controller_viewport:
        style_prefix "navigation_characters"
        yalign 0.63
        xpos 160
        xysize (220, 780)

        id "characters_navi_id"

        vscroll_style "center"
        draggable renpy.variant("touch") mousewheel True arrowkeys True
        scrollbars "vertical"
        #has vbox

        vbox:
            xpos gui.navigation_xpos
            spacing gui.navigation_spacing

            if TurnOffReturn == False:
                textbutton _("Sosotte (You)"):
                    default_focus True id "menu_character_sosotte"
                    action NoReshowMenu("menu_character_sosotte")

                    if character_title_text != "[You, Me, Her, Us. The Person In The Mirror.]":
                        hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Amour{color=#D0821B}[characters_update_amour]{/color}"):
                    action NoReshowMenu("menu_character_amour")
                    if character_title_text != "[Red-Hair, Dull, Helpful.]":
                        hover_sound renpy.random.choice(menu_hover)
                    id "menu_character_amour"
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Betz{color=#D0821B}{/color}"):
                    action NoReshowMenu("menu_character_betz")
                    id "menu_character_betz"
                    if character_title_text != "[Knight In Shining Armor.]":
                        hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)

                text ""

                if DayxNewCharacters:
                    textbutton _("Kale{color=#D0821B}[characters_update_kale]{/color}"):
                        action NoReshowMenu("menu_character_kale")
                        id "menu_character_kale"
                        if character_title_text != "[Betz Brigade Member.]":
                            hover_sound renpy.random.choice(menu_hover)
                        activate_sound renpy.random.choice(turnpage)

                    textbutton _("Julienne{color=#D0821B}[characters_update_julienne]{/color}"):
                        action NoReshowMenu("menu_character_julienne")
                        id "menu_character_julienne"
                        if character_title_text != "[Betz Brigade Member.]":
                            hover_sound renpy.random.choice(menu_hover)
                        activate_sound renpy.random.choice(turnpage)

                    textbutton _("Iris{color=#D0821B}[characters_update_iris]{/color}"):
                        action NoReshowMenu("menu_character_iris")
                        id "menu_character_iris"
                        if character_title_text != "[Betz Brigade Member.]":
                            hover_sound renpy.random.choice(menu_hover)
                        activate_sound renpy.random.choice(turnpage)




    vbar value YScrollValue("characters_navi_id") style 'vscrollbar' keyboard_focus False yalign 0.63 xpos 130 ysize 780

style navigation_characters_button is gui_button
style navigation_characters_button_text is gui_button_text

style navigation_characters_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_characters_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    #text_align 0.5
    selected_color gui.selected_color
    selected_hover_color gui.selected_hover_color



## CHARACTERS ##############################################
## each character has their own screen
###########################################################
style menu_character_vbox:
    yoffset 70
    xsize 820

screen menu_character_sosotte():

    tag book_characters
    use book_characters(_("You")):
        style_prefix "menu_character"

        $ character_name = _("Sosotte")
        image "charactermenu sosotte":
            xpos -430
            ypos -250

        vbox:
            text _("{=sigmar}{color=5B8C63}TRUTH SCRAPPER{/color}{/=sigmar} (she/her/hers)\n")

            text _("{=sigmar}{color=5B8C63}WHAT'S HAPPENING TO ME?{/color}{/=sigmar}")

            text _("• You have a condition which makes you forget everything, every day.")
            text _("• You will remember whatever you have written down in this Scrap Book by touching it.")
            text _("• There's nothing you can do to fix this. Make the best of it.")

            text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

            text _("• Many people consider you adorable. You can use that.")

    on "replace" action [SetVariable("character_name", _("Sosotte")), SetVariable("character_title_text", _("[You, Me, Her, Us. The Person In The Mirror.]")), SetVariable("characters_update_sosotte", "")]




screen menu_character_amour():

    tag book_characters
    use book_characters(_("Amour")):

        style_prefix "menu_character"

        image "charactermenu amour":
            xpos -430
            ypos -270

        vbox:

            text _("{=sigmar}{color=5B8C63}PATH DWELLER / OUR GUIDE{/color}{/=sigmar} (she/he)")


            text _("• Met on Day X-1. Agreed to guide us.\n")

            text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

            text _("• Can ask her all the questions we want. Not likely to know much, though.")
            if DayxAmourVain:
                text _("• Vain. Compliment his face if you need something.")


    on "replace" action [SetVariable("character_name", _("Amour")), SetVariable("character_title_text", _("[Red-Haired, Dull, Helpful.]")), SetVariable("characters_update_amour", "")]


screen menu_character_betz():

    tag book_characters
    use book_characters(_("Betz")):

        style_prefix "menu_character"

        image "charactermenu betz":
            xpos -430
            ypos -270

        vbox:
            yoffset 150

        vbox:
            text _("{=sigmar}{color=5B8C63}PATH DWELLER / OUR GUIDE{/color}{/=sigmar} (he/they)")

            text _("• Met on Day X-1. Signed up as our Guide.\n")

            text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

            text _("• Calls me \"mademoiselle\".")


    on "replace" action [SetVariable("character_name", _("Betz")), SetVariable("character_title_text", _("[Knight In Shining Armor.]")), SetVariable("characters_update_betz", "")]


screen menu_character_kale():

    tag book_characters
    use book_characters(_("KALE")):

        style_prefix "menu_character"

        image "charactermenu kale":
            xpos -430
            ypos -270

        vbox:
            text _("{=sigmar}{color=5B8C63}MINE DWELLER{/color}{/=sigmar} (Dunno.)")

            text _("• Ambushed me in Cul-De-Puits, Day X-1.\n")

            text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

            text _("• Has a MASSIVE puppy crush on Betz.")
            text _("• Doesn't like me. STEER CLEAR.")

    on "replace" action [SetVariable("character_name", _("KALE")), SetVariable("character_title_text", _("[Betz Brigade Member.]")), SetVariable("characters_update_kale", "")]


screen menu_character_julienne():

    tag book_characters
    use book_characters(_("JULIENNE")):

        style_prefix "menu_character"

        image "charactermenu julienne":
            xpos -430
            ypos -270

        vbox:
            text _("{=sigmar}{color=5B8C63}MINE DWELLER{/color}{/=sigmar} (No idea.)")

            text _("• Ambushed me in Cul-De-Puits, Day X-1.\n")

            text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

            text _("• Wants to feed Betz soup.")
            text _("• Doesn't like me much.")

    on "replace" action [SetVariable("character_name", _("JULIENNE")), SetVariable("character_title_text", _("[Betz Brigade Member.]")), SetVariable("characters_update_julienne", "")]


screen menu_character_iris():

    tag book_characters
    use book_characters(_("IRIS")):

        style_prefix "menu_character"

        image "charactermenu iris":
            xpos -430
            ypos -270

        vbox:
            text _("{=sigmar}{color=5B8C63}PATH DWELLER{/color}{/=sigmar} (Wasn't paying attention.)")

            text _("• Ambushed me in Cul-De-Puits, Day X-1.\n")

            text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

            text _("• Seems indifferent towards Betz, honestly.")
            text _("• Blunt, but it's fine. Would recommend getting coffee with.")

    on "replace" action [SetVariable("character_name", _("IRIS")), SetVariable("character_title_text", _("[Betz Brigade Member.]")), SetVariable("characters_update_iris", "")]