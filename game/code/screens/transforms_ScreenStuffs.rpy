## ANIMATIONS ##################################################
## pages turning and animations and such
################################################################

## ADDED FOR DEMO ##
## I would honestly recommend just copy pasting everything here.
## I only edited the nextpage_return and previouspage things, but still.. good practice
image transition_nextpage:
    "Transitions/transition_pageturn_1_into.png"
    pause 0.1
    "Transitions/transition_pageturn_2_into.png"
    pause 0.1
    "Transitions/transition_pageturn_3.png"
    pause 0.1
    "Transitions/transition_pageturn_4.png"
    pause 0.1
    "Transitions/transition_pageturn_5.png"
    pause 0.1
    alpha 0

screen screen_transition_nextpage():
    zorder 100
    image "transition_nextpage"
    timer 0.5 action Return()

image transition_previouspage:
    "Transitions/transition_pageturn_5.png"
    pause 0.1
    "Transitions/transition_pageturn_4.png"
    pause 0.1
    "Transitions/transition_pageturn_3.png"
    pause 0.1
    "Transitions/transition_pageturn_2_outta.png"
    pause 0.1
    "Transitions/transition_pageturn_1_outta.png"
    pause 0.1
    alpha 0

screen screen_transition_nextpage_noreturn():
    zorder 100
    image "transition_nextpage"
    timer 0.5 action Hide()

## ADDED FOR DEMO ##
## Making a version of the previous page transition without return.
screen screen_transition_previouspage_noreturn():
    zorder 100
    image "transition_previouspage"
    timer 0.4 action Hide()

screen screen_transition_previouspage():
    zorder 100
    image "transition_previouspage"
    timer 0.4 action [Hide(), Return()]


image transition blackanim:
    "Transitions/blink blackanim_1.png"
    pause 0.5
    "Transitions/blink blackanim_2.png"
    pause 0.5    
    "Transitions/blink blackanim_3.png"
    pause 0.5
    repeat

################################################################

image clickindicator:
    "gui/button/cursor_idle.png"
    pause 0.5
    "gui/button/cursor_indicator.png"
    pause 0.5
    repeat

image joystickanim:
    "BookMenu/Joystick/joystick_1.png"
    pause 1
    "BookMenu/Joystick/joystick_2.png"
    pause 0.15    
    "BookMenu/Joystick/joystick_3.png"
    pause 0.15
    "BookMenu/Joystick/joystick_4.png"
    pause 0.15
    "BookMenu/Joystick/joystick_5.png"
    pause 0.15
    repeat

################################################################
    
image henshin keycard_start:
    "Transitions/henshin keycard_1.png"
    pause 0.1
    "Transitions/henshin keycard_2.png"
    pause 0.1
    "Transitions/henshin keycard_3.png"
    pause 0.1
    "Transitions/henshin keycard_4.png"
    pause 0.1
    "Transitions/henshin keycard_5.png"
    pause 0.1
    "Transitions/henshin keycard_6.png"
    pause 0.1
    "Transitions/henshin keycard_7.png"
    pause 0.1

image henshin keycard_end:
    "Transitions/henshin keycard_8.png"
    pause 0.1
    "Transitions/henshin keycard_9.png"
    pause 0.1
    "Transitions/henshin keycard_10.png"
    pause 0.1
    "Transitions/henshin keycard_11.png"
    pause 0.1
    "Transitions/henshin keycard_12.png"
    pause 0.1
    "Transitions/henshin keycard_13.png"
    pause 0.1
    alpha 0


image henshin remembering:
    "Transitions/henshin remember_1.png"
    pause 0.1
    "Transitions/henshin remember_2.png"
    pause 0.1
    "Transitions/henshin remember_3.png"
    pause 0.1
    "Transitions/henshin remember_4.png"
    pause 0.2
    "Transitions/henshin remember_4b.png"
    pause 0.3
    "Transitions/henshin remember_5.png"
    pause 0.1
    "Transitions/henshin remember_6.png"
    pause 0.1
    "Transitions/henshin remember_6b.png"
    pause 0.4
    "Transitions/henshin remember_7.png"
    pause 0.1
    "Transitions/henshin remember_8.png"
################################################################

image blink start:
    "Transitions/blink_1.png"
    pause 0.1
    "Transitions/blink_2.png"
    pause 0.05
    "Transitions/blink_3.png"

