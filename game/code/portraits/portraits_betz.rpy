####################################################################################################
# ARMUP
####################################################################################################
### Body
##################################################

layeredimage betz armup:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_neutral default:
            "betz_armup_eyes_neutral"

        attribute e_hm:
            "betz_armup_eyes_hm"
        
        attribute e_mocking:
            "betz_armup_eyes_mocking"
        
        attribute e_smile:
            "betz_armup_eyes_smile"

        attribute e_sad:
            "betz_armup_eyes_sad"

        attribute e_sadclosed:
            "images/Portraits/betz/betz_armup_eyes_sad_C.png"

    group mouth: #betz_armup_mouth_neutral
        attribute m_neutral default:
            "betz_armup_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_armup_mouth_neutral_S.png"

        attribute m_smile:
            "betz_armup_mouth_smile"
        attribute m_smile_s:
            "images/Portraits/betz/betz_armup_mouth_smile_S.png"

        attribute m_realsmile:
            "betz_armup_mouth_realsmile"
        attribute m_realsmile_s:
            "images/Portraits/betz/betz_armup_mouth_realsmile_S.png"

        attribute m_slightsmile:
            "betz_armup_mouth_slightsmile"
        attribute m_slightsmile_s:
            "images/Portraits/betz/betz_armup_mouth_slightsmile_S.png"

    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_armup_sweat_on.png"

        attribute sweat_off default:
            null
##################################################
### Eyes
##################################################

image betz_armup_eyes_neutral:
    "images/Portraits/betz/betz_armup_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_armup_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_armup_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armup_eyes_hm:
    "images/Portraits/betz/betz_armup_eyes_hm_C.png"
    0.1
    "images/Portraits/betz/betz_armup_eyes_hm_OC.png"
    .05
    "images/Portraits/betz/betz_armup_eyes_hm_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armup_eyes_mocking:
    "images/Portraits/betz/betz_armup_eyes_mocking_C.png"
    0.1
    "images/Portraits/betz/betz_armup_eyes_mocking_OC.png"
    .05
    "images/Portraits/betz/betz_armup_eyes_mocking_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armup_eyes_smile:
    "images/Portraits/betz/betz_armup_eyes_smile_C.png"
    0.1
    "images/Portraits/betz/betz_armup_eyes_smile_OC.png"
    .05
    "images/Portraits/betz/betz_armup_eyes_smile_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armup_eyes_sad:
    "images/Portraits/betz/betz_armup_eyes_sad_C.png"
    0.1
    "images/Portraits/betz/betz_armup_eyes_sad_OC.png"
    .05
    "images/Portraits/betz/betz_armup_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

##################################################
### Mouth
##################################################

image betz_armup_mouth_neutral_talking:
    "images/Portraits/betz/betz_armup_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_neutral_S.png"
    pause 0.15
    repeat

image betz_armup_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_armup_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_armup_mouth_neutral_S.png")


image betz_armup_mouth_smile_talking:
    "images/Portraits/betz/betz_armup_mouth_smile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_smile_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_smile_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_smile_S.png"
    pause 0.15
    repeat

image betz_armup_mouth_smile = ConditionSwitch(
    "betzLipflapping", "betz_armup_mouth_smile_talking",
    "True", "images/Portraits/betz/betz_armup_mouth_smile_S.png")


image betz_armup_mouth_realsmile_talking:
    "images/Portraits/betz/betz_armup_mouth_smile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_realsmile_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_smile_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_realsmile_S.png"
    pause 0.15
    repeat

image betz_armup_mouth_realsmile = ConditionSwitch(
    "betzLipflapping", "betz_armup_mouth_realsmile_talking",
    "True", "images/Portraits/betz/betz_armup_mouth_realsmile_S.png")


image betz_armup_mouth_slightsmile_talking:
    "images/Portraits/betz/betz_armup_mouth_smile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_slightsmile_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_smile_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armup_mouth_slightsmile_S.png"
    pause 0.15
    repeat

image betz_armup_mouth_slightsmile = ConditionSwitch(
    "betzLipflapping", "betz_armup_mouth_slightsmile_talking",
    "True", "images/Portraits/betz/betz_armup_mouth_slightsmile_S.png")

####################################################################################################
# ARMS SIDE
####################################################################################################
### Body
##################################################

