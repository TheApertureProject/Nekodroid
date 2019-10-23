import os

import bitly_api
import discord
from discord.ext import commands
from googletrans import Translator

translator = Translator()

BITLY_API_USER = os.environ["BITLYUSERNAME"]
BITLY_API_KEY = os.environ["BITLYTOKEN"]


class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command(aliases=['pfp', 'pp'])
    async def avatar(self, ctx, usr: discord.User):
        e = discord.Embed(description=f"[{usr.name}'s profile picture]({usr.avatar_url})", title='Avatar',
                          color=0x5D5DFF)
        e.set_image(url=usr.avatar_url)
        await ctx.send(embed=e)

    @commands.command(aliases=['qrcode'])
    async def qr(self, ctx, *, thing):
        e = discord.Embed(description=f"QR code request for : `{thing}`", title='QR Generator', color=0x000000)
        e.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={thing}")
        await ctx.send(embed=e)

    @commands.command(aliases=['tl', 'traduce'])
    async def translate(self, ctx, *, term):
        translated = translator.translate(term)
        term2 = translated.text
        e = discord.Embed(title='Translation', description=term2, color=0x0099ff)
        e.set_thumbnail(
            url='https://media.discordapp.net/attachments/476653267036930049/524259270234079232/Google_Translate_logo.svg.png?width=301&height=301')
        await ctx.send(embed=e)

    @commands.command(aliases=['googl', 'bitly'])
    async def shorten(self, ctx, rqurl):
        try:
            bitly_login = bitly_api.Connection(BITLY_API_USER, BITLY_API_KEY)
            response = bitly_login.shorten(uri=rqurl)
            result = response['url']
            await ctx.send(f'***Shortened bit.ly link*** 🔀 <{result}>')
        except Exception as e:
            await ctx.send('An error occured, nya. Please check the entered URL for spaces or invalid caracters, nya !')

    @commands.command(aliases=['emoji', 'loot'])
    async def emote(self, ctx, *, emote: discord.Emoji):
        e = discord.Embed(description=f"Emoji `{emote.name}` requested", title='Emoji', url=emote.url, color=0x0099ff)
        e.set_thumbnail(url=emote.url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Utilities(bot))