image blink end:
    "Transitions/blink_4.png"
    pause 0.1
    "Transitions/blink_5.png"
    pause 0.1
    alpha 0

image blink black:
    "Transitions/blink_3.png"

image blink opacitymid:
    "Transitions/blink_opacity70.png"


image blink white:
    "Transitions/blink_white.png"

## MENU APPEAR #################################################
## zoomin!!!
################################################################

transform Appear_ZoomOvershoot:
    alpha 0.0 zoom 1.1
    0.25
    easeout 0.2 alpha 1.0 zoom 0.98
    easeout 0.25 zoom 1.0

## PAC KEY MOVEMENT #################################################
## right now adding them makes them do this every time you change something. so ill figure it out later
################################################################

transform ItemDissolveIn:
    alpha 0.0
    linear 0.5 alpha 1.0

transform ItemDroppedIn:
    alpha 0.0
    linear 0.5 alpha 1.0

transform ItemSmallZoomIn:
    alpha 0.0 zoom 1.01
    0.25
    easeout 0.2 alpha 1.0 zoom 0.999
    easeout 0.25 zoom 1.0

## CHOICES POSITION ############################################
## i owe nathan my life
################################################################

transform rotateleft:
    rotate_pad True
    rotate 3
    xoffset 20

transform rotatemiddle:
    rotate_pad True
    rotate 0
    yoffset 20

transform rotateright:
    rotate_pad True
    rotate -4
    yoffset 1
    xoffset -14

## HOVERS ######################################################
## lil hover animations, and also any looping icon anims
################################################################
image ctc_intro:
    yalign 0.95 xalign 0.95
    "BookMenu/ctcs/ctc_intro_1.png"
    pause 0.25
    "BookMenu/ctcs/ctc_intro_2.png"
    pause 0.25
    repeat 

    
image ctc_s:
    yalign 0.885 xalign 0.825
    "BookMenu/ctcs/ctc_sosotte_1.png"
    pause 0.25
    "BookMenu/ctcs/ctc_sosotte_2.png"
    pause 0.25
    repeat 

image ctc_b:
    yalign 0.885 xalign 0.825
    "BookMenu/ctcs/ctc_betz_1.png"
    pause 0.25
    "BookMenu/ctcs/ctc_betz_2.png"
    pause 0.25
    repeat 

image ctc_a:
    yalign 0.885 xalign 0.825
    "BookMenu/ctcs/ctc_amour_1.png"
    pause 0.25
    "BookMenu/ctcs/ctc_amour_2.png"
    pause 0.25
    repeat 

image ctc_r:
    yalign 0.885 xalign 0.825
    "BookMenu/ctcs/ctc_default_1.png"
    pause 0.25
    "BookMenu/ctcs/ctc_default_2.png"
    pause 0.25
    repeat 

image button_done_hover:
    "BookMenu/button_done_hover_1.png"
    pause 0.25
    "BookMenu/button_done_hover_2.png"
    pause 0.25
    repeat    

image left_arrow_hover:
    "BookMenu/arrow_left_hover_1.png"
    pause 0.25
    "BookMenu/arrow_left_hover_2.png"
    pause 0.25
    repeat    

image right_arrow_hover:
    "BookMenu/arrow_right_hover_1.png"
    pause 0.25
    "BookMenu/arrow_right_hover_2.png"
    pause 0.25
    repeat

image tab_1_hover:
    "BookMenu/tab_1_hover_1.png"
    pause 0.25
    "BookMenu/tab_1_hover_2.png"
    pause 0.25
    repeat   

image tab_2_hover:
    "BookMenu/tab_2_hover_1.png"
    pause 0.25
    "BookMenu/tab_2_hover_2.png"
    pause 0.25
    repeat 

image tab_3_hover:
    "BookMenu/tab_3_hover_1.png"
    pause 0.25
    "BookMenu/tab_3_hover_2.png"
    pause 0.25
    repeat  

image tab_4_hover:
    "BookMenu/tab_4_hover_1.png"
    pause 0.25
    "BookMenu/tab_4_hover_2.png"
    pause 0.25
    repeat  

image tab_return_hover:
    "BookMenu/tab_return_hover_1.png"
    pause 0.25
    "BookMenu/tab_return_hover_2.png"
    pause 0.25
    repeat  

