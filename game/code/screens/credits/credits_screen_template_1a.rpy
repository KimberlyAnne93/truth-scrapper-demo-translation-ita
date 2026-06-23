## 1a: The basic layout template with big credits blocks on each row.
# Each person is supposed to be credited once per row.
# I used 250x250 avatars, but it can be of any size.
# the site icons are 32x32

# Modified About Screen
screen credits_menu():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("CREDITS"), scroll="controller"):

        style_prefix "credits"
        null height 50 # manual vertical spacing
        
        vbox:
            xsize 1200
            hbox:
                xalign 0.5
                vbox:
                    null height 10 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text _("A Game By") style "credits_role"
                    null height 10 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text _("Adrienne Bazir / insertdisc5") style "credits_name"
                    null height 10  # manual vertical spacing
                    text _("Art, Story & Programming") style "credits_role"
                    null height 100

                    text _("With Support From") style "credits_role"
                    text _("Ontario Creates") style "credits_name"
                    null height 100

################################
########## GRID
################################
        vbox:
            xalign 0.5
            xsize 1200
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Dora Breckinridge") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Production and Operations") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Jess Forrest / Castle If") style "credits_name"
                        null height 10
                        text _("Composer") style "credits_role"
                        null height 10
                
            null height 50
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Halina Heron") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Sound Design") style "credits_role"
                        null height 10

                # Credit block
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Robert Dugay") style "credits_name"
                        null height 10
                        text _("Sound Design") style "credits_role"
                        null height 10
            null height 50

################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Chris Slight") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Community Management") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Jas Belen / spekterjester") style "credits_name"
                        null height 10
                        text _("Social Media Management") style "credits_role"
                        null height 10
            null height 50

################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Tyler Aubie") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("QA") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Feniks") style "credits_name"
                        null height 10
                        text _("Additional Programming") style "credits_role"
                        null height 10
            null height 50

################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("syphenzent") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Additional Programming") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Mauricio Castillo Rodriguez") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Additional Programming") style "credits_role"
                        null height 10
            null height 50

################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Gary Kings") style "credits_name"
                        null height 10
                        text _("Trailer") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Michael Michaelides") style "credits_name"
                        null height 10
                        text _("Trailer Animation") style "credits_role"
                        null height 10

#######################################################################
################################ CONTINUE
#######################################################################
        hbox:
            xalign 0.5
            yoffset -10
            vbox:
                null height 100 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                text _("Marketing by CONTINUE") style "credits_name"
                null height 10  # manual vertical spacing


        vbox:
            xalign 0.5
            xsize 1200
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Will Perkins") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Principal & Creative Director") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Julien Balbontin") style "credits_name"
                        null height 10
                        text _("Partner & Art Director") style "credits_role"
                        null height 10
                
            null height 50
# ################################
# ########## GRID
# ################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Brendan Ross") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Project Manager") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Cara McNeil") style "credits_name"
                        null height 10
                        text _("Marketing Coordinator") style "credits_role"
                        null height 10

#######################################################################
################################ TRANSLATION
#######################################################################
#######################################################################
################################ CONTINUE
#######################################################################
        hbox:
            xalign 0.5
            yoffset -10
            vbox:
                null height 100 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                text _("Localization") style "credits_name"
                null height 10  # manual vertical spacing


        vbox:
            xalign 0.5
            xsize 1200
# ################################
# ########## GRID
# ################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Japanese Localization") style "credits_name"
                        text _("Kakehashi Games") style "credits_name"
                        null height 10  # manual vertical spacing
                        text _("Tomoko Kono") style "credits_role"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("French Localization") style "credits_name"
                        null height 10
                        text _("Brandon Labonté") style "credits_role"
                        null height 10


#######################################################################
################################ PLAYTESTERS
#######################################################################
        hbox:
            xalign 0.5
            yoffset -10
            vbox:
                null height 100 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                text _("Playtesters") style "credits_name"
                null height 10  # manual vertical spacing

        vbox:
            xalign 0.5
            xsize 1200
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Ceilidh Barret") style "credits_name"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Macklin Loosley-Millman") style "credits_name"
                        null height 10
                
            null height 25
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Sonya Oliaji") style "credits_name"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Cat Hannaford") style "credits_name"
                        null height 10
                
            null height 25
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Tyler Ryan Schlossman") style "credits_name"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Heather Mihal") style "credits_name"
                        null height 10
                
            null height 25
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Aaron X Ray") style "credits_name"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Lilo") style "credits_name"
                        null height 10
                
            null height 25
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Stephanie Pitcher") style "credits_name"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Abby Howard and Tony Howard-Arias") style "credits_name"
                        null height 10
                
            null height 25
#######################################################################
################################ SPECIAL THANKS
#######################################################################
        hbox:
            xalign 0.5
            yoffset -10
            vbox:
                null height 100 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                text _("Special Thanks") style "credits_name"
                null height 10  # manual vertical spacing


        vbox:
            xalign 0.5
            xsize 1200
################################
########## GRID
################################
        vbox:
            xalign 0.5
            xsize 1200
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("My mom!!!!") style "credits_name"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Tony and Abby") style "credits_name"
                        null height 10
                
            null height 25
################################
########## BLOCK
################################
            hbox:
                xalign 0.5
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6 #-> if images are not resized properly you can do it with zoom
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text _("Nathan") style "credits_name"
                        null height 10
                # Credit block
                hbox:
                    xsize 600
                    # add "logo" zoom 0.6
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5
                        text _("Manu") style "credits_name"
                        null height 10
                
            null height 25