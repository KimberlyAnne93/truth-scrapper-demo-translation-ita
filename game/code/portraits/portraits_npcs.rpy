######################################################################################################################################################
### MADELEINE
#################################################
##################################################
### Body
##################################################

layeredimage bm pose:
    group body auto: #md_armsup_body
        attribute base default:
            "images/Portraits/betzBrigade/bm_pose_body_base.png"

    group eyes: #md_armsup_eyes_neutral
        attribute e_neutral default:
            "bm_pose_eyes_neutral"

        attribute e_sad:
            "bm_pose_eyes_sad"

        attribute e_vsad:
            "bm_pose_eyes_vsad"
        attribute e_closed:
            "images/Portraits/betzBrigade/bm_pose_eyes_sad_C.png"


    group mouth: #md_armsup_mouth_neutral
        attribute m_neutral default:
            "bm_pose_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betzBrigade/bm_pose_mouth_neutral_S.png"

    group sweat: #md_armsup_eyes_neutral
        attribute sweat_off default:
            null

        attribute sweat_on:
            "bm_pose_sweat_on"

##################################################
### Eyes
##################################################

image bm_pose_eyes_neutral:
    "images/Portraits/betzBrigade/bm_pose_eyes_neutral_C.png"
    .1
    "images/Portraits/betzBrigade/bm_pose_eyes_neutral_OC.png"
    0.05
    "images/Portraits/betzBrigade/bm_pose_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image bm_pose_eyes_sad:
    "images/Portraits/betzBrigade/bm_pose_eyes_sad_C.png"
    .1
    "images/Portraits/betzBrigade/bm_pose_eyes_sad_OC1.png"
    0.05
    "images/Portraits/betzBrigade/bm_pose_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image bm_pose_eyes_vsad:
    "images/Portraits/betzBrigade/bm_pose_eyes_sad_C.png"
    .1
    "images/Portraits/betzBrigade/bm_pose_eyes_sad_OC2.png"
    0.05
    "images/Portraits/betzBrigade/bm_pose_eyes_sad_OC1.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat


##################################################
### Mouth
##################################################

image bm_pose_mouth_neutral_talking:
        "images/Portraits/betzBrigade/bm_pose_mouth_neutral_TA.png"
        pause 0.15
        "images/Portraits/betzBrigade/bm_pose_mouth_neutral_S.png"
        pause 0.15
        "images/Portraits/betzBrigade/bm_pose_mouth_neutral_TO.png"
        pause 0.15
        "images/Portraits/betzBrigade/bm_pose_mouth_neutral_S.png"
        pause 0.15
        repeat

image bm_pose_mouth_neutral = ConditionSwitch(
    "bmLipflapping", "bm_pose_mouth_neutral_talking",
    "True", "images/Portraits/betzBrigade/bm_pose_mouth_neutral_S.png")

######################################################################################################################################################
### BASILIC
#################################################
##################################################
### Body
##################################################

layeredimage bb pose:
    group body auto: #md_armsup_body
        attribute base default:
            "images/Portraits/betzBrigade/bb_pose_body_base.png"

    group eyes: #md_armsup_eyes_neutral
        attribute e_neutral default:
            "bb_pose_eyes_neutral"

        attribute e_anger:
            "bb_pose_eyes_anger"

        attribute e_closed:
            "images/Portraits/betzBrigade/bb_pose_eyes_anger_C.png"

        attribute e_sad:
            "bb_pose_eyes_sad"

        attribute e_surprised:
            "bb_pose_eyes_surprised"

    group mouth: #md_armsup_mouth_neutral
        attribute m_neutral default:
            "bb_pose_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betzBrigade/bb_pose_mouth_neutral_S.png"

        attribute m_pout:
            "bb_pose_mouth_neutral"
        attribute m_pout_s:
            "images/Portraits/betzBrigade/bb_pose_mouth_pout_S.png"

        attribute m_anger:
            "bb_pose_mouth_anger"
        attribute m_anger_s:
            "images/Portraits/betzBrigade/bb_pose_mouth_anger_S.png"

    group sweat: #md_armsup_eyes_neutral
        attribute sweat_off default:
            null

        attribute sweat_on:
            "bb_pose_sweat_on"

##################################################
### Eyes
##################################################

