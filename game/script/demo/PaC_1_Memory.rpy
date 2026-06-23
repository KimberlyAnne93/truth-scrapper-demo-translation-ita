## REMINDERS MENU ###################################################
## reminders menu. the bane of my existence. this is for what it looks like
#####################################################################
default Day0Reroll = 1
default clickindicatorOn = True
screen day0_book_reminders():
    use game_menu_no_navi_no_return(_("Memories")):
        style_prefix "memories"
        vbox:
            xsize 1550
            ysize 500
            text _("THE DWELL • DAY X") xoffset 30 size 70


#Teach the player how to click on memories. only shown one time!
screen clickindicator_day0():
    if clickindicatorOn:
        image "clickindicator":
            xalign 0.5
            xoffset 190
            yalign 0.48
            yoffset -100

## ADDED FOR DEMO ##
## Edited all of this so there's no focus errors.
## Added more focused_on checks to avoid weird focus errors when using a controller.

## NOTE WHEN MAKING NEW MEMORY SCREENS:
    ## Use the id "memory_button" for the memory text, and set its default focus to True so that it's automatically selected if you're using a controller.
    ## Then, make sure to use the six focused_on statements, and replace the "day0_MemoryX" text for the name of the new screen.
    ##
screen day0_Memory1():
    vbox:
        style "memoryvbox"
        yoffset -150
        if Day0Choice == 1:
            textbutton "[MemoryTextForSpot1!t]" id "memory_button" style "memorybox" text_style "memoriesboxtext":
                # Set default_focus to True so that this is automatically focused when the screen shows and nothing is focused.
                # This is especially helpful for controller support!
                default_focus True
                action Call("Day0_WhichMemoryIsGonnaAppear")
                activate_sound renpy.random.choice(write)
        elif Day0Choice >= 2:
            textbutton"[D0C1Text!t]" action None style "memorybox" text_style "memoriesboxtext"
    
    # Have to manually set the focus for appropriate navigation purposes. Here I set it so that
    # if you're focused on the memory, pressing down will make the focus go to the "done" button and viceversa, and left/right won't do anything.
    # When copying over to a new screen, make sure the "day0_Memory1" text is replaced for the name of the actual screen to use.

    focused_on "memory_button" key "focus_down" action SetFocus("pointnclickbuttons", "button_done")
    focused_on "button_done" key "focus_up" action SetFocus("day0_Memory1", "memory_button")
    
    focused_on "memory_button" key "focus_up" action NullAction()
    focused_on "button_done" key "focus_down" action NullAction()

    key "focus_left" action NullAction()
    key "focus_right" action NullAction()

## ADDED FOR DEMO ##
## Fixes yayyy
screen day0_Memory2():
    # Same notes as day0_Memory2
    vbox:
        style "memoryvbox"
        yoffset -150+145
        if Day0Choice == 3:
            textbutton "[MemoryTextForSpot2!t]" id "memory_button" style "memorybox" text_style "memoriesboxtext":
                default_focus True
                action Call("Day0_WhichMemoryIsGonnaAppear")
                activate_sound renpy.random.choice(write)
        elif Day0Choice >= 4:
            textbutton"[D0C2Text!t]" action None style "memorybox" text_style "memoriesboxtext"
    
    focused_on "memory_button" key "focus_down" action SetFocus("pointnclickbuttons", "button_done")
    focused_on "button_done" key "focus_up" action SetFocus("day0_Memory2", "memory_button")
    
    
    focused_on "memory_button" key "focus_up" action NullAction()
    focused_on "button_done" key "focus_down" action NullAction()

    key "focus_left" action NullAction()
    key "focus_right" action NullAction()
## ADDED FOR DEMO ##
## Fixed the wrong name being in the SetFocus("day0_Memory3") line, and no ID being set for it.
screen day0_Memory3():
    vbox:
        style "memoryvbox"
        yoffset -150+145+145
        if Day0Choice == 6:
            textbutton "[MemoryTextForSpot3!t]" id "memory_button" style "memorybox" text_style "memoriesboxtext":
                default_focus True
                action Call("Day0_WhichMemoryIsGonnaAppear")
                activate_sound renpy.random.choice(write)         
        elif Day0Choice >= 7:
            textbutton"[D0C3Text!t]" action None style "memorybox" text_style "memoriesboxtext"

    focused_on "memory_button" key "focus_down" action SetFocus("pointnclickbuttons", "button_done")
    focused_on "button_done" key "focus_up" action SetFocus("day0_Memory3", "memory_button")
    
    
    focused_on "memory_button" key "focus_up" action NullAction()
    focused_on "button_done" key "focus_down" action NullAction()

    key "focus_left" action NullAction()
    key "focus_right" action NullAction()

#####################################################################

label Day0_WhichMemoryIsGonnaAppear():
    $ Day0Reroll += 1
    if Day0Reroll == 4:
        $ Day0Reroll = 1

    if Day0Choice == 6:
        if Day0Reroll == 3:
            $ Day0Reroll = 1


    if Day0Choice == 1:
        $ clickindicatorOn = False
        if Day0Reroll == 1:
            $ MemoryTextForSpot1 = _("{color=6B883C}• Hospital smells like antiseptic. Ew...{image=smell}{/color}")
        if Day0Reroll == 2:
            $ MemoryTextForSpot1 = _("{color=6B883C}• I can see some hospital books about all kinds of medical subjects.{image=sight}{/color}")
        if Day0Reroll == 3:
            $ MemoryTextForSpot1 = _("{color=6B883C}• I can hear hospital machines nearby. Beep beep...{image=hearing}{/color}")

    if Day0Choice == 3:
        if Day0Reroll == 1:
            $ MemoryTextForSpot2 = _("{color=6B883C}• Those painkillers did nothing. My head hurts...{image=str}{/color}")
        if Day0Reroll == 2:
            $ MemoryTextForSpot2 = _("{color=6B883C}• People in the hallway seem happy.{image=psy}{/color}")
        if Day0Reroll == 3:
            $ MemoryTextForSpot2 = _("{color=6B883C}• There's a crossword puzzle on the table. I wonder if I could solve it...{image=int}{/color}")


    if Day0Choice == 6:
        if Day0Reroll == 1:
            $ MemoryTextForSpot3 = _("{color=B06531}• Amour is interesting.{image=amourstat}{/color}")
        if Day0Reroll == 2:
            $ MemoryTextForSpot3 = _("{color=5597A9}• Betz is interesting.{image=betzstat}{/color}")
    return


