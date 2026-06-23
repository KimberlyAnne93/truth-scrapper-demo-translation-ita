
screen test_glossary_hub():
    default current_entry = None
    default unlocked_entries = [ety for ety in character_glossary if ety.is_unlocked()]

    on "show" action [Show("screen_transition_nextpage_noreturn", _zorder = 100), SetVariable("IsPaCDisabled", False)]
    on "replaced" action [Show("screen_transition_nextpage_noreturn", _zorder = 100)]
    on "hide" action [SetVariable("IsPaCDisabled", True)]

    $ prev_entry = unlocked_entries[(unlocked_entries.index(current_entry)-1)%len(unlocked_entries) if current_entry is not None else -1]
    $ next_entry = unlocked_entries[(unlocked_entries.index(current_entry)+1)%len(unlocked_entries) if current_entry is not None else 0]
    key "pad_leftshoulder_press":
        activate_sound renpy.random.choice(turnpage)
        action [KeepInFocus("test_glossary_hub", "characters_navi_id",
                prev_entry.id, "up"),
            Show('screen_transition_nextpage_noreturn'),
            prev_entry.MarkRead(),
            CycleScreenVariable("current_entry", unlocked_entries, reverse=True, loop=True)]
    key "pad_rightshoulder_press":
        activate_sound renpy.random.choice(turnpage)
        action [KeepInFocus("test_glossary_hub", "characters_navi_id",
                next_entry.id, "down"),
            Show('screen_transition_nextpage_noreturn'),
            next_entry.MarkRead(),
            CycleScreenVariable("current_entry", unlocked_entries, loop=True)]

    modal True
    style_prefix "book_characters"

    use hide_mouse_screen

    frame:
        style "book_characters_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"

                side 'c r':
                    controller_viewport:
                        focus_scroll True
                        absorb_events False
                        yinitial 0.0
                        id "history_vp"
                        mousewheel True draggable True pagekeys True
                        which_stick "both"
                        trap_focus('right')
                        has fixed:
                            yfit True xfit True
                        if current_entry:
                            use test_glossary_entry(current_entry)

                    vbar:
                        id "history_bar"
                        value YScrollValueSelected("history_vp", "history_bar")
                        keyboard_focus False

    if current_entry:
        if current_entry.subtitle:
            label "\n[current_entry.page_title!t]{size=*0.5}{color=#707070}\n [current_entry.subtitle!t]{/color}{/size}"
        else:
            label "\n[current_entry.page_title!t]"

    if TurnOffReturn == False:
        if pad_config.is_using_controller():
            add "BookMenu/gamepadbuttons/xbox/xbox_lbrb_chara.png"

    controller_viewport:
        style_prefix "navigation_characters"
        yalign 0.63
        xpos 170
        xysize (300, 780)
        id "characters_navi_id"
        vscroll_style "center"
        draggable renpy.variant("touch")
        mousewheel True arrowkeys True
        has vbox
        xpos gui.navigation_xpos
        spacing gui.navigation_spacing

        if TurnOffReturn == False:
            for ind, entry in enumerate(unlocked_entries):
                ## Do we need a category header?
                if entry.category and (ind == 0 or unlocked_entries[ind - 1].category != entry.category):
                    text "• [entry.category!t]" style 'navigation_characters_text'

                textbutton "{}{}".format(renpy.translate_string(entry.title), "{color=#d0821b} •{/color}" if entry.has_new_content() else ""):
                    style 'navigation_characters_button'
                    id entry.id
                    if entry == current_entry:
                        action NullAction()
                    else:
                        action [Show('screen_transition_nextpage_noreturn'),
                            SetScreenVariable('current_entry', entry),
                            entry.MarkRead()]
                    hover_sound renpy.random.choice(menu_hover)
                    activate_sound renpy.random.choice(turnpage)

    vbar value YScrollValue("characters_navi_id") style 'vscrollbar' keyboard_focus False yalign 0.63 xpos 130 ysize 780


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