layeredimage betz armsides:
    group body auto: #betz_armup_body_armup
        attribute base default

    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_armsides_sweat_on.png"

        attribute sweat_off default:
            null

    group blush:
        attribute blush_on:
            "images/Portraits/betz/betz_armsides_blush_on.png"

        attribute blush_off default:
            null

    group stars:
        attribute stars_on:
            "betz_armsides_stars_on"

        attribute stars_off default:
            null

    group eyes: #betz_armup_eyes_neutral
        attribute e_neutral default:
            "betz_armsides_eyes_neutral"

        attribute e_aneutral:
            "betz_armsides_eyes_aneutral"

        attribute e_smile:
            "betz_armsides_eyes_smile"

        attribute e_slightsmile:
            "betz_armsides_eyes_slightsmile"

        attribute e_surprised:
            "betz_armsides_eyes_surprised"

        attribute e_fakesmile:
            "betz_armsides_eyes_fakesmile"

        attribute e_frown:
            "betz_armsides_eyes_frown"

        attribute e_angry:
            "betz_armsides_eyes_angry"

        attribute e_aangry:
            "betz_armsides_eyes_aangry"

        attribute e_augh:
            "betz_armsides_eyes_augh"

        attribute e_sad:
            "betz_armsides_eyes_sad"

        attribute e_sadclosed:
            "images/Portraits/betz/betz_armsides_eyes_sad_C.png"

        attribute e_asad:
            "betz_armsides_eyes_asad"

        attribute e_sadaside:
            "betz_armsides_eyes_sadaside"

        attribute e_heh:
            "betz_armsides_eyes_heh"

        attribute e_closedsmile:
            "images/Portraits/betz/betz_armsides_eyes_closedsmile_C.png"

        attribute e_uncomfy:
            "images/Portraits/betz/betz_armsides_eyes_uncomfy.png"

    group mouth: #betz_armup_mouth_neutral
        attribute m_neutral default:
            "betz_armsides_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_armsides_mouth_neutral_S.png"

        attribute m_angry:
            "betz_armsides_mouth_angry"
        attribute m_angry_s:
            "images/Portraits/betz/betz_armsides_mouth_angry_S.png"

        attribute m_smile:
            "betz_armsides_mouth_smile"
        attribute m_smile_s:
            "images/Portraits/betz/betz_armsides_mouth_smile_S.png"

        attribute m_slightsmile:
            "betz_armsides_mouth_slightsmile"
        attribute m_slightsmile_s:
            "images/Portraits/betz/betz_armsides_mouth_slightsmile_S.png"

        attribute m_wide:
            "betz_armsides_mouth_wide"
        attribute m_wide_s:
            "images/Portraits/betz/betz_armsides_mouth_wide_S.png"

        attribute m_fakesmile:
            "betz_armsides_mouth_fakesmile"
        attribute m_fakesmile_s:
            "images/Portraits/betz/betz_armsides_mouth_fakesmile_S.png"
        attribute m_fakesmile_oend:
            "betz_armsides_mouth_fakesmile_oend"

##################################################
### Eyes
##################################################

image betz_armsides_eyes_neutral:
    "images/Portraits/betz/betz_armsides_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_aneutral:
    "images/Portraits/betz/betz_armsides_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_aneutral_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_aneutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_frown:
    "images/Portraits/betz/betz_armsides_eyes_frown_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_frown_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_frown_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_smile:
    "images/Portraits/betz/betz_armsides_eyes_smile_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_smile_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_smile_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_slightsmile:
    "images/Portraits/betz/betz_armsides_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_slightsmile_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_surprised:
    "images/Portraits/betz/betz_armsides_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_surprised_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_angry:
    "images/Portraits/betz/betz_armsides_eyes_angry_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_angry_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_angry_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_aangry:
    "images/Portraits/betz/betz_armsides_eyes_angry_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_aangry_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_aangry_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_augh:
    "images/Portraits/betz/betz_armsides_eyes_frown_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_augh_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_augh_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_sad:
    "images/Portraits/betz/betz_armsides_eyes_sad_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_sad_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_asad:
    "images/Portraits/betz/betz_armsides_eyes_sad_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_asad_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_asad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_sadaside:
    "images/Portraits/betz/betz_armsides_eyes_sad_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_sad_OC_aside.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_sad_OC.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_heh:
    "images/Portraits/betz/betz_armsides_eyes_heh_C.png"
    0.1
    "images/Portraits/betz/betz_armsides_eyes_heh_OC.png"
    .05
    "images/Portraits/betz/betz_armsides_eyes_heh_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_armsides_eyes_fakesmile:
    "images/Portraits/betz/betz_armsides_eyes_fakesmile.png"

##################################################
### Mouth
##################################################

image betz_armsides_mouth_neutral_talking:
    "images/Portraits/betz/betz_armsides_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_neutral_S.png"
    pause 0.15
    repeat

image betz_armsides_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_armsides_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_armsides_mouth_neutral_S.png")


image betz_armsides_mouth_angry_talking:
    "images/Portraits/betz/betz_armsides_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_angry_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_angry_S.png"
    pause 0.15
    repeat

image betz_armsides_mouth_angry = ConditionSwitch(
    "betzLipflapping", "betz_armsides_mouth_angry_talking",
    "True", "images/Portraits/betz/betz_armsides_mouth_angry_S.png")


image betz_armsides_mouth_wide_talking:
    "images/Portraits/betz/betz_armsides_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_wide_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_wide_S.png"
    pause 0.15
    repeat

image betz_armsides_mouth_wide = ConditionSwitch(
    "betzLipflapping", "betz_armsides_mouth_wide_talking",
    "True", "images/Portraits/betz/betz_armsides_mouth_wide_S.png")

image betz_armsides_mouth_smile_talking:
    "images/Portraits/betz/betz_armsides_mouth_smile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_smile_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_smile_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_smile_S.png"
    pause 0.15
    repeat

image betz_armsides_mouth_smile = ConditionSwitch(
    "betzLipflapping", "betz_armsides_mouth_smile_talking",
    "True", "images/Portraits/betz/betz_armsides_mouth_smile_S.png")


image betz_armsides_mouth_slightsmile_talking:
    "images/Portraits/betz/betz_armsides_mouth_smile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_slightsmile_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_smile_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_smile_S.png"
    pause 0.15
    repeat

image betz_armsides_mouth_slightsmile = ConditionSwitch(
    "betzLipflapping", "betz_armsides_mouth_slightsmile_talking",
    "True", "images/Portraits/betz/betz_armsides_mouth_slightsmile_S.png")


