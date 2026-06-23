########################################################################################
# Shortcuts
########################################################################################
init python:
    config.keymap['game_menu'].remove('mouseup_3')

translate japanese python:
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "natumemozi.ttf"
########################################################################################
# Auto punctuation
########################################################################################
default persistent.autopunctuation = True

define config.default_textshader = 'typewriter'

init python:
    if persistent.autopunctuation:
        def alter_say_strings( str_to_test ):
            str_map = {
            #1/4 second
                ", " : ", {w=0.05}",
                ": " : ": {w=0.05}",
                #" \"" : " {w=0.05}\"",
                #"\" " : "{w=0.05}\" ",
                "…" : "...",
            # 1/2 second
                # ". " : ". {w=0.25}", 
                # "? " : "? {w=0.25}", 
                # "! " : "! {w=0.25}",
                # "... " : "... {w=0.25}",
                # "; " : "; {w=0.25}",
            }
            for key in str_map:
                str_to_test = str_to_test.replace( key, str_map[ key ] ) 
            return str_to_test

define config.say_menu_text_filter = alter_say_strings



