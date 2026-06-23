## Fen: These are just some barebones functions to track and handle
## information for the stats. Once I've tested my StatManager more thoroughly,
## I may update this to include that!

## The stat names:
## pickedamour, pickedbetz
## pickedsight, pickedsmell, pickedhearing
## pickedstr, pickedint, pickedpsy

# default stats_smell = False
# default stats_sight = False
# default stats_hearing = False

# default stats_str = False
# default stats_int = False
# default stats_psy = False

# default stats_amour = False
# default stats_betz = False

init -500 python in feniks_stat_manager:
    from store import persistent, achievement

    def get_steam_id():
        """
        Safely return this user's Steam ID as a number, if available.
        """
        user_id = None
        if achievement.steam:
            ## Grab the user's ID
            try:
                user_id = achievement.steam.get_account_id()
            except Exception as e:
                ## Failed to get the ID; we'll go with the default
                ## case
                user_id = None
        return user_id

    def set_stat_true(name):
        """
        Toggle this stat to True (1) and prevent it from being toggled
        again by this Steam user.
        """
        user_id = get_steam_id()

        if user_id is not None:
            if name in persistent.feniks_recorded_stats.get(user_id, set()):
                ## Already recorded this stat; abort
                return
        else:
            if name in persistent.feniks_recorded_stats.get(None, set()):
                ## Already recorded this stat; abort
                return

        ## Otherwise, record it as having been chosen.
        if user_id is not None:
            if user_id not in persistent.feniks_recorded_stats:
                persistent.feniks_recorded_stats[user_id] = set()
            persistent.feniks_recorded_stats[user_id].add(name)
        if None not in persistent.feniks_recorded_stats:
            persistent.feniks_recorded_stats[None] = set()
        persistent.feniks_recorded_stats[None].add(name)

        ## Find the stat group this stat is in
        which_group = None
        for grp, items in stat_groups.items():
            if name in items:
                which_group = items
                break
        if not which_group and renpy.config.developer:
            renpy.error("Stat {} doesn't appear to be part of a group".format(name))
        elif which_group:
            ## Mark everything in this group as being chosen also
            for stat in which_group:
                if stat == name:
                    continue
                if user_id is not None:
                    persistent.feniks_recorded_stats[user_id].add(stat)
                persistent.feniks_recorded_stats[None].add(stat)

        ## Actually adjust the stat's value to 1
        if user_id is not None:
            if user_id not in persistent.feniks_persistent_stat_values:
                persistent.feniks_persistent_stat_values[user_id] = dict()
            persistent.feniks_persistent_stat_values[user_id][name] = 1
        if None not in persistent.feniks_persistent_stat_values:
            persistent.feniks_persistent_stat_values[None] = dict()
        persistent.feniks_persistent_stat_values[None][name] = 1

        if not achievement.steam:
            return # Not running on Steam

        ## Store it on Steam too
        achievement.steam.set_int_stat(name, 1)

    def test_global_stats():
        """A quick function to test global stats."""
        if not achievement.steam:
            return
        renpy.invoke_in_thread(
            achievement.steam.request_global_stats_and_run_callback,
            test_global_stats_callback
        )

    def test_global_stats_callback(ret):
        if not ret:
            print("Global stat request: request failed")
            return
        elif ret.value == achievement.steam.steamapi.k_EResultOK.value:
            print("Global stat request: success")
            ## We'll just print out all the stats
            for items in stat_groups.values():
                for item in items:
                    rv = achievement.steam.get_global_int_stat(item)
                    print("   ", item, ":", rv)
            return
        print("Global stat request: some other problem", ret, ret.value)
        return

define feniks_stat_manager.stat_groups = dict(
    route={'pickedamour', 'pickedbetz'},
    sense={'pickedsmell', 'pickedsight', 'pickedhearing'},
    insight={'pickedstr', 'pickedint', 'pickedpsy'},
)

## A dict of sets of stat names which have had their value changed and were
## pushed to the server at least once. The keys correspond to Steam user IDs
## and None for the general case.
default persistent.feniks_recorded_stats = dict()
## A dictionary of stat names to their values inside a dictionary with
## Steam user IDs + the None key for the general case.
default persistent.feniks_persistent_stat_values = dict()