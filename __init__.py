#initializing things I think???

#from Unbelieva-Boat by github user h-ntai 
import json, os, time, random, math, sys, discord, math
from datetime import datetime, timezone, timedelta
from random import randint

#wow Unbelieva-Boat is gross, there's some changes in here. Hopefully not omitting anything necessary
class pythondiscord_bot_handler:
     def find_index_in_db(self, data_to_search, user_to_find, fail_safe=False):
        print(data_to_search)
        user_to_find = int(user_to_find)
        for i in range(len(data_to_search)):
            if data_to_search[i]["user_id"] == user_to_find:
                print("\nfound user\n")
                return int(i), "none"

        # in this case, this isnt a user which isnt yet registrated
        # but someone who doesnt exist on the server
        # or at least thats what is expected when calling with this parameter
        if fail_safe:
            return 0, "error"

        print("\ncreating user\n")
        # we did NOT find him, which means he doesn't exist yet
        # so we automatically create him
        data_to_search.append({
            "user_id": int(user_to_find),
            "cash": 0,
            "bank": 0,
        })

        # now that the user is created, re-check and return int

        for i in range(len(data_to_search)):
            if data_to_search[i]["user_id"] == user_to_find:
                return i, data_to_search