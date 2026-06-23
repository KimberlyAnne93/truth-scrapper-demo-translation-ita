############ VIRTUAL CURSOR SCREEN ###################
### Used for controller support in PAC sections
init 10:
    default vc = VirtualCursor(cursors= 
                                {
                                "default" : ( "gui/button/cursor_idle.png", 11, 31),
                                "button" : ( "gui/button/cursor_menu.png", 11, 31)
                                },  speed=1000.0, snap_to_center=False, which_stick=stick_for_virtual_cursor)

screen virtual_cursor_screen():
    zorder 100
    default x_dir = 0
    default y_dir = 0

    stick_event:
        changed on_move_left_stick
        which_stick stick_for_parallax
        refresh_rate 1.0/60.0

    # If point and click is enabled and we're not in the menu, then enable the virtual mouse
    if IsPaCDisabled == False and is_in_menu == False:
        add vc id "vc_cursor"

define config.overlay_screens += ["virtual_cursor_screen"]

## ADDED FOR DEMO ##
## If you want to hide the gamepad tutorial icon, then just set hasMovedGamepadAfterTutorial to True, to hide it in 2 seconds.
## Or if you want it to be immediate, just hide joystick_tutorial_v2!
default hasMovedGamepadAfterTutorial = None

screen joystick_tutorial_v2:
    layer "say_layer"
    on "show" action SetVariable("hasMovedGamepadAfterTutorial", False)
    if pad_config.is_using_controller():
        use joystick_tuto

        stick_event:
            changed on_move_gamepad_tuto_callback
            which_stick "left"

    if hasMovedGamepadAfterTutorial == True:
        timer 2.0 action Hide()

init python:
    def on_move_gamepad_tuto_callback(x, y, event):
        global hasMovedGamepadAfterTutorial
        if hasMovedGamepadAfterTutorial == False:
            hasMovedGamepadAfterTutorial = True
            renpy.restart_interaction()
        return