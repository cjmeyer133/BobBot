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
import database.__init__
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

voteEmoji = "<:ThumbsUpIcon:1209267015458627746>"
thanksEmoji = "<:ThumbsUpIcon:1209267015458627746>"

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
"AK" : ["1202725827436085278", "<:server1:1212191653767684096>", "1211798235652423710"], #1st 1 
"AL" : ["1202725789037109290", "<:server0:1212191652215660554>", "1211798235652423710"], #1st 0 
"AR" : ["1202725897405210775", "<:server4:1212191659836706837>", "1211798235652423710"], #1st 4 
"AS" : ["1207796958794879100", "<:server2:1212191656191721512>", "1211798235652423710"], #1st 2 
"AZ" : ["1202725869525672010", "<:server3:1212191657542553660>", "1211798235652423710"], #1st 3 
"CA" : ["1202725981790670859", "<:server5:1212191661464231996>", "1211798235652423710"], #1st 5 
"CO" : ["1202726182710280262", "<:server6:1212191663737544716>", "1211798235652423710"], #1st 6 
"CT" : ["1202726031786774528", "<:server7:1212191664999895062>", "1211798235652423710"], #1st 7 
"DC" : ["1202728841504751687", "<:server9:1212191667625525309>", "1211798235652423710"], #1st 9 
"DE" : ["1202726227648192522", "<:server8:1212191666304323655>", "1211798235652423710"], #1st 8 
"FL" : ["1202726289476423741", "<:server0:1212191652215660554>", "1211799377723654164"], #2nd 0
"GA" : ["1202726426537889843", "<:server1:1212191653767684096>", "1211799377723654164"], #2nd 1
"GU" : ["1207797567627333632", "<:server2:1212191656191721512>", "1211799377723654164"], #2nd 2 
"HI" : ["1202726446569623593", "<:server3:1212191657542553660>", "1211799377723654164"], #2nd 3
"IA" : ["1202726553302081577", "<:server7:1212191664999895062>", "1211799377723654164"], #2nd 7
"ID" : ["1202726466832437259", "<:server4:1212191659836706837>", "1211799377723654164"], #2nd 4
"IL" : ["1202726490593034292", "<:server5:1212191661464231996>", "1211799377723654164"], #2nd 5
"IN" : ["1202726525405896754", "<:server6:1212191663737544716>", "1211799377723654164"], #2nd 6
"KS" : ["1202726623389024404", "<:server8:1212191666304323655>", "1211799377723654164"], #2nd 8
"KY" : ["1202726679185723422", "<:server9:1212191667625525309>", "1211799377723654164"], #2nd 9 
"LA" : ["1202726758160404560", "<:server0:1212191652215660554>", "1211800515856433215"], #3rd 0 
"MA" : ["1202725605729116201", "<:server3:1212191657542553660>", "1211800515856433215"], #3rd 3 
"MD" : ["1202726803639369768", "<:server2:1212191656191721512>", "1211800515856433215"], #3rd 2 
"ME" : ["1202726787784769546", "<:server1:1212191653767684096>", "1211800515856433215"], #3rd 1 
"MI" : ["1202726856533614624", "<:server4:1212191659836706837>", "1211800515856433215"], #3rd 4 
"MN" : ["1202727443723591760", "<:server5:1212191661464231996>", "1211800515856433215"], #3rd 5 
"MO" : ["1202727443723591760", "<:server7:1212191664999895062>", "1211800515856433215"], #3rd 7 
"MP" : ["1208110392761389177", "<:server7:1212191664999895062>", "1211800848427126834"], #4th 7 
"MS" : ["1202727521188315137", "<:server6:1212191663737544716>", "1211800515856433215"], #3rd 6 
"MT" : ["1202727107982139473", "<:server8:1212191666304323655>", "1211800515856433215"], #3rd 8 
"NC" : ["1202727886948278353", "<:server5:1212191661464231996>", "1211800848427126834"], #4th 5 
"ND" : ["1202727951356002376", "<:server6:1212191663737544716>", "1211800848427126834"], #4th 6 
"NE" : ["1202727580688711760", "<:server9:1212191667625525309>", "1211800515856433215"], #3rd 9 
"NH" : ["1202727765015527445", "<:server1:1212191653767684096>", "1211800848427126834"], #4th 1 
"NJ" : ["1202727809555107890", "<:server2:1212191656191721512>", "1211800848427126834"], #4th 2 
"NM" : ["1202727834427064320", "<:server3:1212191657542553660>", "1211800848427126834"], #4th 3 
"NV" : ["1202727744325287957", "<:server0:1212191652215660554>", "1211800848427126834"], #4th 0 
"NY" : ["1202727859878240296", "<:server4:1212191659836706837>", "1211800848427126834"], #4th 4 
"OH" : ["1202727977478262834", "<:server8:1212191666304323655>", "1211800848427126834"], #4th 8 
"OK" : ["1202728113721577562", "<:server9:1212191667625525309>", "1211800848427126834"], #4th 9 
"OR" : ["1202728134642901022", "<:server0:1212191652215660554>", "1211802177077649470"], #5th 0 
"PA" : ["1202728166456565831", "<:server1:1212191653767684096>", "1211802177077649470"], #5th 1 
"PR" : ["1208111221300002836", "<:server2:1212191656191721512>", "1211802177077649470"], #5th 2 
"RI" : ["1202728206701166592", "<:server3:1212191657542553660>", "1211802177077649470"], #5th 3 
"SC" : ["1202728254990061648", "<:server4:1212191659836706837>", "1211802177077649470"], #5th 4 
"SD" : ["1202728300565368853", "<:server5:1212191661464231996>", "1211802177077649470"], #5th 5 
"TN" : ["1202728540987199518", "<:server6:1212191663737544716>", "1211802177077649470"], #5th 6  
"TX" : ["1202728587002650624", "<:server7:1212191664999895062>", "1211802177077649470"], #5th 7 
"UT" : ["1202728725226193036", "<:server8:1212191666304323655>", "1211802177077649470"], #5th 8 
"VA" : ["1202728774672842843", "<:server0:1212191652215660554>", "1211802403314077776"], #6th 0  
"VI" : ["1208112579235283014", "<:server1:1212191653767684096> ", "1211802403314077776"], #6th 1 
"VT" : ["1202728746663018576", "<:server9:1212191667625525309>", "1211802177077649470"], #5th 9 
"WA" : ["1202728794343997481", "<:server2:1212191656191721512> ", "1211802403314077776"], #6th 2  
"WI" : ["1202728976733184030", "<:server4:1212191659836706837>", "1211802403314077776"], #6th 4 
"WV" : ["1202728921825677383", "<:server3:1212191657542553660>", "1211802403314077776"], #6th 3 
"WY" : ["1202729013252984892", "<:server5:1212191661464231996>", "1211802403314077776"]  #6th 5 
}
state_names= list(stateRegionNamesAndAbbrevs.keys())
state_abbr= list(stateRegionNamesAndAbbrevs.values())

