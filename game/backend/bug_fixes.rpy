python early:
    def parse_pause(l):
        delay = l.simple_expression()
        if not l.eol():
            renpy.error("expected end of line.")
        return { "delay" : delay }

    def lint_pause(p):
        if p["delay"]:
            _try_eval(p["delay"], 'pause statement')

    def execute_pause(p):
        if p["delay"]:
            delay = eval(p["delay"])
            if config.pause_with_transition and not persistent.hard_pauses:
                renpy.with_statement(Pause(delay))
            else:
                renpy.pause(delay, hard=persistent.hard_pauses)
        else:
            renpy.pause()

    renpy.register_statement(
        'pause',
        parse=parse_pause,
        lint=lint_pause,
        execute=execute_pause)

default persistent.hard_pauses = True

init python:

    class CustomSkip(Skip):
        """
        A custom skipping action which won't skip during point and click
        sections, unless there's dialogue.
        """
        def __call__(self):
            if IsPaCDisabled or InPaCDialogue:
                return super(CustomSkip, self).__call__()
            ## Otherwise, no skipping

    ## Remove the usual skipping action and make them all a toggle so we
    ## can have a confirmation screen.
    config.keymap["skip"] = [ ]
    config.keymap["toggle_skip"] += [ 'anymod_K_LCTRL', 'anymod_K_RCTRL' ]

    ## Ask for confirmation before skipping.
    skip_keymap_override = renpy.Keymap(
        toggle_skip=CustomSkip(fast=False, confirm=True),
    )

    class NoReshowMenu(ShowMenu):
        """
        A duplicate of ShowMenu but it's insensitive if the screen is
        already showing.
        """
        def __call__(self):
            screen = self.screen or store._game_menu_screen

            if screen is None:
                return False

            if screen in config.show_menu_enable:
                extra = eval(config.show_menu_enable[screen])
            else:
                extra = True

            sensitive = extra and not renpy.get_screen(screen)
            if sensitive:
                return super(NoReshowMenu, self).__call__()
            # Otherwise we do nothing


    class ShowNextScreen(Action):
        """
        A custom action which cycles through screens
        in the provided direction. For the glossary.
        """
        def __init__(self, screen_list, dir=1, focus_screen=None, focus_vp=None):
            self.screen_list = screen_list
            self.dir = dir
            self.focus_screen = focus_screen
            self.focus_vp = focus_vp
        def __call__(self):
            current_screen = None
            for screen in self.screen_list:
                if renpy.get_screen(screen):
                    current_screen = screen
                    break
            if current_screen is None:
                new_screen = self.screen_list[0]
            else:
                next_index = (self.screen_list.index(current_screen) + self.dir) % len(self.screen_list)
                new_screen = self.screen_list[next_index]
            renpy.run(NoReshowMenu(new_screen))
            if self.focus_screen:
                renpy.run(SetFocus(self.focus_screen, new_screen))
            if self.focus_vp:
                ## There's a viewport we should try to update
                vp_disp = renpy.get_displayable(self.focus_screen, self.focus_vp, "screens")
                the_focus = renpy.display.focus.get_focused()
                if vp_disp:
                    focus_index = vp_disp.vp_children.index(the_focus) if the_focus in vp_disp.vp_children else None
                    if focus_index is not None:
                        vp_disp.keep_in_view("up" if self.dir==1 else "down", focus_index)

    class KeepInFocus(Action):
        """
        An action which will attempt to set focus to a displayable with
        a particular ID in the provided controller viewport.

        Attributes:
        -----------
        screen : str
            The name of the screen where the controller viewport and child are.
        vp : str
            The ID of the controller viewport.
        target_id : str
            The ID of the focused child.
        direction : "up"/"left"/"right"/"down"
            The direction the focus is considered to have come from.
        """
        def __init__(self, screen, vp, target_id, direction="down"):
            self.screen = screen
            self.vp = vp
            self.target_id = target_id
            self.direction = direction
        def __call__(self):
            renpy.set_focus(self.screen, self.target_id)
            vp_disp = renpy.get_displayable(self.screen, self.vp, "screens")
            if vp_disp:
                target_disp = renpy.get_displayable(self.screen, self.target_id, "screens")
                if target_disp and target_disp in vp_disp.vp_children:
                    focus_index = vp_disp.vp_children.index(target_disp)
                    vp_disp.keep_in_view(self.direction, focus_index)

    config.underlay.append(skip_keymap_override)

## A simple screen which ensures skipping is turned off when it's shown,
## and prevents beginning to skip while it's shown.
screen prevent_skipping():
    if not InPaCDialogue:
        on ('show', 'replace') action SetVariable("config.skipping", False)
        key ['skip', 'toggle_skip'] action NullAction()


init python:

    ## A fix for line breaks
    ## https://www.unicode.org/reports/tr14/tr14-30.html for the codes
    renpy.language_tailor("«「", "OP") # Opening punctuation
    renpy.language_tailor("»」", "CL") # Closing punctuation

# True if we should force the left stick to be able to focus buttons instead of the camera
default leftstick_focus = False

init python:
    ## A fix for Japanese fonts not having a dot character
    config.font_name_map["和風ぽっぷ.ttf"] = FontGroup().add("SigmarOne.otf", start="•", end="•").add("fonts/和風ぽっぷ.ttf", start=None, end=None)
    config.font_name_map["natumemozi.ttf"] = FontGroup().add("SigmarOne.otf", start="•", end="•").add("fonts/natumemozi.ttf", start=None, end=None)

