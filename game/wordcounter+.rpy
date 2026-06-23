###############################################################################################################
### LINT+ REN'PY WORD COUNTER  ################################################################################
###############################################################################################################
#
# Thanks for downloading Lint+! ( https://kigyo.itch.io/renpy-word-counter )
# Below are a bunch of variables that let you customize the generated output according to your needs.
#
# Your purchase also lets you access additional features: label-based statistics & progress tracking!
# You can now get a detailed analysis of how many lines/words are in each label of your game, 
# and see how many words were written since Lint was last run.
#
# Thank you, and may this tool help track your progress better than ever! :D
# - KigyoDev

## Preferences: Progress ###################################################################################################

# Display your progress since last time Lint was used (True by default)
define wordcounter_progress = True

# Display your progress since your last defined threshold ("save" by default)
#      "save": Saves a new word count to use for a later "load" 
#              (You'll typically only want to run this once, and then switch to "load")
#              Note: Saved word counts are deleted when persistent is cleared!
#      "load": Displays statistics compared to your last saved word count
# [INT, INT] : Provide a fixed line and word count to reference (e.g. [7894, 145562])
#      False : Disables this feature
define wordcounter_last_version = "save"

## Preferences: Counters ################################################################################################

# Line and word counts for every character
# default value: True
define wordcounter_characters = True

# Line and word counts for each .rpy file
# default value: True
define wordcounter_files = True

# Line and word counts for every character, within each .rpy file
# default value: True
define wordcounter_character_files = True

# Display the number of menus and available choices in the game
# default value: True
define wordcounter_menu_choices = True

# Count words from choice menus as well
# default value: True
define wordcounter_menu_is_character = False
# What the choices are called in the counter
# default value: "CHOICES"
define wordcounter_menu_name = "CHOICES"

# Show character/symbol counts, which might be too much detail - otherwise only displays number of lines and words
# default value: False
define wordcounter_display_character_count = False

# Line and word counts for every label
# default value: True
define wordcounter_labels = True

# The old character statistics which only displays line counts
# default value: False
define config.lint_character_statistics = False

## Preferences: File paths ################################################################################################

# Name of the folder your script files are in, if any. This can make the generated output look nicer.
#   Example: "script/"
# default value: ""
define script_folder_path = ""

# List of folders and files you want to ignore.
#   Example: if you want to make sure nothing in the "unused" folder and the "script.rpy" file is counted, write ["unused", "script.rpy"]
#   Note: Be careful with unintentionally matching filenames! Ignoring "no" will also ignore any folders and file names containing "no".
# default value: []
define script_ignore_path = []


## Preferences: Characters ################################################################################################

# List of equivalent characters that should be counted as one. Given ("x", "y"), "y" will be counted as "x".
#   Example: if "ann", "xann", and "nann" should all be considered "ann", write [("ann", "xann"), ("ann", "nann")]
# default value: []
define wordcounter_same = []

# List of characters who should be hidden from the character statistics. They still contribute to the total file word count.
# default value: ["extend"]
define wordcounter_hidden = ["extend"]

# List of characters who should not count towards any word counts.
# default value: []
define wordcounter_uncounted = []



###############################################################################################################
### The Code ##################################################################################################
###############################################################################################################

