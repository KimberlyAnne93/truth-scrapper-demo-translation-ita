label script_0:
    stop music fadeout 3.0
    pause 4.0
    $ save_name = _("(Day ??? • Time ??? • ???)")

    $ DateAndPlace = _("            Day ??? • Time ??? • ???")
    show screen dateandplace



    #########################
    ## Point and Click Dream
    #########################
    $ IsPaCDisabled = False
    $ WhichPaC = "day0_dream"
    $ pointnclickbuttons_order = _("Myosotis, do this for me.")
    play music memories
    hide blink
    pause 3.0
    show screen pointnclickbuttonhelp with dissolve
    pause 1.0
    $ renpy.choice_for_skipping()
    show screen pointnclick_day0_dream onlayer front with dissolve
    pause 1.0
    $ pointnclick_day0_flower_click = True    
    hide cgpfar day0_dream_1_flower_idle
    call screen pointnclick_day0_dream onlayer front

    # all happens in the specific PaC file.

    #when finished the whole thing:
    label pointnclick_day0_dream_continue():
    $renpy.hide_screen("pointnclick_day0_dream", layer="front")
    stop music
    play sound glassbreak

    $ pointnclickbuttons_order = _("WE CAN DO THIS, TOGETHER!!!")
    show cgfar day0_dream_5_bg at dreamshakesmall
    show cgmid day0_dream_5_flower at dreamshake
    $ IsPaCDisabled = True
    pause 3.0
    hide screen pointnclickbuttonhelp
    hide cgfar day0_dream_5_bg
    hide cgmid day0_dream_5_flower



    default NewDayScreenText = _("THE DWELL • DAY X")
    play sound turnpage_single
    show transition_nextpage onlayer overlay

    show screen empty_page
    pause 2.0
    play sound daystartcalm
    pause 3.75

    show screen newDayScreen with wiperight
    $ renpy.force_autosave(take_screenshot=True, block=False)
    pause 4.25

    #back to a new page with the photo
    play sound turnpage_single
    show transition_nextpage onlayer overlay
    hide screen empty_page
    hide screen newDayScreen
    pause 3.0    
    return