class the_role():
    def init(self, name, id):
        self.name=name
        self.id=id


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

db_handler = database.__init__.channel_db_handler(bot)  # ("channel_database.json")
reward_db_handler = database.__init__.reward_db_handler(bot) #("database/reward_database.json")
##########################
# ASYNCHRONOUS FUNCTIONS #
###########################



@client.event
async def on_ready():
    #prints this when bot has connected to discord
    await the_tree.sync(guild=discord.Object(id=1200191417457324069))
    checkResult = await db_handler.check_json()
    if(checkResult == "good"):
        print("Yay, opened the file correctly!")    
    else:
        print("The file database/channel_database.json failed to open properly")

    print(f'{client.user} has connected to Discord!')


@client.event
async def on_raw_reaction_add(reaction):
    the_guild=client.get_guild(1200191417457324069)
    emoji=str(reaction.emoji)
    postID=str(reaction.message_id)
    #check the #claim-roles channel's posts for numbers
    channelID = 1202360433768677396
    if reaction.channel_id == channelID:
        for i in stateReactionRoleData:
            state_react=stateReactionRoleData[i]
            if emoji == state_react[1] and postID == state_react[2]:
           # add_roles(*roles, reason=None, atomic=True)
                state_name=state_names[state_abbr.index(i)]
                role_use=the_role()
                the_role.init(role_use, state_name, int(state_react[0]))
                await reaction.member.add_roles(role_use, reason="reaction", atomic=True)
                member=reaction.member
                print('Role added to '+str(member))
                
                citylist=db_handler.find_city_by_state(i)
                if citylist == []:
                    citymsg="Thanks! There are no city channels for "+state_name+" yet, but you can propose a city channel in the server using the command /suggest-channel."
                if citylist != []:
                    citymsg="Thanks! Here are the city channels in "+state_name+": \n"
                for c in citylist:
                    city_name=c.get("city")
                    city_channel=str(c.get("channel_ID"))
                    citymsg=citymsg+city_name+" can be found at https://discord.com/channels/1200191417457324069/"+city_channel+" .\n"
                await member.send(citymsg)


    #check the #city-proposal channel's posts for votes (the thumbs up)
    proposalchannelID = 1202356899773685770
    cat_channel=the_guild.get_channel(1200192781004582962).category
    if reaction.channel_id == proposalchannelID:
        
        on_a_proposal_post = db_handler.find_entry_by_id("proposed", reaction.message_id)
        if on_a_proposal_post[0] != "error" and on_a_proposal_post[0] != -1:
            
            id_of_proposal_post = db_handler.find_id_by_index("proposed", on_a_proposal_post[0])
            print("here, we should \n1. check the number of thumbs up reactions on the post\n2. if that's more than 5, \n\t2a. make a channel for the city/state \n\t2b. remove this post from the proposed database and \n\t2c. add the new channel to the exisiting database")
            message = await client.get_channel(reaction.channel_id).fetch_message(reaction.message_id) #I think this line is weird
            
            #check the number of votes the message has
            thumbs_up_count = 0
            for reaction in message.reactions:
                if str(reaction.emoji) == voteEmoji:
                    thumbs_up_count = reaction.count

            #if it has enough votes...
            if thumbs_up_count > 1:
                #make a new channel for the proposed city and change the database to reflect that
                print("Make new channel here!")
                #grab the city and state/region from the database

                city = db_handler.find_city_by_index("proposed", on_a_proposal_post[0])
                abbr = db_handler.find_state_by_index("proposed", on_a_proposal_post[0])

                #name should be "city-stateorregion" in all lowercase, with spaces replaced with hyphens
                newChannelName = city.lower().replace(" ", "-")+"-"+abbr.lower().replace(" ", "-")
                channel_list=the_guild.channels
                for i in channel_list:
                    if i.name==newChannelName:
                        do_not_add=True
                        break
                    if i.name != newChannelName:
                        do_not_add=False
                        continue
                if do_not_add == False:
                    role=validStatesRegionsAndRoles.get(abbr)
                    user_role=the_guild.get_role(int(role))
                    #get the state from the dict to use it in the channel description
                    state = abbr
                    for key, value in stateRegionNamesAndAbbrevs.items():
                        if value == abbr:
                            state = key
                    print(f"abbr is {abbr} and state is {state}")
                    channel=await the_guild.create_text_channel(newChannelName, category=cat_channel, topic=f"Find Adderall in {city}, {state}. To make a request, run this command:\n/find-adderall-here param:ir_or_xr param:strength")
                    await channel.set_permissions(the_guild.default_role, read_messages=False)
                    await channel.set_permissions(user_role, read_messages=True)
                    #update the database appropriately
                    await db_handler.create_new_entry("existing", channel.id, city, abbr)
                    await db_handler.remove_entry("proposed", id_of_proposal_post)

    #check the city channels' threaded posts for thanks (the thumbs up)

