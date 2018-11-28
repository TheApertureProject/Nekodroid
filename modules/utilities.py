import discord
from discord.ext import commands

class Utilities:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.guild_only()
    @commands.command()
    async def pp(self, ctx, usr: discord.User):
        e = discord.Embed(description="{}'s profile picture".format(usr.name), title='Avatar', color=0x5D5DFF, timestamp=datetime.utcnow())
        e.set_image(url=usr.avatar_url)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Utilities(bot))