screen test_glossary_entry(entry):

    vbox:
        xsize 800 spacing 10
        null height 20
        for line in entry.lines:
            if line.is_unlocked:
                if line.content is None:
                    null properties line.properties
                elif line.is_image:
                    add line.content properties line.properties
                else:
                    text line.content properties line.properties

    for img in entry.images:
        if img.is_unlocked:
            add img.content properties img.properties

label test_glossary_label():
    "Testing glossary"
    $ renpy.run(ShowMenu("test_glossary_hub"))
    $ DayxNewCharacters = True
    $ renpy.run(ShowMenu("test_glossary_hub"))
    $ DayxAmourVain = True
    $ renpy.run(ShowMenu("test_glossary_hub"))
    "Back to game"
    return

define character_glossary = [ ]


glossary character_glossary:
    title "Sosotte" page_title "You"
    subtitle "[You, Me, Her, Us. The Person In The Mirror.]"

    image "charactermenu sosotte":
        xpos -430
        ypos -250

    text _("{=sigmar}{color=5B8C63}TRUTH SCRAPPER{/color}{/=sigmar} (she/her/hers)\n")

    text _("{=sigmar}{color=5B8C63}WHAT'S HAPPENING TO ME?{/color}{/=sigmar}")

    text _("• You have a condition which makes you forget everything, every day.")
    text _("• You will remember whatever you have written down in this Scrap Book by touching it.")
    text _("• There's nothing you can do to fix this. Make the best of it.")

    text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

    text _("• Many people consider you adorable. You can use that.")


glossary character_glossary:
    title "Amour"
    subtitle "[Red-Haired, Dull, Helpful.]"

    image "charactermenu amour":
        xpos -430
        ypos -270

    text "{=sigmar}{color=5B8C63}PATH DWELLER / OUR GUIDE{/color}{/=sigmar} (she/he)"
    text "• Met on Day X-1. Agreed to guide us.\n"
    text "{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}" color "#5b8c63"
    text "• Can ask her all the questions we want. Not likely to know much, though."
    if DayxAmourVain:
        text "• Vain. Compliment his face if you need something."

glossary character_glossary:
    title "Betz"
    subtitle "[Knight In Shining Armor.]"
    image "charactermenu betz":
        xpos -430
        ypos -270

    text _("{=sigmar}{color=5B8C63}PATH DWELLER / OUR GUIDE{/color}{/=sigmar} (he/they)")

    text _("• Met on Day X-1. Signed up as our Guide.\n")

    text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

    text _("• Calls me \"mademoiselle\".")

glossary character_glossary:
    title "KALE"
    subtitle "[Betz Brigade Member.]"
    condition DayxNewCharacters

    image "charactermenu kale":
        xpos -430
        ypos -270

    text _("{=sigmar}{color=5B8C63}MINE DWELLER{/color}{/=sigmar} (Dunno.)")

    text _("• Ambushed me in Cul-De-Puits, Day X-1.\n")

    text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

    text _("• Has a MASSIVE puppy crush on Betz.")
    text _("• Doesn't like me. STEER CLEAR.")


glossary character_glossary:
    title "JULIENNE"
    subtitle "[Betz Brigade Member.]"
    condition DayxNewCharacters

    image "charactermenu julienne":
        xpos -430
        ypos -270

    text _("{=sigmar}{color=5B8C63}MINE DWELLER{/color}{/=sigmar} (No idea.)")

    text _("• Ambushed me in Cul-De-Puits, Day X-1.\n")

    text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

    text _("• Wants to feed Betz soup.")
    text _("• Doesn't like me much.")


glossary character_glossary:
    title "IRIS"
    subtitle "[Betz Brigade Member.]"
    condition DayxNewCharacters

    image "charactermenu iris":
        xpos -430
        ypos -270

    text _("{=sigmar}{color=5B8C63}PATH DWELLER{/color}{/=sigmar} (Wasn't paying attention.)")

    text _("• Ambushed me in Cul-De-Puits, Day X-1.\n")

    text _("{=sigmar}{color=5B8C63}NOTES:{/color}{/=sigmar}")

    text _("• Seems indifferent towards Betz, honestly.")
    text _("• Blunt, but it's fine. Would recommend getting coffee with.")