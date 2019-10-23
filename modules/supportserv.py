from discord.ext import commands


class SupportServ(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def kawaii(self, ctx):
        if ctx.guild.id == 462871882916560896:
            await ctx.user.add_role('KawaiiRP')
            await ctx.send('Role added. Just visit <#525421450241376266> to get the RP started !')
        else:
            await ctx.send(
                "I'm sorry, but this command can be used on Kanna's support server only. Join here → https://discord.gg/PTT9UpZ")


def setup(bot):
    bot.add_cog(SupportServ(bot))
