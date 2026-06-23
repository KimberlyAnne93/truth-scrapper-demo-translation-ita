## GLOSSARY ##########################################################
## we're doing it.
#####################################################################
default glossary_name = "name"
default glossary_title_text = ""
default GotNewGlossary = False
# play sound menu_notif





default glossary_update_truthscrapper = " •"
default glossary_update_pathdweller = " •"
default glossary_update_minedweller = " •"

default glossary_update_thedwell = " •"
default glossary_update_culdepuits = " •"
default glossary_update_greatartisan = " •"
default glossary_update_judgecritic = " •"
default glossary_update_saturation = " •"
default glossary_update_saturateditems = " •"
default glossary_update_caravans = " •"

default glossary_update_keycards = " •"
default glossary_update_iamx = " •"
default glossary_update_pronouns = " •"
default glossary_update_gender = " •"

default glossary_update_hazard = " •"
default glossary_update_thread = " •"
default glossary_update_investigate = " •"

default glossary_update_guide = " •"


### ADDED FOR DEMO ###
### Edited the screen to show the next pager transition properly
## MAIN MENU ##############################################
## setting up menu
###########################################################
screen book_glossary(scroll=None, yinitial=0.0):

    on "show" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), Show("navigation_glossary", _zorder=0), SetVariable("IsPaCDisabledStored", IsPaCDisabled), SetVariable("IsPaCDisabled", True)]
    on "replaced" action [Show("screen_transition_nextpage_noreturn", _zorder = 100)]
    on "hide" action [Hide("navigation_glossary"), SetVariable("IsPaCDisabled", IsPaCDisabledStored)]

    use hide_mouse_screen
    zorder 0
    modal True


    style_prefix "book_glossary"

    frame:
        style "book_glossary_outer_frame"

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

                        #side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    label "\n[glossary_name!t]{size=*0.5}{color=#707070}\n [glossary_title_text!t]{/color}{/size}":
        xoffset 90



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
            image "bbutton":
                xalign 1.0
                yalign 0.10
            key "pad_b_press" activate_sound renpy.random.choice(turnpage) action [ShowMenu("screen_transition_previouspage")]
    ##################

    # page turn at the bottom because it needs to be in front of everything


style book_glossary_label is game_menu_label
style book_glossary_label_text is game_menu_label_text
style book_glossary_text is gui_text

style book_glossary_outer_frame:
    bottom_padding 45
    top_padding 220
    background "gui/overlay/game_menu_side_bigger.png"
    foreground "gui/superoverlay/glossary.png"

style menu_glossary_label_text:
    size gui.label_text_size
    line_spacing 0

style book_glossary_label:
    xpos 425
    yoffset 50
    ysize 180


## ADDED FOR DEMO ##
## Editing this so that scrolling with bumpers works, and so that there's a default focus.

## LIST ###################################################
## list of glossary on the side
###########################################################
init python:

    def get_glossary_item_list():
        """
        A function which returns a list of the screens to cycle through
        in the character menu.
        """
        ret = [ ]
        if TurnOffReturn == False:
            ret.append("menu_glossary_investigate")
            ret.append("menu_glossary_truthscrapper")
            ret.append("menu_glossary_pathdweller")
            ret.append("menu_glossary_minedweller")
            ret.append("menu_glossary_guide")
            ret.append("menu_glossary_thedwell")
            ret.append("menu_glossary_culdepuits")
            ret.append("menu_glossary_hazard")
            ret.append("menu_glossary_greatartisan")
            ret.append("menu_glossary_judgecritic")
            ret.append("menu_glossary_saturation")
            ret.append("menu_glossary_saturateditem")
            ret.append("menu_glossary_caravan")
            ret.append("menu_glossary_thread")
            ret.append("menu_glossary_iamx")
            ret.append("menu_glossary_pronouns")
            ret.append("menu_glossary_gender")
        return ret


screen navigation_glossary(scroll="viewport"):
    zorder 0

