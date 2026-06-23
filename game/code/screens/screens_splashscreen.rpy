image closedbook_title = "gui/title/main_title_0.png"
image emptypage_title = "gui/overlay/game_menu.png"
image insertdisc5_logo:
    yalign 0.57 xalign 0.5
    "gui/title/insertdisc5 logo1.png"
    pause 0.3
    "gui/title/insertdisc5 logo2.png"
    pause 0.3
    "gui/title/insertdisc5 logo3.png"
    pause 0.3
    repeat
image ontariocreates_logo:
    yalign 0.6 xalign 0.44
    "gui/title/ontariocreates logo.png"



image transition_nextpage_title_1 ="images/transitions/transition_pageturn_1_title.png"
image transition_nextpage_title_2 ="images/transitions/transition_pageturn_2_title.png"
image transition_nextpage_title_3 ="images/transitions/transition_pageturn_3_title.png"
image transition_nextpage_title_4 ="images/transitions/transition_pageturn_4.png"
image transition_nextpage_title_5 ="images/transitions/transition_pageturn_5.png"
image transition_nextpage_title_1b ="images/transitions/transition_pageturn_1_into.png"
image transition_nextpage_title_2b ="images/transitions/transition_pageturn_2_into.png"
image transition_nextpage_title_3b ="images/transitions/transition_pageturn_3.png"

image titletext = ParameterizedText(xalign=0.5, yalign=0.35, size=70)

screen titletextcenter():
    style_prefix "titletextcenter"

    hbox:
        xalign 0.5
        yalign 0.5
        xsize 1200
        text _("Thank you for downloading the demo for Truth Scrapper!\n\nJust so you know, the events in this demo don’t play out the way they do in the final game, and the script has been modified to help you jump right into the story with all the context you need.\n\nThat means this is a standalone experience, and your progress won’t carry over into the full game, and so the demo is canon-but-not-really.\n\nOk? Ok! Thanks for playing!!!")

style titletextcenter_text:
    color "#FFFFFF"
    textalign 0.5
    size 50

image titletextcenter = ParameterizedText(xalign=0.45, yalign=0.5, size=70, textalign=0.5, color="#FFFFFF")
label splashscreen:
    scene black
    with Pause(0.3)
    show screen titletextcenter with dissolve
    show ctc_intro with dissolve
    
    pause

    #hide
    play sound menu_confirm
    hide ctc_intro
    hide screen titletextcenter
    with dissolve
    with Pause(0.2)


    #book
    show closedbook_title with dissolve
    with Pause(1)

    hide closedbook_title
    play music title
    show emptypage_title

    play sound openbook
    show transition_nextpage_title_1 onlayer overlay
    with Pause(0.1)
    show transition_nextpage_title_2 onlayer overlay
    hide transition_nextpage_title_1 
    show titletext _("A GAME BY")
    show insertdisc5_logo  #logo here!!!!!!!!!!!!!!!!!!!!!! 
    with Pause(0.05)
    show transition_nextpage_title_3b onlayer overlay
    hide transition_nextpage_title_2b
    with Pause(0.05)
    show transition_nextpage_title_4 onlayer overlay
    hide transition_nextpage_title_3
    with Pause(0.05)
    show transition_nextpage_title_5 onlayer overlay
    hide transition_nextpage_title_4
    with Pause(0.05)
    hide transition_nextpage_title_5

    with Pause(3.5)
    #pause here.

    play sound turnpage_single
    show transition_nextpage_title_1b onlayer overlay
    hide insertdisc5_logo #HIDE logo here!!!!!!!!!!!!!!!!!!!!!!
    hide titletext
    with Pause(0.05)
    show transition_nextpage_title_2b onlayer overlay
    hide transition_nextpage_title_1b 
    show titletext _("WITH HELP FROM")
    show ontariocreates_logo  #logo here!!!!!!!!!!!!!!!!!!!!!! 
    with Pause(0.05)
    show transition_nextpage_title_3b onlayer overlay
    hide transition_nextpage_title_2b
    with Pause(0.05)
    show transition_nextpage_title_4 onlayer overlay
    hide transition_nextpage_title_3
    with Pause(0.05)
    show transition_nextpage_title_5 onlayer overlay
    hide transition_nextpage_title_4
    with Pause(0.05)
    hide transition_nextpage_title_5

    with Pause(3)
    #pause here.


    play sound turnpage_single
    show transition_nextpage_title_1b onlayer overlay
    hide titletext
    hide ontariocreates_logo #HIDE logo here!!!!!!!!!!!!!!!!!!!!!!
    with Pause(0.05)
    show transition_nextpage_title_2b onlayer overlay
    hide transition_nextpage_title_1b   
    with Pause(0.05)
    show transition_nextpage_title_3b onlayer overlay
    hide transition_nextpage_title_2b
    with Pause(0.05)    
    return