# #initializing things I think???

# #from Unbelieva-Boat by github user h-ntai 
# import json, os, time, random, math, sys, discord, math
# from datetime import datetime, timezone, timedelta
# from random import randint

# #wow Unbelieva-Boat is gross, there's some changes in here. Hopefully not omitting anything necessary
# class pythondiscord_bot_handler:
#     def __init__(self, client):
#         # we do the path from the main.py file, so we go into the db folder, then select
#         self.pathToJson = "database/database.json"
#         self.client = client
#         # for the json "variables", dont want to make a whole function to find index for variables
#         # wont be many anyways. so making it manually
#         self.variable_dict = {
#             "daily": 0,
#         }

#         # for colors
#         self.discord_error_rgb_code = discord.Color.from_rgb(239, 83, 80)
#         self.discord_blue_rgb_code = discord.Color.from_rgb(3, 169, 244)
#         self.discord_success_rgb_code = discord.Color.from_rgb(102, 187, 106)

#         # check if file is created, else create it
#         if not os.path.exists(self.pathToJson):
#             creating_file = open(self.pathToJson, "w")
#             # adding default json config into the file if creating new
#             # all the users will get created automatically in the function self.find_index_in_db()
#             # but for the different jobs etc the program needs configs for variables and symbols
#             creating_file.write("""{\n\t"userdata": [], 
#         										"symbols": [
#         											{"name":"currency_symbol","symbol_emoji":":dollar:"}				
#         										],
#         										"items": [
#         											{}				
#         										],
#         										"income_roles": [
#         											{}				
#         										]
#         										\n}""")
#             creating_file.close()

#         #

#         # check if json file is corrupted
#         #  -> in self.check_json()
#         # called from main.py

#     def get_currency_symbol(self, test=False, value="unset"):
#         if not test:
#             # get currency symbol to use
#             temp_json_opening = open(self.pathToJson, "r")
#             temp_json_content = json.load(temp_json_opening)
#             # the currency symbol is always at position 0 in the "symbols" part
#             currency_symbol = temp_json_content["symbols"][0]["symbol_emoji"]
#             self.currency_symbol = discord.utils.get(self.client.emojis, id=int(currency_symbol))
#         else:
#             try:
#                 self.currency_symbol = discord.utils.get(self.client.emojis, id=int(value))
#                 print(str(self.currency_symbol))
#                 if self.currency_symbol == None:
#                     return "error"
#             except:
#                 return "error"

#         # if we handle a already created file, we need certain variables

#     async def check_json(self):

#         temp_json_opening = open(self.pathToJson, "r")
#         temp_json_content = json.load(temp_json_opening)
        
#         """
#         possibly to add : 
#             improve the error system, raising specific errors with a "error_info"
#             for example : "userdata missing"
#         """
#         try:
#             check_content = temp_json_content
#             # userdata space
#             userdata = check_content["userdata"]
#             # variables
#             variables = check_content["variables"]
#             daily = variables[self.variable_dict["daily"]]

#             # symbol
#             currency_symbol = check_content["symbols"][0]
#             items = check_content["items"]
#             roles = check_content["income_roles"]

#             # didnt fail, so we're good
#             temp_json_opening.close()
#         except Exception as e:
#             # something is missing, inform client
#             return "error"

#     """
#     GLOBAL FUNCTIONS
#     """

#     # need to overwrite the whole json when updating, luckily the database won't be enormous
#     def overwrite_json(self, content):
#         self.json_db = open(self.pathToJson, "w")
#         self.clean_json = json.dumps(content, indent=4, separators=(",", ": "))
#         self.json_db.write(self.clean_json)
#         self.json_db.close()

#     # find the user in the database
#     def find_index_in_db(self, data_to_search, user_to_find, fail_safe=False):
#         print(data_to_search)
#         user_to_find = int(user_to_find)
#         for i in range(len(data_to_search)):
#             if data_to_search[i]["user_id"] == user_to_find:
#                 print("\nfound user\n")
#                 return int(i), "none"

#         # in this case, this isnt a user which isnt yet registrated
#         # but someone who doesnt exist on the server
#         # or at least thats what is expected when calling with this parameter
#         if fail_safe:
#             return 0, "error"

