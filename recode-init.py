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
from discord.utils import get

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
"American Samoa" : "AS",
"Arizona" : "AZ",
"Arkansas" : "AR",
"California" : "CA",
"Colorado" : "CO",
"Connecticut" : "CT",
"Delaware" : "DE",
"Washington, DC" : "DC",
"Florida" : "FL",
"Georgia" : "GA",
"Guam" : "GU",
"Hawaii" : "HI",
"Idaho" : "ID",
"Illinois": "IL",
"Indiana": "IN",
"Iowa" : "IA",
"Kansas": "KS",
"Kentucky": "KY",
"Louisiana" : "LA",
"Maine" : "ME",
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

stateReactionRoleData = {
#ABR : [roleID, :emoji_name:, postID]
# "Florida" : "FL",
# "Georgia" : "GA",
# "Guam" : "GU",
# "Hawaii" : "HI",
# "Idaho" : "ID",
# "Illinois": "IL",
# "Indiana": "IN",
# "Iowa" : "IA",
# "Kansas": "KS",
# "Kentucky": "KY",
"AK" : ["1202725827436085278", "<:server1:1212059088586805258>", "1211798235652423710"], #1st 1 
"AL" : ["1202725789037109290", "<:server0:1212059040675397712>", "1211798235652423710"], #1st 0 
"AR" : ["1202725897405210775", "<:server4:1212059094714687528>", "1211798235652423710"], #1st 4 
"AS" : ["1207796958794879100", "<:server2:1212059090935750677>", "1211798235652423710"], #1st 2 
"AZ" : ["1202725869525672010", "<:server3:1212059093481562233>", "1211798235652423710"], #1st 3 
"CA" : ["1202725981790670859", "<:server5:1212059096476286986>", "1211798235652423710"], #1st 5 
"CO" : ["1202726182710280262", "<:server6:1212059098091233300>", "1211798235652423710"], #1st 6 
"CT" : ["1202726031786774528", "<:server7:1212059098967969833>", "1211798235652423710"], #1st 7 
"DC" : ["1202728841504751687", "<:server9:1212059101320716358>", "1211798235652423710"], #1st 9 
"DE" : ["1202726227648192522", "<:server8:1212059099835924520>", "1211798235652423710"], #1st 8 
"FL" : ["1202726289476423741", ":regional_indicator_F:", "1202731356036005968"], #2nd 0 #"southern"
"GA" : ["1202726426537889843", ":regional_indicator_G:", "1202731356036005968"], #2nd 1 #"southern"
"GU" : ["1207797567627333632", ":regional_indicator_G:", "1203053376594772069"], #2nd 2 #"territories"
"HI" : ["1202726446569623593", ":regional_indicator_H:", "1202725835941871688"], #2nd 3 #"western"
"IA" : ["1202726553302081577", ":regional_indicator_A:", "1202725518890246217"], #2nd 7 #"midwestern"
"ID" : ["1202726466832437259", ":regional_indicator_I:", "1202725835941871688"], #2nd 4 #"western"
"IL" : ["1202726490593034292", ":regional_indicator_L:", "1202725518890246217"], #2nd 5 #"midwestern"
"IN" : ["1202726525405896754", ":regional_indicator_I:", "1202725518890246217"], #2nd 6 #"midwestern"
"KS" : ["1202726623389024404", ":regional_indicator_K:", "1202725518890246217"], #2nd 8 #"midwestern"
"KY" : ["1202726679185723422", ":regional_indicator_K:", "1202732644865941636"], #2nd 9 #"eastern"
"LA" : ["1202726758160404560", ":regional_indicator_L:", "1202731356036005968"], #3rd 0 #"southern"
"MA" : ["1202725605729116201", ":regional_indicator_M:", "1202721704774996079"], #3rd 3 #"north-eastern"
"MD" : ["1202726803639369768", ":regional_indicator_M:", "1202732644865941636"], #3rd 2 #"eastern"
"ME" : ["1202726787784769546", ":regional_indicator_N:", "1202721704774996079"], #3rd 1 #"north-eastern"
"MI" : ["1202726856533614624", ":regional_indicator_M:", "1202725518890246217"], #3rd 4 #"midwestern"
"MN" : ["1202727443723591760", ":regional_indicator_T:", "1202721704774996079"], #3rd 5 #"north-eastern"
"MO" : ["1202727443723591760", ":regional_indicator_R:", "1202725518890246217"], #3rd 7 #"midwestern"
"MP" : ["1208110392761389177", ":regional_indicator_M:", "1203053376594772069"], #4th 7 #"territories"
"MS" : ["1202727521188315137", ":regional_indicator_M:", "1202731356036005968"], #3rd 6 #"southern"
"MT" : ["1202727107982139473", ":regional_indicator_M:", "1202725835941871688"], #3rd 8 #"western"
"NC" : ["1202727886948278353", ":regional_indicator_N:", "1202732644865941636"], #4th 5 #"eastern"
"ND" : ["1202727951356002376", ":regional_indicator_N:", "1202725518890246217"], #4th 6 #"midwestern"
"NE" : ["1202727580688711760", ":regional_indicator_B:", "1202725518890246217"], #3rd 9 #"midwestern"
"NH" : ["1202727765015527445", ":regional_indicator_H:", "1202721704774996079"], #4th 1 #"north-eastern"
"NJ" : ["1202727809555107890", ":regional_indicator_J:", "1202721704774996079"], #4th 2 #"north-eastern"
"NM" : ["1202727834427064320", ":regional_indicator_N:", "1202731356036005968"], #4th 3 #"southern"
"NV" : ["1202727744325287957", ":regional_indicator_N:", "1202725835941871688"], #4th 0 #"western"
"NY" : ["1202727859878240296", ":regional_indicator_Y:", "1202721704774996079"], #4th 4 #"north-eastern"
"OH" : ["1202727977478262834", ":regional_indicator_O:", "1202725518890246217"], #4th 8 #"midwestern"
"OK" : ["1202728113721577562", ":regional_indicator_O:", "1202731356036005968"], #4th 9 #"southern"
"OR" : ["1202728134642901022", ":regional_indicator_O:", "1202725835941871688"], #5th 0 #"western"
"PA" : ["1202728166456565831", ":regional_indicator_P:", "1202721704774996079"], #5th 1 #"north-eastern"
"PR" : ["1208111221300002836", ":regional_indicator_P:", "1203053376594772069"], #5th 2 #"territories"
"RI" : ["1202728206701166592", ":regional_indicator_R:", "1202721704774996079"], #5th 3 #"north-eastern"
"SC" : ["1202728254990061648", ":regional_indicator_S:", "1202732644865941636"], #5th 4 #"eastern"
"SD" : ["1202728300565368853", ":regional_indicator_S:", "1202725518890246217"], #5th 5 #"midwestern"
"TN" : ["1202728540987199518", ":regional_indicator_T:", "1202732644865941636"], #5th 6 #"eastern" 
"TX" : ["1202728587002650624", ":regional_indicator_T:", "1202731356036005968"], #5th 7 #"southern"
"UT" : ["1202728725226193036", ":regional_indicator_U:", "1202725835941871688"], #5th 8 #"western"
"VA" : ["1202728774672842843", ":regional_indicator_V:", "1202732644865941636"], #6th 0 #"eastern" 
"VI" : ["1208112579235283014", ":regional_indicator_V:", "1203053376594772069"], #6th 1 #"territories"
"VT" : ["1202728746663018576", ":regional_indicator_V:", "1202721704774996079"], #5th 9 #"north-eastern"
"WA" : ["1202728794343997481", ":regional_indicator_W:", "1202725835941871688"], #6th 2 #"western" 
"WI" : ["1202728976733184030", ":regional_indicator_W:", "1202725518890246217"], #6th 4 #"midwestern"
"WV" : ["1202728921825677383", ":regional_indicator_W:", "1202732644865941636"], #6th 3 #"eastern"
"WY" : ["1202729013252984892", ":regional_indicator_Y:", "1202725835941871688"]  #6th 5 #"western"
}


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

