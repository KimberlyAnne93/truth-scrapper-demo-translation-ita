## CHARACTERS #################################################
## screen characters moving.
################################################################
default option_shake = True
##################################################
### EXPRESSIONS
##################################################
transform reset:
    yalign 0 xalign 0.5 alpha 1.0

transform charayay:
    linear 0.1 yalign 0 yoffset 15 alpha 1.0
    linear 0.1 yoffset -30 
    easeout 0.15 yoffset 0

transform charaaw:
    linear 0.005 yalign 0 yoffset -15 alpha 1.0
    linear 0.1 yoffset 30
    easeout 0.15 yoffset 0

transform charashake:
    easein 0.05 yalign 0 xoffset 15 yoffset 15 alpha 1.0
    easein 0.05 xoffset -10 yoffset 10
    ease 0.1 xoffset 0 yoffset 0

#################################################
### APPEAR
##################################################
transform appearToleft:
    alpha 0.0 yalign 0 xalign 0.2 
    easein 0.5*(not renpy.is_skipping()) xalign 0.25 alpha 1.0

transform appearToright:
    alpha 0.0 yalign 0 xalign 0.8
    easein 0.5*(not renpy.is_skipping()) xalign 0.75 alpha 1.0

transform appearleftTomiddle:
    alpha 0.0 yalign 0 xalign 0.45
    easein 0.5*(not renpy.is_skipping()) xalign 0.5 alpha 1.0

transform appearTomiddleup:
    alpha 0.0 yalign 0 yoffset 50 xalign 0.5
    easein 0.5*(not renpy.is_skipping()) yoffset 0 alpha 1.0


transform appearTorightup:
    alpha 0.0 yalign 0 yoffset 50 xalign 0.25
    easein 0.5*(not renpy.is_skipping()) yoffset 0 alpha 1.0

transform appearToleftup:
    alpha 0.0 yalign 0 yoffset 50 xalign 0.75
    pause 0.1
    easein 0.5*(not renpy.is_skipping()) yoffset 0 alpha 1.0
    
##################################################
### teleport
##################################################
transform teleportleft:
    xalign 0.25 yalign 0 alpha 1.0

transform teleportright:
    xalign 0.75 yalign 0 alpha 1.0

transform teleportmiddle:
    xalign 0.5 alpha 1.0


##################################################
### MOVE
##################################################
transform toleft:
    easein 1 xalign 0.25 yalign 0 alpha 1.0

transform toright:
    easein 1 xalign 0.75 yalign 0 alpha 1.0

transform tomiddle:
    ease 1 xalign 0.5 alpha 1.0

transform toup:
    yalign -0.5
    ease 0.5 yalign 0.0 alpha 1.0

##################################################
### DISAPPEAR
##################################################
transform zoomsaway:
    ease 0.5 xalign 0.7
    ease 0.25 xalign -1.5

transform dissappearTomiddle:
    xalign 0.5 alpha 1.0
    easein 0.5*(not renpy.is_skipping()) alpha 0.0 yoffset 50

#######################

## SOSOTTE #################################################
## sosotte reactions
############################################################

#works for bg and characters.
transform shake:
    ease .04 yalign 0 yoffset 24 xoffset 24
    ease .04 yoffset 24 xoffset -24
    ease .04 yoffset -16 xoffset 16
    ease .04 yoffset -16 xoffset -16
    ease .02 yoffset 8 xoffset 8
    ease .02 yoffset -8 xoffset 8
    ease .01 yoffset 4 xoffset -4
    ease .01 yoffset -4 xoffset 4
    ease .02 yoffset -2 xoffset 2
    ease .02 yoffset 2 xoffset -2
    ease .03 yoffset 0 xoffset 0

transform tremble:
    ease .02 yoffset -2 xoffset 2
    ease .02 yoffset -1 xoffset -2
    ease .02 yoffset 2 xoffset 1
    ease .02 yoffset -1 xoffset -2
    repeat

transform trembleonce:
    ease .04 yalign 0 yoffset 24 xoffset 24
    ease .04 yoffset 24 xoffset -24
    ease .04 yoffset -16 xoffset 16
    ease .04 yoffset -16 xoffset -16
    ease .02 yoffset 8 xoffset 8
    ease .02 yoffset -8 xoffset 8
    ease .02 yoffset -2 xoffset 2
    ease .02 yoffset 2 xoffset -2
    ease .03 yoffset 0 xoffset 0

