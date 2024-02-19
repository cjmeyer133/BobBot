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



