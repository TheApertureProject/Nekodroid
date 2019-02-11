import discord
from discord.ext import commands
from random import randint
import asyncio
import random
import json

with open('./fun.json', 'r') as cjson:
pictures = json.load(cjson)

HUGSG = pictures["hug"]

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
    
    @commands.command()
    async def roll(self, ctx, usr: discord.User):
        gifurl=random.choice(HUGSG)
        e = discord.Embed(description=f"test", color=0x36393E)
        e.set_image(url=f"https://media.discordapp.net/attachments/{gifurl}")

def setup(bot):
    bot.add_cog(Fun(bot))
