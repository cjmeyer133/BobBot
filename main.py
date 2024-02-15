#this should be the code for the bot, but honestly IDK what I'm doing so don't mind how Frankenstein it is

#use command pip install 
#for discord, asyncpg, keep?

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




            