transform tremblepanic:
    ease .04 yalign 0 yoffset 24 xoffset 24
    ease .04 yoffset 24 xoffset -24
    ease .04 yoffset -16 xoffset 16
    ease .04 yoffset -16 xoffset -16
    ease .02 yoffset 8 xoffset 8
    ease .02 yoffset -8 xoffset 8
    ease .02 yoffset -2 xoffset 2
    ease .02 yoffset 2 xoffset -2
    ease .03 yoffset 0 xoffset 0
    pause 1.0
    repeat

label BGshake():
    show bg at shake
    show cgpfar at shake
    show cgfar at shake
    show cgmid at shake
    show cgmidback at shake
    show cgclose at shake
    show cgpclose at shake
    return

default shakeoffsetXnumber = 0

transform shakeOffset:
    ease .04 yalign 0 yoffset 24 xoffset 24+shakeoffsetXnumber
    ease .04 yoffset 24 xoffset -24+shakeoffsetXnumber
    ease .04 yoffset -16 xoffset 16+shakeoffsetXnumber
    ease .04 yoffset -16 xoffset -16+shakeoffsetXnumber
    ease .02 yoffset 8 xoffset 8+shakeoffsetXnumber
    ease .02 yoffset -8 xoffset 8+shakeoffsetXnumber
    ease .01 yoffset 4 xoffset -4+shakeoffsetXnumber
    ease .01 yoffset -4 xoffset 4+shakeoffsetXnumber
    ease .02 yoffset -2 xoffset 2+shakeoffsetXnumber
    ease .02 yoffset 2 xoffset -2+shakeoffsetXnumber
    ease .03 yoffset 0 xoffset 0+shakeoffsetXnumber

#sosotte goes yay! c character b background
transform syayC:
    ease 0.15 yalign 0 yoffset 30
    ease 0.25 yoffset 0

transform syayB:
    ease 0.15 yalign 0 yoffset 20
    ease 0.25 yoffset 0


label syayBG():
    show bg at syayB
    show cgpfar at syayB
    show cgfar at syayB
    show cgmid at syayB
    show cgmidback at syayB
    show cgclose at syayB
    show cgpclose at syayB
    return

#sosotte goes aw.
transform sawC:
    ease 0.5 yalign 0 yoffset -60

transform sawB:
    ease 0.5 yalign 0 yoffset -50

label sawBG():
    show bg at sawB
    show cgpfar at sawB
    show cgfar at sawB
    show cgmid at sawB
    show cgmidback at sawB
    show cgclose at sawB
    show cgpclose at sawB
    return

#sosotte resets.
transform sresetC:
    ease 0.5 yalign 0 yoffset 0

transform sresetB:
    ease 0.5 yalign 0 yoffset 0

label sresetBG():
    show bg at sresetB
    show cgpfar at sresetB
    show cgfar at sresetB
    show cgmid at sresetB
    show cgmidback at sresetB
    show cgclose at sresetB
    show cgpclose at sresetB
    return

#sosotte nods
transform snodC:
    ease 0.15 yalign 0 yoffset 20
    ease 0.15 yoffset -30
    ease 0.15 yoffset 30   
    ease 0.2 yoffset 0

transform snodB:
    ease 0.15 yalign 0 yoffset 10
    ease 0.15 yoffset -20
    ease 0.15 yoffset 20
    ease 0.2 yoffset 0

label snodBG():
    show bg at snodB
    show cgpfar at snodB
    show cgfar at snodB
    show cgmid at snodB
    show cgmidback at snodB
    show cgclose at snodB
    show cgpclose at snodB
    return

#sosotte says no
transform snoC:
    ease 0.3 xoffset 30
    ease 0.3 xoffset -20
    ease 0.3 xoffset 20
    ease 0.6 xoffset -20
    ease 0.6 yoffset 0

transform snoB:
    ease 0.3 xoffset 20
    ease 0.3 xoffset -10
    ease 0.3 xoffset 10
    ease 0.6 xoffset -10
    ease 0.6 yoffset 0

#####################################################################

transform simpleFadeIn:
    alpha 0.0
    on idle:
        linear 1.0 alpha 1.0

