import dbl
import discord
from discord.ext import commands
import aiohttp
import asyncio
import logging
import os

DBLTOKEN = os.environ["DBLTOKEN"]

class DiscordBotsOrgAPI(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.token = DBLTOKEN
        self.dblpy = dbl.Client(self.bot, self.token)
        self.bot.loop.create_task(self.update_stats())
	
    async def update_stats(self):
        while True:
            try:
                await self.dblpy.post_server_count()
            except Exception as e:
                print(e.args)
            await asyncio.sleep(1800)

def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
