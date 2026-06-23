################################################################################
##
## Stat Manager for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v0.9
##
################################################################################
## This file contains code for managing statistics in Ren'Py. It can also
## integrate with Steam to aggregate stats for all players, allowing for
## statistics like "10% of players never found the amulet" or "60% of players
## chose to go on a beach date".
## This file contains wrapper functions for some Steam API functions which
## do not currently exist in the engine and are needed to access global stats.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## If you'd like to see how to use this tool, check the other file,
## stat_manager_examples.rpy! This is just the backend; you don't need to
## understand everything in this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################

init -999 python in _renpysteam:

    def get_global_float_stat(name):
        """
        :doc: steam_stats

        Returns the global value of the stat with `name`, or None if no such
        stat exists.
        """
        from ctypes import c_float, byref

        rv = c_float(0)

        if not steamapi.SteamUserStats().GetGlobalStatDouble(name.encode("utf-8"), byref(rv)):
            return None

        return rv.value

    def get_global_int_stat(name):
        """
        :doc: steam_stats

        Returns the global value of the stat with `name`, or None if no such
        stat exists.
        """
        from ctypes import c_longlong, byref

        rv = c_longlong(0)

        if not steamapi.SteamUserStats().GetGlobalStatInt64(name.encode("utf-8"), byref(rv)):
            return None

        return rv.value

    def set_avgrate_stat(name, count_this_session, session_length):
        """
        :doc: steam_stats

        Updates an AVGRATE stat with new values.

        To submit the stats to the server you must call StoreStats.Call
        :func:`_renpysteam.store_stats` to push this change to the server.

        Returns True if the call was successful, False otherwise.
        """
        from ctypes import c_double, c_float
        count_this_session = c_float(count_this_session)
        session_length = c_double(session_length)

        return steamapi.SteamUserStats().UpdateAvgRateStat(name.encode("utf-8"),
            count_this_session, session_length)

    def request_global_stats(days=0):
        """
        :doc: steam_stats

        Asynchronously fetches global stats data, which is available for stats
        marked as "aggregated" in the App Admin panel of the Steamworks website.

        `days`
            How many days of day-by-day history to retrieve in addition to the
            overall totals. The limit is 60. An integer.

        Returns:
            SteamAPICall_t to be used with a GlobalStatsReceived_t call result.
        """

        return steamapi.SteamUserStats().RequestGlobalStats(days)

    def get_global_stats_call_result(call):
        """
        :doc: steam_stats

        Returns the result of an API call to retrieve global Steam stats.

        `call`
            The SteamAPICall_t returned by the call to fetch global Steam stats.

        This returns an object of callback_type if the call completed, None if
        the call hasn't finished, and raises APIFailure if the call failed. (It's
        recommended that APIFailures are caught and the API call retried.)
        """

        return steamapi.get_api_call_result(call, steamapi.GlobalStatsReceived_t)

    def request_global_stats_and_run_callback(callback, days=0, max_tries=100):
        """
        :doc: steam_stats

        Requests global stats data via request_global_stats, and runs callback
        once the global stats have been fetched successfully. This should be
        called in a thread.

        `callback`
            A callable function which will be run after requesting the stats.
            It is passed a single value, False if the request failed, and the
            EResult object from a successfully returned callback if it succeeded.
        `days`
            How many days of day-by-day history to retrieve in addition to the
            overall totals. The limit is 60. An integer.
        `max_tries`
            How many times to retry the check to see if global stats are
            returned before timing out. A new attempt is performed every 0.1
            seconds.
        """
        from time import sleep

        ## Start by requesting the data.
        cb = request_global_stats(days)
        api_call_result = None
        num_tries = 0

        ## Now keep checking to see if the request was completed.
        while True:
            num_tries += 1
            if num_tries >= max_tries:
                break

            try:
                api_call_result = get_global_stats_call_result(cb)
            except Exception as e:
                api_call_result = None
                ## Try a new request if it fails
                cb = request_global_stats(days)

            if api_call_result:
                break

            # Sleep and try again
            sleep(0.1)

        if not api_call_result:
            ## Never did return successfully
            callback(False)
            return

        ## Otherwise, success! Run the callback. Pass it the result code
        callback(api_call_result.m_eResult)
        return

    def reset_all_stats(achievements_too=False):
        """
        :doc: steam_stats

        Resets the current users stats and, optionally achievements.

        This automatically calls StoreStats to persist the changes to the
        server. This should typically only be used for testing purposes during
        development.

        Returns: bool
            True indicating success; otherwise False.
        """
        return steamapi.SteamUserStats().ResetAllStats(achievements_too)