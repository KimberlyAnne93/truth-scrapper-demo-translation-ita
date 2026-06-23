##################################################
### Body
##################################################

layeredimage amour armsup:
    group body auto: #amour_armsup_body
        attribute base default

    group eyes: #amour_armsup_eyes_neutral
        attribute e_neutral default:
            "amour_armsup_eyes_neutral"

        attribute e_neutral_closed:
            "images/Portraits/amour/amour_armsup_eyes_neutral_C.png"

        attribute e_angry:
            "amour_armsup_eyes_angry"

        attribute e_surprised:
            "amour_armsup_eyes_surprised"

        attribute e_sad:
            "amour_armsup_eyes_sad"
        
    group mouth: #amour_armsup_mouth_neutral
        attribute m_3 default:
            "amour_armsup_mouth_neutral"
        attribute m_3_s:
            "images/Portraits/amour/amour_armsup_mouth_neutral_S.png"

        attribute m_o:
            "amour_armsup_mouth_o"
        attribute m_o_s:
            "images/Portraits/amour/amour_armsup_mouth_o_S.png"

        attribute m_oend:
            "amour_armsup_mouth_oend"
        attribute m_oend_s:
            "images/Portraits/amour/amour_armsup_mouth_o_T.png"

        attribute m_flat:
            "amour_armsup_mouth_flat"
        attribute m_flat_s:
            "images/Portraits/amour/amour_armsup_mouth_flat_S.png"

        attribute m_sad:
            "amour_armsup_mouth_sad"
        attribute m_sad_s:
            "images/Portraits/amour/amour_armsup_mouth_sad_S.png"

##################################################
### Eyes
##################################################

image amour_armsup_eyes_neutral:
    "images/Portraits/amour/amour_armsup_eyes_neutral_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_armsup_eyes_neutral_C.png"
    0.1
    "images/Portraits/amour/amour_armsup_eyes_neutral_OC.png"
    .1
    repeat

image amour_armsup_eyes_surprised:
    "images/Portraits/amour/amour_armsup_eyes_surprised_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_armsup_eyes_surprised_C.png"
    0.1
    "images/Portraits/amour/amour_armsup_eyes_surprised_OC.png"
    .1
    repeat

image amour_armsup_eyes_angry:
    "images/Portraits/amour/amour_armsup_eyes_angry_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_armsup_eyes_angry_C.png"
    0.1
    "images/Portraits/amour/amour_armsup_eyes_angry_OC.png"
    .1
    repeat

image amour_armsup_eyes_sad:
    "images/Portraits/amour/amour_armsup_eyes_sad_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_armsup_eyes_sad_C.png"
    0.1
    "images/Portraits/amour/amour_armsup_eyes_sad_OC.png"
    .1
    repeat

##################################################
### Mouth
##################################################

image amour_armsup_mouth_neutral_talking:
        "images/Portraits/amour/amour_armsup_mouth_neutral_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_neutral_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_neutral_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_neutral_S.png"
        pause 0.15
        repeat

image amour_armsup_mouth_neutral = ConditionSwitch(
    "amourLipflapping", "amour_armsup_mouth_neutral_talking",
    "True", "images/Portraits/amour/amour_armsup_mouth_neutral_S.png")

####################

image amour_armsup_mouth_flat_talking:
        "images/Portraits/amour/amour_armsup_mouth_flat_TA.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_flat_S.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_flat_TO.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_flat_S.png"
        pause 0.15
        repeat

image amour_armsup_mouth_flat = ConditionSwitch(
    "amourLipflapping", "amour_armsup_mouth_flat_talking",
    "True", "images/Portraits/amour/amour_armsup_mouth_flat_S.png")

####################

image amour_armsup_mouth_o_talking:
        "images/Portraits/amour/amour_armsup_mouth_o_T.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_o_S.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_flat_TO.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_o_S.png"
        pause 0.15
        repeat