@client.event
async def on_raw_reaction_remove(reaction):
    channelID = 1202360433768677396
    the_guild=client.get_guild(1200191417457324069)
    the_member=the_guild.get_member(reaction.user_id)
    guild=discord.Object(id=1200191417457324069)
    emoji=str(reaction.emoji)
    postID=str(reaction.message_id)
    print(reaction.emoji)
    if reaction.channel_id == channelID:
        for i in stateReactionRoleData:
            state_react=stateReactionRoleData[i]
            if emoji == state_react[1] and postID == state_react[2]:
           # add_roles(*roles, reason=None, atomic=True)
                state_name=state_names[state_abbr.index(i)]
                role_use=the_role()
                the_role.init(role_use, state_name, int(state_react[0]))
                await the_member.remove_roles(role_use, reason="reaction", atomic=True)
                print('Role removed') 






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
    city = city.strip() #remove any white space at the beginning or end of the city name
    # Check if the stateOrRegionAbbr is valid
    if state_or_region in stateRegionNamesAndAbbrevs:
        state_or_region = stateRegionNamesAndAbbrevs.get(state_or_region)
    if state_or_region not in validStatesRegionsAndRoles:
        await interaction.response.send_message(f"Sorry, no state or region exists with the name or abbreviation \"{state_or_region}\".")
        return


    index_in_existing = db_handler.find_city_state_in_db("existing", city, state_or_region)
    print(f"{index_in_existing} is where the city/state combo is in existing")
    # Check if the city/state combo already exists
    if int(index_in_existing) != -1:
        channel_link = db_handler.find_id_by_city_state("existing", city, state_or_region)
        await interaction.response.send_message(f"This city/state combo already has a channel. Here's a link to it: https://discord.com/channels/1200191417457324069/{channel_link}\nTo join it, be sure you've signed up for the {state_or_region} role by reacting with a {stateReactionRoleData.get(state_or_region)[1]} here https://discord.com/channels/1200191417457324069/1202360433768677396/{stateReactionRoleData.get(state_or_region)[2]}")
        return

    index_in_proposed = db_handler.find_city_state_in_db("proposed", city, state_or_region)
    print(f"{index_in_existing} is where the city/state combo is in proposed")
    # Check if the city/state combo was already suggested
    if int(index_in_proposed) != -1:
        suggestion_post_link = db_handler.find_id_by_city_state("proposed", city, state_or_region)
        await interaction.response.send_message(f"This city/state combo was already suggested. Here's the link: https://discord.com/channels/1200191417457324069/1202356899773685770/{suggestion_post_link}")
        return

    #Make a post in the #city-proposal channel
    channel = client.get_channel(1202356899773685770)
    print(f"{channel}")    
    if channel:
        message = f"Are you looking for Adderall in {city}, {state_or_region}? React with a <:ThumbsUpIcon:1209267015458627746> to this post to indicate your interest in a {city} channel! When this gets to 5 votes, the channel will be created."
        post = await channel.send(message)

        embed = discord.Embed()
        embed.description = f"Your suggestion is now available to be voted on! See the poll at https://discord.com/channels/1200191417457324069/1202356899773685770/{post.id} ."

        # Add the post ID (post.id) to the suggestionPosts part of the database
        await db_handler.create_new_entry("proposed", post.id, city, state_or_region)
        await interaction.response.send_message(embed=embed)
    else:

        await interaction.response.send_message("Couldn't find the #city-proposal channel.")
    return



