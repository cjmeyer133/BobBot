#adapted from Unbelieva-Boat by github user h-ntai 
import json, os, time, random, math, sys, discord, math
from datetime import datetime, timezone, timedelta
from random import randint

class channel_db_handler:
    def __init__(self, client):
        # we do the path from the main.py file, so we go into the db folder, then select
        self.pathToJson = "database/channel_database.json"
        self.client = client
        # for the json "variables", dont want to make a whole function to find index for variables
        # wont be many anyways. so making it manually
        self.existing_entry_dict = {
            "channel_ID": 0,
            "city": 1,
            "state_abbr": 2
        }
        self.proposed_entry_dict = {
            "post_ID": 0,
            "city": 1,
            "state_abbr": 2
        }

        # check if file is created, else create it
        if not os.path.exists(self.pathToJson):
            # this "w" overwrites all the (junk) data that was in this file before it was first opened
            creating_file = open(self.pathToJson, "w") 
            # adding default json config into the file if creating new
            # most entries into existing and proposed will get created in the function self.create_new_entry()
            creating_file.write("""{\n\t"existing":  [
                                    {"channel_ID":"1200192781004582962","city":"Worcester","state_abbr":"MA"}
                                ], 
        						"proposed": [
        							{}				
								]
        	    				\n}""")
            creating_file.close()

        #

        # check if json file is corrupted
        #  -> in self.check_json()
        # called from main.py


    async def check_json(self):

        temp_json_opening = open(self.pathToJson, "r")
        temp_json_content = json.load(temp_json_opening)
        
        try:
            check_content = temp_json_content
            # existing channels
            existing = check_content["existing"]
            # check if the Worcester entry is there
            worcID = existing[0][self.existing_entry_dict["channel_ID"]]
            print(worcID+" is the channel_ID for the worcester channel")
            worcCity = existing[0][self.existing_entry_dict["city"]]
            print(worcCity+" is the city for the worcester channel")
            worcAbbr = existing[0][self.existing_entry_dict["state_abbr"]]
            print(worcAbbr+" is the state or region abbreviation for the worcester channel")

            # proposed channels
            proposed = check_content["proposed"]

            # didnt fail, so we're good
            temp_json_opening.close()
        except Exception as e:
            # something is missing, inform client
            return "error"

    """
    GLOBAL FUNCTIONS
    """

    # need to overwrite the whole json when updating, luckily the database won't be enormous
    def overwrite_json(self, content):
        self.json_db = open(self.pathToJson, "w")
        self.clean_json = json.dumps(content, indent=4, separators=(",", ": "))
        self.json_db.write(self.clean_json)
        self.json_db.close()


    # def find_index_in_db(self, data_to_search, user_to_find, fail_safe=False):
    #     print(data_to_search)
    #     user_to_find = int(user_to_find)
    #     for i in range(len(data_to_search)):
    #         if data_to_search[i]["user_id"] == user_to_find:
    #             print("\nfound user\n")
    #             return int(i), "none"

    #     # in this case, this isnt a user which isnt yet registrated
    #     # but someone who doesnt exist on the server
    #     # or at least thats what is expected when calling with this parameter
    #     if fail_safe:
    #         return 0, "error"

    #     print("\ncreating user\n")
    #     # we did NOT find him, which means he doesn't exist yet
    #     # so we automatically create him
    #     data_to_search.append({
    #         "user_id": int(user_to_find),
    #         "cash": 0,
    #         "bank": 0,
    #     })

    #     # now that the user is created, re-check and return int

    #     for i in range(len(data_to_search)):
    #         if data_to_search[i]["user_id"] == user_to_find:
    #             return i, data_to_search
  

    #CHANNEL HANDLING

    #
    # CREATE NEW CITY/STATE COMBO IN EITHER THE PROPOSED OR EXISTING CHANNELS DB
    #

    async def create_new_entry(self, db, ID, city, abbr):
        # check for errors in db entry
        if(db != "existing" and db != "proposed"):
            return "error", "Provide a database name that exists, either \"existing\" or \"proposed\""
        
        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        json_entries = json_content[db]

        for i in range(len(json_entries)):
            if (db == "existing" and json_entries[i]["channel_ID"] == ID):
                return "error", "Entry for that channel ID already exists."
            if (db == "proposed" and json_entries[i]["post_ID"] == ID):
                return "error", "Entry for that post ID already exists."

        # add it to the json
        if(db == "existing"):
            json_entries.append({
                "channel_ID": ID,
                "city": city,
                "state_abbr": abbr
            })
        if(db == "proposed"):
            json_entries.append({
                "post_ID": ID,
                "city": city,
                "state_abbr": abbr
            })

        # overwrite, end
        json_content[db] = json_entries
        self.overwrite_json(json_content)

        return "success", "success"

    #
    # EDIT CITY/STATE COMBO IN EITHER THE PROPOSED OR EXISTING CHANNELS DB
    #

    # async def edit_variables(self, user, channel, username, user_pfp, module_name, variable_name, new_value):
    #     # load json
    #     json_file = open(self.pathToJson, "r")
    #     json_content = json.load(json_file)

    #     if module_name not in self.variable_dict.keys():
    #         return "error", "module not found"
    #     module_index = self.variable_dict[module_name]

    #     json_module_content = json_content["variables"][module_index]
    #     try:
    #         old_value = json_module_content[variable_name]
    #     except:
    #         return "error", f"variable name of module {module_name} not found"

    #     # changing value
    #     json_module_content[variable_name] = new_value

    #     # not asking for verification, would just have to reverse by another edit
    #     # inform user
    #     color = self.discord_success_rgb_code
    #     embed = discord.Embed(
    #         description=f"✅  Changed variable '{variable_name}' of module '{module_name}'\nBefore: '{old_value}'. Now: '{new_value}'",
    #         color=color)
    #     embed.set_author(name=username, icon_url=user_pfp)
    #     await channel.send(embed=embed)

    #     # overwrite, end
    #     json_content["variables"][module_index] = json_module_content
    #     self.overwrite_json(json_content)

    #     return "success", "success"


    #
    # REMOVE CITY/STATE COMBO FROM EITHER THE PROPOSED OR EXISTING CHANNELS DB
    #

    # async def remove_entry(self, item_name):
    #     # load json
    #     json_file = open(self.pathToJson, "r")
    #     json_content = json.load(json_file)

    #     json_items = json_content["items"]
    #     item_found = item_index = 0
    #     for i in range(len(json_items)):
    #         if json_items[i]["name"] == item_name:
    #             item_found = 1
    #             item_index = i
    #     if not item_found:
    #         return "error", "Item not found."

    #     # delete from the "items" section
    #     json_items.pop(item_index)

    #     # delete for everyone who had it in their inventory
    #     user_content = json_content["userdata"]
    #     for i in range(len(user_content)):
    #         # tricky
    #         # i suppose the variable type will either be a string with "none"
    #         # or a list with lists : ["item_name", amount], so items = [ [], [] ] etc
    #         if user_content[i]["items"] == "none":
    #             pass
    #         else:
    #             try:
    #                 for ii in range(len(user_content[i]["items"])):
    #                     print(user_content[i]["items"][ii])
    #                     current_name = user_content[i]["items"][ii][0]
    #                     if current_name == item_name:
    #                         user_content[i]["items"].pop(ii)
    #             except Exception as e:
    #                 print(e)

    #     # overwrite, end
    #     json_content["items"] = json_items
    #     self.overwrite_json(json_content)

    #     return "success", "success"       
    
    #
    # CHECK DB FOR CITY/STATE COMBO
    #

    # async def check_DB(self, user, channel, username, user_pfp):
    #     # load json
    #     json_file = open(self.pathToJson, "r")
    #     json_content = json.load(json_file)

    #     user_index, new_data = self.find_index_in_db(json_content["userdata"], user)
    #     user_content = json_content["userdata"][user_index]

    #     items = user_content["items"]
    #     if items == "none":
    #         inventory_checkup = "**Inventory empty. No items owned.**"
    #     else:
    #         inventory_checkup = ""
    #         for i in range(len(items)):
    #             inventory_checkup += f"Item: `{items[i][0]}`; amount: `{items[i][1]}`\n"

    #     color = self.discord_blue_rgb_code
    #     embed = discord.Embed(title="Owned Items", description=f"{inventory_checkup}", color=color)
    #     embed.set_author(name=username, icon_url=user_pfp)
    #     embed.set_footer(text="nice")
    #     await channel.send(embed=embed)

    #     # overwrite, end
    #     # not needed

    #     return "success", "success"