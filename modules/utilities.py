import discord
from discord.ext import commands
import datetime
import googletrans
from googletrans import Translator
translator = Translator()

class Utilities:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def pp(self, ctx, usr: discord.User):
        e = discord.Embed(description=f"[{usr.name}'s profile picture]({usr.avatar_url})", title='Avatar', color=0x5D5DFF)
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
        a = f"""***Input*** 🔀 {term}
***Translation*** 🔀 {term2}"""
        e = discord.Embed(description=a, title='Translation', color=0x0099ff)
        e.set_thumbnail(url='https://media.discordapp.net/attachments/476653267036930049/524259270234079232/Google_Translate_logo.svg.png?width=301&height=301')
        await ctx.send(a)
        

    @commands.command()
    async def wiki(self, ctx, *, searchterm):
        await ctx.send(f"***Wikipedia Search*** 🔀 https://en.wikipedia.org/wiki/{searchterm}")

def setup(bot):
    bot.add_cog(Utilities(bot))