@the_tree.command(
    name = "find-adderall-here", 
    description="Start a new thread to find a pharmacy that can fulfill your prescription.", 
    guild=discord.Object(id=1200191417457324069)
)
async def find_adderall_here(interaction, ir_or_xr:str, strength:str):
    #if the channel this command was used in is within the FIND-BY-CITY category, it can be used
    category = "find-by-city"
    if interaction.channel.category.name == category:
        #check to ensure the command was NOT sent in a thread
        if interaction.channel.type == "public_thread" or interaction.channel.type == "private_thread":
            await interaction.response.send_message(content=f"You can't run this command in a thread! Try running it in the main part of the channel.", ephemeral=True)
            return
        
        #check to ensure the ir/er param is valid
        ir = ["ir", "immediate release", "immediate"]
        xr = ["xr", "extended release", "extended"]
        if not (ir_or_xr.lower() in ir or ir_or_xr.lower() in xr):
            await interaction.response.send_message(content = f"The parameter \'ir_or_xr\' takes the release time of your prescription, either immediate release (ir) or extended release (xr). \n\"{ir_or_xr}\" could not be understood as either of those. Please try again.\n\nHint: If your prescription does not have the letters XR in it, it may be IR. Check with your doctor if you are unsure.", ephemeral = True)
            return 

        #check to ensure dosage is probably correct...
        if strength.lower().find("mg") == -1 and strength.lower().find("milligrams") == -1:
            await interaction.response.send_message(content = f"The parameter \'strength\' takes the strength of each capsule/tablet of Adderall in milligrams (mg) according to your prescription. \"{strength}\" was not understandable as a medicine strength. Try entering a number followed by \"mg\" or \"milligrams\".\nPlease try again.", ephemeral = True)
            return
        
        #post a threaded message in the same channel as the command was sent from for others to respond to
        id = db_handler.find_entry_by_id("existing",interaction.channel.id)[0]
        if id < 0 or id == "error":
            print(f"ID should have been a number >= 0, but instead it was {id}")
            await interaction.response.send_message(content = f"Sorry, something went wrong. Try running this command in another channel.", ephemeral = True)
            return
        city = db_handler.find_city_by_index("existing", id)
        print(interaction.user)
        user = interaction.user
        ir_or_xr_stand = "IR" if (ir_or_xr.lower() in ir) else "XR"
        threadParent = await interaction.channel.send(f"User {user.mention} is looking for Adderall in {city}! If you can help, please reply in this thread.\nRequired Strength: {strength}\nIR or XR: {ir_or_xr_stand}")
        threadChannel = await threadParent.create_thread(name=f"{user.global_name.lower()}-{strength.lower().replace(" ", "-")}-{ir_or_xr_stand.lower()}")
        await threadChannel.send(f"{interaction.user.mention}, don't forget to react with a <:ThumbsUpIcon:1209267015458627746> to another user who gives you the info to fulfill your request. Then, you can both earn points!")
        await interaction.response.send_message(content = f"Thread successfully created! See it here: https://discord.com/channels/1200191417457324069/{interaction.channel.id}/{threadParent.id}", ephemeral = True)
    else:
        #if the command can't be used here, send an error message
        await interaction.response.send_message(content=f"You can't run this command in this channel! Try running it in a channel under the category \'{category}\'.", ephemeral=True)


