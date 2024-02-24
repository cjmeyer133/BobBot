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
GUILD=os.getenv('GUILD_ID')

########################
# INTENTS/CLIENT SETUP #
########################

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

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