#         print("\ncreating user\n")
#         # we did NOT find him, which means he doesn't exist yet
#         # so we automatically create him
#         data_to_search.append({
#             "user_id": int(user_to_find),
#             "cash": 0,
#             "bank": 0,
#             # "balance" : cash + bank
#             # "roles": "None" ; will be checked when calculating weekly auto-role-income
#             "items": "none",
#             "last_daily": "none",
#             "rate": 50,
#             "daily_mult": 1.0
#         })
#         """
#             POSSIBLE ISSUE :
#                 that we need to create user by overwrite, then problem of doing that while another command is
#                 supposed to have it open etc. hopefully it works just as such
#         """
#         # now that the user is created, re-check and return int

#         for i in range(len(data_to_search)):
#             if data_to_search[i]["user_id"] == user_to_find:
#                 return i, data_to_search

#     def find_index_in_db(self, data_to_search, user_to_find, fail_safe=False):
#         print(data_to_search)
#         user_to_find = int(user_to_find)
#         for i in range(len(data_to_search)):
#             if data_to_search[i]["user_id"] == user_to_find:
#                 print("\nfound user\n")
#                 return int(i), "none"

#         # in this case, this isnt a user which isnt yet registrated
#         # but someone who doesnt exist on the server
#         # or at least thats what is expected when calling with this parameter
#         if fail_safe:
#             return 0, "error"

#         print("\ncreating user\n")
#         # we did NOT find him, which means he doesn't exist yet
#         # so we automatically create him
#         data_to_search.append({
#             "user_id": int(user_to_find),
#             "cash": 0,
#             "bank": 0,
#         })

#         # now that the user is created, re-check and return int

#         for i in range(len(data_to_search)):
#             if data_to_search[i]["user_id"] == user_to_find:
#                 return i, data_to_search



#     #
#     # ADD-MONEY
#     #

#     async def add_money(self, user, channel, username, user_pfp, reception_user, amount, recept_uname):
#         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)
#         reception_user_index, new_data = self.find_index_in_db(json_content["userdata"], reception_user)

#         if new_data != "none":
#             json_content["userdata"] = new_data

#         json_recept_content = json_content["userdata"][reception_user_index]

#         json_recept_content["cash"] += int(amount)

#         # inform user
#         color = self.discord_success_rgb_code
#         embed = discord.Embed(
#             description=f"✅  Added {str(self.currency_symbol)} {'{:,}'.format(int(amount))} to <@{recept_uname.id}>'s cash balance",
#             color=color)
#         embed.set_author(name=username, icon_url=user_pfp)
#         await channel.send(embed=embed)

#         # overwrite, end
#         json_content["userdata"][reception_user_index] = json_recept_content
#         self.overwrite_json(json_content)

#         return "success", "success"

#     #
#     # REMOVE-MONEY
#     #

#     async def remove_money(self, user, channel, username, user_pfp, reception_user, amount, recept_uname):
#         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)
#         reception_user_index, new_data = self.find_index_in_db(json_content["userdata"], reception_user)

#         if new_data != "none":
#             json_content["userdata"] = new_data

#         json_recept_content = json_content["userdata"][reception_user_index]

#         json_recept_content["cash"] -= int(amount)

#         # inform user
#         color = self.discord_success_rgb_code
#         embed = discord.Embed(
#             description=f"✅  Removed {str(self.currency_symbol)} {'{:,}'.format(int(amount))} from <@{recept_uname.id}>'s cash balance",
#             color=color)
#         embed.set_author(name=username, icon_url=user_pfp)
#         await channel.send(embed=embed)

#         # overwrite, end
#         json_content["userdata"][reception_user_index] = json_recept_content
#         self.overwrite_json(json_content)

#         return "success", "success"

#     #
#     # EDIT VARIABLES
#     #

#     async def edit_variables(self, user, channel, username, user_pfp, module_name, variable_name, new_value):
#         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)

#         if module_name not in self.variable_dict.keys():
#             return "error", "module not found"
#         module_index = self.variable_dict[module_name]

#         json_module_content = json_content["variables"][module_index]
#         try:
#             old_value = json_module_content[variable_name]
#         except:
#             return "error", f"variable name of module {module_name} not found"

