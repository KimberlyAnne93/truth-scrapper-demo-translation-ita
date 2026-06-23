###### VARIABLES FOR CONTROLLER SUPPORT AND PARALLAX #######

default v_cursor_enabled = True
# Will be set to "quick" or "book" depending on what is selected
default current_dpad_menu = None

default current_book_highlight = None

# Is the player in a game menu or not?
default is_in_menu = False

# Set this to "left", "right" or "both" to control what sticks move the cursor/parallax.
define stick_for_virtual_cursor = "both"
define stick_for_parallax = "both"

# I use this list to figure out the focus for the UI in the get_book_ui_focus function.
# This lists the book menu buttons from top to bottom.

# We store a tuple: 
    # [0] = the ID of the button that would be highlighted

define bookUI_vertical_order = [("menu_memories", "bookUI_memories", "bookUI_memories_fake"), 
                                ("menu_mystery", "bookUI_mystery", "bookUI_mystery_fake"),
                                ("menu_characters", "bookUI_characters", "bookUI_characters_fake"), 
                                ("menu_glossary", "bookUI_glossary", "bookUI_glossary_fake")]

## ADDED FOR DEMO ##
## Added the tutorial button to the map! ##
# Same story as the previous one, but for game menu buttons.
define game_menu_button_maps = { "History" : "history_mb", 
                                "Save" : "save_mb",
                                "Load" : "load_mb",
                                "Options" : "options_mb",
                                "About" : "about_mb",
                                "Tutorial" : "tutorial_mb" }
