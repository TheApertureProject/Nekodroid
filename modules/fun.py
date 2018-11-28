import discord
from discord.ext import commands
from random import randint
import asyncio

class Fun:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def roll(self, ctx, value: int):
        try:
            result=randint(1,value)
            msg=await ctx.send(f'And the result is...')
            await asyncio.sleep(2)
            await msg.edit(content=f'And the result is... **`{result}`** !')
        except Exception as e:
            print(e.args)
            await ctx.send('Please send a valid number of messages !')

def setup(bot):
    bot.add_cog(Fun(bot))
