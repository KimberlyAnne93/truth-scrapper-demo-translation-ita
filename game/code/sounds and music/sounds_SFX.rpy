init python:
    renpy.music.register_channel("soundloop","sfx",loop=True,tight=True)

## MENU #######################################################
## menu sounds
###############################################################
define turnpage = ['sfx/ui_TRS_PageTurn-001.ogg', 'sfx/ui_TRS_PageTurn-002.ogg','sfx/ui_TRS_PageTurn-003.ogg','sfx/ui_TRS_PageTurn-004.ogg','sfx/ui_TRS_PageTurn-005.ogg',]
define turnpage_single = ['sfx/ui_TRS_PageTurn-001.ogg']

define menu_notif = ['sfx/ui_TRS_NewMemoryAvailable.ogg']

define menu_hover = ['sfx/ui_TRS_MenuHover-001.ogg'] #for menus
define menu_hover_random = ['sfx/ui_TRS_MenuHover-001.ogg', 'sfx/ui_TRS_MenuHover-002.ogg', 'sfx/ui_TRS_MenuHover-003.ogg', 'sfx/ui_TRS_MenuHover-004.ogg', 'sfx/ui_TRS_MenuHover-005.ogg']
define menu_hover_paper_random = ['sfx/ui_TRS_PaperIconHover-001.ogg', 'sfx/ui_TRS_PaperIconHover-002.ogg', 'sfx/ui_TRS_PaperIconHover-003.ogg', 'sfx/ui_TRS_PaperIconHover-004.ogg']
define menu_confirm = ['sfx/ui_TRS_MenuClick-001.ogg']
define menu_cancel = ['sfx/ui_TRS_PageTurnCancel-001.ogg', 'sfx/ui_TRS_PageTurnCancel-002.ogg', 'sfx/ui_TRS_PageTurnCancel-003.ogg']

define memories_hover_random = ['sfx/ui_TRS_MemoryWritingHover-001.ogg', 'sfx/ui_TRS_MemoryWritingHover-002.ogg', 'sfx/ui_TRS_MemoryWritingHover-003.ogg']

define custo_hover = ['sfx/sfx_TRS_CustomizeHover-001.ogg'] #for customization scenes
define custo_hover_random = ['sfx/sfx_TRS_CustomizeHover-001.ogg', 'sfx/sfx_TRS_CustomizeHover-002.ogg', 'sfx/sfx_TRS_CustomizeHover-003.ogg']
define custo_confirm_random = ['sfx/sfx_TRS_CustomizeClick-001.ogg', 'sfx/sfx_TRS_CustomizeClick-002.ogg', 'sfx/sfx_TRS_CustomizeClick-003.ogg']

define dialogue_hover = ['sfx/ui_TRS_DialogueBoxHover-001.ogg'] #for dialoguebox
define dialogue_hover_random = ['sfx/ui_TRS_DialogueBoxHover-001.ogg', 'sfx/ui_TRS_DialogueBoxHover-002.ogg', 'sfx/ui_TRS_DialogueBoxHover-003.ogg', 'sfx/ui_TRS_DialogueBoxHover-004.ogg', 'sfx/ui_TRS_DialogueBoxHover-005.ogg']

define pac_hover = ['sfx/sfx_TRS_PCHoverItem-001.ogg', 'sfx/sfx_TRS_PCHoverItem-002.ogg', 'sfx/sfx_TRS_PCHoverItem-003.ogg'] #for pacs
define pac_click = ['sfx/sfx_TRS_PCClickItem-001.ogg', 'sfx/sfx_TRS_PCClickItem-002.ogg', 'sfx/sfx_TRS_PCClickItem-003.ogg']

define pactmark = ['sfx/sfx_TRS_CarvePactMark.ogg']
define sosottepactmark = ['sfx/sfx_TRS_SosottePactMark.ogg']
define amourpactmark = ['sfx/sfx_TRS_AmourPactMark.ogg']
define betzpactmark = ['sfx/sfx_TRS_BetzPactMark.ogg']

define write = ['sfx/sfx_TRS_WritingJournal-001.ogg']
define write_random = ['sfx/sfx_TRS_WritingJournal-001.ogg', 'sfx/sfx_TRS_WritingJournal-002.ogg', 'sfx/sfx_TRS_WritingJournal-003.ogg']
define writeimportant = ['sfx/sfx_TRS_WritingImportantThings.ogg']