image betz_armsides_mouth_fakesmile_talking:
    "images/Portraits/betz/betz_armsides_mouth_fakesmile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_fakesmile_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_fakesmile_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_armsides_mouth_fakesmile_S.png"
    pause 0.15
    repeat

image betz_armsides_mouth_fakesmile = ConditionSwitch(
    "betzLipflapping", "betz_armsides_mouth_fakesmile_talking",
    "True", "images/Portraits/betz/betz_armsides_mouth_fakesmile_S.png")
image betz_armsides_mouth_fakesmile_oend = ConditionSwitch(
    "betzLipflapping", "betz_armsides_mouth_fakesmile_talking",
    "True", "images/Portraits/betz/betz_armsides_mouth_fakesmile_TA.png")

##################################################
### Stars
##################################################

image betz_armsides_stars_on:
    "images/Portraits/betz/betz_armsides_stars_1.png"
    0.25
    "images/Portraits/betz/betz_armsides_stars_2.png"
    0.25
    "images/Portraits/betz/betz_armsides_stars_3.png"
    0.25
    "images/Portraits/betz/betz_armsides_stars_2.png"
    0.25
    repeat

####################################################################################################
# BLUSH
####################################################################################################
### Body
##################################################

layeredimage betz blush:
    group body auto: #betz_armup_body_armup
        attribute base default
        attribute pajamas

    group eyes: #betz_armup_eyes_neutral
        attribute e_upset default:
            "betz_blush_eyes_upset"

        attribute e_blush:
            "betz_blush_eyes_blush"

        attribute e_horror:
            "betz_blush_eyes_horror"

    group mouth: #betz_armup_mouth_neutral
        attribute m_uwah default:
            "betz_blush_mouth_uwah"
        attribute m_uwah_s:
            "images/Portraits/betz/betz_blush_mouth_uwah_S.png"

        attribute m_uwah_open:
            "betz_blush_mouth_uwah_open"

        attribute m_scream default:
            "betz_blush_mouth_scream"
        attribute m_scream_s:
            "images/Portraits/betz/betz_blush_mouth_scream_S.png"


    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_blush_sweat_on.png"

        attribute sweat_off default:
            null

    group sweat2:
        attribute sweat2_on:
            "images/Portraits/betz/betz_blush_sweat2_on.png"

        attribute sweat2_off default:
            null

    group air:
        attribute air_on:
            "betz_blush_air_on"

        attribute air_off default:
            null

##################################################
### Eyes
##################################################

image betz_blush_eyes_upset:
    "images/Portraits/betz/betz_blush_eyes_upset_C.png"
    0.1
    "images/Portraits/betz/betz_blush_eyes_upset_OC.png"
    .05
    "images/Portraits/betz/betz_blush_eyes_upset_O.png"
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    choice:
        0.0
    repeat

image betz_blush_eyes_blush:
    "images/Portraits/betz/betz_blush_eyes_blush_C.png"
    0.1
    "images/Portraits/betz/betz_blush_eyes_blush_OC.png"
    .05
    "images/Portraits/betz/betz_blush_eyes_blush_O.png"
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    choice:
        0.0
    repeat

image betz_blush_eyes_horror:
    "images/Portraits/betz/betz_blush_eyes_horror_C.png"
    0.1
    "images/Portraits/betz/betz_blush_eyes_horror_OC.png"
    .05
    "images/Portraits/betz/betz_blush_eyes_horror_O.png"
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    choice:
        0.0
    repeat
##################################################
### Mouth
##################################################

image betz_blush_mouth_uwah_talking:
    "images/Portraits/betz/betz_blush_mouth_uwah_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_blush_mouth_uwah_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_blush_mouth_uwah_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_blush_mouth_uwah_S.png"
    pause 0.15
    repeat

image betz_blush_mouth_uwah = ConditionSwitch(
    "betzLipflapping", "betz_blush_mouth_uwah_talking",
    "True", "images/Portraits/betz/betz_blush_mouth_uwah_S.png")

image betz_blush_mouth_uwah_open = ConditionSwitch(
    "betzLipflapping", "betz_blush_mouth_uwah_talking",
    "True", "images/Portraits/betz/betz_blush_mouth_uwah_TA.png")

image betz_blush_mouth_scream_talking:
    "images/Portraits/betz/betz_blush_mouth_scream_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_blush_mouth_scream_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_blush_mouth_scream_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_blush_mouth_scream_S.png"
    pause 0.15
    repeat

image betz_blush_mouth_scream = ConditionSwitch(
    "betzLipflapping", "betz_blush_mouth_scream_talking",
    "True", "images/Portraits/betz/betz_blush_mouth_scream_TA.png")

##################################################
### sweat in the air
##################################################

image betz_blush_air_on:
    "images/Portraits/betz/betz_blush_air_move_1.png"
    0.25
    "images/Portraits/betz/betz_blush_air_move_2.png"
    0.25
    repeat

####################################################################################################
# UPSET
####################################################################################################
### Body
##################################################

layeredimage betz upset:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_wetbeast default:
            "betz_upset_eyes_wetbeast"

        attribute e_closed:
            "images/Portraits/betz/betz_upset_eyes_closed.png"
        
    group mouth: #betz_armup_mouth_neutral
        attribute m_uwu default:
            "betz_upset_mouth_uwu"
        attribute m_uwu_s:
            "betz_upset_mouth_uwu_s"
        attribute m_uwuteeth:
            "betz_upset_mouth_uwuteeth"
        attribute m_uwuteeth_anim:
            "betz_upset_mouth_uwuteeth_anim"
        attribute m_uwuteeth_s:
            "images/Portraits/betz/betz_upset_mouth_wetbeast_C.png"
        attribute m_scream:
            "betz_upset_mouth_scream"

    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_upset_sweat_on.png"

        attribute sweat_off default:
            null

