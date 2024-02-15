#this should be the code for the bot, but honestly IDK what I'm doing so don't mind how Frankenstein it is

#from Unbelieva-Boat by github user h-ntai 
import json, os, time, random, math, sys, discord, math
from datetime import datetime, timezone, timedelta
from random import randint

# imports
import discord, os, json, sys
import random
from discord.ext.commands import Bot
# custom database handler
import database
from time import sleep

from keep import alive
#end from there

#from examples in discord.py github
import asyncio
import logging
import logging.handlers

from typing import List, Optional

import asyncpg  # asyncpg is not a dependency of the discord.py, and is only included here for illustrative purposes.
from discord.ext import commands
from discord import app_commands
from aiohttp import ClientSession
#end from there

alive()

# init discord stuff and json handling
BOT_PREFIX = ("gg")
BOT_PREFIX_LIST = ["gg"]
token = os.environ["token"]
# emojis
emoji_worked = "✅"
emoji_error = "❌"
discord_error_rgb_code = discord.Color.from_rgb(239, 83, 80)
intents = discord.Intents.all()
client = Bot(command_prefix=BOT_PREFIX, intents=intents)  # init bot
db_handler = database.pythonboat_database_handler(client)  # ("database.json")
with open("owner.json") as f:
    adminlist = json.load(f)

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
            