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
                    {"channel_ID":1200192781004582962,"city":"Worcester","state_abbr":"MA"}
                ], 
    		"proposed": [
        							
			]
        	\n}""")
            creating_file.close()

        #

        # check if json file is corrupted
        #  -> in self.check_json()
        # called from main.py


    async def check_json(self):

        try:
            print("Got into the check function")
            with open(self.pathToJson, "r") as temp_json_opening:
                temp_json_content = json.load(temp_json_opening)
            print("Opened the file")

            check_content = temp_json_content
            # existing channels
            existing = check_content["existing"]

            # proposed channels
            proposed = check_content["proposed"]
            print("Both expected main sections of content appeared")
            print(f"existing is {existing}")
            # check if the Worcester entry is there
            worcID = existing[0]['channel_ID']
            print(f"{worcID} is the channel_ID for the worcester channel")
            worcCity = existing[0]['city']
            print(f"{worcCity} is the city for the worcester channel")
            worcAbbr = existing[0]['state_abbr']
            print(f"{worcAbbr} is the state or region abbreviation for the worcester channel")
            print("The existing section contained an appropriate entry for Worcester")

            return "good"
        except FileNotFoundError:
            print(f"The file {self.pathToJson} could not be found.")
            return "error"
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return "error"
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "error"

    """
    GLOBAL FUNCTIONS
    """

    # need to overwrite the whole json when updating
    def overwrite_json(self, content):
        self.json_db = open(self.pathToJson, "w")
        self.clean_json = json.dumps(content, indent=4, separators=(",", ": "))
        self.json_db.write(self.clean_json)
        self.json_db.close()


    #return indices
    def find_entry_by_id(self, db, ID_to_find):
        if(db != "existing" and db != "proposed"):
            return "error", "Provide a database name that exists, either \"existing\" or \"proposed\""

        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine the data to loop over
        data_to_search = json_content[db]
        print(data_to_search)

        ID_to_find = int(ID_to_find)
        for i in range(len(data_to_search)):
            if (db == "existing" and data_to_search[i]["channel_ID"] == ID_to_find):
                print("\nfound entry\n")
                return int(i), "none"
            if (db == "proposed" and data_to_search[i]["post_ID"] == ID_to_find):
                print("\nfound entry\n")
                return int(i), "none"
            
        #if we get here, the ID does not exist in the given data
        return -1, "ID not found"
            
    def find_city_state_in_db(self, db, city, state_abbr):
        if(db != "existing" and db != "proposed"):
            print("Provide a database name that exists, either \"existing\" or \"proposed\"")
            return -1

        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine the data to loop over
        data_to_search = json_content[db]
        print(data_to_search)
        print(len(data_to_search))

        
        for i in range(len(data_to_search)):
            if (data_to_search[i]["city"] == city and data_to_search[i]["state_abbr"] == state_abbr):
                print("\nfound entry\n")
                return int(i)
          
        #if we get here, the combo does not exist in the given data
        print("city/state combo not found")
        return -1
    
    def find_all_indices_by_state(self, db, city, state_abbr):
        if(db != "existing" and db != "proposed"):
            print("Provide a database name that exists, either \"existing\" or \"proposed\"")
            return -1

        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine the data to loop over
        data_to_search = json_content[db]
        print(data_to_search)
        
        for i in range(len(data_to_search)):
            if (data_to_search[i]["city"] == city and data_to_search[i]["state_abbr"] == state_abbr):
                print("\nfound entry\n")
                if(db == "existing"):
                    return data_to_search[i]["channel_ID"]
                if(db == "proposed"):
                    return data_to_search[i]["post_ID"]
          
        #if we get here, the combo does not exist in the given data
        print("city/state combo not found")
        return -1

    #returns an id
    def find_id_by_index(self, db, index):
        if(db != "existing" and db != "proposed"):
            print("Provide a database name that exists, either \"existing\" or \"proposed\"")
            return -1

        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine the data to index
        data_to_search = json_content[db]
        
        data_at_index=data_to_search[index]
        data_list=list(data_at_index.values())

        #get the id from the given index and database
        return data_list[0]
    
    def find_id_by_city_state(self, db, city, state_abbr):
        if(db != "existing" and db != "proposed"):
            print("Provide a database name that exists, either \"existing\" or \"proposed\"")
            return -1

        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine the data to loop over
        data_to_search = json_content[db]
        print(data_to_search)
        
        for i in range(len(data_to_search)):
            if (data_to_search[i]["city"] == city and data_to_search[i]["state_abbr"] == state_abbr):
                print("\nfound entry\n")
                if(db == "existing"):
                    return data_to_search[i]["channel_ID"]
                if(db == "proposed"):
                    return data_to_search[i]["post_ID"]
            
        #if we get here, the combo does not exist in the given data
        print("city/state combo not found")
        return -1

    #returns a city
    def find_city_by_index(self, db, index):
        if(db != "existing" and db != "proposed"):
            print("Provide a database name that exists, either \"existing\" or \"proposed\"")
            return -1

        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine the data to index
        data_to_search = json_content[db]
        
                
        data_at_index=data_to_search[index]
        data_list=list(data_at_index.values())

        #get the city from the given index and database
        return data_list[1]

        
    
    #retuns a state or region abbreviation
    def find_state_by_index(self, db, index):
        if(db != "existing" and db != "proposed"):
            print("Provide a database name that exists, either \"existing\" or \"proposed\"")
            return -1

        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine the data to index
        data_to_search = json_content[db]
                
        data_at_index=data_to_search[index]
        data_list=list(data_at_index.values())

        #get the state from the given index and database
        return data_list[2]

    
    
    def find_city_by_state(self, state_abbr):
        
        #open and load the contents
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)
        city_list=[]

        #determine the data to search
        data_to_search=json_content['existing']


        for i in range(len(data_to_search)):
            if (data_to_search[i]["state_abbr"] == state_abbr):
                city_list.append(data_to_search[i])
                print("\nfound entry\n")
        return city_list


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

    async def edit_variable(self, db, ID, variable_name, new_value):
        # check for errors in db entry
        if(db != "existing" and db != "proposed"):
            return "error", "Provide a database name that exists, either \"existing\" or \"proposed\""
        
        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        #determine which entry to edit
        id_index = self.find_entry_by_id(self, db, ID)
        if(id_index == -1):
            return "failure", f"failed to find the provided id {id} in the specified database {db}"

        json_entry_content = json_content[db][id_index]
        old_value = "N/A"
        try:
            old_value = json_entry_content[variable_name]
        except:
            return "error", f"var not found in db {db}"

        # changing value
        json_entry_content[variable_name] = new_value
        print(f"changed {variable_name} {old_value} to {new_value} in db {db} at index {id_index}")
        
        # not asking for verification, would just have to reverse by another edit

        # overwrite, end
        json_content[db][id_index] = json_entry_content
        self.overwrite_json(json_content)

        return "success", "success"


    #
    # REMOVE CITY/STATE COMBO FROM EITHER THE PROPOSED OR EXISTING CHANNELS DB
    #

    async def remove_entry(self, db, ID):
        # load json
        json_file = open(self.pathToJson, "r")
        json_content = json.load(json_file)

        json_DB = json_content[db]
        index_to_remove = self.find_entry_by_id(db, ID)
        if(index_to_remove == -1):
            return "failure", f"failed to find the provided id {id} in the specified database {db}"

        # delete from the "items" section
        json_DB.pop(index_to_remove[0])

        # overwrite, end
        json_content[db] = json_DB
        self.overwrite_json(json_content)

        return "success", "success"       


class reward_db_handler():
    def __init__(self, client):
        # we do the path from the main.py file, so we go into the db folder, then select
        self.pathToJson = "database/reward_database.json"
        self.client = client
        # for the json "variables", dont want to make a whole function to find index for variables
        # wont be many anyways. so making it manually
        self.users_entry_dict={
            "username":0,
            "coins": 1,
            "items": 2
            }
        # self.existing_entry_dict = {
        #     "channel_ID": 0,
        #     "city": 1,
        #     "state_abbr": 2
        # }
        # self.proposed_entry_dict = {
        #     "post_ID": 0,
        #     "city": 1,
        #     "state_abbr": 2
        # }

        # check if file is created, else create it
        if not os.path.exists(self.pathToJson):
            # this "w" overwrites all the (junk) data that was in this file before it was first opened
            creating_file = open(self.pathToJson, "w") 
            # adding default json config into the file if creating new
            # most entries into existing and proposed will get created in the function self.create_new_entry()
            creating_file.write("""{\n\t"users":  [
                    {"username": "BobBot", "coins": 999999999, "items": 999999999}
                ]
        	\n}""")
            creating_file.close()


    async def check_json(self):

        try:
            print("Got into the check function")
            with open(self.pathToJson, "r") as temp_json_opening:
                temp_json_content = json.load(temp_json_opening)
            print("Opened the file")

            check_content = temp_json_content
            # users with coins
            users = check_content["users"]

            # check if the BobBot
            botID = users[0]['username']
            print(f"{botID} is the username for the BobBot entry")
            botCoins = users[0]['coins']
            print(f"{botCoins} is the number of coins for the BobBot entry")
            itemvalue = users[0]['items']
            print(f"{itemvalue} is the number of items for the BobBot entry")
            print("BobBot's entry is good to go.")
            return "good"
        except FileNotFoundError:
            print(f"The file {self.pathToJson} could not be found.")
            return "error"
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return "error"
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "error"

    # need to overwrite the whole json when updating
    def overwrite_json(self, content):
        self.json_db = open(self.pathToJson, "w")
        self.clean_json = json.dumps(content, indent=4, separators=(",", ": "))
        self.json_db.write(self.clean_json)
        self.json_db.close()