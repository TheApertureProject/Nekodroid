import discord
from discord.ext import commands
import datetime

class Help:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    MAINSERV = 462871882916560896

    @commands.command()
    async def info(self, ctx):
        a = """Created by Poulpy#9355
        Hosted on Heroku
        Running on discord.py v1.0.0a
        [Invite link](https://discordapp.com/oauth2/authorize?client_id=467332623677521940&scope=bot&permissions=2146958591)
        [Official Server](https://discord.gg/PTT9UpZ)"""
        b = "Important changes were made to Kanna recently including a brand new file architecture and management. Just check the [GitHub Repository](https://github.com/TheApertureProject/KannaNightly) to know more about these changes !"
        e = discord.Embed(description="Kanna Kamui, the Kawaii Discord bot !", title='More about me', color=0xF4A2FF, timestamp=datetime.utcnow())
        e.set_thumbnail(url="https://media.discordapp.net/attachments/489041727697584148/505805443453419541/1540620568476.png?width=376&height=376")
        e.add_field(name="Information", value=a)
        e.set_footer(text=botversion)
        e.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        await ctx.send(embed=e)

    @commands.command()
    async def bugreport(self, ctx, *, bug):
        my_guild = bot.get_guild(MAINSERV)
        bugreport = my_guild.get_channel(462876207097053195)
        e = discord.Embed(description=bug, title='Bug Report', color=16711680, timestamp=datetime.utcnow())
        e.set_footer(text='Kanna - The Kawaii Discord bot')
        e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await bugreport.send(embed=e)
        await ctx.send('A~a bug ?... Hope my master will be able to correct that... Anyway, thanks !')

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        my_guild = bot.get_guild(MAINSERV)
        suggested = my_guild.get_channel(464517370036224011)
        e = discord.Embed(description=suggestion, title='Suggestion', color=4259584, timestamp=datetime.utcnow())
        e.set_footer(text='Kanna - The Kawaii Discord bot')
        e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await suggested.send(embed=e)
        await ctx.send('Suggestion sent ! Thanks for your implication !')

def setup(bot):
    bot.add_cog(Help(bot))
