#this should be the code for the bot, but honestly IDK what I'm doing so don't mind how Frankenstein it is

import asyncio
import logging
import logging.handlers
import os

from typing import List, Optional

import asyncpg  # asyncpg is not a dependency of the discord.py, and is only included here for illustrative purposes.
import discord
from discord.ext import commands
from aiohttp import ClientSession