#making it easier to call the tree to add functions
the_tree = client.tree

##########################
# ASYNCHRONOUS FUNCTIONS #
###########################



@client.event
async def on_ready():
    #prints this when bot has connected to discord
    await the_tree.sync(guild=discord.Object(id=1200191417457324069))
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_raw_reaction_add(reaction):
    channelID = '1202360433768677396'
    guild=discord.Object(id=1200191417457324069)
    emoji=reaction.emoji
    print(reaction.emoji)
    for i in stateReactionRoleData:
        state_react=stateReactionRoleData[i]   
        if reaction.channel_id != channelID:
            continue 
        if emoji == f"<{state_react[1]}>":
           # add_roles(*roles, reason=None, atomic=True)
            await reaction.member.add_roles(get(guild.roles, id=state_react[0]), reason="reaction", atomic=True)

#function to add money to a user
async def add_money(self, user, channel, username, user_pfp, reception_user, amount, recept_uname):
         # load json
         json_file = open(self.pathToJson, "r")
         json_content = json.load(json_file)
         reception_user_index, new_data = self.find_index_in_db(json_content["userdata"], reception_user)

         if new_data != "none":
             json_content["userdata"] = new_data

         json_recept_content = json_content["userdata"][reception_user_index]

         json_recept_content["cash"] += int(amount)

         # inform user
         color = self.discord_success_rgb_code
         embed = discord.Embed(
         description=f"✅  Added {str(self.currency_symbol)} {'{:,}'.format(int(amount))} to <@{recept_uname.id}>'s cash balance",
             color=color)
         embed.set_author(name=username, icon_url=user_pfp)
         await channel.send(embed=embed)

         # overwrite, end
         json_content["userdata"][reception_user_index] = json_recept_content
         self.overwrite_json(json_content)

         return "success", "success"