image amour_armsup_mouth_o = ConditionSwitch(
    "amourLipflapping", "amour_armsup_mouth_o_talking",
    "True", "images/Portraits/amour/amour_armsup_mouth_o_S.png")

image amour_armsup_mouth_oend = ConditionSwitch(
    "amourLipflapping", "amour_armsup_mouth_o_talking",
    "True", "images/Portraits/amour/amour_armsup_mouth_o_T.png")


image amour_armsup_mouth_sad_talking:
        "images/Portraits/amour/amour_armsup_mouth_flat_TA.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_sad_S.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_flat_TO.png" 
        pause 0.15
        "images/Portraits/amour/amour_armsup_mouth_sad_S.png"
        pause 0.15
        repeat

image amour_armsup_mouth_sad = ConditionSwitch(
    "amourLipflapping", "amour_armsup_mouth_sad_talking",
    "True", "images/Portraits/amour/amour_armsup_mouth_sad_S.png")

##############################################################################################################################################################################################
# CALL SAUL
##################################################
### Body
##################################################

layeredimage amour callsaul:
    group body auto: #amour_armsup_body
        attribute base default
        attribute pajamas

    group eyes: #amour_armsup_eyes_neutral
        attribute e_neutral default:
            "amour_callsaul_eyes_neutral"

        attribute e_angry:
            "amour_callsaul_eyes_angry"

        attribute e_surprised:
            "amour_callsaul_eyes_surprised"

        
    group mouth: #amour_armsup_mouth_neutral
        attribute m_3 default:
            "amour_callsaul_mouth_smiling"
        attribute m_3_s:
            "images/Portraits/amour/amour_callsaul_mouth_smiling_S.png"

        attribute m_o:
            "amour_callsaul_mouth_o"
        attribute m_o_s:
            "images/Portraits/amour/amour_callsaul_mouth_o_S.png"
        attribute m_oend:
            "amour_callsaul_mouth_oend"

        attribute m_buh:
            "amour_callsaul_mouth_buh"
        attribute m_buh_s:
            "images/Portraits/amour/amour_callsaul_mouth_buh_S.png"


##################################################
### Eyes
##################################################

image amour_callsaul_eyes_neutral:
    "images/Portraits/amour/amour_callsaul_eyes_neutral_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_callsaul_eyes_neutral_C.png"
    0.1
    "images/Portraits/amour/amour_callsaul_eyes_neutral_OC.png"
    .1
    repeat

image amour_callsaul_eyes_angry:
    "images/Portraits/amour/amour_callsaul_eyes_angry_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_callsaul_eyes_angry_C.png"
    0.1
    "images/Portraits/amour/amour_callsaul_eyes_angry_OC.png"
    .1
    repeat

image amour_callsaul_eyes_surprised:
    "images/Portraits/amour/amour_callsaul_eyes_surprised_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_callsaul_eyes_surprised_C.png"
    0.1
    "images/Portraits/amour/amour_callsaul_eyes_surprised_OC.png"
    .1
    repeat

##################################################
### Mouth
##################################################

image amour_callsaul_mouth_smiling_talking:
        "images/Portraits/amour/amour_callsaul_mouth_smiling_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_callsaul_mouth_smiling_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_callsaul_mouth_smiling_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_callsaul_mouth_smiling_S.png"
        pause 0.15
        repeat

image amour_callsaul_mouth_smiling = ConditionSwitch(
    "amourLipflapping", "amour_callsaul_mouth_smiling_talking",
    "True", "images/Portraits/amour/amour_callsaul_mouth_smiling_S.png")

####################

image amour_callsaul_mouth_o_talking:
        "images/Portraits/amour/amour_callsaul_mouth_o_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_callsaul_mouth_o_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_callsaul_mouth_o_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_callsaul_mouth_o_S.png"
        pause 0.15
        repeat

