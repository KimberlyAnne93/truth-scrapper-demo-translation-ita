## DAY 1 ##################################################
## 
################################################################
# big shake for the dream
transform dreamshake:
    ease .04 yalign 0 yoffset 224 xoffset 224
    ease .04 yoffset 124 xoffset -124
    ease .04 yoffset -86 xoffset 86
    ease .04 yoffset -56 xoffset -56
    ease .02 yoffset 28 xoffset 28
    ease .02 yoffset -18 xoffset 18
    ease .01 yoffset 4 xoffset -4
    ease .01 yoffset -4 xoffset 4
    ease .02 yoffset -2 xoffset 2
    ease .02 yoffset 2 xoffset -2
    ease .03 yoffset 0 xoffset 0

transform dreamshakesmall:
    ease .04 yalign 0 yoffset 124 xoffset 124
    ease .04 yoffset 94 xoffset -94
    ease .04 yoffset -86 xoffset 86
    ease .04 yoffset -56 xoffset -56
    ease .02 yoffset 28 xoffset 28
    ease .02 yoffset -18 xoffset 18
    ease .01 yoffset 4 xoffset -4
    ease .01 yoffset -4 xoffset 4
    ease .02 yoffset -2 xoffset 2
    ease .02 yoffset 2 xoffset -2
    ease .03 yoffset 0 xoffset 0

#waking up
transform wakingupday1:
    yalign 0.1
    linear 0.5 yalign 0.0


#sky
transform parallaxvertical:
    yalign 0.0
    linear 120.0 yalign 1.0
    repeat

#amour cg
transform cg_meetingamour_move_amour:
    ease 3.0 yalign 0.2

transform cg_meetingamour_move_bg:
    ease 3.0 yalign 0.4

transform cg_meetingamour_immediate_bg:
    yalign 7

#betz cg
transform cg_meetingbetz_move_betz:
    yalign 0.2

transform cg_meetingbetz_move_bg:
    ease 3.0 yalign 0.5

transform cg_meetingbetz_immediate_bg:
    yalign 7

#train arrives
transform trainarrives:
    #yoffset 300
    xoffset 500 yoffset 100 alpha 0
    easeout 0.5 xoffset 400 yoffset 90 alpha 1
    easein 2.0 xoffset -25 yoffset -5
    easein 1.0 xoffset 10 yoffset 3
    easein 2.0 xoffset 0 yoffset 0

#train
transform train_sidecamera:
    xoffset 400
    easeout 0.4 yoffset 2
    ease 0.4 yoffset 0
    repeat 

transform train_sidecamerastatic:
    xoffset 400


transform train_sidecamerastaticamour:
    xoffset 45

transform train_rattle:
    xoffset -400
    easeout 0.1 yoffset 2
    ease 0.1 yoffset 0
    repeat 

transform train_rattleslow:
    xoffset -400
    easeout 0.4 yoffset 2
    ease 0.4 yoffset 0
    repeat 

transform train_rattle_x:
    easeout 0.1 yoffset 2
    ease 0.1 yoffset 0
    repeat 

transform train_rattleslow_x:
    easeout 0.4 yoffset 2
    ease 0.4 yoffset 0
    repeat 

# slow writing
define wiperightslow = CropMove(1.0, "wiperight")

#slow dissolve TO 0%
transform slowdissolvein:
    alpha 1.0
    easeout 2*(not renpy.is_skipping()) alpha 0.0

#slow dissolve TO 100%
transform slowdissolve:
    alpha 0.0
    easeout 2*(not renpy.is_skipping()) alpha 1.0

#betz brigade
transform teleportrightbrigade:
    xalign 0.9 yalign 0

transform teleportleftbrigade:
    xalign 0.1 yalign 0

# higher colette
transform highercolette:
    yoffset -70

# letter
transform letterappear:
    yoffset -70

#mirror
transform mirrorlook:
    yoffset -150
    easein 1.5 yoffset 0

transform mirrorlook2:
    yoffset 100
    easein 2.0 yoffset 0

transform mirrorlook3:
    yoffset 50
    easein 1.7 yoffset 0

transform tremble:
    ease .02 yoffset -2 xoffset 2
    ease .02 yoffset -1 xoffset -2
    ease .02 yoffset 2 xoffset 1
    ease .02 yoffset -1 xoffset -2
    repeat

# nightclub

transform cg_nightclub_start:
    yalign 1.3

transform cg_nightclub_move_bg:
    ease 3.0 yalign 0.6

transform cg_nightclub_move_chara:
    ease 3.0 yalign 0.3

transform cg_nightclub_end_chara:
    yalign 0.3

transform cg_nightclub_end_bg:
    yalign 0.6
    ease .15 yoffset -5
    ease .15 yoffset 5
    pause 0.25
    repeat

transform bg_dance:
    ease .15 yoffset -5
    ease .15 yoffset 5
    pause 0.25
    repeat

transform bg_dance_close:
    ease .15 yoffset -8
    ease .15 yoffset 8
    pause 0.25
    repeat

#lightsout
transform lightsout:
    alpha 0.0
    easeout 2*(not renpy.is_skipping()) alpha 1.0

#lightsback
transform lightsback:
    alpha 1.0
    easeout 2*(not renpy.is_skipping()) alpha 0.0

transform longdissolve:
    alpha 1.0
    easeout 3*(not renpy.is_skipping()) alpha 0.0


transform partyentrancecharayay:
    linear 0.1 yalign 0.3 yoffset 15 alpha 1.0
    linear 0.1 yoffset -30 
    easeout 0.15 yoffset 0

transform partyentrancecharashake:
    easein 0.05 yalign 0.3 xoffset 15 yoffset 15 alpha 1.0
    easein 0.05 xoffset -10 yoffset 10
    ease 0.1 xoffset 0 yoffset 0

#lightsout
transform quickdissolve:
    alpha 0.0
    easeout 1*(not renpy.is_skipping()) alpha 1.0

transform veryslowdissolvein:
    alpha 0.0
    easeout 4*(not renpy.is_skipping()) alpha 1.0

transform squash_hori:
    xalign 0.5 yalign 0.0
    xzoom 1.0
    yzoom 1.0
    linear 0.1*(not renpy.is_skipping()) xzoom 0.95 yzoom 1.05

transform stretch_hori:
    xalign 0.5 yalign 0.0
    easeout 0.1*(not renpy.is_skipping()) xzoom 1.1 yzoom 0.9
    ease 0.1*(not renpy.is_skipping()) xzoom 1.0 yzoom 1.0

transform opacityhalf:
    alpha 0.9
    linear 7*(not renpy.is_skipping()) alpha 0.0