#Function to remove money from a user
async def remove_money(self, user, channel, username, user_pfp, reception_user, amount, recept_uname):
         # load json
         json_file = open(self.pathToJson, "r")
         json_content = json.load(json_file)
         reception_user_index, new_data = self.find_index_in_db(json_content["userdata"], reception_user)

         if new_data != "none":
             json_content["userdata"] = new_data

         json_recept_content = json_content["userdata"][reception_user_index]

         json_recept_content["cash"] -= int(amount)

         # inform user
         color = self.discord_success_rgb_code
         embed = discord.Embed(
             description=f"✅  Removed {str(self.currency_symbol)} {'{:,}'.format(int(amount))} from <@{recept_uname.id}>'s cash balance",
             color=color)
         embed.set_author(name=username, icon_url=user_pfp)
         await channel.send(embed=embed)

         # overwrite, end
         json_content["userdata"][reception_user_index] = json_recept_content
         self.overwrite_json(json_content)

         return "success", "success"



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
    if state_or_region in stateRegionNamesAndAbbrevs:
        state_or_region = stateRegionNamesAndAbbrevs.get(state_or_region)
    if state_or_region not in validStatesRegionsAndRoles:
        await interaction.response.send_message(f"Sorry, no state or region exists with the name or abbreviation \"{state_or_region}\".")
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
    print(f"{channel}")    
    if channel:
        message = f"Are you looking for Adderall in {city}, {state_or_region}? React with a ⏫ to this post to indicate your interest in a {city} channel! When this gets to 5 votes, the channel will be created."
        post = await channel.send(message)

        embed = discord.Embed()
        embed.description = f"Your suggestion is now available to be voted on! See the poll at https://discord.com/channels/1200191417457324069/1202356899773685770/{post.id} ."

        # Add the post ID (post.id) to the suggestionPosts part of the database
        #database.add_suggestion(city, stateOrRegionAbbr, suggestion_post.id)
        await interaction.response.send_message(embed=embed)
    else:

        await interaction.response.send_message("Couldn't find the #city-proposal channel.")
    return

#Function to buy items
async def buy_item(self, user, channel, username, user_pfp, item_name, amount, user_roles, server_object,
                        user_object):
         # load json
         json_file = open(self.pathToJson, "r")
         json_content = json.load(json_file)

         json_items = json_content["items"]
         item_found = item_index = 0
         for i in range(len(json_items)):
             if json_items[i]["name"] == item_name:
                 item_found = 1
                 item_index = i
         if not item_found:
             return "error", "Item not found."
         item = json_items[item_index]
         # get variables
         item_name = item_name
         item_price = item["price"]
         req_roles = item["required_roles"]
         give_roles = item["given_roles"]
         rem_roles = item["removed_roles"]
         max_bal = item["maximum_balance"]
         remaining_stock = item["amount_in_stock"]
         expiration_date = item["expiration_date"]
         reply_message = item["reply_message"]

         # calculate expiration
         today = datetime.today()
         expire = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S.%f")
         if today > expire:
             return "error", f"Item has already expired. Expiring date was {expiration_date}"
         # else we're good

         # 1. check req roles
         try:
             if req_roles == "none":
                 pass
             else:
                 for i in range(len(req_roles)):
                     if int(req_roles[i]) not in user_roles:
                         return "error", f"User does not seem to have all required roles."
         except Exception as e:
             print(e)
             return "error", f"Unexpected error."

         # 2. check give roles
         try:
             if rem_roles == "none":
                 pass
             else:
                 for i in range(len(rem_roles)):
                     role = discord.utils.get(server_object.roles, id=int(rem_roles[i]))
                     print(role)
                     await user_object.remove_roles(role)
         except Exception as e:
             print(e)
             return "error", f"Unexpected error."

         # 3. check rem roles
         try:
             if req_roles == "none":
                 pass
             else:
                 for i in range(len(give_roles)):
                     role = discord.utils.get(server_object.roles, id=int(give_roles[i]))
                     print(role)
                     await user_object.add_roles(role)
         except Exception as e:
             print(e)
             return "error", f"Unexpected error."

         # 4. check if enough money
         sum_price = item_price * amount
         sum_price = round(sum_price, 0)
         user_index, new_data = self.find_index_in_db(json_content["userdata"], user)
         user_content = json_content["userdata"][user_index]
         user_cash = user_content["cash"]
         if user_cash < sum_price:
             return "error", f"Error! Not enough money in cash to purchase.\nto pay: {sum_price} ; in cash: {user_cash}"

         # 5. rem money, print message, add to inventory
         user_content["cash"] -= sum_price
    
         if user_content["items"] == "none":
             user_content["items"] = [[item_name, amount]]
         else:
             user_content["items"].append([item_name, amount])

         color = self.discord_blue_rgb_code
         embed = discord.Embed(
             description=f"You have bought {amount} {item_name} and paid {str(self.currency_symbol)} **{'{:,}'.format(int(sum_price))}**",
             color=color)
         embed.set_author(name=username, icon_url=user_pfp)
         embed.set_footer(text=reply_message)
         await channel.send(embed=embed)

         # overwrite, end
         json_content["userdata"][user_index] = user_content
         json_content["items"] = json_items
         self.overwrite_json(json_content)

         return "success", "success"


#############
# START BOT #
#############

client.run(TOKEN)