image amour_callsaul_mouth_o = ConditionSwitch(
    "amourLipflapping", "amour_callsaul_mouth_o_talking",
    "True", "images/Portraits/amour/amour_callsaul_mouth_o_S.png")

image amour_callsaul_mouth_oend = ConditionSwitch(
    "amourLipflapping", "amour_callsaul_mouth_o_talking",
    "True", "images/Portraits/amour/amour_callsaul_mouth_o_TA.png")

####################

image amour_callsaul_mouth_buh_talking:
        "images/Portraits/amour/amour_callsaul_mouth_buh_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_callsaul_mouth_buh_T.png" #for oh sound
        pause 0.15
        repeat

image amour_callsaul_mouth_buh = ConditionSwitch(
    "amourLipflapping", "amour_callsaul_mouth_buh_talking",
    "True", "images/Portraits/amour/amour_callsaul_mouth_buh_S.png")



##############################################################################################################################################################################################
# LOOKUP
##################################################
### Body
##################################################

layeredimage amour lookup:
    group body auto: #amour_armsup_body
        attribute base default

    group eyes: #amour_armsup_eyes_neutral
        attribute e_hm default:
            "amour_lookup_eyes_hm"
        
    group mouth: #amour_armsup_mouth_neutral
        attribute m_hm default:
            "amour_lookup_mouth_hm"
        attribute m_hm_s:
            "images/Portraits/amour/amour_lookup_mouth_hm_S.png"

        attribute m_blep:
            "amour_lookup_mouth_blep"
        attribute m_blep_s:
            "images/Portraits/amour/amour_lookup_mouth_blep_S.png"

##################################################
### Eyes
##################################################

image amour_lookup_eyes_hm:
    "images/Portraits/amour/amour_lookup_eyes_hm_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_lookup_eyes_hm_C.png"
    0.1
    "images/Portraits/amour/amour_lookup_eyes_hm_OC.png"
    .1
    repeat

##################################################
### Mouth
##################################################

image amour_lookup_mouth_hm_talking:
        "images/Portraits/amour/amour_lookup_mouth_hm_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_lookup_mouth_hm_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_lookup_mouth_hm_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_lookup_mouth_hm_S.png"
        pause 0.15
        repeat

image amour_lookup_mouth_hm = ConditionSwitch(
    "amourLipflapping", "amour_lookup_mouth_hm_talking",
    "True", "images/Portraits/amour/amour_lookup_mouth_hm_S.png")


image amour_lookup_mouth_blep = ConditionSwitch(
    "amourLipflapping", "amour_lookup_mouth_hm_talking",
    "True", "images/Portraits/amour/amour_lookup_mouth_blep_S.png")

##############################################################################################################################################################################################
# SIDE
##################################################
### Body
##################################################

layeredimage amour side:
    group body auto: #amour_armsup_body
        attribute base default

    group eyes: #amour_armsup_eyes_neutral
        attribute e_neutral default:
            "amour_side_eyes_neutral"

        attribute e_hm:
            "amour_side_eyes_hm"

        attribute e_frown:
            "amour_side_eyes_frown"

        attribute e_surprised:
            "amour_side_eyes_surprised" 

        attribute e_sad:
            "amour_side_eyes_sad"           
        
    group mouth: #amour_armsup_mouth_neutral
        attribute m_3 default:
            "amour_side_mouth_neutral"
        attribute m_3_s:
            "images/Portraits/amour/amour_side_mouth_neutral_S.png"
        attribute m_3_open:
            "images/Portraits/amour/amour_side_mouth_neutral_TA.png"

        attribute m_eh:
            "amour_side_mouth_eh"
        attribute m_eh_s:
            "images/Portraits/amour/amour_side_mouth_eh_S.png"

        attribute m_oh:
            "amour_side_mouth_eh"
        attribute m_oh_s:
            "images/Portraits/amour/amour_side_mouth_eh_S.png"

        attribute m_sad:
            "amour_side_mouth_sad"
        attribute m_sad_s:
            "images/Portraits/amour/amour_side_mouth_sad_S.png"

        attribute m_chat:
            "amour_side_mouth_chat"