image book_newMemory_idle:
    "BookMenu/book_newMemory_1.png"
    pause 0.4
    "BookMenu/book_newMemory_2.png"
    pause 0.4
    "BookMenu/book_newMemory_3.png"
    pause 0.4
    "BookMenu/book_newMemory_2.png"
    pause 0.4
    "BookMenu/book_newMemory_1.png"
    pause 0.4
    "BookMenu/book_newMemory_2.png"
    pause 0.4
    "BookMenu/book_newMemory_3.png"
    pause 0.4
    "BookMenu/book_newMemory_2.png"
    pause 0.4
    "BookMenu/book_newMemory_1.png"


image book_newMystery_idle:
    "BookMenu/book_newMystery_1.png"
    pause 0.4
    "BookMenu/book_newMystery_2.png"
    pause 0.4
    "BookMenu/book_newMystery_3.png"
    pause 0.4
    "BookMenu/book_newMystery_2.png"
    pause 0.4
    "BookMenu/book_newMystery_1.png"
    pause 0.4
    "BookMenu/book_newMystery_2.png"
    pause 0.4
    "BookMenu/book_newMystery_3.png"
    pause 0.4
    "BookMenu/book_newMystery_2.png"
    pause 0.4
    "BookMenu/book_newMystery_1.png"


image book_newCharacter_idle:
    "BookMenu/book_newCharacter_1.png"
    pause 0.4
    "BookMenu/book_newCharacter_2.png"
    pause 0.4
    "BookMenu/book_newCharacter_3.png"
    pause 0.4
    "BookMenu/book_newCharacter_2.png"
    pause 0.4
    "BookMenu/book_newCharacter_1.png"
    pause 0.4
    "BookMenu/book_newCharacter_2.png"
    pause 0.4
    "BookMenu/book_newCharacter_3.png"
    pause 0.4
    "BookMenu/book_newCharacter_2.png"
    pause 0.4
    "BookMenu/book_newCharacter_1.png"


image book_newGlossary_idle:
    "BookMenu/book_newGlossary_1.png"
    pause 0.4
    "BookMenu/book_newGlossary_2.png"
    pause 0.4
    "BookMenu/book_newGlossary_3.png"
    pause 0.4
    "BookMenu/book_newGlossary_2.png"
    pause 0.4
    "BookMenu/book_newGlossary_1.png"
    pause 0.4
    "BookMenu/book_newGlossary_2.png"
    pause 0.4
    "BookMenu/book_newGlossary_3.png"
    pause 0.4
    "BookMenu/book_newGlossary_2.png"
    pause 0.4
    "BookMenu/book_newGlossary_1.png"

image quickmenu_history_hover:
    "gui/button/quickmenu_history_hover_1.png"
    pause 0.4
    "gui/button/quickmenu_history_hover_2.png"
    pause 0.4
    repeat

image quickmenu_skip_hover:
    "gui/button/quickmenu_skip_hover_1.png"
    pause 0.4
    "gui/button/quickmenu_skip_hover_2.png"
    pause 0.4
    repeat

image quickmenu_save_hover:
    "gui/button/quickmenu_save_hover_1.png"
    pause 0.4
    "gui/button/quickmenu_save_hover_2.png"
    pause 0.4
    repeat

image quickmenu_options_hover:
    "gui/button/quickmenu_options_hover_1.png"
    pause 0.4
    "gui/button/quickmenu_options_hover_2.png"
    pause 0.4
    repeat

image quickmenu_auto_hover:
    "gui/button/quickmenu_auto_hover_1.png"
    pause 0.4
    "gui/button/quickmenu_auto_hover_2.png"
    pause 0.4
    repeat

image quickmenu_auto_hover_playing:
    "gui/button/quickmenu_auto_hover_1_playing.png"
    pause 0.4
    "gui/button/quickmenu_auto_hover_2_playing.png"
    pause 0.4
    repeat

image skip:
    "gui/skip_1.png"
    pause 0.25
    "gui/skip_2.png"
    pause 0.25
    repeat

image tutocheck:
    "gui/title/main_title_tutorial_1.png"
    pause 0.25
    "gui/title/main_title_tutorial_2.png"
    pause 0.25
    "gui/title/main_title_tutorial_3.png"
    pause 0.25
    "gui/title/main_title_tutorial_2.png"
    pause 0.25
    repeat