init python:

    import collections

    # The main function
    def wordcounter():

        all_stmts = list(renpy.game.script.all_stmts)
        all_stmts.sort(key=lambda n : n.filename)

        charastats = collections.defaultdict(Count)
        filestats = collections.defaultdict(Count)
        labelstats = collections.defaultdict(Count)
        filecharastats = {}
        filelabelstats = {}

        menu_count = 0
        options_count = 0
        choice_chara = wordcounter_menu_name

        last_label = "start"
        unignored_name = "game/" + script_folder_path + "TOTAL"

        filecharastats[unignored_name] = collections.defaultdict(Count)
        filelabelstats[unignored_name] = collections.defaultdict(Count)

        for node in all_stmts:
            if isinstance(node, renpy.ast.Say):
                speaker = node.who
                for i in wordcounter_same:
                    if i[1] == speaker:
                        speaker = i[0]
                        break
                
                if not_ignored_path(node.filename) and speaker not in wordcounter_uncounted:
                    filestats[unignored_name].add(node.what)
                    filestats[node.filename].add(node.what)
                    labelstats[last_label].add(node.what)

                    if node.filename not in filecharastats:
                        filecharastats[node.filename] = collections.defaultdict(Count)
                    if node.filename not in filelabelstats:
                        filelabelstats[node.filename] = collections.defaultdict(Count)

                    if speaker not in wordcounter_hidden:
                        charastats[speaker if speaker else 'narrator' ].add(node.what)
                        filecharastats[node.filename][speaker if speaker else 'narrator' ].add(node.what)
                    
                    filelabelstats[node.filename][last_label].add(node.what)


            elif isinstance(node, renpy.ast.Menu):
                menu_count += 1
                for l, c, b in node.items:
                    options_count += 1
                    if not_ignored_path(node.filename) and wordcounter_menu_is_character:
                        filestats[unignored_name].add(l)
                        filestats[node.filename].add(l)
                        labelstats[last_label].add(l)
                        charastats[choice_chara].add(l)

                        if node.filename not in filecharastats:
                            filecharastats[node.filename] = collections.defaultdict(Count)
                        if node.filename not in filelabelstats:
                            filelabelstats[node.filename] = collections.defaultdict(Count)

                        filecharastats[node.filename][choice_chara].add(l)
                        filelabelstats[node.filename][last_label].add(l)
            
            elif isinstance(node, renpy.ast.Label):
                last_label = node.name

        if renpy.config.developer and wordcounter_characters:
            print("\n")
            report_character_stats(charastats)

        if renpy.config.developer and wordcounter_files and wordcounter_labels:
            print("\n")
            report_file_label_stats(filestats, filelabelstats)
        elif renpy.config.developer and wordcounter_files:
            print("\n")
            report_file_stats(filestats)
        elif renpy.config.developer and wordcounter_labels:
            print("\n")
            report_label_stats(labelstats)

        if renpy.config.developer and wordcounter_character_files:
            print("\n")
            report_file_chara_stats(filestats, filecharastats)
        
        if renpy.config.developer and wordcounter_menu_choices:
            print("\n")
            report_menu_stats(menu_count, options_count)


    # This makes sure the above function is actually called whenever you use Lint
    config.lint_hooks.append(wordcounter)

    def not_ignored_path(filename):
        for i in script_ignore_path:
            if i in filename:
                return False
        return True

    # The print functions:
    def report_character_stats(charastats, title = True):

        if title:
            print("Character statistics:")

        count_to_char = collections.defaultdict(list)

        for char in charastats:
            count_to_char[charastats[char].blocks].append(char)

        for count, chars in sorted(count_to_char.items(), reverse=True):
            chars.sort()

            if len(chars) == 1:
                start = chars[0] + " has "
                end = humanize(charastats[chars[0]].words)
            elif len(chars) == 2:
                start = chars[0] + " and " + chars[1] + " have "
                end = humanize(charastats[chars[0]].words) + " and " + humanize(charastats[chars[1]].words)
            else:
                start = ", ".join(chars[:-1]) + ", and " + chars[-1] + " have "
                end = ""
                for char in chars[:-1]:
                    end += humanize(charastats[char].words) + ", "
                end += "and " + humanize(charastats[chars[-1]].words)

            print(" * " + start + humanize(count) +
                (" line" if count == 1 else " lines") + ", and " +
                end + " words" + (" each." if len(chars) > 1 else ".") )

    def report_label_stats(labelstats, title = True, filestats = None):

        if title:
            print("Label statistics:")

        count_to_char = collections.defaultdict(list)

        longest_name = 20
        longest_blocks = 5
        longest_words = 6
        blank = " "
        total_text = "TOTAL"

        for lbl in labelstats:
            if len(lbl) >= longest_name:
                longest_name = len(lbl)
            if len(humanize(labelstats[lbl].blocks)) > longest_blocks:
                longest_blocks = len(humanize(labelstats[lbl].blocks))
            if len(humanize(labelstats[lbl].words)) > longest_words:
                longest_words = len(humanize(labelstats[lbl].words))
        
        if filestats:
            if len(total_text) >= longest_name:
                longest_name = len(total_text)
            if len(humanize(filestats.blocks)) > longest_blocks:
                longest_blocks = len(humanize(filestats.blocks))
            if len(humanize(filestats.words)) > longest_words:
                longest_words = len(humanize(filestats.words))

        for lbl in labelstats:
            if wordcounter_display_character_count:
                print(" * " + lbl + "  |" + humanize(labelstats[lbl].blocks) +
                        " lines, " + humanize(labelstats[lbl].words) + " words, and " + humanize(labelstats[lbl].characters) + " characters.")
            else:
                print("  *  " + ((longest_name-len(lbl))*blank) + lbl + "  |  " + ((longest_blocks-len(humanize(labelstats[lbl].blocks))) * blank) + humanize(labelstats[lbl].blocks) + "  |  " + ((longest_words-len(humanize(labelstats[lbl].words)))*blank) + humanize(labelstats[lbl].words))
        if filestats:
            print("  *  " + ((longest_name-len(total_text))*blank) + total_text + "  |  " + (((longest_blocks-len(humanize(filestats.blocks))) * blank)) + humanize(filestats.blocks) + "  |  " + ((longest_words-len(humanize(filestats.words)))*blank) + humanize(filestats.words))

                        
    def report_file_label_stats(filestats, filelabelstats):

        print("File & Label statistics:")

        count_to_char = collections.defaultdict(list)

        for file in filestats:
            print("[" + file[5+len(script_folder_path):] + "] contains " + humanize(filestats[file].blocks) +
                    " lines and " + humanize(filestats[file].words) + " words:")

            if file == "game/" + script_folder_path + "TOTAL":
                longest_name = 20
                longest_blocks = 10
                longest_words = 11
                blank = " "
                total_text = "TOTAL"

                if wordcounter_last_version:
                    if wordcounter_last_version == "save":
                        persistent.wordcounter_last_version_count = int(filestats[file].words)
                        persistent.wordcounter_last_version_blocks = int(filestats[file].blocks)
                        print("  *  Current word counts saved for later!")
                    elif isinstance(wordcounter_last_version, list) and len(wordcounter_last_version) == 2:
                        persistent.wordcounter_last_version_blocks = int(wordcounter_last_version[0])
                        persistent.wordcounter_last_version_count = int(wordcounter_last_version[1])

                    if wordcounter_last_version == "load" or isinstance(wordcounter_last_version, list) and len(wordcounter_last_version) == 2:
                        difference = filestats[file].words - persistent.wordcounter_last_version_count
                        difference_blocks = filestats[file].blocks - persistent.wordcounter_last_version_blocks
                        difference_prefix = "+"
                        difference_blocks_prefix = "+"
                        if difference < 0:
                            difference_prefix = ""
                        if difference_blocks < 0:
                            difference_blocks_prefix = ""
                        if difference == 0:
                            difference = len(humanize(persistent.wordcounter_last_version_count)) * "-"
                        else:
                            difference = difference_prefix + humanize(difference)
                        if difference_blocks == 0:
                            difference_blocks = len(humanize(persistent.wordcounter_last_version_blocks)) * "-"
                        else:
                            difference_blocks = difference_blocks_prefix + humanize(difference_blocks)

                        print("  *  " + ((longest_name-len('previous save'))*blank) + 'previous save' + "  |  " + (((longest_blocks-len(humanize(persistent.wordcounter_last_version_blocks))) * blank)) + humanize(persistent.wordcounter_last_version_blocks) + "  |  " + ((longest_words-len(humanize(persistent.wordcounter_last_version_count)))*blank) + humanize(persistent.wordcounter_last_version_count))
                        print("  *  " + ((longest_name-len('DIFFERENCE'))*blank) + 'DIFFERENCE' + "  |  " + (((longest_blocks-len(difference_blocks)) * blank)) + difference_blocks + "  |  " + ((longest_words-len(difference))*blank) + difference)
                    
                    else:
                        print("  *  Invalid value for \"wordcounter_last_version\". Please make sure it says either \"save\" or \"load\".")
                        
                if wordcounter_progress:
                    difference = filestats[file].words - persistent.wordcounter_last_count
                    difference_blocks = filestats[file].blocks - persistent.wordcounter_last_blocks
                    difference_prefix = "+"
                    difference_blocks_prefix = "+"
                    if difference < 0:
                        difference_prefix = ""
                    if difference_blocks < 0:
                        difference_blocks_prefix = ""
                    if difference == 0:
                        difference = len(humanize(persistent.wordcounter_last_count)) * "-"
                    else:
                        difference = difference_prefix + humanize(difference)
                    if difference_blocks == 0:
                        difference_blocks = len(humanize(persistent.wordcounter_last_blocks)) * "-"
                    else:
                        difference_blocks = difference_blocks_prefix + humanize(difference_blocks)

                    print("  *  " + ((longest_name-len('previous lint'))*blank) + 'previous lint' + "  |  " + (((longest_blocks-len(humanize(persistent.wordcounter_last_blocks))) * blank)) + humanize(persistent.wordcounter_last_blocks) + "  |  " + ((longest_words-len(humanize(persistent.wordcounter_last_count)))*blank) + humanize(persistent.wordcounter_last_count))
                    print("  *  " + ((longest_name-len('DIFFERENCE'))*blank) + 'DIFFERENCE' + "  |  " + (((longest_blocks-len(difference_blocks)) * blank)) + difference_blocks + "  |  " + ((longest_words-len(difference))*blank) + difference)
                
                    persistent.wordcounter_last_count = int(filestats[file].words)
                    persistent.wordcounter_last_blocks = int(filestats[file].blocks)

                print("  *  " + ((longest_name-len(total_text))*blank) + total_text + "  |  " + (((longest_blocks-len(humanize(filestats[file].blocks))) * blank)) + humanize(filestats[file].blocks) + "  |  " + ((longest_words-len(humanize(filestats[file].words)))*blank) + humanize(filestats[file].words))

            else:
                report_label_stats(filelabelstats[file], False, filestats[file])
            print("")

    def report_file_stats(filestats):

        print("File statistics:")

        count_to_char = collections.defaultdict(list)

        for file in filestats:
            if wordcounter_display_character_count:
                print(" * [" + file[5+len(script_folder_path):] + "] contains " + humanize(filestats[file].blocks) +
                        " lines, " + humanize(filestats[file].words) + " words, and " + humanize(filestats[file].characters) + " characters.")
            else:
                print(" * [" + file[5+len(script_folder_path):] + "] contains " + humanize(filestats[file].blocks) +
                        " lines and " + humanize(filestats[file].words) + " words.")

    def report_file_chara_stats(filestats, filecharastats):

        print("Detailed File statistics:")

        count_to_char = collections.defaultdict(list)

        for file in filestats:
            print("[" + file[5+len(script_folder_path):] + "] contains " + humanize(filestats[file].blocks) +
                    " lines and " + humanize(filestats[file].words) + " words:")
            report_character_stats(filecharastats[file], False)
            print("")
    
    def report_menu_stats(menu_count, options_count):

        print("Menu statistics:")

        print("The game has " + str(menu_count) + " menus, with a total of " + str(options_count) + " possible choices, \nfor an average of " +
        "{:,.2f}".format(options_count and options_count/menu_count or 0) + " choices per menu.")
    

    # Auxiliary functions directly copied from lint.py - I take no credit for these:
    def humanize(n):
        s = str(n)
        rv = []
        for i, c in enumerate(reversed(s)):
            if i and not (i % 3):
                rv.insert(0, ',')
            rv.insert(0, c)
        return ''.join(rv)

    class Count(object):
        def __init__(self):
            self.blocks = 0
            self.words = 0
            self.characters = 0

        def add(self, s):
            self.blocks += 1
            self.words += len(s.split())
            self.characters += len(s)

# Saved values for your progress stats. Editing these directly won't do anything
default persistent.wordcounter_last_count = 0
default persistent.wordcounter_last_blocks = 0
default persistent.wordcounter_last_version_count = 0
default persistent.wordcounter_last_version_blocks = 0

init python:
    build.classify("**wordcounter**.rpy", None)
    build.classify("**wordcounter**.rpyc", "archive")