##################################################
### Eyes
##################################################

image amour_side_eyes_hm:
    "images/Portraits/amour/amour_side_eyes_hm_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_side_eyes_hm_C.png"
    0.1
    "images/Portraits/amour/amour_side_eyes_hm_OC.png"
    .1
    repeat

image amour_side_eyes_neutral:
    "images/Portraits/amour/amour_side_eyes_neutral_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_side_eyes_neutral_C.png"
    0.1
    "images/Portraits/amour/amour_side_eyes_neutral_OC.png"
    .1
    repeat

image amour_side_eyes_surprised:
    "images/Portraits/amour/amour_side_eyes_surprised_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_side_eyes_neutral_C.png"
    0.1
    "images/Portraits/amour/amour_side_eyes_surprised_OC.png"
    .1
    repeat

image amour_side_eyes_frown:
    "images/Portraits/amour/amour_side_eyes_frown_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_side_eyes_frown_C.png"
    0.1
    "images/Portraits/amour/amour_side_eyes_frown_OC.png"
    .1
    repeat

image amour_side_eyes_sad:
    "images/Portraits/amour/amour_side_eyes_sad_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/Portraits/amour/amour_side_eyes_sad_C.png"
    0.1
    "images/Portraits/amour/amour_side_eyes_sad_OC.png"
    .1
    repeat
##################################################
### Mouth
##################################################

image amour_side_mouth_neutral_talking:
        "images/Portraits/amour/amour_side_mouth_neutral_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_neutral_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_neutral_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_neutral_S.png"
        pause 0.15
        repeat

image amour_side_mouth_neutral = ConditionSwitch(
    "amourLipflapping", "amour_side_mouth_neutral_talking",
    "True", "images/Portraits/amour/amour_side_mouth_neutral_S.png")


image amour_side_mouth_eh_talking:
        "images/Portraits/amour/amour_side_mouth_eh_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_eh_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_eh_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_eh_S.png"
        pause 0.15
        repeat

image amour_side_mouth_eh = ConditionSwitch(
    "amourLipflapping", "amour_side_mouth_eh_talking",
    "True", "images/Portraits/amour/amour_side_mouth_eh_S.png")

image amour_side_mouth_oh_talking:
        "images/Portraits/amour/amour_side_mouth_eh_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_eh_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_oh_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_eh_S.png"
        pause 0.15
        repeat

image amour_side_mouth_oh = ConditionSwitch(
    "amourLipflapping", "amour_side_mouth_oh_talking",
    "True", "images/Portraits/amour/amour_side_mouth_eh_S.png")

image amour_side_mouth_chat:
    "images/Portraits/amour/amour_side_mouth_neutral_S.png"
    pause 1.5
    "images/Portraits/amour/amour_side_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/amour/amour_side_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/amour/amour_side_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/amour/amour_side_mouth_neutral_S.png"
    pause 0.15
    "images/Portraits/amour/amour_side_mouth_neutral_TA.png" #for ah sound
    pause 0.15
    "images/Portraits/amour/amour_side_mouth_neutral_S.png" #for closed mouth
    pause 0.15
    "images/Portraits/amour/amour_side_mouth_neutral_TO.png" #for oh sound
    pause 0.15
    "images/Portraits/amour/amour_side_mouth_neutral_S.png"
    pause 0.15
    repeat

image amour_side_mouth_sad_talking:
        "images/Portraits/amour/amour_side_mouth_eh_TA.png" #for ah sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_sad_S.png" #for closed mouth
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_eh_TO.png" #for oh sound
        pause 0.15
        "images/Portraits/amour/amour_side_mouth_sad_S.png"
        pause 0.15
        repeat

image amour_side_mouth_sad = ConditionSwitch(
    "amourLipflapping", "amour_side_mouth_sad_talking",
    "True", "images/Portraits/amour/amour_side_mouth_sad_S.png")




