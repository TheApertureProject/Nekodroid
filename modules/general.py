import discord
from discord.ext import commands

class General:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong !')

def setup(bot):
    bot.add_cog(General(bot))
