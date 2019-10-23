import asyncio
from random import randint

import aiohttp
import discord
import nekos
from discord.ext import commands

sorrie = '<:tohruilybutimshy:614150526933663754>'


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    # Gather images using nekos.life API
    async def nekosdotlife(self, rqimg):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/{rqimg}") as resp:
                resp.raise_for_status()
                payload = await resp.json()
            image = payload
            image_url = image["url"]
        return image_url

    @commands.command()
    async def roll(self, ctx, value: int):
        try:
            result = randint(1, value)
            msg = await ctx.send(f'And the result is...')
            await asyncio.sleep(2)
            await msg.edit(content=f'And the result is... **`{result}`** !')
        except Exception as e:
            print(e.args)
            await ctx.send('Please send a valid number of messages !')
    @commands.command(aliases=['cuddle'])
    async def hug(self, ctx, usr: discord.User):
        img_url = await self.nekosdotlife("hug")
        e = discord.Embed(description=f"{ctx.author.name} gently hugged {usr.mention} ~", url=img_url, color=0x36393E)
        e.set_image(url=img_url)
        await ctx.send(embed=e)

    @commands.command()
    async def pat(self, ctx, usr: discord.User):
        img_url = await self.nekosdotlife("pat")
        e = discord.Embed(description=f"{ctx.author.name} gently pat {usr.mention}'s head.", url=img_url, color=0x36393E)
        e.set_image(url=img_url)
        await ctx.send(embed=e)

    @commands.command()
    async def kiss(self, ctx, usr: discord.User):
        img_url = await self.nekosdotlife("kiss")
        e = discord.Embed(title=f"{ctx.author.name} passionately kissed {usr.mention}. So lovely ~", url=img_url, color=0x36393E)
        e.set_image(url=img_url)
        await ctx.send(embed=e)

    @commands.command(aliases=['hit'])
    async def slap(self, ctx, usr: discord.User):
        img_url = await self.nekosdotlife("slap")
        e = discord.Embed(description=f"{ctx.author.name} slapped {usr.mention} !", url=img_url, color=0x36393E)
        e.set_image(url=img_url)
        await ctx.send(embed=e)

    @commands.command(alisases=['fact'])
    async def facts(self, ctx):
        some_fact = nekos.fact()
        e = discord.Embed(title="Facts", description=some_fact, color=0x36393E)
        e.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/560801259968266240/609132350051188749/1565298690301.png")
        await ctx.send(embed=e)

    @commands.command()
    async def why(self, ctx):
        some_question = nekos.why()
        e = discord.Embed(title="Still wondering", description=some_question, color=0x36393E)
        e.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/560801259968266240/609142219147837461/1565301178948.png")
        await ctx.send(embed=e)

    @commands.command(aliases=['cats'])
    async def cat(self, ctx):
        some_cat = nekos.cat()
        e = discord.Embed(title="Meow~", color=0x36393E)
        e.set_image(url=some_cat)
        await ctx.send(embed=e)

    @commands.Cog.listener()
    async def on_message(self, message):
        btq_id = 583242472881127434
        if 'neko' in message.content and message.guild.id != btq_id:
            await message.channel.send(nekos.textcat())
        if 'Neko' in message.content and message.guild.id != btq_id:
            await message.channel.send(nekos.textcat())
            
def setup(bot):
    bot.add_cog(Fun(bot))
