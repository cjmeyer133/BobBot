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


###############
# GLOBAL VARS #
###############

stateRegionNamesAndAbbrevs = {
"Alabama" : "AL",
"Alaska" : "AK",
"Arizona" : "AZ",
"Arkansas" : "AR",
"California" : "CA",
"Colorado" : "CO",
"Connecticut" : "CT",
"Delaware" : "DE",
"Washington, DC" : "DC",
"Florida" : "FL",
"Georgia" : "GA",
"Hawaii" : "HI",
"Idaho" : "ID",
"Illinois": "IL",
"Indiana": "IN",
"Iowa" : "IA",
"Kansas": "KS",
"Kentucky": "KY",
"Louisiana" : "LA",
"Maine" : "MA",
"Maryland" : "MD",
"Massachusetts" : "MA",
"Michigan" : "MI",
"Minnesota" : "MN",
"Mississippi" : "MS",
"Missouri" : "MO",
"Montana" : "MT",
"Nebraska" : "NE",
"Nevada" : "NV",
"New Hampshire" : "NH",
"New Jersey" : "NJ",
"New Mexico" : "NM",
"New York" : "NY",
"North Carolina" : "NC",
"North Dakota" : "ND",
"Northern Mariana Islands" : "MP",
"Ohio" : "OH",
"Oklahoma" : "OK",
"Oregon" : "OR",
"Pennsylvania" : "PA",
"Puerto Rico" : "PR",
"Rhode Island" : "RI",
"South Carolina" : "SC",
"South Dakota" : "SD",
"Tennessee" : "TN",
"Texas" : "TX",
"Utah" : "UT",
"Vermont" : "VT",
"Virginia" : "VA",
"U.S. Virgin Islands" : "VI",
"Washington" : "WA",
"West Virginia" : "WV",
"Wisconsin" : "WI",
"Wyoming" : "WY"}

validStatesRegionsAndRoles = {
"AK" : "1202725827436085278", 
"AL" : "1202725789037109290", 
"AR" : "1202725897405210775", 
"AS" : "1207796958794879100", 
"AZ" : "1202725869525672010", 
"CA" : "1202725981790670859", 
"CO" : "1202726031786774528", 
"CT" : "1202726182710280262", 
"DC" : "1202728841504751687", 
"DE" : "1202726227648192522",
"FL" : "1202726289476423741", 
"GA" : "1202726426537889843",
"GU" : "1207797567627333632", 
"HI" : "1202726446569623593", 
"IA" : "1202726553302081577", 
"ID" : "1202726466832437259", 
"IL" : "1202726490593034292", 
"IN" : "1202726525405896754", 
"KS" : "1202726623389024404", 
"KY" : "1202726679185723422", 
"LA" : "1202726758160404560", 
"MA" : "1202725605729116201", 
"MD" : "1202726803639369768", 
"ME" : "1202726787784769546", 
"MI" : "1202726856533614624", 
"MN" : "1202727443723591760", 
"MO" : "1202727443723591760", 
"MP" : "1208110392761389177", 
"MS" : "1202727521188315137", 
"MT" : "1202727107982139473", 
"NC" : "1202727886948278353", 
"ND" : "1202727951356002376", 
"NE" : "1202727580688711760", 
"NH" : "1202727765015527445", 
"NJ" : "1202727809555107890", 
"NM" : "1202727834427064320", 
"NV" : "1202727744325287957", 
"NY" : "1202727859878240296", 
"OH" : "1202727977478262834", 
"OK" : "1202728113721577562", 
"OR" : "1202728134642901022", 
"PA" : "1202728166456565831", 
"PR" : "1208111221300002836", 
"RI" : "1202728206701166592", 
"SC" : "1202728254990061648", 
"SD" : "1202728300565368853", 
"TN" : "1202728540987199518", 
"TX" : "1202728587002650624", 
"UT" : "1202728725226193036", 
"VA" : "1202728774672842843", 
"VI" : "1208112579235283014", 
"VT" : "1202728746663018576", 
"WA" : "1202728794343997481", 
"WI" : "1202728976733184030", 
"WV" : "1202728921825677383", 
"WY" : "1202729013252984892"}

#CREATE ME
#suggestionPosts = A table, loaded from database.json, with the following fields: postID (string, id, unique, not null), city (string, not null), stateOrRegion (string, key of [validStatesRegionsAndRoles], not null). Contains one entry for every city/state combo that has been suggested, but not approved.
#existingChannels = A table, loaded from database.json, with the following fields: channelID (string, id, unique, not null), city (string, not null), stateOrRegion (string, key of [validStatesRegionsAndRoles], not null). Contains one entry for every city/state combo that has been approved.

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
dClient = discord.Client(intents=discord.Intents.default())

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
    description="A test command with variables",
    guild=discord.Object(id=1200191417457324069)
)
async def create_item(interaction, itemname: str, cost: int):
    costs=str(cost)
    #in theory, it should be written to the database here
    await interaction.response.send_message(str(itemname+" costs $"+costs))

#Bot command: /suggest-channel param:city param:stateOrRegionAbbr ->
#If the state stateOrRegionAbbr is not one of the approved abbreviations, tell the user "Sorry, no state or region exists with the abbreviation [stateOrRegion]".
#If this city/state combo already exists, stop the user from suggesting it
#If this city/state combo was already suggested in suggestionPosts, stop the user from suggesting it and give them the link to the bot’s post
#Otherwise, make a post in the #city-proposal channel, e.g. "Are you looking for Adderall in [city], [stateOrRegion]? React with a ⏫to this post to indicate your interest in a [city] channel! When this gets to 5 votes, the channel will be created." Then, add the ID of this post to the suggestionPosts part of the database.
@the_tree.command(
    name='suggest-channel',
    description="Propose a new channel for your city!", 
    guild=discord.Object(id=1200191417457324069)
)
async def suggest_channel(interaction, city :str, state_or_region :str):
    # Check if the stateOrRegionAbbr is valid
    
    if state_or_region not in validStatesRegionsAndRoles:
        await interaction.response.send_message(f"Sorry, no state or region exists with the abbreviation \"{state_or_region}\". Try an abbreviation like \"MA\" or \"DC\".")
        return

    # Check if the city/state combo already exists
    # if database.check_existing_channel(city, stateOrRegionAbbr):
    #     await ctx.send("This city/state combo already has a channel.")
    #     return

    # Check if the city/state combo was already suggested
    # if database.check_existing_suggestion(city, stateOrRegionAbbr):
    #     suggestion_post_link = database.get_suggestion_post_link(city, stateOrRegionAbbr)
    #     await ctx.send(f"This city/state combo was already suggested. Here's the link: {suggestion_post_link}")
    #     return

    #Make a post in the #city-proposal channel
    channel = client.get_channel(1202356899773685770)
    print(f"{client.user}")
    print(f"{channel}")    
    if channel:
        message = f"Are you looking for Adderall in {city}, {state_or_region}? React with a ⏫ to this post to indicate your interest in a {city} channel! When this gets to 5 votes, the channel will be created."
        await channel.send(message)

        # Add the post ID to the suggestionPosts part of the database
        #database.add_suggestion(city, stateOrRegionAbbr, suggestion_post.id)
        await interaction.response.send_message("Your suggestion has been noted.")
    else:

        await interaction.response.send_message("Couldn't find the #city-proposal channel.")
    return


#############
# START BOT #
#############

client.run(TOKEN)
