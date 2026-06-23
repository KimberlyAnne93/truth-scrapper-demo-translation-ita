init -1 python:
    ## Shows the vertical bar as if it was selected in case a controller VP is selected.
    ## This is to fake the vbar focus in the history menu- you're not really focusing the bar, but the viewport! It's just a neat visual trick.
    class YScrollValueSelected(BarValue, FieldEquality):
        """
        :doc: value

        The value of an adjustment that vertically scrolls the viewport with the
        given id, on the current screen. The viewport must be defined before a bar
        with this value is.
        """

        equality_fields = [ 'viewport' , 'vbar']

        def __init__(self, viewport, vbar):
            self.viewport = viewport
            self.vbar = vbar
            self.is_focused = False

        def get_adjustment(self):

            w = renpy.get_widget(None, self.viewport)
            if not isinstance(w, Viewport):
                raise Exception("The displayable with id %r is not declared, or not a viewport." % self.viewport)

            return w.yadjustment
        
        def periodic(self, st):
            self.is_focused = isinstance(renpy.display.focus.get_focused(), ControllerVP)

            if self.is_focused:
                v = renpy.get_widget(None, self.vbar)
                v.style = style.vscrollbar_vp_focused
            else:
                v = renpy.get_widget(None, self.vbar)
                v.style = style.vscrollbar

            return 0

        def get_style(self):
            return "scrollbar", "vscrollbar"
    
    from operator import itemgetter
    def collect(l, index):
        return map(itemgetter(index), l)

    ## Function to get the next item that should be focused in the book UI buttons
    ## Used to map focus in bookUI_memories
    def get_book_ui_focus(from_id, direction = 1):
        global current_book_highlight
        tup = None
        index = None
        index_initial = None
        for x in bookUI_vertical_order:
            if x[0] == from_id:
                tup = x
                index = bookUI_vertical_order.index(x)
                index_initial = bookUI_vertical_order.index(x)
                break

        if not tup:
            print(f"There is not a displayable with the id {from_id} in 'bookUI_vertical_order'.")
            return None
        
        to_focus = None

        if direction == 1:
            # We want to go down, so add on numbers. If we arrive at our initial index, then
            # abort the operation and return the same initial tuple.
            while to_focus is None:
                # Increase the index or loop back if required
                if index == len(bookUI_vertical_order) - 1:
                    index = 0
                else:
                    index += 1

                if index == index_initial:
                    print("We have looped back to the beginning! Returning the same screen as nothing can be selected")
                    to_focus = bookUI_vertical_order[index_initial]
                    to_focus = ( bookUI_vertical_order[index_initial][0], bookUI_vertical_order[index_initial][1] )

                # If we cannot find the main screen, try to find the fake one. Select the correct to_focus based on this.
                if renpy.get_screen(bookUI_vertical_order[index][1]):
                    print(f"We found the {bookUI_vertical_order[index][1]} screen!")
                    to_focus = bookUI_vertical_order[index]
                    to_focus = ( bookUI_vertical_order[index][0], bookUI_vertical_order[index][1] )
                elif renpy.get_screen(bookUI_vertical_order[index][2]):
                    print(f"We found the fake screen named {bookUI_vertical_order[index][2]}!")
                    to_focus = bookUI_vertical_order[index]
                    to_focus = ( bookUI_vertical_order[index][0], bookUI_vertical_order[index][2] )
            
        elif direction == -1:
            # We want to go up, so remove numbers. If we arrive at our initial index, then
            # abort the operation and return the same initial tuple.
            while to_focus is None:
                # Increase the index or loop back if required
                if index == 0:
                    index = len(bookUI_vertical_order) - 1
                else:
                    index -= 1

                if index == index_initial:
                    print("We have looped back to the beginning! Returning the same screen as nothing can be selected")
                    to_focus = bookUI_vertical_order[index_initial]
                    to_focus = ( bookUI_vertical_order[index_initial][0], bookUI_vertical_order[index_initial][1] )

                if renpy.get_screen(bookUI_vertical_order[index][1]):
                    print(f"We found the {bookUI_vertical_order[index][1]} screen!")
                    to_focus = ( bookUI_vertical_order[index][0], bookUI_vertical_order[index][1] )
                elif renpy.get_screen(bookUI_vertical_order[index][2]):
                    print(f"We found the fake screen named {bookUI_vertical_order[index][2]}!")
                    to_focus = ( bookUI_vertical_order[index][0], bookUI_vertical_order[index][2] )
        
        current_book_highlight = to_focus[0]
        return to_focus
    
    ## ADDED FOR DEMO ##
    ## Created new focus actions. Copy everything below this!
    class ClearDisplayFocus(Action):
        """
        An action that clears the focus and restarts the interaction appropriately.
        """
        
        def __call__(self):
            renpy.display.focus.set_focused(None, None, None)
            renpy.restart_interaction()
    
    class TriggerFocusDownAndPress(Action):
        """
        An action that triggers the 'focus down' and 'press' events.
        For use in scrolling ControllerVPs and pressing with a given key, such as in the glossary navigation.
        """
        def __init__(self, vp_id, screen_name):
            self.vp_id = vp_id
            self.screen_name = screen_name
        def __call__(self):
            renpy.queue_event("focus_down", up=False)
            vp_disp = renpy.get_displayable(self.screen_name, self.vp_id, "screens")
            prev_focus = renpy.display.focus.get_focused()
            if vp_disp:
                if prev_focus in vp_disp.vp_children:
                    if vp_disp.get_nearest_child(prev_focus, "down") != None:
                        renpy.queue_event("button_select", up=False)
            else:
                # No viewport displayable found, please fix?
                # Trigger the button select still.
                renpy.queue_event("button_select", up=False)
            return
    
    class TriggerFocusUpAndPress(Action):
        """
        An action that triggers the 'focus up' and 'press' events.
        For use in scrolling ControllerVPs and pressing with a given key, such as in the glossary navigation.
        """

        def __init__(self, vp_id, screen_name):
            self.vp_id = vp_id
            self.screen_name = screen_name
        def __call__(self):
            renpy.queue_event("focus_up", up=False)
            vp_disp = renpy.get_displayable(self.screen_name, self.vp_id, "screens")
            prev_focus = renpy.display.focus.get_focused()
            if vp_disp:
                if prev_focus in vp_disp.vp_children:
                    if vp_disp.get_nearest_child(prev_focus, "up") != None:
                        renpy.queue_event("button_select", up=False)
            else:
                # No viewport displayable found, please fix?
                # Trigger the button select still.
                renpy.queue_event("button_select", up=False)
            return
    
    class SetBookUIFocus(Action):
        """
        An action that uses SetFocus as a base, to set the appropriate focus of the Book UI menu elements.
        Arguments are "focused_element" and "direction". 

        focused_element: This argument must equal the id of the currently focused displayable.
        direction: '-1' if you want to go up the list, '1' if you want to go down the list.
        """
        def __init__(self, focused_element, direction, layer="screens"):
            self.layer = layer
            self.direction = direction
            self.focused_element = focused_element
        def get_sensitive(self):
            ## Only sensitive if this isn't already the currently
            ## focused displayable
            focused = renpy.display.focus.get_focused()
            desired = get_book_ui_focus(self.focused_element, self.direction)
            disp = renpy.get_displayable(desired[1], desired[0], self.layer)
            return focused is not disp
        def __call__(self):
            desired = get_book_ui_focus(self.focused_element, self.direction)
            renpy.set_focus(desired[1], desired[0], self.layer)
    
    ## Sets the focus to the correct game menu button
    ## ADDED FOR DEMO ##
    ## Fixed focus to have a fallback, and to still restart the interaction if found.
    class SetFocusGameMenuButton(Action):
        """ 
        An action that sets the focus to the appropriate displayable based on the 'game_menu' screen's 'title' value, only if the player is using a controller.
        This action is used so that once you enter the pause menu, the appropriate button is focused and the player's
        focus is not messed with by Ren'Py's focus orders.

        This is especially useful if you're in a point and click section, so you are not focusing the background buttons.
        
        If 'title' is not one a key of 'game_menu_button_maps', then we don't focus anything at all.
        """

        def __init__(self, title):
            self.title = title
        
        def __call__(self):
            if pad_config.is_using_controller() == False:
                return None
            
            if self.title in game_menu_button_maps:
                print(f"Setting focus to button with id {game_menu_button_maps[self.title]}")
                renpy.set_focus("navigation", game_menu_button_maps[self.title])
                renpy.restart_interaction()
            else:
                print(f"No button with the id {self.title} in game_menu_button_maps. Focusing history instead!")
                renpy.set_focus("navigation", "history_mb")
                renpy.restart_interaction()