@the_tree.command(
    name = "mod-money", 
    description="Changes a user's coins by the provided amount. Amount can be positive or negative whole number.", 
    guild=discord.Object(id=1200191417457324069)
)
async def mod_money(interaction, username: str, amount: int):

    index=reward_db_handler.find_index_with_username(username)
    if index==False:
        reward_db_handler.create_new_entry(username, amount, 0)
        await interaction.response.send_message(username+"\'s new coint amount is "+str(amount))
    else:
        coin_mod=reward_db_handler.mod_coins(username, amount)
        await interaction.response.send_message(coin_mod[0]+"\'s new coin amount is"+coin_mod[1])




@the_tree.command(
    name = "mod-items", 
    description="Changes a user's item quantity by amount that can be positive or negative whole number.", 
    guild=discord.Object(id=1200191417457324069)
)
async def mod_item_count(interaction, username: str, amount: int):

    index=reward_db_handler.find_index_with_username(username)
    if index==False:
        reward_db_handler.create_new_entry(username, 0, amount)
        await interaction.response.send_message(username+"\'s new item amount is "+str(amount))
    else:
        item_mod=reward_db_handler.mod_items(username, amount)
        await interaction.response.send_message(item_mod[0]+"\'s new item amount is"+item_mod[1])


@the_tree.command(
    name = "currency-info", 
    description="Pulls the coin and item count for a specified user", 
    guild=discord.Object(id=1200191417457324069)
)
async def check_amount(interaction, username: str):

    index=reward_db_handler.find_index_with_username(username)
    if index==False:
        reward_db_handler.create_new_entry(username, 0, 0)
        await interaction.response.send_message(username+" has 0 coins and 0 items.")
    else:
        coin_amount=reward_db_handler.find_coins_with_index(index)
        item_amount=reward_db_handler.find_items_with_index(index)
        await interaction.response.send_message(username+" has "+coin_amount+" coins and "+item_amount+" items.")