##################################################
### Eyes
##################################################

image betz_upset_eyes_wetbeast:
    "images/Portraits/betz/betz_upset_eyes_wetbeast_1.png"
    pause 0.1
    "images/Portraits/betz/betz_upset_eyes_wetbeast_2.png"
    pause 0.1
    repeat


##################################################
### Mouth
##################################################

image betz_upset_mouth_uwu_talking:
    "images/Portraits/betz/betz_upset_mouth_wetbeast_O.png" #for ah sound
    pause 0.1
    "images/Portraits/betz/betz_upset_mouth_wetbeast_C.png" #for closed mouth
    pause 0.1
    repeat

image betz_upset_mouth_uwu_s:
    "images/Portraits/betz/betz_upset_mouth_uwu_1.png" #for ah sound
    pause 0.1
    "images/Portraits/betz/betz_upset_mouth_uwu_2.png" #for ah sound
    pause 0.1
    repeat

image betz_upset_mouth_uwuteeth_s:
    "images/Portraits/betz/betz_upset_mouth_wetbeast_C.png" #for ah sound
    pause 0.1
    "images/Portraits/betz/betz_upset_mouth_wetbeast_C_2.png" #for ah sound
    pause 0.1
    repeat

image betz_upset_mouth_uwu = ConditionSwitch(
    "betzLipflapping", "betz_upset_mouth_uwu_talking",
    "True", "betz_upset_mouth_uwu_s")

image betz_upset_mouth_uwuteeth = ConditionSwitch(
    "betzLipflapping", "betz_upset_mouth_uwu_talking",
    "True", "images/Portraits/betz/betz_upset_mouth_wetbeast_C.png")

image betz_upset_mouth_uwuteeth_anim = ConditionSwitch(
    "betzLipflapping", "betz_upset_mouth_uwu_talking",
    "True", "betz_upset_mouth_uwuteeth_s")

image betz_upset_mouth_scream = ConditionSwitch(
    "betzLipflapping", "images/Portraits/betz/betz_upset_mouth_wetbeast_O.png",
    "True", "images/Portraits/betz/betz_upset_mouth_wetbeast_C.png")
####################################################################################################
# AMOUR LOOK
####################################################################################################
### Body
##################################################

layeredimage betz alook:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_neutral default:
            "betz_alook_eyes_neutral"

    group mouth: #betz_armup_mouth_neutral
        attribute m_neutral default:
            "betz_alook_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_alook_mouth_neutral_S.png"

##################################################
### Eyes
##################################################

image betz_alook_eyes_neutral:
    "images/Portraits/betz/betz_alook_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_alook_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_alook_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

##################################################
### Mouth
##################################################

image betz_alook_mouth_neutral_talking:
    "images/Portraits/betz/betz_alook_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_alook_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_alook_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_alook_mouth_neutral_S.png"
    pause 0.15
    repeat

image betz_alook_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_alook_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_alook_mouth_neutral_S.png")


####################################################################################################
# LAUGH ENDLESS
####################################################################################################
### Body
##################################################

layeredimage betz laugh_endless:
    group body auto: #betz_armup_body_armup
        attribute body_anim default:
            "betz_laugh_endless_body_updown"

    group face: #betz_armup_eyes_neutral
        attribute face default:
            "betz_laugh_endless_face_neutral"

##################################################
### Body
##################################################

image betz_laugh_endless_body_updown:
    "images/Portraits/betz/betz_coughlaugh_body_up.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_body_down.png"
    0.15  
    repeat  

##################################################
### Eyes
##################################################

image betz_laugh_endless_face_neutral:
    "images/Portraits/betz/betz_coughlaugh_face_up_smile.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_face_down_smile.png"
    0.15  
    repeat 

####################################################################################################
# LAUGH GIGGLE
####################################################################################################
### Body
##################################################

layeredimage betz laugh_giggle:
    group body auto: #betz_armup_body_armup
        attribute body_anim default:
            "betz_laugh_giggle_body_updown"

    group face: #betz_armup_eyes_neutral
        attribute face default:
            "betz_laugh_giggle_face_neutral"

##################################################
### Body
##################################################

image betz_laugh_giggle_body_updown:
    "images/Portraits/betz/betz_coughlaugh_body_up.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_body_down.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_body_up.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_body_down.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_body_up.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_body_down.png"
    0.1 
    "images/Portraits/betz/betz_coughlaugh_body_up.png"
    0.15

##################################################
### Eyes
##################################################

image betz_laugh_giggle_face_neutral:
    "images/Portraits/betz/betz_coughlaugh_face_up_smile.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_face_down_smile.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_face_up_smile.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_face_down_smile.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_face_up_smile.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_face_down_smile.png"
    0.1
    "images/Portraits/betz/betz_coughlaugh_face_up_smile.png"
    0.15

####################################################################################################
# COUGH
####################################################################################################
### Body
##################################################

layeredimage betz cough:
    group body auto: #betz_armup_body_armup
        attribute body_anim default:
            "betz_cough_body_anim"

    group face: #betz_armup_eyes_neutral
        attribute face default:
            "betz_cough_face_anim"

##################################################
### Body
##################################################

image betz_cough_body_anim:
    "images/Portraits/betz/betz_coughlaugh_body_down.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_body_up.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_body_down.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_body_up.png"

