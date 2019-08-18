import discord
from discord.ext import commands
from random import randint
import asyncio
import random
import json
import nekos

with open('./fun.json', 'r') as cjson:
    pictures = json.load(cjson)

HUGSG = pictures["hug"]
PATSG = pictures["pat"]

class Fun(commands.Cog):

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
    async def hug(self, ctx, usr: discord.User):
        gifurl = random.choice(HUGSG)
        e = discord.Embed(description=f"{ctx.author.name} gently hugged {usr.name} ~", color=0x36393E)
        e.set_image(url=f"https://media.discordapp.net/attachments/{gifurl}")
        await ctx.send(embed=e)

    @commands.command()
    async def pat(self, ctx, usr: discord.User):
        gifurl = random.choice(PATSG)
        e = discord.Embed(description=f"{ctx.author.name} gently patted {usr.name}'s head.", color=0x36393E)
        e.set_image(url=f"https://media.discordapp.net/attachments/{gifurl}")
        await ctx.send(embed=e)

    @commands.command(alisases=['fact'])
    async def facts(self, ctx):
        some_fact = nekos.fact()
        e = discord.Embed(title = "Facts", description=some_fact, color=0x36393E)
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/560801259968266240/609132350051188749/1565298690301.png")
        await ctx.send(embed=e)


    @commands.command()
    async def why(self, ctx):
        some_question = nekos.why()
        e = discord.Embed(title = "Still wondering", description=some_question, color=0x36393E)
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/560801259968266240/609142219147837461/1565301178948.png")
        await ctx.send(embed=e)
        
    @commands.command(aliases=['cats'])
    async def cat(self, ctx):
        some_cat = nekos.cat()
        e = discord.Embed(title = "Meow~", color=0x36393E)
        e.set_image(url=some_cat)
        await ctx.send(embed=e)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if 'neko' in message.content:
            await message.channel.send(f'`{nekos.textcat()}`')
        if 'nekodroid' in message.content:
            await message.add_reaction('<:lurk:612729955830333595>')

def setup(bot):
    bot.add_cog(Fun(bot))
