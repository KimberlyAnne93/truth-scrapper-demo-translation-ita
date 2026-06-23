## MUSIC #######################################################
## tracks
###############################################################
define title = ['music/00 Bossa de Sosotte.wav']

define culdepuis = ['music/04 Cul de Puits.wav']
define culdepuis_spooky = ['music/14 Ville Insolite.wav']
define dwellentrance = ['music/07 The Dwell.wav']
define dwell = ['music/07 The Dwell.wav']
define dwell_spooky = ['music/thedwell_spooky.mp3']
define train = ['music/06 Cara Van.wav']

define thirdgod = ['music/15 Troisieme Dieu.wav']

define search = ['music/08 Bibliotheque.wav']
define search_spooky = ['music/16 Sombre Bibliotheque.wav']
define saturate_city = ['music/13 Saturation (City).wav']
define saturate_dwell = ['music/09 Saturation (Dwell).wav']

define amour = ['music/03 Theme D_Amour.wav']
define betz = ['music/12 Theme de Betz.wav']

define goofy = ['music/05 Valse de Ville.wav']
define spooky = ['music/10 Cache dans la Dwell.wav']
define pursuit = ['music/11 Poursuite.wav']
define bittersweet = ['music/01 Champ Vide.wav']
define tense = ['music/17 Sceptique.wav']
define tensemore = ['music/17 Sceptique - Variant 1.wav']

define nightclub = ['music/20 Boite de Nuit v1.wav']

#ASK SOMEONE TO DO THIS BETTER
define nightclubfar = ['music/20 Boite de Nuit_bassboosted.wav']

define romance = ['music/21 Sosotte le Romantique v1.wav']



define heartbeat = ['music/heartbeat.mp3']
define heartbeatsong = ['music/18 Coeur Battant.wav']
define heartbeatsongspooky = ['music/19 Souvenirs Brisés.wav']
define heartbeatsongspookyalt = ['music/19 Souvenirs Brisés - Variant 1.wav']

define memories = ['music/02 Vieux Souvenirs.wav']


## BGSOUND #######################################################
## soundscapes
###############################################################
init python:
    renpy.music.register_channel("bg","bg",loop=True,tight=True)
    renpy.music.register_channel("bg2","bg",loop=True,tight=True)

define birdsnight = ['sfx/amb_TRS_NightField.ogg']
define birdsday = ['sfx/amb_TRS_MorningBirds.ogg']

define height = ['sfx/amb_TRS_CityDistant.ogg']

define city = ['sfx/amb_TRS_City.ogg']
define citysky = ['sfx/amb_TRS_CitySky.ogg']
define insidebusy = ['sfx/amb_TRS_GuildOffice.ogg']
define inside = ['sfx/amb_TRS_InsideRoomLoop.ogg']
define bathroom = ['sfx/amb_TRS_InsideRoomLoop.ogg']
define colette = ['sfx/amb_TRS_InsideOfficeLoop.ogg']

define bgtrain = ['sfx/amb_TRS_TrainRide.ogg']

define bgdwell = ['sfx/amb_TRS_CaveBusy.ogg']
define bgdwell_empty = ['sfx/amb_TRS_CaveEmpty.ogg']

define shower = ['sfx/amb_TRS_ShowerRunningInside.ogg']
define showeroutside = ['sfx/amb_TRS_ShowerRunningOutside.ogg']


#TO ADD LATER
define partyinside = ['sfx/amb_TRS_GuildOffice.ogg']