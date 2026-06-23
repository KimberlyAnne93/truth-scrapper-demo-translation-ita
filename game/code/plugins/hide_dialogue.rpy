label hide_windows:
    $ mouse_visible = False
    return False

init python:
    renpy.add_layer("frame_layer", below="screens")
    renpy.add_layer("say_layer", above="screens")
    
    config.context_clear_layers = [ 'top', 'bottom', 'say_layer' ]
    config.clear_layers = ['screens']
    config.say_layer = 'say_layer'
    config.choice_layer = 'say_layer'

screen _ctc:
    layer 'say_layer'
    zorder 100
    add ctc