default persistent.parallaxOn = True
# MORE CONTROLLER SUPPORT: bookmenu_0_main, big screens
########################################################################################
# gamepad mouse stuff (THANKS SYPHERZENT)
screen mouse_parallax_screen():
    if mouse_parallax is None:
        $ mouse_parallax = MouseParallax([(-20,"farthestBack"),(-40,"prettyFarBack"), (-60,"farBack"),(-75,"moreback"),(-80,"back"),(-98,"bgfront"),(-100,"front"),(-105,"superfront"),(-110,"transitions"),(-111,"supertransitions") ,])

    add mouse_parallax
init -20 python:

    def MoveLeftStick(x_dir, y_dir):
        global left_stick_x, left_stick_y
        x, y = left_stick_x, left_stick_y
        if x_dir:
            x = float(left_stick_x + x_dir)
            if x <= 0:
                x = 1.0
            elif x >= 1920:
                x = 1919.0
        if y_dir:
            y = float(left_stick_y + y_dir)
            if y <= 0:
                y = 1.0
            elif y >= 1080:
                y = 1079.0
        return (x, y)

    def MoveRightStick(x_dir, y_dir):
        global right_stick_x, right_stick_y
        x, y = right_stick_x, right_stick_y
        if x_dir:
            x = float(right_stick_x + x_dir)
            if x <= 0:
                x = 1.0
            elif x >= 1920:
                x = 1919.0
        if y_dir:
            y = float(right_stick_y + y_dir)
            if y <= 0:
                y = 1.0
            elif y >= 1080:
                y = 1079.0
        return (x, y)

    def MoveMouseCursor(x_dir,y_dir):
        start_x, start_y = renpy.get_mouse_pos()
        x, y = start_x, start_y
        if x_dir:
            x = int(start_x + x_dir)
            if x <= 0:
                x = 1
            elif x >= 1920:
                x = 1919
        if y_dir:
            y = int(start_y + y_dir)
            if y <= 0:
                y = 1
            elif y >= 1080:
                y = 1079
        return (x, y)
########################################################################################

init -10 python:

    class MouseParallax(renpy.Displayable):
        def __init__(self,layer_info):
            super(renpy.Displayable,self).__init__()
            self.xoffset,self.yoffset=0.0,0.0
            self.sort_layer=sorted(layer_info,reverse=True)
            cflayer=[]
            masteryet=False
            for m,n in self.sort_layer:
                if(not masteryet)and(m<0):
                    cflayer.append("master")
                    masteryet=True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient","screens","overlay"])
            config.layers=cflayer
            config.after_default_callbacks.append(self.overlay)
            return
        def render(self,width,height,st,at):
            return renpy.Render(width,height)
        def parallax(self,m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(function=func, subpixel=True)
        def overlay(self):
            renpy.show_screen("mouse_parallax_screen", _layer = "overlay")
            for m,n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)],n)
            renpy.redraw(self,0)
            return
        def event(self,ev,x,y,st):
            import pygame
        # VARIABLE HERE!!!!!!!!!!!!!!!!!! vvvvvvvvvvvvvvvvvvv
            if ev.type==pygame.MOUSEMOTION and persistent.parallaxOn:
                global right_stick_x, right_stick_y
                right_stick_x, right_stick_y = x, y
                self.xoffset, self.yoffset= ((float)(x)/(config.screen_width))-0.5,((float)(y)/(config.screen_height))-1.0
            return None

    def trans(d, st, at, disp=None, m=None):
        global v_cursor_enabled, IsPaCDisabled
        if pad_config.is_using_controller() or pad_config.is_using_keyboard():
            global main_menu
            offset_x, offset_y = 0, 0
            if main_menu:
                offset_x, offset_y= ((float)(right_stick_x_lerped)/(config.screen_width))-0.5,((float)(right_stick_y_lerped)/(config.screen_height))-1.0
            elif IsPaCDisabled == False:
                mouse_disp = renpy.get_displayable("virtual_cursor_screen", "vc_cursor")
                if mouse_disp:
                    offset_x, offset_y = ((float)(mouse_disp._x.value)/(config.screen_width))-0.5,((float)(mouse_disp._y.value)/(config.screen_height))-1.0
            else:
                offset_x, offset_y= ((float)(left_stick_x_lerped)/(config.screen_width))-0.5,((float)(left_stick_y_lerped)/(config.screen_height))-1.0
            d.xoffset, d.yoffset = int(round(m*offset_x)), int(round(m*offset_y))
        else:
            offset_x, offset_y = ((float)(renpy.get_mouse_pos()[0])/(config.screen_width))-0.5,((float)(renpy.get_mouse_pos()[1])/(config.screen_height))-1.0
            d.xoffset, d.yoffset = int(round(m*offset_x)), int(round(m*offset_y))
        if persistent.parallaxOn is False:
            d.xoffset, d.yoffset=0,0

        return 0

    def smooth_towards(a, b, speed, dt)  -> float:
        v = b-a;
        stepDist = speed * dt;
        if stepDist >= abs(v):
            return b;
        return a + sign(v)*stepDist

    global mouse_parallax
    mouse_parallax = MouseParallax([(-20,"farthestBack"),(-40,"prettyFarBack"), (-60,"farBack"),(-75,"moreback"),(-80,"back"),(-98,"bgfront"),(-100,"front"),(-105,"superfront"),(-110,"transitions"),(-111,"supertransitions") ,])
    config.tag_layer = {

    'cgbg': 'farthestBack',
    'bg' : 'farthestBack',
    'cgpfar': 'prettyFarBack',
    'cgfar': 'farBack',
    'cgmidback': 'moreback',
    'cgmid': 'back',
    'cgclose': 'bgfront',
    'cgpclose': 'front',

    'pacclose': 'front',
    'henshin': 'supertransitions',
    'blink': 'transitions',
    'transition': 'transitions',

    # put your list of character images here
    # amour will always be in front of betz. sorry you're gonna have to figure this shit out later
    'amour': 'front',
    'betz': 'front',

    'sosotte': 'front',

    'md': 'front',
    'ma': 'front',
    'marcel': 'back',
    'bb': 'front',
    'bv': 'front',
    'bm': 'front',
    'colette': 'back',
    'p': 'front',
    'ts': 'back',
    }
