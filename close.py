from discord.ext import commands


class SupportServ(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def request(self, ctx, botid:int, botname):
        await ctx.send("Requête acceptée :)")
    
def setup(bot):
    bot.add_cog(SupportServ(bot))
