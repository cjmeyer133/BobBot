#I'm putting things together again in a separate document being a bit more picky.
#this particular one is for the init file

import json, os, time, random, math, sys, discord, math
from datetime import datetime, timezone, timedelta
from random import randint

class pythondiscord_bot_handler:
    def __init__(self, client):
        # we do the path from the main.py file, so we go into the db folder, then select
        self.pathToJson = "database/database.json"
        self.client = client
        # for the json "variables", dont want to make a whole function to find index for variables
        # wont be many anyways. so making it manually
        self.variable_dict = {
            "daily": 0,}

        if not os.path.exists(self.pathToJson):
            creating_file = open(self.pathToJson, "w")
            # adding default json config into the file if creating new
            # all the users will get created automatically in the function self.find_index_in_db()
            # but for the different jobs etc the program needs configs for variables and symbols
            creating_file.write("""{\n\t"userdata": [], 
        										"symbols": [
        											{"name":"currency_symbol","symbol_emoji":":dollar:"}				
        										],
        										"items": [
        											{}				
        										],
        										"income_roles": [
        											{}				
        										]
        										\n}""")
            creating_file.close()


    def get_currency_symbol(self, test=False, value="unset"):
        if not test:
            # get currency symbol to use
            temp_json_opening = open(self.pathToJson, "r")
            temp_json_content = json.load(temp_json_opening)
            # the currency symbol is always at position 0 in the "symbols" part
            currency_symbol = temp_json_content["symbols"][0]["symbol_emoji"]
            self.currency_symbol = discord.utils.get(self.client.emojis, id=int(currency_symbol))
        else:
            try:
                self.currency_symbol = discord.utils.get(self.client.emojis, id=int(value))
                print(str(self.currency_symbol))
                if self.currency_symbol == None:
                    return "error"
            except:
                return "error"

    # if we handle a already created file, we need certain variables
    async def check_json(self):

        temp_json_opening = open(self.pathToJson, "r")
        temp_json_content = json.load(temp_json_opening)
        
        """
        possibly to add : 
            improve the error system, raising specific errors with a "error_info"
            for example : "userdata missing"
        """
        try:
            check_content = temp_json_content
            # userdata space
            userdata = check_content["userdata"]
            # variables
            variables = check_content["variables"]
            daily = variables[self.variable_dict["daily"]]

            # symbol
            currency_symbol = check_content["symbols"][0]
            items = check_content["items"]
            roles = check_content["income_roles"]

            # didnt fail, so we're good
            temp_json_opening.close()
        except Exception as e:
            # something is missing, inform client
            return "error"