# LB AND RB BUTTONS AND GAMEPAD

    default item_list = get_glossary_item_list()
    if TurnOffReturn == False:
        if pad_config.is_using_controller():
            image "BookMenu/gamepadbuttons/xbox/xbox_lbrb_glossary.png"
        if item_list:
            key ["pad_leftshoulder_press"] action ShowNextScreen(item_list, -1, "navigation_glossary", "glossary_navi_id")
            key ["pad_rightshoulder_press"] action ShowNextScreen(item_list, 1, "navigation_glossary", "glossary_navi_id")

    controller_viewport:
        style_prefix "navigation_glossary"
        yalign 0.63
        xpos 170
        xysize (300, 780)

        id "glossary_navi_id"

        vscroll_style "center"
        draggable renpy.variant("touch") mousewheel True arrowkeys True
        scrollbars "vertical"
        trap_focus ("up", "down", "left", "right")

        vbox:
            xpos gui.navigation_xpos
            spacing gui.navigation_spacing
            if TurnOffReturn == False:
# CASE
                text _("• YOU")

                textbutton _("Read Me{color=#D0821B}[glossary_update_investigate]{/color}"):
                    default_focus True
                    id "menu_glossary_investigate"
                    action NoReshowMenu("menu_glossary_investigate")
                    activate_sound renpy.random.choice(turnpage)




