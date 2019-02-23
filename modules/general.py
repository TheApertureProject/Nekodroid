import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong !')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('Ping !')

    @commands.command(aliases=['support'])
    async def join(self, ctx):
        await ctx.send('***Support Server*** 🔀 https://discord.gg/QE2yg6G')

    @commands.command(aliases=['add'])
    async def invite(self, ctx):
        await ctx.send('***Invite Link*** 🔀 <https://discordapp.com/oauth2/authorize?client_id=467332623677521940&scope=bot&permissions=2146958591>')

def setup(bot):
    bot.add_cog(General(bot))