##################################################
### Eyes
##################################################

image betz_cough_face_anim:
    "images/Portraits/betz/betz_coughlaugh_face_down_blush.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_face_up_blush.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_face_down_blush.png"
    0.15
    "images/Portraits/betz/betz_coughlaugh_face_up_blush.png"


####################################################################################################
# BETZ CURIOUS
####################################################################################################
### Body
##################################################

layeredimage betz curious:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_neutral default:
            "betz_curious_eyes_neutral"

        attribute e_around:
            "betz_curious_eyes_around"

        attribute e_down:
            "betz_curious_eyes_down"

        attribute e_downangry:
            "betz_curious_eyes_downangry"

        attribute e_vangry:
            "betz_curious_eyes_vangry"

        attribute e_sad:
            "betz_curious_eyes_sad"

        attribute e_closed:
            "images/Portraits/betz/betz_curious_eyes_sad_C.png"

    group mouth: #betz_armup_mouth_neutral
        attribute m_neutral default:
            "betz_curious_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_curious_mouth_neutral_S.png"

        attribute m_smile:
            "betz_curious_mouth_smile"
        attribute m_smile_s:
            "images/Portraits/betz/betz_curious_mouth_smile_S.png"

    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_curious_sweat_on.png"

        attribute sweat_off default:
            null

##################################################
### Eyes
##################################################

image betz_curious_eyes_neutral:
    "images/Portraits/betz/betz_curious_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_curious_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_curious_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_curious_eyes_down:
    "images/Portraits/betz/betz_curious_eyes_down_C.png"
    0.1
    "images/Portraits/betz/betz_curious_eyes_down_OC.png"
    .05
    "images/Portraits/betz/betz_curious_eyes_down_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_curious_eyes_sad:
    "images/Portraits/betz/betz_curious_eyes_sad_C.png"
    0.1
    "images/Portraits/betz/betz_curious_eyes_sad_OC.png"
    .05
    "images/Portraits/betz/betz_curious_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_curious_eyes_downangry:
    "images/Portraits/betz/betz_curious_eyes_downangry_C.png"
    0.1
    "images/Portraits/betz/betz_curious_eyes_downangry_OC.png"
    .05
    "images/Portraits/betz/betz_curious_eyes_downangry_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_curious_eyes_vangry:
    "images/Portraits/betz/betz_curious_eyes_vangry_C.png"
    0.1
    "images/Portraits/betz/betz_curious_eyes_vangry_OC.png"
    .05
    "images/Portraits/betz/betz_curious_eyes_vangry_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_curious_eyes_around:
    "images/Portraits/betz/betz_curious_eyes_neutral_C.png"
    0.1
    choice:
        "images/Portraits/betz/betz_curious_eyes_neutral_OC.png"
        .05
        "images/Portraits/betz/betz_curious_eyes_neutral_O.png"
    choice:
        "images/Portraits/betz/betz_curious_eyes_neutral_OC_side.png"
        .05
        "images/Portraits/betz/betz_curious_eyes_neutral_O_side.png"
    pause 0.001
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat
##################################################
### Mouth
##################################################

image betz_curious_mouth_neutral_talking:
    "images/Portraits/betz/betz_curious_mouth_neutral_T.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_curious_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    repeat

image betz_curious_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_curious_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_curious_mouth_neutral_S.png")

image betz_curious_mouth_smile_talking:
    "images/Portraits/betz/betz_curious_mouth_neutral_T.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_curious_mouth_smile_S.png" #for closed mouth
    pause 0.15
    repeat

image betz_curious_mouth_smile = ConditionSwitch(
    "betzLipflapping", "betz_curious_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_curious_mouth_smile_S.png")

####################################################################################################
# HIDING
####################################################################################################
### Body
##################################################

layeredimage betz hiding:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_sad default:
            "betz_hiding_eyes_sad"
        
    group mouth: #betz_armup_mouth_neutral
        attribute m_neutral default:
            "betz_hiding_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_hiding_mouth_neutral_S.png"

##################################################
### Eyes
##################################################

image betz_hiding_eyes_sad:
    "images/Portraits/betz/betz_hiding_eyes_sad_C.png"
    0.1
    "images/Portraits/betz/betz_hiding_eyes_sad_OC.png"
    .05
    "images/Portraits/betz/betz_hiding_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat


##################################################
### Mouth
##################################################

image betz_hiding_mouth_neutral_talking:
    "images/Portraits/betz/betz_hiding_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_hiding_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_hiding_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_hiding_mouth_neutral_S.png"
    pause 0.15
    repeat

image betz_hiding_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_hiding_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_hiding_mouth_neutral_S.png")


####################################################################################################
# BASHFUL
####################################################################################################
### Body
##################################################

layeredimage betz bashful:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_neutral default:
            "betz_bashful_eyes_neutral"

        attribute e_around:
            "betz_bashful_eyes_around"

        attribute e_looking:
            "betz_bashful_eyes_looking"

        attribute e_horror:
            "betz_bashful_eyes_horror"

        attribute e_horrorstatic:
            "betz_bashful_eyes_horrorstatic"

        attribute e_ssad:
            "betz_bashful_eyes_ssad"

    group mouth: #betz_armup_mouth_neutral
        attribute m_neutral default:
            "betz_bashful_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_bashful_mouth_neutral_S.png"

        attribute m_sad:
            "betz_bashful_mouth_sad"
        attribute m_sad_s:
            "images/Portraits/betz/betz_bashful_mouth_sad_S.png"

    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_bashful_sweat_on.png"

        attribute supersweat_on:
            "images/Portraits/betz/betz_bashful_supersweat_on.png"

        attribute sweat_off default:
            null
