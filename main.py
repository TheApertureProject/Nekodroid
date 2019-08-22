import logging
logging.basicConfig(level='INFO')
import os
import sys
try:
    import json
    import asyncio
    import discord
    from discord.ext import commands
    print('All modules successfully imported.')
except ImportError:
    print('Importing librairies failed. Some of the librairies may be missing or corrupted')
    sys.exit

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

PREFIX = config["prefix"]
modules = config["modules"]
OWNER = config["owner_id"]
VERSION = config["version"]
TOKEN = os.environ["TOKEN"]

bot = commands.Bot(command_prefix=[PREFIX, "nya ", "Nya "])

bot.config = config
bot.ready = False

async def status():
    while True:
        names = [f'\'nya help\' !', 'on my supportserv, nya.', f'on {len(bot.guilds)} servers, nya !', f'with {len(bot.users)} users. Nya.']
        for name in names:
            await bot.change_presence(activity=discord.Game(name=name))
            await asyncio.sleep(120)

@bot.event
async def on_connect():
    print('Successfully connected !')

@bot.event
async def on_ready():
    loaded = 0
    bot.remove_command('help')
    for module in modules:
        try:
            logging.info('Loading %s', module)
            bot.load_extension(f'modules.{module}')
        except Exception:
            logging.exception('Failed to load %s', module)
    print('Logged in.')
    bot.loop.create_task(status())

bot.run(TOKEN)