#         # changing value
#         json_module_content[variable_name] = new_value

#         # not asking for verification, would just have to reverse by another edit
#         # inform user
#         color = self.discord_success_rgb_code
#         embed = discord.Embed(
#             description=f"✅  Changed variable '{variable_name}' of module '{module_name}'\nBefore: '{old_value}'. Now: '{new_value}'",
#             color=color)
#         embed.set_author(name=username, icon_url=user_pfp)
#         await channel.send(embed=embed)

#         # overwrite, end
#         json_content["variables"][module_index] = json_module_content
#         self.overwrite_json(json_content)

#         return "success", "success"

#     #
#     # EDIT CURRENCY SYMBOL
#     #

#     async def change_currency_symbol(self, user, channel, username, user_pfp, new_emoji_name):
#         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)

#         json_emoji = json_content["symbols"][0]

#         old_value = json_emoji["symbol_emoji"]

#         test_emoji = self.get_currency_symbol(True, new_emoji_name)
#         if test_emoji == "error":
#             return "error", "Emoji not found."

#         # changing value
#         json_emoji["symbol_emoji"] = new_emoji_name

#         # not asking for verification, would just have to reverse by another edit
#         # inform user
#         color = self.discord_success_rgb_code
#         embed = discord.Embed(description=f"✅  Changed emoji from '{old_value}' to '{new_emoji_name}'", color=color)
#         embed.set_author(name=username, icon_url=user_pfp)
#         await channel.send(embed=embed)

#         # overwrite, end
#         json_content["symbols"][0] = json_emoji
#         self.overwrite_json(json_content)

#         return "success", "success"

  

#     #ITEM HANDLING


#     # CREATE NEW ITEM
#     #

#     async def create_new_item(self, item_name, cost, description, duration, stock, roles_id_required, roles_id_to_give,
#                               roles_id_to_remove, max_bal, reply_message):
#         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)

#         json_items = json_content["items"]

#         for i in range(len(json_items)):
#             if json_items[i]["name"] == item_name:
#                 return "error", "Item with such name already exists."

#         # calculate item duration
#         today = datetime.today()
#         print(today)
#         expiration_date = today + timedelta(days=duration)

#         print("expiration date : ", expiration_date)

#         json_items.append({
#             "name": item_name,
#             "price": cost,
#             "description": description,
#             "duration": duration,
#             "amount_in_stock": stock,
#             "required_roles": roles_id_required,
#             "given_roles": roles_id_to_give,
#             "removed_roles": roles_id_to_remove,
#             "maximum_balance": max_bal,
#             "reply_message": reply_message,
#             "expiration_date": str(expiration_date)
#         })

#         # overwrite, end
#         json_content["items"] = json_items
#         self.overwrite_json(json_content)

#         return "success", "success"

#     #
#     # REMOVE ITEM
#     #

#     async def remove_item(self, item_name):
#         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)

#         json_items = json_content["items"]
#         item_found = item_index = 0
#         for i in range(len(json_items)):
#             if json_items[i]["name"] == item_name:
#                 item_found = 1
#                 item_index = i
#         if not item_found:
#             return "error", "Item not found."

#         # delete from the "items" section
#         json_items.pop(item_index)

#         # delete for everyone who had it in their inventory
#         user_content = json_content["userdata"]
#         for i in range(len(user_content)):
#             # tricky
#             # i suppose the variable type will either be a string with "none"
#             # or a list with lists : ["item_name", amount], so items = [ [], [] ] etc
#             if user_content[i]["items"] == "none":
#                 pass
#             else:
#                 try:
#                     for ii in range(len(user_content[i]["items"])):
#                         print(user_content[i]["items"][ii])
#                         current_name = user_content[i]["items"][ii][0]
#                         if current_name == item_name:
#                             user_content[i]["items"].pop(ii)
#                 except Exception as e:
#                     print(e)

#         # overwrite, end
#         json_content["items"] = json_items
#         self.overwrite_json(json_content)

#         return "success", "success"       
#     #
#     # BUY ITEM
#     #

#     async def buy_item(self, user, channel, username, user_pfp, item_name, amount, user_roles, server_object,
#                        user_object):
#         # load json
#         json_file = open(self.pathToJson, "r")
#         json_content = json.load(json_file)

