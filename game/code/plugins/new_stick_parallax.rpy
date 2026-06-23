## RIGHT CONTROLLER STICK DISTANCE
default right_stick_x = 0.0
default right_stick_y = 0.0
default right_stick_x_lerped = 0.0
default right_stick_y_lerped = 0.0

default left_stick_x = 0.0
default left_stick_y = 0.0
default left_stick_x_lerped = 0.0
default left_stick_y_lerped = 0.0

## LERP STICK DISPLAYABLES
## These will interpolate the stick values and send them to the above variables respectively
## The 'lerped' versions are the ones that have been smoothed via exponential decay
init python:
    class LerpRightStick(renpy.Displayable):
        def __init__(self, speed = 1.0, **kwargs):
            super(LerpRightStick, self).__init__(**kwargs)
            global right_stick_x, right_stick_y
            self.speed = speed
            self.last_st = None
            self.last_rs_x = float(right_stick_x)
            self.last_rs_y = float(right_stick_y)

            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):
            global right_stick_x, right_stick_y

            if self.last_st is None:
                self.last_st = st
            
            dt = st - self.last_st

            global right_stick_x_lerped
            global right_stick_y_lerped

            #right_stick_x_lerped = lerp(float(self.last_rs_x), float(right_stick_x), 0.006 * self.speed)
            right_stick_x_lerped = absolute(expDecay(self.last_rs_x, right_stick_x, 23, 0.006))
            right_stick_y_lerped = absolute(expDecay(self.last_rs_y, right_stick_y, 23, 0.006))

            self.last_rs_x = right_stick_x_lerped
            self.last_rs_y = right_stick_y_lerped

            self.last_st = st
            render = renpy.Render(self.width, self.height)
            return render
        def event(self, ev, x, y, st):
            if ev.type==pygame.MOUSEMOTION:
                right_stick_x, right_stick_y = x, y

            renpy.redraw(self, 0)
            return None
    
    class LerpLeftStick(renpy.Displayable):
        def __init__(self, speed = 1.0, **kwargs):
            super(LerpLeftStick, self).__init__(**kwargs)
            global left_stick_x, left_stick_y
            self.speed = speed
            self.last_st = None
            self.last_rs_x = float(left_stick_x)
            self.last_rs_y = float(left_stick_y)

            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            global left_stick_x, left_stick_y

            if self.last_st is None:
                self.last_st = st
            
            dt = st - self.last_st

            global left_stick_x_lerped
            global left_stick_y_lerped

            #right_stick_x_lerped = lerp(float(self.last_rs_x), float(right_stick_x), 0.006 * self.speed)
            left_stick_x_lerped = absolute(expDecay(self.last_rs_x, left_stick_x, 23, 0.006))
            left_stick_y_lerped = absolute(expDecay(self.last_rs_y, left_stick_y, 23, 0.006))

            self.last_rs_x = left_stick_x_lerped
            self.last_rs_y = left_stick_y_lerped

            self.last_st = st

            renpy.redraw(self, 0)
            return render
        def event(self, ev, x, y, st):
            if ev.type==pygame.MOUSEMOTION:
                left_stick_x, left_stick_y = x, y

            renpy.redraw(self, 0)
            return None

    ## Move left stick callback
    def on_move_left_stick(x, y, stick):
        global left_stick_x, left_stick_y
        left_stick_x, left_stick_y = MoveLeftStick(absolute(x) * (persistent.gamepad_nav_speed+50.0), absolute(y) * (persistent.gamepad_nav_speed +50.0) )

    ## On press anything callback
    ## Used to turn the mouse on/off depending on the input provided
    def on_press_anything(previous, new, event):
        if new == pad_config.EventListener.CONTROLLER:
            if previous == pad_config.EventListener.CONTROLLER:
                return
            print("MOVED JOY HAT")
            global v_cursor_enabled
            v_cursor_enabled = True
            mouse_disp = renpy.get_displayable("virtual_cursor_screen", "vc_cursor")
            if mouse_disp:
                mouse_disp.move_mouse(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1], 0, _warper.ease)
            renpy.store.mouse_visible = False
        
        elif new == pad_config.EventListener.MOUSE:
            print("MOVED MOUSE")
            renpy.store.mouse_visible = True
            global v_cursor_enabled
            v_cursor_enabled = False
            current_dpad_menu = None

    def hide_mouse_based_on_state():
        renpy.store.mouse_visible = pad_config.is_using_mouse()
    
    config.periodic_callbacks += [hide_mouse_based_on_state]
    ## Add the callback to the input type callback
    pad_config.INPUT_TYPE_CALLBACKS += [ on_press_anything ]