import discord
from discord.ext import commands
from random import randint
import asyncio
import random
import json
import nekos
import aiohttp

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    async def nekosdotlife(img0):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/{img0}") as resp:
                await resp.raise_for_status()
                print(resp.read(), resp.headers)
                payload = await resp.json()
            image = payload
            image_url = image["url"]
        return image_url
        
    
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
        e = discord.Embed(description=f"{ctx.author.name} gently hugged {usr.name} ~", color=0x36393E)
        e.set_image(url=self.nekosdotlife("hug"))
        await ctx.send(embed=e)

    @commands.command()
    async def pat(self, ctx, usr: discord.User):
        e = discord.Embed(description=f"{ctx.author.name} gently patted {usr.name}'s head.", color=0x36393E)
        e.set_image(url=self.nekosdotlife("pat"))
        await ctx.send(embed=e)
        
    @commands.command()
    async def kiss(self, ctx, usr: discord.User):
        e = discord.Embed(description=f"{ctx.author.name} passionately kissed {usr.name}. So lovely ~", color=0x36393E)
        e.set_image(url=self.nekosdotlife("kiss"))
        await ctx.send(embed=e)

    @commands.command(aliases=['hit'])
    async def slap(self, ctx, usr: discord.User):
        e = discord.Embed(description=f"{ctx.author.name} slapped {usr.name} !", color=0x36393E)
        e.set_image(url=self.nekosdotlife("slap"))
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
            await message.channel.send(nekos.textcat())
        if 'neko' in message.content:
            await message.channel.send(nekos.textcat())

def setup(bot):
    bot.add_cog(Fun(bot))