define openbook = ['sfx/ui_TRS_OpenBook.ogg']
define closebook = ['sfx/ui_TRS_CloseBook.ogg']

define daystart = ['music/00 Stinger - City v1.wav']
define daystartcalm = ['music/00 Stinger - Calm v1.wav']

define blinkstart = ['sfx/sfx_TRS_SosotteEyesClose.ogg']
define blinkend = ['sfx/sfx_TRS_SosotteEyesOpen.ogg']

define stats = ['emotes/ui_TRS_Passive-003.ogg']

## SFX dialogue ###############################################
## dialogue
###############################################################
define ctcsosotte = ['dialogue/sfx_TRS_writing_crayon_paper1 (v2)-003.ogg']
define ctcsosottenarrator = ['dialogue/sfx_TRS_SosotteThinking.ogg']
define ctcamour = ['dialogue/sfx_TRS_writing_metal_cardboard_revised_options-001.ogg']
define ctcbetz = ['dialogue/sfx_TRS_writing_pencil_cardboard (v2)-019.ogg']

define ctcnpclow = ['dialogue/sfx_TRS_Voice-low.ogg']
define ctcnpcmid = ['dialogue/sfx_TRS_Voice-mid.ogg']
define ctcnpchigh = ['dialogue/sfx_TRS_Voice-high.ogg']

## EVERYDAY SOUNDS ############################################
## story sounds
###############################################################


define happy = ['emotes/sfx_TRS_EmoteHappy_2.ogg']
define shout = ['emotes/sfx_TRS_EmoteShout_2.ogg'] #betz shouting funny
define angryshout = ['emotes/sfx_TRS_EmoteShout_shockstyle.ogg'] #notfunny anymore
define shock = ['emotes/sfx_TRS_EmoteShock_2.ogg'] #like omg oh no!
define scare = ['emotes/sfx_TRS_EmoteScare v2.ogg'] #big reveal
define waitasec = ['emotes/sfx_TRS_EmoteWaitASecond.ogg'] #hey wait a second but its like hmm.... spooky...
define idea = ['emotes/sfx_TRS_EmoteIdea_crushed.ogg'] #like a oh!
define sad = ['emotes/sfx_TRS_EmoteSad_crushed.ogg']
define tada = ['emotes/sfx_TRS_EmoteTada-001.ogg']
define shiny = ['emotes/sfx_TRS_BetzSparkles.ogg'] #betz sparkles
define stinger = ['emotes/sfx_TRS_EmoteScare v2.ogg'] #big reveal

## HENSHIN SOUNDS #############################################
## HENSHIN
###############################################################

define henshinpactmark = ['sfx/sfx_TRS_CarvePactMark.ogg']
define henshinremembering = ['sfx/sfx_TRS_MagicRemembering.ogg']
define henshinsaturate = ['sfx/sfx_TRS_MagicMakingItem.ogg']
define henshinteleport = ['sfx/sfx_TRS_MagicTeleporting.ogg']
define openkeycarddoor = ['sfx/sfx_TRS_OpenMagicalDoor.ogg']

define rockgodappear = ['sfx/sfx_TRS_MagicRockGod.ogg']
define magicdisappear = ['sfx/sfx_TRS_MagicDissipating.ogg']


define windblowing = ['sfx/sfx_TRS_WindBlowShort.ogg'] #cold

## STORY ######################################################
## story sounds
###############################################################

define endofdaybell = ['sfx/sfx_TRS_MineBell.ogg']
define noonbell = ['sfx/sfx_TRS_ClocktowerBell.ogg']

define clothes = ['sfx/sfx_TRS_StandMovementShort.ogg']

define tic = ['sfx/sfx_TRS_TeardropsOnBook.ogg'] #for when she cries
define glassbreak = ['sfx/sfx_TRS_DreamGlassBreak.ogg']
define clay = ['sfx/sfx_TRS_ClayMovement-001.ogg', 'sfx/sfx_TRS_ClayMovement-002.ogg', 'sfx/sfx_TRS_ClayMovement-003.ogg', 'sfx/sfx_TRS_ClayMovement-004.ogg']

define rocksound = ['sfx/sfx_TRS_DreamGlassBreak.ogg'] #for the hazard being around
define smallrock = ['sfx/sfx_TRS_SmallRockFall.ogg']