##############################################################################################################################################################################################
# LAUGHING
##################################################
### Body
##################################################

image amour laughing:
    "images/Portraits/amour/amour_laughing_down.png"
    .2
    "images/Portraits/amour/amour_laughing_up.png"
    .2
    repeat

##############################################################################################################################################################################################
# MEETING AMOUR
##################################################
### Body
##################################################

layeredimage amour meetingamour:
    group body auto: #amour_armsup_body
        attribute base default

    group eyes: #amour_armsup_eyes_neutral
        attribute e_neutral default:
            "amour_meetingamour_eyes"
        
    group mouth: #amour_armsup_mouth_neutral
        attribute m_3 default:
            "amour_meetingamour_mouth"
        attribute m_3_s:
            "images/Portraits/amour/amour_armsup_mouth_neutral_S.png"

##################################################
### Eyes
##################################################

image amour_meetingamour_eyes:
    "images/CGs/Day1_Meeting Amour/amour_meetingamour_eyes_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/CGs/Day1_Meeting Amour/amour_meetingamour_eyes_C.png"
    0.1
    "images/CGs/Day1_Meeting Amour/amour_meetingamour_eyes_OC.png"
    .1
    repeat


##################################################
### Mouth
##################################################

image amour_meetingamour_mouthtalking:
        "images/CGs/Day1_Meeting Amour/amour_meetingamour_mouth_TA.png" #for ah sound
        pause 0.15
        "images/CGs/Day1_Meeting Amour/amour_meetingamour_mouth_S.png" #for closed mouth
        pause 0.15
        "images/CGs/Day1_Meeting Amour/amour_meetingamour_mouth_TO.png" #for oh sound
        pause 0.15
        "images/CGs/Day1_Meeting Amour/amour_meetingamour_mouth_S.png"
        pause 0.15
        repeat

image amour_meetingamour_mouth = ConditionSwitch(
    "amourLipflapping", "amour_meetingamour_mouthtalking",
    "True", "images/CGs/Day1_Meeting Amour/amour_meetingamour_mouth_S.png")

##############################################################################################################################################################################################
# WAKE UP DAY 3
##################################################
### Body
##################################################

layeredimage amour d3wake:
    group body auto: #amour_armsup_body
        attribute base default

    group eyes: #amour_armsup_eyes_neutral
        attribute e_neutral default:
            "amour_d3wake_eyes"
        
    group mouth: #amour_armsup_mouth_neutral
        attribute m_3 default:
            "amour_d3wake_mouth"
        attribute m_3_s:
            "images/CGs/Day3_WakeUp/amour_d3wake_mouth_S.png"

##################################################
### Eyes
##################################################

image amour_d3wake_eyes:
    "images/CGs/Day3_WakeUp/amour_d3wake_eyes_O.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        2.5
    "images/CGs/Day3_WakeUp/amour_d3wake_eyes_C.png"
    0.1
    "images/CGs/Day3_WakeUp/amour_d3wake_eyes_OC.png"
    .1
    repeat


##################################################
### Mouth
##################################################

image amour_d3wake_mouthtalking:
        "images/CGs/Day3_WakeUp/amour_d3wake_mouth_TA.png" #for ah sound
        pause 0.15
        "images/CGs/Day3_WakeUp/amour_d3wake_mouth_S.png" #for closed mouth
        pause 0.15
        "images/CGs/Day3_WakeUp/amour_d3wake_mouth_TO.png" #for oh sound
        pause 0.15
        "images/CGs/Day3_WakeUp/amour_d3wake_mouth_S.png"
        pause 0.15
        repeat

image amour_d3wake_mouth = ConditionSwitch(
    "amourLipflapping", "amour_d3wake_mouthtalking",
    "True", "images/CGs/Day3_WakeUp/amour_d3wake_mouth_S.png")