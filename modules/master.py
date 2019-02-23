import discord
from discord.ext import commands
import sys

class Master(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    def is_owner(ctx):
        if ctx.author.id == 458586186328571913:
            return True
        else:
            return False
    
    @commands.check(is_owner)
    @commands.command()
    async def leaveserv(self, ctx, idnum):
        idnum= self.bot.get_guild(idnum)
        await idnum.leave()
        await ctx.send(f'Server {idnum.name} left.')
    
    @commands.check(is_owner)
    @commands.command(pass_context=True)
    async def say(self, ctx, channel: discord.TextChannel, *, text):
        await ctx.message.delete()
        await channel.send(text)

    @say.error
    async def say_handler(self, ctx, err):
        if isinstance(err, commands.CheckFailure):
            await ctx.send('Sorry, but only my master can use this command !')
        else:
            raise err

    @commands.check(is_owner)
    @commands.command()
    async def shutdown(self, ctx):
        try:
            await ctx.send('Yes Master !')
            await ctx.send('Shutting down...')
            await ctx.send('Bye !')
            sys.exit()
        except Exception as e:
            print(e.args)
            await ctx.send('An error occured. You should check the logs, I am sure it is nothing !')

    @shutdown.error
    async def shutdown_handler(self, ctx, err):
        if isinstance(err, commands.CheckFailure):
            await ctx.send('Access denied. You are not my Master !')
        else:
            raise err

def setup(bot):
    bot.add_cog(Master(bot))
