## ⚠️ SETUP ###################################################
## variables and stuff
#############################################################
# Max Number of choices.
default MaxNumberChoice = 8

#as the day starts
default MaxNumberChoice_Day1 = 8
# ADDING MORE DAYS? CHECK MEMORYREROLL TO ADD MAX NUMBER THERE

default D0C1Text = 0
default D0C2Text = 0
default D0C3Text = 0



# leave as "error". if you can see error, shit went wrong.
default MemoryTextForSpotChoice = "WUH OH SOMETHING WENT WRONG"
default TempMemoryText = ""
default TempMemoryNumber = 1
default ClickingOnChoice = False

# Which day is it?
default VisibleDayPageMemory = 1
default CurrentDay = 1
# should be updated in the script each new day

# variable for image notif for when you have a new possible choice
default GotNewChoice = False
default clickindicator_memory1Clicked = False
default clickindicator_memory2Clicked = False
default clickindicator_memory3Clicked = False

#The Choices Section Hell
default MemoryTextForSpot1 = ""
default MemoryTextForSpot2 = ""
default MemoryTextForSpot3 = ""

default MemoryNumberForSpot1 = 1
default MemoryNumberForSpot2 = 2
default MemoryNumberForSpot3 = 3
default allchoices = [MemoryNumberForSpot1, MemoryNumberForSpot2, MemoryNumberForSpot3]
default MemoryCheck = False


default stats_smell = False
default stats_sight = False
default stats_hearing = False

default stats_str = False
default stats_int = False
default stats_psy = False

default stats_amour = False
default stats_betz = False

default BookMenuVisible = False


########################################################################################################################
# Labels depending on which memory you clicked. afaik it doesn't need to change ever
########################################################################################################################
label WhichMemoryIsGonnaAppear_1():
    # for day 1, indicator to show you can click on them
    $ clickindicator_memory1Clicked = True
    $ TempMemoryNumber = MemoryNumberForSpot1
    #so if it's an amour memory and the opposite is right after, it won't skip it
    $ MemoryNumberForSpot1 = 0
    #show the poor beast you're right
    $ allchoices = [MemoryNumberForSpot1, MemoryNumberForSpot2, MemoryNumberForSpot3]


    $ TempMemoryNumber += 1

    if TempMemoryNumber == 1:
        $ TempMemoryText = _("{color=6B883C}• Cul-De-Puits has refreshing views. I guess.{image=sight}{/color}") #in other places

    if TempMemoryNumber == 2:
        $ TempMemoryText = "{color=6B883C}• Cul-De-Puits has nice smells. I guess.{image=smell}{/color}" #in other places

    if TempMemoryNumber == 3:
        $ TempMemoryText = "{color=6B883C}• Cul-De-Puits sounds lovely. I guess.{image=hearing}{/color}" #in other places
    if TempMemoryNumber == 4:
        $ TempMemoryText = "{color=6B883C}• Cul-De-Puits has refreshing views. I guess.{image=sight}{/color}"
        $ TempMemoryNumber = 1


    $ MemoryTextForSpot1 = TempMemoryText
    $ MemoryNumberForSpot1 = TempMemoryNumber
    
    $ allchoices = [MemoryNumberForSpot1, MemoryNumberForSpot2, MemoryNumberForSpot3]
    call MemoryRecord() from _call_MemoryRecord
    call screen book_reminders
    return

########################################################################################################################

label WhichMemoryIsGonnaAppear_2():
    $ clickindicator_memory2Clicked = True
    $ TempMemoryNumber = MemoryNumberForSpot2
    $ MemoryNumberForSpot2 = 0
    $ allchoices = [MemoryNumberForSpot1, MemoryNumberForSpot2, MemoryNumberForSpot3]


    $ TempMemoryNumber += 1

    if TempMemoryNumber == 4:
        $ TempMemoryText = "{color=6B883C}• The sun is shining, making my body all warm.{image=str}{/color}" #in other places

    if TempMemoryNumber == 5:
        $ TempMemoryText = "{color=6B883C}• There are so many lovely Saturated Items around.{image=int}{/color}" #in other places

    if TempMemoryNumber == 6:
        $ TempMemoryText = "{color=6B883C}• People around the city seem happy.{image=psy}{/color}" #in other places
    if TempMemoryNumber == 7:
        $ TempMemoryText = "{color=6B883C}• The sun is shining, making my body all warm.{image=str}{/color}"
        $ TempMemoryNumber = 4



    $ MemoryTextForSpot2 = TempMemoryText
    $ MemoryNumberForSpot2 = TempMemoryNumber
    
    $ allchoices = [MemoryNumberForSpot1, MemoryNumberForSpot2, MemoryNumberForSpot3]
    call MemoryRecord() from _call_MemoryRecord_1
    call screen book_reminders
    return

########################################################################################################################

label WhichMemoryIsGonnaAppear_3():
    $ clickindicator_memory3Clicked = True
    $ TempMemoryNumber = MemoryNumberForSpot3
    $ MemoryNumberForSpot3 = 0
    $ allchoices = [MemoryNumberForSpot1, MemoryNumberForSpot2, MemoryNumberForSpot3]

    $ TempMemoryNumber += 1

    if TempMemoryNumber == 7:
        $ TempMemoryText = "{color=B06531}• Amour is interesting.{image=amourstat}{/color}" #in other places

    elif TempMemoryNumber == 8:
        $ TempMemoryText = "{color=5597A9}• Betz is interesting.{image=betzstat}{/color}"

    if TempMemoryNumber == 9:
        $ TempMemoryText = "{color=B06531}• Amour is interesting.{image=amourstat}{/color}"
        $ TempMemoryNumber = 7


    $ MemoryTextForSpot3 = TempMemoryText
    $ MemoryNumberForSpot3 = TempMemoryNumber
    
    $ allchoices = [MemoryNumberForSpot1, MemoryNumberForSpot2, MemoryNumberForSpot3]
    call MemoryRecord() from _call_MemoryRecord_2
    call screen book_reminders
    return
    


label MemoryRecord():

    if 1 in allchoices:
        $ stats_sight = True
    else:
        $ stats_sight = False

    if 2 in allchoices:
        $ stats_smell = True
    else:
        $ stats_smell = False

    if 3 in allchoices:
        $ stats_hearing = True
    else:
        $ stats_hearing = False



    if 4 in allchoices:
        $ stats_str = True
    else:
        $ stats_str = False

    if 5 in allchoices:
        $ stats_int = True
    else:
        $ stats_int = False

    if 6 in allchoices:
        $ stats_psy = True
    else:
        $ stats_psy = False

    if 7 in allchoices:
        $ stats_amour = True
    else:
        $ stats_amour = False

    if 8 in allchoices:
        $ stats_betz = True
    else:
        $ stats_betz = False


########################################################################################################################
# new choice notification
########################################################################################################################

label NewChoiceNotif():
    ## add image, turn switch on for visible, turn switch off when you go into the menu. image and stuff is in bookmenu_main
    $ GotNewChoice = True
    play sound renpy.random.choice(menu_notif)
    return

########################################################################################################################
# new choice notification
########################################################################################################################

label RecallMemoryPageText ():
    call screen book_reminders
    return