#         json_items = json_content["items"]
#         item_found = item_index = 0
#         for i in range(len(json_items)):
#             if json_items[i]["name"] == item_name:
#                 item_found = 1
#                 item_index = i
#         if not item_found:
#             return "error", "Item not found."
#         item = json_items[item_index]
#         # get variables
#         item_name = item_name
#         item_price = item["price"]
#         req_roles = item["required_roles"]
#         give_roles = item["given_roles"]
#         rem_roles = item["removed_roles"]
#         max_bal = item["maximum_balance"]
#         remaining_stock = item["amount_in_stock"]
#         expiration_date = item["expiration_date"]
#         reply_message = item["reply_message"]

#         # calculate expiration
#         today = datetime.today()
#         expire = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S.%f")
#         if today > expire:
#             return "error", f"Item has already expired. Expiring date was {expiration_date}"
#         # else we're good

#         # 1. check req roles
#         try:
#             if req_roles == "none":
#                 pass
#             else:
#                 for i in range(len(req_roles)):
#                     if int(req_roles[i]) not in user_roles:
#                         return "error", f"User does not seem to have all required roles."
#         except Exception as e:
#             print(e)
#             return "error", f"Unexpected error."

#         # 2. check give roles
#         try:
#             if rem_roles == "none":
#                 pass
#             else:
#                 for i in range(len(rem_roles)):
#                     role = discord.utils.get(server_object.roles, id=int(rem_roles[i]))
#                     print(role)
#                     await user_object.remove_roles(role)
#         except Exception as e:
#             print(e)
#             return "error", f"Unexpected error."

#         # 3. check rem roles
#         try:
#             if req_roles == "none":
#                 pass
#             else:
#                 for i in range(len(give_roles)):
#                     role = discord.utils.get(server_object.roles, id=int(give_roles[i]))
#                     print(role)
#                     await user_object.add_roles(role)
#         except Exception as e:
#             print(e)
#             return "error", f"Unexpected error."

#         # 4. check if enough money
#         sum_price = item_price * amount
#         sum_price = round(sum_price, 0)
#         user_index, new_data = self.find_index_in_db(json_content["userdata"], user)
#         user_content = json_content["userdata"][user_index]
#         user_cash = user_content["cash"]
#         if user_cash < sum_price:
#             return "error", f"Error! Not enough money in cash to purchase.\nto pay: {sum_price} ; in cash: {user_cash}"

#         # 5. check if not too much money
#         user_bank = user_content["bank"]
#         if max_bal != "none":
#             if (user_bank + user_cash) > max_bal:
#                 return "error", f"Error! You have too much money to purchase.\nnet worth: {'{:,}'.format(int(user_bank + user_cash))} ; max bal: {max_bal}"

#         # 6. check if enough in stock or not
#         if max_bal != "none":
#             if remaining_stock <= 0:
#                 return "error", f"Error! Item not in stock."
#             elif amount > remaining_stock:
#                 return "error", f"Error! Not enough remaining in stock ({remaining_stock} remaining)."

#         # 8. rem money, substract stock, print message, add to inventory
#         user_content["cash"] -= sum_price
#         item["amount_in_stock"] -= amount

#         if user_content["items"] == "none":
#             user_content["items"] = [[item_name, amount]]
#         else:
#             user_content["items"].append([item_name, amount])

#         color = self.discord_blue_rgb_code
#         embed = discord.Embed(
#             description=f"You have bought {amount} {item_name} and paid {str(self.currency_symbol)} **{'{:,}'.format(int(sum_price))}**",
#             color=color)
#         embed.set_author(name=username, icon_url=user_pfp)
#         embed.set_footer(text=reply_message)
#         await channel.send(embed=embed)

#         # overwrite, end
#         json_content["userdata"][user_index] = user_content
#         json_content["items"] = json_items
#         self.overwrite_json(json_content)

#         return "success", "success"

#     #
#     # CHECK INVENTORY
#     #

#     async def check_inventory(self, user, channel, username, user_pfp):
#         # load json
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

#         # overwrite, end
#         # not needed

#         return "success", "success"