define singleclap = ['sfx/sfx_TRS_HandClap.ogg'] #when sosotte claps

define keygiven = ['sfx/sfx_TRS_KeysJingle.ogg']
define keyopen = ['sfx/sfx_TRS_KeysOpenDoor.ogg']
define dooropen = ['sfx/sfx_TRS_OpenOldDoor.ogg']

define fall = ['sfx/sfx_TRS_SosotteTripFall.ogg']
define fallreal = ['sfx/sfx_TRS_EmoteShout_crushed.ogg']

define touchbath = ['sfx/sfx_TRS_TouchBathtub.ogg']
define showerstart = ['sfx/sfx_TRS_ShowerTurnOn.ogg']
define showerend = ['sfx/sfx_TRS_ShowerTurnOff.ogg']


define monstercatch = ['sfx/sfx_TRS_MonsterCatchSosotte.ogg']
define monstersting = ['sfx/sfx_TRS_MonsterSting.ogg']
define longsting = ['sfx/ui_TRS_Stinger.ogg']

define monsterdrawing = ['sfx/sfx_TRS_MonsterScribble.ogg']
define bracelet = ['sfx/sfx_TRS_TieThreadWrist.ogg']

define stab1 = ['sfx/sfx_TRS_Stab-001.ogg']
define stab2 = ['sfx/sfx_TRS_Stab-002.ogg']
define stab3 = ['sfx/sfx_TRS_Stab-003.ogg']
define bite = ['sfx/sfx_TRS_BiteFlesh.ogg']
define bloodsplatter = ['sfx/sfx_TRS_BloodSplatterPage.ogg']
define skincarve = ['sfx/sfx_TRS_SkinCarving.ogg']

define graspshort = ['sfx/sfx_TRS_GraspShort.ogg']
define grasplong = ['sfx/sfx_TRS_GraspLong.ogg']

define glassclink = ['sfx/sfx_TRS_GlassClink.ogg']

define hit =['sfx/sfx_TRS_Hit.ogg']

define chomp =['sfx/sfx_TRS_ChompShort.ogg']
define chomplong =['sfx/sfx_TRS_ChompLong.ogg']
define gulp =['sfx/sfx_TRS_DrinkGulpShort.ogg']
define gulplong =['sfx/sfx_TRS_DrinkGulpLong.ogg']
define sip =['sfx/sfx_TRS_DrinkSipShort.ogg']
define siplong =['sfx/sfx_TRS_DrinkSipLong.ogg']


### SOUNDS THAT NEED TO BE UPDATED 

define woof = ['emotes/sfx_TRS_EmoteHappy_2.ogg']
define lanternout = ['sfx/sfx_TRS_StandMovementShort.ogg']
define scuffle = ['emotes/sfx_TRS_EmoteShout_shockstyle.ogg'] #caro and emile getting attacked at a distance
define enlightened = ['sfx/sfx_TRS_WindBlowShort.ogg']
define charging = ['emotes/sfx_TRS_BetzSparkles.ogg']
## WALKING ####################################################
## 
###############################################################
define slowfootsteps_dwell = ['sfx/running.ogg']

define walkinggrass = ['sfx/sfx_TRS_FootstepWalkGrass.ogg']
define runninggrass =['sfx/sfx_TRS_FootstepRunGrass.ogg']
define runninggrassfall = ['sfx/sfx_TRS_FootstepTripFallGrass.ogg']

define walkingcity = ['sfx/sfx_TRS_FootstepWalkCity.ogg']
define runningcity = ['sfx/sfx_TRS_FootstepRunCity.ogg']
define walkingcityloop = ['sfx/sfx_TRS_FootstepWalkCityLoop.ogg']
define runningcityloop = ['sfx/sfx_TRS_FootstepRunCityLoop.ogg']


define walkingdwell = ['sfx/sfx_TRS_FootstepWalkCave.ogg']
define runningdwell =['sfx/sfx_TRS_FootstepRunCave.ogg']
define runningdwellloop =['sfx/sfx_TRS_FootstepRunCaveLoop.ogg']

define walkingspooky = ['sfx/sfx_TRS_FootstepSpooky.ogg']

define walkingwood = ['sfx/sfx_TRS_FootstepWalkWood.ogg']

define trainarrive = ['sfx/sfx_TRS_TrainArrive.ogg']