##################################################
### Eyes
##################################################

image betz_bashful_eyes_neutral:
    "images/Portraits/betz/betz_bashful_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_bashful_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_bashful_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_bashful_eyes_looking:
    "images/Portraits/betz/betz_bashful_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_bashful_eyes_looking_OC.png"
    .05
    "images/Portraits/betz/betz_bashful_eyes_looking_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_bashful_eyes_around:
    "images/Portraits/betz/betz_bashful_eyes_neutral_C.png"
    0.1
    choice:
        "images/Portraits/betz/betz_bashful_eyes_neutral_OC.png"
        .05
        "images/Portraits/betz/betz_bashful_eyes_neutral_O.png"
    choice:
        "images/Portraits/betz/betz_bashful_eyes_looking_OC.png"
        .05
        "images/Portraits/betz/betz_bashful_eyes_looking_O.png"
    pause 0.001
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_bashful_eyes_horror:
    "images/Portraits/betz/betz_bashful_eyes_horror_C.png"
    0.1
    choice:
        "images/Portraits/betz/betz_bashful_eyes_horror2_OC.png"
        .05
        "images/Portraits/betz/betz_bashful_eyes_horror2_O.png"
    choice:
        "images/Portraits/betz/betz_bashful_eyes_horror_OC.png"
        .05
        "images/Portraits/betz/betz_bashful_eyes_horror_O.png"
    pause 0.001
    choice:
        1.0
    choice:
        0.5
    choice:
        0.0
    repeat

image betz_bashful_eyes_horrorstatic:
    "images/Portraits/betz/betz_bashful_eyes_horror_C.png"
    0.1
    "images/Portraits/betz/betz_bashful_eyes_horror_OC.png"
    .05
    "images/Portraits/betz/betz_bashful_eyes_horror_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    repeat

image betz_bashful_eyes_ssad:
    "images/Portraits/betz/betz_bashful_eyes_ssad_C.png"
    0.1
    "images/Portraits/betz/betz_bashful_eyes_ssad_OC.png"
    .05
    "images/Portraits/betz/betz_bashful_eyes_ssad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

##################################################
### Mouth
##################################################

image betz_bashful_mouth_neutral_talking:
    "images/Portraits/betz/betz_bashful_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_bashful_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_bashful_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_bashful_mouth_neutral_S.png"
    pause 0.15
    repeat

image betz_bashful_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_bashful_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_bashful_mouth_neutral_S.png")

image betz_bashful_mouth_sad_talking:
    "images/Portraits/betz/betz_bashful_mouth_sad_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_bashful_mouth_sad_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_bashful_mouth_sad_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_bashful_mouth_sad_S.png"
    pause 0.15
    repeat

image betz_bashful_mouth_sad = ConditionSwitch(
    "betzLipflapping", "betz_bashful_mouth_sad_talking",
    "True", "images/Portraits/betz/betz_bashful_mouth_sad_S.png")

##############################################################################################################################################################################################
# MEETING BETZ
##################################################
### Body
##################################################

layeredimage betz meetingbetz:
    group body auto: #betz_armsup_body
        attribute base default

    group eyes: #betz_armsup_eyes_neutral
        attribute e_neutral default:
            "betz_meetingbetz_eyes_neutral"

        attribute e_smile:
            "betz_meetingbetz_eyes_smile"

        attribute e_sad:
            "betz_meetingbetz_eyes_sad"
        
    group mouth: #betz_armsup_mouth_neutral
        attribute m_neutral default:
            "betz_meetingbetz_mouth_neutral"
        attribute m_neutral_s:
            "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_S.png"

        attribute m_smile:
            "betz_meetingbetz_mouth_smile"
        attribute m_neutral_s:
            "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_smile_S.png"

        attribute m_sad:
            "betz_meetingbetz_mouth_sad"
        attribute m_sad_s:
            "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_sad_S.png"
##################################################
### Eyes
##################################################

image betz_meetingbetz_eyes_neutral:
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_neutral_C.png"
    0.1
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_neutral_OC.png"
    .05
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_meetingbetz_eyes_smile:
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_neutral_C.png"
    0.1
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_neutral_OC.png"
    .05
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_smile_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_meetingbetz_eyes_sad:
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_sad_C.png"
    0.1
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_sad_OC.png"
    .05
    "images/CGs/Day2_Meeting Betz/betz_meetingbetz_eyes_sad_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat
##################################################
### Mouth
##################################################

image betz_meetingbetz_mouthtalking_neutral:
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_TA.png" #for ah sound
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_S.png" #for closed mouth
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_TO.png" #for oh sound
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_S.png"
        pause 0.15
        repeat

image betz_meetingbetz_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_meetingbetz_mouthtalking_neutral",
    "True", "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_S.png")


image betz_meetingbetz_mouthtalking_smile:
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_smile_TA.png" #for ah sound
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_smile_S.png" #for closed mouth
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_smile_TO.png" #for oh sound
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_smile_S.png"
        pause 0.15
        repeat

image betz_meetingbetz_mouth_smile = ConditionSwitch(
    "betzLipflapping", "betz_meetingbetz_mouthtalking_smile",
    "True", "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_smile_S.png")


