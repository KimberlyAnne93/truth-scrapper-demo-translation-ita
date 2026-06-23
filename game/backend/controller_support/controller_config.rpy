



















init python:
    build.classify("**controller_config.rpy", None)
    build.classify("**controller_config.rpyc", "archive")

init -500 python in pad_config:
    
    _constant = True
    
    
    
    
    
    ICON_FOLDER = "backend/controller_support/controller_ui/"
    
    ICON_EXTENSION = "svg"
    
    
    
    DEFAULT_DPI = 150
    
    DEFAULT_ICON_SIZE = 75
    
    
    
    
    ICON_COLOR_TYPE = 2
    
    
    
    
    
    XBOX_A_COLOR = "#BAE236"
    XBOX_B_COLOR = "#FC551D"
    XBOX_X_COLOR = "#23C3F6"
    XBOX_Y_COLOR = "#FEB21B"
    
    PS_X_COLOR = "#5FD3F8"
    PS_O_COLOR = "#FD6248"
    PS_SQUARE_COLOR = "#F450A5"
    PS_TRIANGLE_COLOR = "#36E2A7"
    
    
    
    XBOX_CONTROLLER_NAMES = ["xbox", "microsoft"]
    PLAYSTATION_CONTROLLER_NAMES = ["ps3", "dualshock", "ps4", "playstation",
        "ps5", "dualsense", "ps2", "ps1", "sony", "ds4", "ds5"]
    NINTENDO_CONTROLLER_NAMES = ["nintendo", "joycon", "pro controller",
        "switch", "gamecube", "wii"]
    STEAM_CONTROLLER_NAMES = ["steam", "valve"]
    
    
    
    
    
    
    KEYBOARD_ROW1 = _("qwertyuiop")
    KEYBOARD_ROW2 = _("asdfghjkl'")
    KEYBOARD_ROW3 = _("zxcvbnm,.?")
    
    
    
    SHIFT_DICT = {
        "," : "-",
        "." : "_",
        "'" : '"',
        "?" : "/",
        
    }
    
    
    KEYBOARD_BUTTON_WIDTH = 120
    
    KEYBOARD_BUTTON_HEIGHT = 90
    
    KEYBOARD_BUTTON_SPACING = 5
    
    
    
    
    
    
    
    
    DEFAULT_VIRTUAL_CURSORS = { }
    
    
    
    
    
    
    RESTORE_FOCUS_SCREENS = [ "main_menu", "game_menu", "controller_remap", "book_glossary", "navigation_glossary" ]
    
    
    
    
    INPUT_TYPE_CALLBACKS = [ refresh_controller_ui, refresh_redrawables ]
    INPUT_CHANGE_REDRAWABLES = [ ]
    
    
    
    
    CONTROLLER_DISCONNECT_CALLBACKS = [ ]
    CONTROLLER_CONNECT_CALLBACKS = [ choose_icon_set ]
    
    
    
    
    STICK_MAX = 32767
    STICK_MIN = -32768
    
    MINIMUM_DEADZONE = 1024
    DEFAULT_DEADZONE = 4096
    MAXIMUM_DEADZONE = 16384
    
    MINIMUM_SENSITIVITY = 0.2
    DEFAULT_SENSITIVITY = 1.0
    MAXIMUM_SENSITIVITY = 3.0
    
    
    
    
    
    EVENT_TO_ICON = {
        
        
        "pad_leftshoulder_press" : "l1",
        "pad_leftshoulder_release" : "l1",
        "repeat_pad_leftshoulder_press" : "l1",

        
        "pad_rightshoulder_press" : "r1",
        "pad_rightshoulder_release" : "r1",
        "repeat_pad_rightshoulder_press" : "r1",

        
        
        "pad_lefttrigger_pos" : "l2",
        "pad_lefttrigger_zero" : "l2",
        "repeat_pad_lefttrigger_pos" : "l2",

        
        "pad_righttrigger_pos" : "r2",
        "pad_righttrigger_zero" : "r2",
        "repeat_pad_righttrigger_pos" : "r2",

        
        
        "pad_a_press" : "a",
        "pad_a_release" : "a",
        "repeat_pad_a_press" : "a",

        
        "pad_b_press" : "b",
        "pad_b_release" : "b",
        "repeat_pad_b_press" : "b",

        
        "pad_x_press" : "x",
        "pad_x_release" : "x",
        "repeat_pad_x_press" : "x",

        
        "pad_y_press" : "y",
        "pad_y_release" : "y",
        "repeat_pad_y_press" : "y",

        
        
        "pad_dpleft_press" : "left",
        "pad_dpleft_release" : "left",
        "repeat_pad_dpleft_press" : "left",

        
        "pad_dpright_press" : "right",
        "pad_dpright_release" : "right",
        "repeat_pad_dpright_press" : "right",

        
        "pad_dpup_press" : "up",
        "pad_dpup_release" : "up",
        "repeat_pad_dpup_press" : "up",

        
        "pad_dpdown_press" : "down",
        "pad_dpdown_release" : "down",
        "repeat_pad_dpdown_press" : "down",

        
        
        "pad_leftstick_press" : "l3",
        "pad_leftstick_release" : "l3",
        "repeat_pad_leftstick_press" : "l3",

        "pad_leftx_pos" : "left_stick",
        "repeat_pad_leftx_pos" : "left_stick",
        "pad_leftx_neg" : "left_stick",
        "repeat_pad_leftx_neg" : "left_stick",
        "pad_lefty_pos" : "left_stick",
        "repeat_pad_lefty_pos" : "left_stick",
        "pad_lefty_neg" : "left_stick",
        "repeat_pad_lefty_neg" : "left_stick",

        
        "pad_rightstick_press" : "r3",
        "pad_rightstick_release" : "r3",
        "repeat_pad_rightstick_press" : "r3",

        "pad_rightx_pos" : "right_stick",
        "repeat_pad_rightx_pos" : "right_stick",
        "pad_rightx_neg" : "right_stick",
        "repeat_pad_rightx_neg" : "right_stick",
        "pad_righty_pos" : "right_stick",
        "repeat_pad_righty_pos" : "right_stick",
        "pad_righty_neg" : "right_stick",
        "repeat_pad_righty_neg" : "right_stick",

        
        "pad_back_press" : "select",
        "pad_back_release" : "select",
        "repeat_pad_back_press" : "select",

        
        "pad_guide_press" : "home",
        "pad_guide_release" : "home",
        "repeat_pad_guide_press" : "home",

        
        "pad_start_press" : "start",
        "pad_start_release" : "start",
        "repeat_pad_start_press" : "start",
    }
    
    ICON_TO_ALT_TEXT = {
        "l3" : _("Press Left stick"),
        "r3" : _("Press Right stick"),
        "left" : _("Left"),
        "right" : _("Right"),
        "up" : _("Up"),
        "down" : _("Down"),
        "left_stick" : _("Left stick"),
        "right_stick" : _("Right stick"),

        
        
        "a" : [_("A Button"), _("Cross Button"), _("A Button"), _("A Button"),
            _("A Button")],
        "b" : [_("B Button"), _("Circle Button"), _("B Button"), _("B Button"),
            _("B Button")],
        "x" : [_("X Button"), _("Square Button"), _("X Button"), _("X Button"),
            _("X Button")],
        "y" : [_("Y Button"), _("Triangle Button"), _("Y Button"), _("Y Button"),
            _("Y Button")],
        "l1" : [_("Left Bumper"), _("L1 Button"), _("L Button"), _("L1 Button"),
            _("Left Shoulder")],
        "r1" : [_("Right Bumper"), _("R1 Button"), _("R Button"), _("R1 Button"),
            _("Right Shoulder")],
        "l2" : [_("Left Trigger"), _("L2 Button"), _("ZL Button"), _("L2 Trigger"),
            _("Left Trigger")],
        "r2" : [_("Right Trigger"), _("R2 Button"), _("ZR Button"), _("R2 Trigger"),
            _("Right Trigger")],
        "select" : [_("Back Button"), _("Share Button"), _("Minus Button"), _("View Button"),
            _("Select Button")],
        "start" : [_("Start Button"), _("Options Button"), _("Plus Button"), _("Menu Button"),
            _("Start Button")],
        "home" : [_("Home Button"), _("PS Button"), _("Home Button"), _("Steam Button"),
            _("Home Button")],
    }
    
    EVENT_LISTENER = EventListener(callbacks=INPUT_TYPE_CALLBACKS, on_changed=True)
    PRESS_ANYTHING = EventListener(callbacks=[wait_for_event], on_changed=False)



default persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE = None

default persistent.left_stick_dead_zone = dict()
default persistent.right_stick_dead_zone = dict()

default persistent.left_stick_max = dict()
default persistent.right_stick_max = dict()

default persistent.left_stick_invert_x = False
default persistent.left_stick_invert_y = False
default persistent.right_stick_invert_x = False
default persistent.right_stick_invert_y = False

default persistent.left_stick_sensitivity = 1.0
default persistent.right_stick_sensitivity = 1.0




init 999 python in pad_config:
    EVENT_LISTENER = EventListener(callbacks=INPUT_TYPE_CALLBACKS, on_changed=True)

    FOCUS_MANAGERS = [FocusManager(x) for x in RESTORE_FOCUS_SCREENS]


screen event_listener():
    layer 'overlay'
    zorder 999


    add pad_config.EVENT_LISTENER


    for manager in pad_config.FOCUS_MANAGERS:
        add manager

    if persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE:
        add persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE

init python:

    config.always_shown_screens.append("event_listener")
    _game_menu_screen = "game_menu"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