#function to add money to a user
# @the_tree.command(
#     name='add-money',
#     description="Give money to a user", 
#     guild=discord.Object(id=1200191417457324069)
# )
# async def add_money(self, user, channel, username, user_pfp, reception_user, amount, recept_uname):
#          # load json
#          json_file = open(self.pathToJson, "r")
#          json_content = json.load(json_file)
#          reception_user_index, new_data = self.find_index_in_db(json_content["userdata"], reception_user)

#          if new_data != "none":
#              json_content["userdata"] = new_data

#          json_recept_content = json_content["userdata"][reception_user_index]

#          json_recept_content["cash"] += int(amount)

#          # inform user
#          color = self.discord_success_rgb_code
#          embed = discord.Embed(
#          description=f"✅  Added {str(self.currency_symbol)} {'{:,}'.format(int(amount))} to <@{recept_uname.id}>'s cash balance",
#              color=color)
#          embed.set_author(name=username, icon_url=user_pfp)
#          await channel.send(embed=embed)

#          # overwrite, end
#          json_content["userdata"][reception_user_index] = json_recept_content
#          self.overwrite_json(json_content)

#          return "success", "success"

# #Function to remove money from a user
# @the_tree.command(
#     name='remove-money',
#     description="Remove money from a user", 
#     guild=discord.Object(id=1200191417457324069)
# )
# async def remove_money(self, user, channel, username, user_pfp, reception_user, amount, recept_uname):
#          # load json
#          json_file = open(self.pathToJson, "r")
#          json_content = json.load(json_file)
#          reception_user_index, new_data = self.find_index_in_db(json_content["userdata"], reception_user)

#          if new_data != "none":
#              json_content["userdata"] = new_data

#          json_recept_content = json_content["userdata"][reception_user_index]

#          json_recept_content["cash"] -= int(amount)

#          # inform user
#          color = self.discord_success_rgb_code
#          embed = discord.Embed(
#              description=f"✅  Removed {str(self.currency_symbol)} {'{:,}'.format(int(amount))} from <@{recept_uname.id}>'s cash balance",
#              color=color)
#          embed.set_author(name=username, icon_url=user_pfp)
#          await channel.send(embed=embed)

#          # overwrite, end
#          json_content["userdata"][reception_user_index] = json_recept_content
#          self.overwrite_json(json_content)

#          return "success", "success"

# #Function to buy items
# @the_tree.command(
#     name='buy-item',
#     description="Buy an item with your money", 
#     guild=discord.Object(id=1200191417457324069)
# )
# async def buy_item(self, user, channel, username, user_pfp, item_name, amount, user_roles, server_object,
#                         user_object):
#          # load json
#          json_file = open(self.pathToJson, "r")
#          json_content = json.load(json_file)

#          json_items = json_content["items"]
#          item_found = item_index = 0
#          for i in range(len(json_items)):
#              if json_items[i]["name"] == item_name:
#                  item_found = 1
#                  item_index = i
#          if not item_found:
#              return "error", "Item not found."
#          item = json_items[item_index]
#          # get variables
#          item_name = item_name
#          item_price = item["price"]
#          req_roles = item["required_roles"]
#          give_roles = item["given_roles"]
#          rem_roles = item["removed_roles"]
#          max_bal = item["maximum_balance"]
#          remaining_stock = item["amount_in_stock"]
#          expiration_date = item["expiration_date"]
#          reply_message = item["reply_message"]

#          # calculate expiration
#          today = datetime.today()
#          expire = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S.%f")
#          if today > expire:
#              return "error", f"Item has already expired. Expiring date was {expiration_date}"
#          # else we're good

