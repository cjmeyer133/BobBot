#trying to get working commands/bot

###########
# IMPORTS #
###########
import os

import discord
import asyncio
from dotenv import load_dotenv

import json, time, random, math, sys
from datetime import datetime, timezone, timedelta
from random import randint

import logging
import logging.handlers

from discord.ext.commands import Bot
# custom database handler
import database
from time import sleep

from keep import alive

#############
# GET TOKEN #
#############

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


########################
# INTENTS/CLIENT SETUP #
########################

intents = discord.Intents.all()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = discord.app_commands.CommandTree(self)


client = MyClient(intents=intents)

##########################
# ASYNCHRONOUS FUNCTIONS #
###########################



@client.event
async def on_ready():
    #prints this when bot has connected to discord
    print(f'{client.user} has connected to Discord!')


#######################
# ON DEMAND FUNCTIONS #
#######################











#############
# START BOT #
#############

client.run(TOKEN)