image bb_pose_eyes_neutral:
    "images/Portraits/betzBrigade/bb_pose_eyes_neutral_C.png"
    .1
    "images/Portraits/betzBrigade/bb_pose_eyes_neutral_OC.png"
    0.05
    "images/Portraits/betzBrigade/bb_pose_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image bb_pose_eyes_sad:
    "images/Portraits/betzBrigade/bb_pose_eyes_sad_C.png"
    .1
    "images/Portraits/betzBrigade/bb_pose_eyes_sad_OC.png"
    0.05
    "images/Portraits/betzBrigade/bb_pose_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image bb_pose_eyes_anger:
    "images/Portraits/betzBrigade/bb_pose_eyes_anger_C.png"
    .1
    "images/Portraits/betzBrigade/bb_pose_eyes_anger_OC.png"
    0.05
    "images/Portraits/betzBrigade/bb_pose_eyes_anger_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image bb_pose_eyes_surprised:
    "images/Portraits/betzBrigade/bb_pose_eyes_surprised_C.png"
    .1
    "images/Portraits/betzBrigade/bb_pose_eyes_surprised_OC.png"
    0.05
    "images/Portraits/betzBrigade/bb_pose_eyes_surprised_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat
##################################################
### Mouth
##################################################

image bb_pose_mouth_neutral_talking:
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_TA.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_S.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_TO.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_S.png"
        pause 0.15
        repeat

image bb_pose_mouth_neutral = ConditionSwitch(
    "bbLipflapping", "bb_pose_mouth_neutral_talking",
    "True", "images/Portraits/betzBrigade/bb_pose_mouth_neutral_S.png")


image bb_pose_mouth_pout_talking:
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_TA.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_pout_S.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_TO.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_pout_S.png"
        pause 0.15
        repeat

image bb_pose_mouth_pout = ConditionSwitch(
    "bbLipflapping", "bb_pose_mouth_pout_talking",
    "True", "images/Portraits/betzBrigade/bb_pose_mouth_pout_S.png")


image bb_pose_mouth_anger_talking:
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_TA.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_anger_S.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_neutral_TO.png"
        pause 0.15
        "images/Portraits/betzBrigade/bb_pose_mouth_anger_S.png"
        pause 0.15
        repeat

image bb_pose_mouth_anger = ConditionSwitch(
    "bbLipflapping", "bb_pose_mouth_anger_talking",
    "True", "images/Portraits/betzBrigade/bb_pose_mouth_anger_S.png")

######################################################################################################################################################
### VANILLE
#################################################
##################################################
### Body
##################################################

layeredimage bv pose:
    group body auto: #md_armsup_body
        attribute base default:
            "images/Portraits/betzBrigade/bv_pose_body_base.png"

    group eyes: #md_armsup_eyes_neutral
        attribute e_neutral default:
            "bv_pose_eyes_neutral"

        attribute e_serious:
            "bv_pose_eyes_serious"

        attribute e_sad:
            "bv_pose_eyes_sad"

    group mouth: #md_armsup_mouth_neutral
        attribute m_neutral default:
            "bv_pose_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betzBrigade/bv_pose_mouth_neutral_S.png"

##################################################
### Eyes
##################################################

image bv_pose_eyes_neutral:
    "images/Portraits/betzBrigade/bv_pose_eyes_neutral_C.png"
    .1
    "images/Portraits/betzBrigade/bv_pose_eyes_neutral_OC.png"
    0.05
    "images/Portraits/betzBrigade/bv_pose_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image bv_pose_eyes_sad:
    "images/Portraits/betzBrigade/bv_pose_eyes_sad_C.png"
    .1
    "images/Portraits/betzBrigade/bv_pose_eyes_sad_OC.png"
    0.05
    "images/Portraits/betzBrigade/bv_pose_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image bv_pose_eyes_serious:
    "images/Portraits/betzBrigade/bv_pose_eyes_serious_C.png"
    .1
    "images/Portraits/betzBrigade/bv_pose_eyes_serious_OC.png"
    0.05
    "images/Portraits/betzBrigade/bv_pose_eyes_serious_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

##################################################
### Mouth
##################################################

image bv_pose_mouth_neutral_talking:
        "images/Portraits/betzBrigade/bv_pose_mouth_neutral_TA.png"
        pause 0.15
        "images/Portraits/betzBrigade/bv_pose_mouth_neutral_S.png"
        pause 0.15
        "images/Portraits/betzBrigade/bv_pose_mouth_neutral_TO.png"
        pause 0.15
        "images/Portraits/betzBrigade/bv_pose_mouth_neutral_S.png"
        pause 0.15
        repeat

image bv_pose_mouth_neutral = ConditionSwitch(
    "bvLipflapping", "bv_pose_mouth_neutral_talking",
    "True", "images/Portraits/betzBrigade/bv_pose_mouth_neutral_S.png")

