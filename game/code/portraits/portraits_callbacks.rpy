init python:
    renpy.music.register_channel("ctc","ctc")


## CTC #######################################################
## ctc sounds
###############################################################
init python:
    def sfxsosotte(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(ctcsosotte,channel="ctc", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="ctc")

    def sfxsosottenarrator(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(ctcsosottenarrator,channel="ctc", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="ctc")

    def sfxamour(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(ctcamour,channel="ctc", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="ctc")

    def sfxbetz(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(ctcbetz,channel="ctc", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="ctc")

    def sfxnpclow(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(ctcnpclow,channel="ctc", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="ctc")

    def sfxnpcmid(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(ctcnpcmid,channel="ctc", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="ctc")

    def sfxnpchigh(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(ctcnpchigh,channel="ctc", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="ctc")



## LIPFLAPS #######################################################
## baababababababa
###############################################################
default amourLipflapping = False
init python:
    def lipflap_amour(event, **kwargs):
        global amourLipflapping
        if event == "show":
            amourLipflapping = True
        elif event == "slow_done":
            amourLipflapping = False

            
default betzLipflapping = False
init python:
    def lipflap_betz(event, **kwargs):
        global betzLipflapping
        if event == "show":
            betzLipflapping = True
        elif event == "slow_done":
            betzLipflapping = False


default mdLipflapping = False
init python:
    def lipflap_md(event, **kwargs):
        global mdLipflapping
        if event == "show":
            mdLipflapping = True
        elif event == "slow_done":
            mdLipflapping = False

default maLipflapping = False
init python:
    def lipflap_ma(event, **kwargs):
        global maLipflapping
        if event == "show":
            maLipflapping = True
        elif event == "slow_done":
            maLipflapping = False


default sosotteLipflapping = False
init python:
    def lipflap_sosotte(event, **kwargs):
        global sosotteLipflapping
        if event == "show":
            sosotteLipflapping = True
        elif event == "slow_done":
            sosotteLipflapping = False

default mLipflapping = False
init python:
    def lipflap_m(event, **kwargs):
        global mLipflapping
        if event == "show":
            mLipflapping = True
        elif event == "slow_done":
            mLipflapping = False


default bmLipflapping = False
init python:
    def lipflap_bm(event, **kwargs):
        global bmLipflapping
        if event == "show":
            bmLipflapping = True
        elif event == "slow_done":
            bmLipflapping = False

default bvLipflapping = False
init python:
    def lipflap_bv(event, **kwargs):
        global bvLipflapping
        if event == "show":
            bvLipflapping = True
        elif event == "slow_done":
            bvLipflapping = False

default bbLipflapping = False
init python:
    def lipflap_bb(event, **kwargs):
        global bbLipflapping
        if event == "show":
            bbLipflapping = True
        elif event == "slow_done":
            bbLipflapping = False

default pLipflapping = False
init python:
    def lipflap_p(event, **kwargs):
        global pLipflapping
        if event == "show":
            pLipflapping = True
        elif event == "slow_done":
            pLipflapping = False

default tsLipflapping = False
init python:
    def lipflap_ts(event, **kwargs):
        global tsLipflapping
        if event == "show":
            tsLipflapping = True
        elif event == "slow_done":
            tsLipflapping = False