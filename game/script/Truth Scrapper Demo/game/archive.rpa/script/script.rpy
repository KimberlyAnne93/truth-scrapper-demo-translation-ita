# The script of the game goes in this file.

##################################################
## ALL THE DANG STORY BASED VARIABLES
##################################################
### Story Stuff
#idk what this is for lol
default DisablePageFlip = False
#can you use PaC or no
default IsPaCDisabled = True
default TurnOffReturn = False

default WhichPaC = "0"
default pointnclickbuttons_order = "0"

default amourname = "???"    
default betzname = "???"

default info_narra_start = "{color=#193D23}"
default info_dialogue_start = "{color=#193D23}"
default info_end = "{/color}"

default temptext = ""

default objectname = ""

default persistent.firstplaythroughdone = False

default persistent.stats_smell_end = False
default persistent.stats_sight_end = False
default persistent.stats_hearing_end = False

default persistent.stats_str_end = False
default persistent.stats_int_end = False
default persistent.stats_psy_end = False

default persistent.stats_amour_end = False
default persistent.stats_betz_end = False

style narra:
    color "#3D6944"
    outlines [ (0, "#B3AEA4", 2, 2) ]

style dialogue:
    color "#404040"

##################################################
## ACHIEVOS
##################################################
init python:
    achievement.register("amour")
    achievement.register("betz")
    achievement.register("sight")
    achievement.register("smell")
    achievement.register("hear")
    achievement.register("str")
    achievement.register("int")
    achievement.register("psy")
    achievement.register("complete")

##################################################
### Important Characters
##################################################
## HEY!!! IF YOU'RE ADDING CHARACTER PORTRAITS: make sure to add them at the end of plugin_parallax too
##################################################
define narrator = Character(what_color="#3D6944", histcolor="#6B883C", ctc="ctc_s", ctc_pause="ctc_s", ctc_timedpause=Null(), ctc_position="fixed", callback=sfxsosottenarrator)
define s = Character(_("ME"), color="#404040", histcolor="#6B883C", namebox_background=Frame("gui/nameboxes/namebox_sosotte.png"), ctc="ctc_s", ctc_pause="ctc_s", ctc_timedpause=Null(),ctc_position="fixed", callback=[lipflap_sosotte, sfxsosotte])
define a = Character(_("[amourname!t]"), color="#FFFFFF", histcolor="#B06531", namebox_background=Frame("gui/nameboxes/namebox_amour.png"), ctc="ctc_a", ctc_pause="ctc_a", ctc_timedpause=Null(), ctc_position="fixed", image="amour", callback=[lipflap_amour,sfxamour])
define b = Character(_("[betzname!t]"), color="#404040", histcolor="#5597A9", namebox_background=Frame("gui/nameboxes/namebox_betz.png"), ctc="ctc_b", ctc_pause="ctc_b", ctc_timedpause=Null(), ctc_position="fixed", image="betz", callback=[lipflap_betz,sfxbetz])


### Side Characters
define defaultcharacter = Character(_("default"), ctc="ctc_r", ctc_pause="ctc_r", ctc_timedpause=Null(), ctc_position="fixed")

define bb = Character("[bbname!t]", image="bb", callback=sfxnpcmid, color="#0C0C0C", namebox_background=Frame("gui/nameboxes/namebox_default.png"), kind=defaultcharacter)
define bm = Character("[bmname!t]", image="bm", callback=sfxnpchigh, color="#0C0C0C", namebox_background=Frame("gui/nameboxes/namebox_default_2.png"), kind=defaultcharacter)
define bv = Character("[bvname!t]", image="bv", callback=sfxnpclow, color="#0C0C0C", namebox_background=Frame("gui/nameboxes/namebox_default.png"), kind=defaultcharacter)

define obj = Character("[objectname!t]", color="#0C0C0C", namebox_background=Frame("gui/nameboxes/namebox_default_2.png"), kind=defaultcharacter, callback=sfxnpcmid)

##################################################
label main_menu:
    $ renpy.restart_interaction()
    show main_title_5 as bg
    show main_title_4 as cgfar
    show main_title_3 as cgpclose
    show main_title_2 as cgmidback
    call screen main_menu()
    return

label start:
    $ hide_mouse_based_on_state()
    show transition_nextpage onlayer overlay
    show screen frame_page onlayer frame_layer
    show screen dateandplace

    call script_0
    call script_1
    call script_2
    call script_3
    call script_4
# This ends the game.
    return