image betz_meetingbetz_mouthtalking_sad:
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_TA.png" #for ah sound
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_sad_S.png" #for closed mouth
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_neutral_TO.png" #for oh sound
        pause 0.15
        "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_sad_S.png"
        pause 0.15
        repeat

image betz_meetingbetz_mouth_sad = ConditionSwitch(
    "betzLipflapping", "betz_meetingbetz_mouthtalking_sad",
    "True", "images/CGs/Day2_Meeting Betz/betz_meetingbetz_mouth_sad_S.png")

##############################################################################################################################################################################################
# IN HANDS
##################################################
### Body
##################################################

layeredimage betz inhands:
    group body:
        attribute talking default:
            "betz_inhands_body_talking"

        attribute silent:
            "images/Portraits/betz/betz_inhands_2.png"

##################################################
### Eyes
##################################################

image betz_inhands_body_talkingtalk:
    "images/Portraits/betz/betz_inhands_1.png"
    0.15
    "images/Portraits/betz/betz_inhands_2.png"
    .15
    repeat

image betz_inhands_body_talking = ConditionSwitch(
    "betzLipflapping", "betz_inhands_body_talkingtalk",
    "True", "images/Portraits/betz/betz_inhands_2.png")

##############################################################################################################################################################################################
# WAKE UP DAY 3
##################################################
### Body
##################################################

layeredimage betz d3wake:
    group body auto: #betz_armsup_body
        attribute base default

    group eyes: #betz_armsup_eyes_neutral
        attribute e_neutral default:
            "betz_d3wake_eyes"
        
    group mouth: #betz_armsup_mouth_neutral
        attribute m_3 default:
            "betz_d3wake_mouth"
        attribute m_3_s:
            "images/CGs/Day3_WakeUp/betz_armsup_mouth_neutral_S.png"

##################################################
### Eyes
##################################################

image betz_d3wake_eyes:
    "images/CGs/Day3_WakeUp/betz_d3wake_eyes_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/CGs/Day3_WakeUp/betz_d3wake_eyes_C.png"
    0.1
    "images/CGs/Day3_WakeUp/betz_d3wake_eyes_OC.png"
    .1
    repeat


##################################################
### Mouth
##################################################

image betz_d3wake_mouthtalking:
        "images/CGs/Day3_WakeUp/betz_d3wake_mouth_TA.png" #for ah sound
        pause 0.15
        "images/CGs/Day3_WakeUp/betz_d3wake_mouth_S.png" #for closed mouth
        pause 0.15
        "images/CGs/Day3_WakeUp/betz_d3wake_mouth_TO.png" #for oh sound
        pause 0.15
        "images/CGs/Day3_WakeUp/betz_d3wake_mouth_S.png"
        pause 0.15
        repeat

image betz_d3wake_mouth = ConditionSwitch(
    "betzLipflapping", "betz_d3wake_mouthtalking",
    "True", "images/CGs/Day3_WakeUp/betz_d3wake_mouth_S.png")

####################################################################################################
# ATALK
####################################################################################################
### Body
##################################################

layeredimage betz atalk:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_neutral default:
            "betz_atalk_eyes_neutral"
        attribute e_frown:
            "betz_atalk_eyes_frown"
        attribute e_anger:
            "betz_atalk_eyes_anger"
        attribute e_hm:
            "betz_atalk_eyes_hm"
        attribute e_ugh:
            "betz_atalk_eyes_ugh"
        attribute e_sneutral:
            "betz_atalk_eyes_sneutral"
        attribute e_sgentle:
            "betz_atalk_eyes_sgentle"
        attribute e_sworried:
            "betz_atalk_eyes_sworried"


    group mouth: #betz_armup_mouth_neutral
        attribute m_neutral default:
            "betz_atalk_mouth_neutral"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_atalk_mouth_neutral_S.png"

        attribute m_smile:
            "betz_atalk_mouth_smile"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_atalk_mouth_smile_S.png"

        attribute m_wide:
            "betz_atalk_mouth_wide"
        attribute m_neutral_s:
            "images/Portraits/betz/betz_atalk_mouth_wide_S.png"

        attribute m_chat:
            "betz_atalk_mouth_chat"

    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_atalk_sweat_on.png"

        attribute sweat_off default:
            null
##################################################
### Eyes
##################################################

image betz_atalk_eyes_neutral:
    "images/Portraits/betz/betz_atalk_eyes_neutral_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_neutral_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_neutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_atalk_eyes_frown:
    "images/Portraits/betz/betz_atalk_eyes_frown_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_frown_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_frown_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_atalk_eyes_anger:
    "images/Portraits/betz/betz_atalk_eyes_anger_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_anger_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_anger_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_atalk_eyes_hm:
    "images/Portraits/betz/betz_atalk_eyes_hm_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_hm_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_hm_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_atalk_eyes_ugh:
    "images/Portraits/betz/betz_atalk_eyes_ugh_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_ugh_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_ugh_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_atalk_eyes_sgentle:
    "images/Portraits/betz/betz_atalk_eyes_sgentle_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_sgentle_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_sgentle_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_atalk_eyes_sneutral:
    "images/Portraits/betz/betz_atalk_eyes_sneutral_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_sneutral_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_sneutral_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_atalk_eyes_sworried:
    "images/Portraits/betz/betz_atalk_eyes_sworried_C.png"
    0.1
    "images/Portraits/betz/betz_atalk_eyes_sworried_OC.png"
    .05
    "images/Portraits/betz/betz_atalk_eyes_sworried_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat
##################################################
### Mouth
##################################################