# GUILDS
                text _("• GUILDS")

                textbutton _("Truth Scrapper{color=#D0821B}[glossary_update_truthscrapper]{/color}"):
                    action NoReshowMenu("menu_glossary_truthscrapper")
                    id "menu_glossary_truthscrapper"
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Path Dweller{color=#D0821B}[glossary_update_pathdweller]{/color}"):
                    id "menu_glossary_pathdweller"
                    action NoReshowMenu("menu_glossary_pathdweller")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Mine Dweller{color=#D0821B}[glossary_update_minedweller]{/color}"):
                    id "menu_glossary_minedweller"
                    action NoReshowMenu("menu_glossary_minedweller")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Guide{color=#D0821B}[glossary_update_guide]{/color}"):
                    id "menu_glossary_guide"
                    action NoReshowMenu("menu_glossary_guide")
                    activate_sound renpy.random.choice(turnpage)

    # PLACES
                text _("• PLACES")

                textbutton _("The Dwell{color=#D0821B}[glossary_update_thedwell]{/color}"):
                    id "menu_glossary_thedwell"
                    action NoReshowMenu("menu_glossary_thedwell")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Cul-De-Puits{color=#D0821B}[glossary_update_culdepuits]{/color}"):
                    id "menu_glossary_culdepuits"
                    action NoReshowMenu("menu_glossary_culdepuits")
                    activate_sound renpy.random.choice(turnpage)


    # THE DWELL

                text _("• THE DWELL")

                textbutton _("The Hazard{color=#D0821B}[glossary_update_hazard]{/color}"):
                    id "menu_glossary_hazard"
                    action NoReshowMenu("menu_glossary_hazard")
                    activate_sound renpy.random.choice(turnpage)

    # RELIGIONS

                text _("• RELIGION")
                textbutton _("Great Artisan{color=#D0821B}[glossary_update_greatartisan]{/color}"):
                    id "menu_glossary_greatartisan"
                    action NoReshowMenu("menu_glossary_greatartisan")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Judge Critic{color=#D0821B}[glossary_update_judgecritic]{/color}"):
                    id "menu_glossary_judgecritic"
                    action NoReshowMenu("menu_glossary_judgecritic")
                    activate_sound renpy.random.choice(turnpage)

    # SATURATION

                text _("• SATURATION")
                textbutton _("Saturation{color=#D0821B}[glossary_update_saturation]{/color}"):
                    id "menu_glossary_saturation"
                    action NoReshowMenu("menu_glossary_saturation")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Saturated\nItems{color=#D0821B}[glossary_update_saturateditems]{/color}"):
                    id "menu_glossary_saturateditem"
                    action NoReshowMenu("menu_glossary_saturateditem")
                    activate_sound renpy.random.choice(turnpage)

    # SATRUATED ITEMS


                text _("• ITEMS")
                textbutton _("Cara Vans{color=#D0821B}[glossary_update_caravans]{/color}"):
                    id "menu_glossary_caravan"
                    action NoReshowMenu("menu_glossary_caravan")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Saturated\nThread{color=#D0821B}[glossary_update_thread]{/color}"):
                    id "menu_glossary_thread"
                    action NoReshowMenu("menu_glossary_thread")
                    activate_sound renpy.random.choice(turnpage)

    # WORDS
                text _("• WORDS")
                textbutton _("\"I am...\"{color=#D0821B}[glossary_update_iamx]{/color}"):
                    id "menu_glossary_iamx"
                    action NoReshowMenu("menu_glossary_iamx")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Pronouns{color=#D0821B}[glossary_update_pronouns]{/color}"):
                    id "menu_glossary_pronouns"
                    action NoReshowMenu("menu_glossary_pronouns")
                    activate_sound renpy.random.choice(turnpage)

                textbutton _("Gender{color=#D0821B}[glossary_update_gender]{/color}"):
                    id "menu_glossary_gender"
                    action NoReshowMenu("menu_glossary_gender")
                    activate_sound renpy.random.choice(turnpage)
    vbar value YScrollValue("glossary_navi_id") style 'vscrollbar' keyboard_focus False yalign 0.63 xpos 130 ysize 780

style navigation_glossary_button is gui_button
style navigation_glossary_button_text is gui_button_text

style navigation_glossary_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound renpy.random.choice(menu_hover)
    activate_sound renpy.random.choice(turnpage)

style navigation_glossary_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.0
    selected_color gui.selected_color
    selected_hover_color gui.selected_hover_color

style navigation_glossary_text:
    color '#707070'

style navigation_glossary_vscrollbar:
    xpos -310


## CHARACTERS ##############################################
## each glossary has their own screen
###########################################################
style menu_glossary_vbox:
    yoffset 70
    xoffset 90
    xsize 1100

screen menu_glossary_truthscrapper():

    tag book_glossary
    use book_glossary(_("truthscrapper")):

        style_prefix "menu_glossary"

        vbox:
            text _("• It's the research guild you're a part of. We've worked for them for a while.")


    on "replace" action [SetVariable("glossary_name", _("Truth Scrapper")), SetVariable("glossary_title_text", _("[Your Guild.]")), SetVariable("glossary_update_truthscrapper", "")]

screen menu_glossary_investigate():

    tag book_glossary
    use book_glossary(_("investigate")):

        style_prefix "menu_glossary"

        vbox:
            text _("• You are Sosotte, and you forget everything every day until you touch this Scrap Book.")
            text ""
            text _("• You are a Truth Scrapper, and usually your job is to investigate and solve cases. Unless you're on break, which happens often.")
            text ""
            text _("• No, we don't know about our past. Yes, we've looked. No, we haven't found anything. Make your peace with it in the next five minutes, so you can enjoy your one day on this earth.")


    on "replace" action [SetVariable("glossary_name", _("READ ME")), SetVariable("glossary_title_text", _("[For the empty-minded]")), SetVariable("glossary_update_investigate", "")]

screen menu_glossary_pathdweller():

    tag book_glossary
    use book_glossary(_("pathdweller")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Treasure hunters of the Dwell.")


    on "replace" action [SetVariable("glossary_name", _("Path Dweller")), SetVariable("glossary_title_text", _("[Treasure Hunters of the Dwell.]")), SetVariable("glossary_update_pathdweller", "")]

screen menu_glossary_minedweller():

    tag book_glossary
    use book_glossary(_("minedweller")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Miners of the Dwell.")

    on "replace" action [SetVariable("glossary_name", _("Mine Dweller")), SetVariable("glossary_title_text", _("[Miners of the Dwell.]")), SetVariable("glossary_update_minedweller", "")]


screen menu_glossary_thedwell():

    tag book_glossary
    use book_glossary(_("thedwell")):

        style_prefix "menu_glossary"

        vbox:
            text _("• An underground cavern at the bottom of a giant sinkhole. It's several floors deep, and the cavern is as wide as the sinkhole.")

            text _("• Truth Scrappers have been attacked there, so I've been sent to investigate.")

            text _("• Every floor has a locked door, which can easily be opened with a Saturated Key Card.")


    on "replace" action [SetVariable("glossary_name", _("The Dwell")), SetVariable("glossary_title_text", _("[Our Destination.]")), SetVariable("glossary_update_thedwell", "")]



screen menu_glossary_culdepuits():

    tag book_glossary
    use book_glossary(_("culdepuits")):

        style_prefix "menu_glossary"

        vbox:
            text _("• KOO-deh-POO-ee.")
            text _("• A city built around the walls of a sinkhole.")


    on "replace" action [SetVariable("glossary_name", _("Cul-De-Puits")), SetVariable("glossary_title_text", _("[City above the Dwell.]")), SetVariable("glossary_update_culdepuits", "")]


screen menu_glossary_greatartisan():

    tag book_glossary
    use book_glossary(_("greatartisan")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Creator God of Artisanism, the religion around here.")
            text ""
            text _("• Saturated this world and gave it soul and life, if you're a Mid Artisan. Which we're not, by the way.")

    on "replace" action [SetVariable("glossary_name", _("Great Artisan")), SetVariable("glossary_title_text", _("[God, but mostly a swear.]")), SetVariable("glossary_update_greatartisan", "")]

screen menu_glossary_judgecritic():

    tag book_glossary
    use book_glossary(_("judgecritic")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Judge God of Artisanism.")
            text ""
            text _("• Judged the Great Artisan's Saturated World worthy.")

    on "replace" action [SetVariable("glossary_name", _("Judge Critic")), SetVariable("glossary_title_text", _("[God, but mostly for feedback.]")), SetVariable("glossary_update_judgecritic", "")]

screen menu_glossary_saturation():

    tag book_glossary
    use book_glossary(_("saturation")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Making an item more useful, via Saturation Rituals. Makes a Saturated Item. Like this Scrap Book!")


    on "replace" action [SetVariable("glossary_name", _("Saturation")), SetVariable("glossary_title_text", _("[Giving an Item powers.]")), SetVariable("glossary_update_saturation", "")]



screen menu_glossary_saturateditem():
    tag book_glossary
    use book_glossary(_("saturateditem")):

        style_prefix "menu_glossary"

        vbox:
            text _("• An item Saturated with soul and life.")
            text _("• Made of an object (Form) and a way to make it useful (Core).")
            text ""
            text _("• Example: This Scrap Book is made of a Book Form and a Memory Core. Hence our last name, \"Bookform\".")

    on "replace" action [SetVariable("glossary_name", _("Saturated Items")), SetVariable("glossary_title_text", _("[Magical objects.]")), SetVariable("glossary_update_saturateditems", "")]

screen menu_glossary_caravan():
    tag book_glossary
    use book_glossary(_("caravan")):

        style_prefix "menu_glossary"

        vbox:
            text _("• A Saturated Train used to travel between the Dwell and Cul-De-Puits.")

    on "replace" action [SetVariable("glossary_name", _("Cara Van")), SetVariable("glossary_title_text", _("[Trains of the Dwell.]")), SetVariable("glossary_update_caravans", "")]

screen menu_glossary_keycards():
    tag book_glossary
    use book_glossary(_("keycards")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Key Cards are dull rectangles with notches, made to open doors.")
            text _("• Inside the Dwell, they need to be Saturated to work. No other barriers of entry, like specific Rituals, are needed.")
            text _("• One Key Card will only work for a corresponding door, though.")

    on "replace" action [SetVariable("glossary_name", _("Key Card")), SetVariable("glossary_title_text", _("[Keys to the Dwell.]")), SetVariable("glossary_update_keycards", "")]

screen menu_glossary_iamx():

    tag book_glossary
    use book_glossary(_("I Am X")):

        style_prefix "menu_glossary"

        vbox:
            text _("• \"My name is Sosotte. I am she.\" How to introduce yourself and your pronouns.")
            text ""
            text _("• People might introduce themselves to you with new pronouns depending on the day. Gender is fluid, after all.")
            text _("• By the way, we use she, sometimes they. But I think it'd be fine if we wanted to try something completely different for a day.")
            text ""
            text _("• NOTE: I tried art/art/arts, and that felt shatteringly awful. Don't.")
            text _("• NOTE: I tried he/him/his. Did not care for that.")
            text _("• NOTE: I tried fae/faer/faers. Felt alright, and it's so cute it could be used to get someone's guard down...")


    on "replace" action [SetVariable("glossary_name", _("\"I Am...\"")), SetVariable("glossary_title_text", _("[Introducing Yourself.]")), SetVariable("glossary_update_iamx", "")]

screen menu_glossary_pronouns():

    tag book_glossary
    use book_glossary(_("Pronouns")):

        style_prefix "menu_glossary"

        vbox:
            text _("• How other people refer to you.")
            text _("• She/her/hers -> \"She Saturated her item. It's hers.\"")
            text _("• People might change every day, but it's polite to use what you've first or last heard them introduce themselves with.")
            text ""
            text _("• Some pronouns we have heard:")
            text _("{space=80}Art/art/arts: Usually used by Mid Artisans.")
            text _("{space=80}(item)/(item)im/(item)is: For words or concepts, like \"book/bookim/bookis\".")

    on "replace" action [SetVariable("glossary_name", _("Pronouns")), SetVariable("glossary_title_text", _("[Like An Accessory.]")), SetVariable("glossary_update_pronouns", "")]


screen menu_glossary_thread():

    tag book_glossary
    use book_glossary(_("thread")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Saturated thread that can be found throughout the Dwell.")
            text _("• They're a way to navigate through the Dwell, and for Dwellers to find their way back.")


    on "replace" action [SetVariable("glossary_name", _("Saturated Thread")), SetVariable("glossary_title_text", _("[Thread of the Dwell.]")), SetVariable("glossary_update_thread", "")]


screen menu_glossary_hazard():

    tag book_glossary
    use book_glossary(_("hazard")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Unknown being that used to attack people staying in the Dwell after dark.")


    on "replace" action [SetVariable("glossary_name", _("The Hazard")), SetVariable("glossary_title_text", _("[The Dwell's Cryptid.]")), SetVariable("glossary_update_hazard", "")]


screen menu_glossary_guide():

    tag book_glossary
    use book_glossary(_("guide")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Visitors of the Dwell have to be registered as a temporary visitor, and accompanied by a Guide.")
            text ""
            text _("• As of Day X-1, both Amour and Betz are my Guides.")



    on "replace" action [SetVariable("glossary_name", _("Guide")), SetVariable("glossary_title_text", _("[Help In The Dwell.]")), SetVariable("glossary_update_guide", "")]


screen menu_glossary_gender():

    tag book_glossary
    use book_glossary(_("gender")):

        style_prefix "menu_glossary"

        vbox:
            text _("• Some like to always wear the same style.")
            text _("• Some like to change it up every so often.")
            text _("• Some like to wear something wildly different every day.")
            text ""
            text _("• Some think it doesn't have much impact on their lives.")
            text _("• Some think it's their whole reason for waking up in the morning.")
            text _("• Some don't think about it at all. To each their own.")
            text ""
            text ""
            text _("• Sosotte, we are a \"cute and lovely girl\". Unless you don't feel like it today!")



    on "replace" action [SetVariable("glossary_name", _("Gender")), SetVariable("glossary_title_text", _("[Like Fashion.]")), SetVariable("glossary_update_gender", "")]