#          # 1. check req roles
#          try:
#              if req_roles == "none":
#                  pass
#              else:
#                  for i in range(len(req_roles)):
#                      if int(req_roles[i]) not in user_roles:
#                          return "error", f"User does not seem to have all required roles."
#          except Exception as e:
#              print(e)
#              return "error", f"Unexpected error."

#          # 2. check give roles
#          try:
#              if rem_roles == "none":
#                  pass
#              else:
#                  for i in range(len(rem_roles)):
#                      role = discord.utils.get(server_object.roles, id=int(rem_roles[i]))
#                      print(role)
#                      await user_object.remove_roles(role)
#          except Exception as e:
#              print(e)
#              return "error", f"Unexpected error."

#          # 3. check rem roles
#          try:
#              if req_roles == "none":
#                  pass
#              else:
#                  for i in range(len(give_roles)):
#                      role = discord.utils.get(server_object.roles, id=int(give_roles[i]))
#                      print(role)
#                      await user_object.add_roles(role)
#          except Exception as e:
#              print(e)
#              return "error", f"Unexpected error."

#          # 4. check if enough money
#          sum_price = item_price * amount
#          sum_price = round(sum_price, 0)
#          user_index, new_data = self.find_index_in_db(json_content["userdata"], user)
#          user_content = json_content["userdata"][user_index]
#          user_cash = user_content["cash"]
#          if user_cash < sum_price:
#              return "error", f"Error! Not enough money in cash to purchase.\nto pay: {sum_price} ; in cash: {user_cash}"

#          # 5. rem money, print message, add to inventory
#          user_content["cash"] -= sum_price
    
#          if user_content["items"] == "none":
#              user_content["items"] = [[item_name, amount]]
#          else:
#              user_content["items"].append([item_name, amount])

#          color = self.discord_blue_rgb_code
#          embed = discord.Embed(
#              description=f"You have bought {amount} {item_name} and paid {str(self.currency_symbol)} **{'{:,}'.format(int(sum_price))}**",
#              color=color)
#          embed.set_author(name=username, icon_url=user_pfp)
#          embed.set_footer(text=reply_message)
#          await channel.send(embed=embed)

#          # overwrite, end
#          json_content["userdata"][user_index] = user_content
#          json_content["items"] = json_items
#          self.overwrite_json(json_content)

#          return "success", "success"

#Function to check inventory
#async def check_inventory(self, user, channel, username, user_pfp):
         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)

#         user_index, new_data = self.find_index_in_db(json_content["userdata"], user)
#         user_content = json_content["userdata"][user_index]

#         items = user_content["items"]
#         if items == "none":
#             inventory_checkup = "**Inventory empty. No items owned.**"
#         else:
#             inventory_checkup = ""
#             for i in range(len(items)):
#                 inventory_checkup += f"Item: `{items[i][0]}`; amount: `{items[i][1]}`\n"

#         color = self.discord_blue_rgb_code
#         embed = discord.Embed(title="Owned Items", description=f"{inventory_checkup}", color=color)
#         embed.set_author(name=username, icon_url=user_pfp)
#         embed.set_footer(text="nice")
#         await channel.send(embed=embed)

#         return "success", "success"

#Function to check their points
#async def check_balance(self, user, channel, username, user_pfp):
         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)

#         user_index, new_data = self.find_index_in_db(json_content["userdata"], user)
#         user_content = json_content["userdata"][user_index]

#         points = user_content["cash"]
#         if points == "none":
#             balance_checkup = "**No points on account.**"
#         else:
#             balance_checkup = ""
#             balance_checkup += f"Points: `points`\n"

#         color = self.discord_blue_rgb_code
#         embed = discord.Embed(title="Owned Items", description=f"{inventory_checkup}", color=color)
#         embed.set_author(name=username, icon_url=user_pfp)
#         embed.set_footer(text="nice")
#         await channel.send(embed=embed)

#         return "success", "success"

#############
# START BOT #
#############

client.run(TOKEN)