image betz_atalk_mouth_neutral_talking:
    "images/Portraits/betz/betz_atalk_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_S.png"
    pause 0.15
    repeat

image betz_atalk_mouth_neutral = ConditionSwitch(
    "betzLipflapping", "betz_atalk_mouth_neutral_talking",
    "True", "images/Portraits/betz/betz_atalk_mouth_neutral_S.png")


image betz_atalk_mouth_smile_talking:
    "images/Portraits/betz/betz_atalk_mouth_smile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_smile_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_smile_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_smile_S.png"
    pause 0.15
    repeat

image betz_atalk_mouth_smile = ConditionSwitch(
    "betzLipflapping", "betz_atalk_mouth_smile_talking",
    "True", "images/Portraits/betz/betz_atalk_mouth_smile_S.png")

image betz_atalk_mouth_wide_talking:
    "images/Portraits/betz/betz_atalk_mouth_wide_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_wide_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_wide_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_wide_S.png"
    pause 0.15
    repeat

image betz_atalk_mouth_wide = ConditionSwitch(
    "betzLipflapping", "betz_atalk_mouth_wide_talking",
    "True", "images/Portraits/betz/betz_atalk_mouth_wide_S.png")

image betz_atalk_mouth_chat:
    "images/Portraits/betz/betz_atalk_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_S.png"
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_atalk_mouth_neutral_S.png"
    pause 0.15
    pause 1.5
    repeat
####################################################################################################
# AANGRY
####################################################################################################
### Body
##################################################

layeredimage betz aangry:
    group body auto: #betz_armup_body_armup
        attribute base default

    group eyes: #betz_armup_eyes_neutral
        attribute e_angry default:
            "betz_aangry_eyes_anger"
        attribute e_squint:
            "betz_aangry_eyes_squint"
        attribute e_angy:
            "betz_aangry_eyes_angy"
        attribute e_sangy:
            "betz_aangry_eyes_sangy"
        attribute e_closed:
            "images/Portraits/betz/betz_aangry_eyes_squint_C.png"
    group mouth: #betz_armup_mouth_neutral
        attribute m_angry default:
            "betz_aangry_mouth_angry"
        attribute m_angry_s:
            "images/Portraits/betz/betz_aangry_mouth_angry_S.png"

        attribute m_smile:
            "betz_aangry_mouth_smile"
        attribute m_smile_s:
            "images/Portraits/betz/betz_aangry_mouth_smile_S.png"

        attribute m_hmf:
            "betz_aangry_mouth_hmf"
        attribute m_smile_s:
            "images/Portraits/betz/betz_aangry_mouth_hmf_S.png"

    group sweat:
        attribute sweat_on:
            "images/Portraits/betz/betz_aangry_sweat_on.png"

        attribute sweat_off default:
            null
##################################################
### Eyes
##################################################

image betz_aangry_eyes_anger:
    "images/Portraits/betz/betz_aangry_eyes_squint_C.png"
    0.1
    "images/Portraits/betz/betz_aangry_eyes_squint_OC.png"
    .05
    "images/Portraits/betz/betz_aangry_eyes_angry_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_aangry_eyes_squint:
    "images/Portraits/betz/betz_aangry_eyes_squint_C.png"
    0.1
    "images/Portraits/betz/betz_aangry_eyes_squint_OC.png"
    .05
    "images/Portraits/betz/betz_aangry_eyes_squint_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_aangry_eyes_angy:
    "images/Portraits/betz/betz_aangry_eyes_squint_C.png"
    0.1
    "images/Portraits/betz/betz_aangry_eyes_squint_OC.png"
    .05
    "images/Portraits/betz/betz_aangry_eyes_angy_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat

image betz_aangry_eyes_sangy:
    "images/Portraits/betz/betz_aangry_eyes_sangy_C.png"
    0.1
    "images/Portraits/betz/betz_aangry_eyes_sangy_OC.png"
    .05
    "images/Portraits/betz/betz_aangry_eyes_sangy_O.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    choice:
        0.0
    repeat
##################################################
### Mouth
##################################################

image betz_aangry_mouth_angry_talking:
    "images/Portraits/betz/betz_aangry_mouth_angry_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_aangry_mouth_angry_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_aangry_mouth_angry_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_aangry_mouth_angry_S.png"
    pause 0.15
    repeat

image betz_aangry_mouth_angry = ConditionSwitch(
    "betzLipflapping", "betz_aangry_mouth_angry_talking",
    "True", "images/Portraits/betz/betz_aangry_mouth_angry_S.png")

image betz_aangry_mouth_smile_talking:
    "images/Portraits/betz/betz_aangry_mouth_smile_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_aangry_mouth_smile_S.png" #for closed mouth
    pause 0.15
    repeat

image betz_aangry_mouth_smile = ConditionSwitch(
    "betzLipflapping", "betz_aangry_mouth_smile_talking",
    "True", "images/Portraits/betz/betz_aangry_mouth_smile_S.png")

image betz_aangry_mouth_hmf_talking:
    "images/Portraits/betz/betz_aangry_mouth_hmf_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/betz/betz_aangry_mouth_hmf_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/betz/betz_aangry_mouth_hmf_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/betz/betz_aangry_mouth_hmf_S.png"
    pause 0.15
    repeat

image betz_aangry_mouth_hmf = ConditionSwitch(
    "betzLipflapping", "betz_aangry_mouth_hmf_talking",
    "True", "images/Portraits/betz/betz_aangry_mouth_hmf_S.png")