#trying to get working commands/bot

###########
# IMPORTS #
###########
import os

import discord
from discord.ext import commands

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

bot = commands.Bot(command_prefix="/",intents=intents)

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

the_tree = client.tree

##########################
# ASYNCHRONOUS FUNCTIONS #
###########################



@client.event
async def on_ready():
    #prints this when bot has connected to discord
    await the_tree.sync(guild=discord.Object(id=1200191417457324069))
    print(f'{client.user} has connected to Discord!')





#######################
# ON DEMAND FUNCTIONS #
#######################


# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that
# it will take some time (up to an hour) to register the
# command if it's for all guilds.
@the_tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=1200191417457324069)
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@the_tree.command(
    name="testing",
    description="A test command",
    guild=discord.Object(id=1200191417457324069)
)
async def create_item(self, itemname: str, cost: int):
    costs=str(cost)
    await self.response.send_message(str(itemname+" costs $"+costs))
    


#############
# START BOT #
#############

client.run(TOKEN)
