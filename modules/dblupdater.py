import asyncio
import logging
import os
import dbl
from discord.ext import commands

DBLTOKEN = os.environ["DBLTOKEN"]

class DiscordBotsOrgAPI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = 'DBLTOKEN'
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)

    async def on_guild_post():
        print("Server count posted successfully")

def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
