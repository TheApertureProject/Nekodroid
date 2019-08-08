import discord
from discord.ext import commands
import datetime
import json

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

VERSION = config["version"]
PREFIX = config["prefix"]
prefiximg = ':prefiximg:589180796796141568'

bot = commands.Bot(command_prefix=PREFIX)

class Help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    def is_owner(ctx):
        if ctx.author.id == 458586186328571913:
            return True
        else :
            return False

    @commands.command()
    async def info(self, ctx):
        a = """Created by Poulpy#9355
[Discord Bot List page](https://discordbots.org/bot/467332623677521940) - Upvote Nekodroïd and support us !
🆕 [Sho! Music Network](https://discord.gg/bzzjyFt)
[Invite link](https://discordapp.com/oauth2/authorize?client_id=467332623677521940&scope=bot&permissions=2146958591)
[Official Server](https://discord.gg/PTT9UpZ)"""
        e = discord.Embed(description="Nekodroïd. A Kawaii Discord bot, nya !", title='More about me', color=0xF4A2FF)
        e.set_thumbnail(url="https://images.discordapp.net/avatars/467332623677521940/fddc0fea6101618cd58828d03eac4310.png?size=512")
        e.add_field(name='Information', value=a)
        e.set_footer(text=VERSION)
        e.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)

    @commands.command(aliases=['perms', 'permission', 'requirements', 'requirement'])
    async def permissions(self, ctx):
        a = """`SEND_MESSAGES` All commands
`EMBED_LINKS` Embedded commands
`USE_EXTERNAL_EMOJIS` Help command group
`KICK_MEMBERS` kick
`BAN_MEMBERS` ban
`ADD_REACTIONS` *on_command_error* error handler
`ADMINISTRATOR` Facultative - no use for now"""
        e = discord.Embed(description=a, title='Permissions requirements', color=0xF4A2FF)
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/476653267036930049/523888437493891087/1OoXboCzk0gYvTNwNnV4S9A2x.png")
        e.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)

    @commands.group(invoke_without_command=True, aliases=['hlp', 'commandlist', 'commands'])
    async def help(self, ctx):
        e = discord.Embed(description="Help categories", title='➡️Interactive help', color=0x33CC33)
        e.set_thumbnail(url="https://cdn.discordapp.com/emojis/377480330103488532.png?v=1")
        e.add_field(name='`info`', value='Bot information related commands')
        e.add_field(name='`utilities`', value='All our amazing utilities !')
        e.add_field(name='`moderator`', value='Moderation related commands')
        e.add_field(name='`fun`', value='Fun related commands ~^^')
        e.set_footer(text=f'Type {PREFIX}help <category> to display specific commands.')
        e.add_field(name='🆕 Sho! Music Network', value='Quality electro [here](https://discord.gg/bzzjyFt) uwu')
        if ctx.author.id == 458586186328571913 :
            e.add_field(name='`master`', value="My master's commands !")
        await ctx.send(embed=e)

    @help.command(name="info")
    async def help_info(self, ctx):
        e = discord.Embed(description="Basic commands", title='➡️Commands list', color=0x00FFC0)
        e.set_thumbnail(url="https://cdn.discordapp.com/emojis/470912852543275009.gif?v=1")
        e.add_field(name=f'<{prefiximg}>`info`', value='Get to know me :3')
        e.add_field(name=f'<{prefiximg}>`ping`', value='Test my reactivity !')
        e.add_field(name=f'<{prefiximg}>`help`', value='Displays the primary help message')
        await ctx.send(embed=e)

    @help.command(name='utilities')
    async def help_utilities(self, ctx):
        c = discord.Embed(description='Utilities', title='➡️Commands list', color=0x003366)
        c.set_thumbnail(url="https://cdn.discordapp.com/emojis/395627468276367370.png?v=1")
        c.add_field(name=f'<{prefiximg}>`translate <text>`', value='Translate a text string from any language to english')
        c.add_field(name=f'<{prefiximg}>`pp <user>`', value='Get the profile picture of some user')
        c.add_field(name=f'<{prefiximg}>`qr <url>`', value='Shorten a url adress (or a simple text string) into a QR Code')
        c.add_field(name=f'<{prefiximg}>`shorten <url>`', value='Shorten a URL adress into a bit.ly link')
        c.add_field(name=f'<{prefiximg}>`emote <emoji>`', value='Get the download link of some emoji')
        c.add_field(name=f'<{prefiximg}>`wiki <request>`', value='Search WikiPedia')
        await ctx.send(embed=c)

    @help.command(name="moderator")
    async def help_moderator(self, ctx):
        a = discord.Embed(description="Moderator commands", title='➡️Commands list', color=0xffff00) 
        a.set_thumbnail(url="https://cdn.discordapp.com/emojis/474539445379661824.png?v=1")
        a.add_field(name=f'<{prefiximg}>`kick <member/id>`', value='Kick someone from the server')
        a.add_field(name=f'<{prefiximg}>`ban <member/id> <reason>`', value='Kick a member from the server permanently (ban)')
        a.add_field(name=f'<{prefiximg}>`clear <amount of messages>`', value='Delete a specific number of messages (no limit - be extremely careful)')
        a.add_field(name=f'<{prefiximg}>`mute <member/id> <reason>`', value='Mute a member')
        a.add_field(name=f'<{prefiximg}>`unmute <member/id> <reason>`', value='Unmute a member')
        a.add_field(name=f'<{prefiximg}>`setmute`', value='Create and set a `Muted` role on your server')
        await ctx.send(embed=a)

    @help.command(name="fun")
    async def help_fun(self, ctx):
        d = discord.Embed(description='Fun', title='➡️Commands list', color=0xFFA2DD)
        d.set_thumbnail(url="https://cdn.discordapp.com/emojis/398860813881835533.png?v=1")
        d.add_field(name='`roll <number>`', value="Roll a dice with the specified number of faces (no limit !)")
        d.add_field(name='`pat <user>`', value="Pat some user ~")
        d.add_field(name='`hug <user>`', value="Hug some user.")
        d.add_field(name='`facts`', value="Returns a random fact.")
        d.add_field(name='`why`', value="Returns a question.")
        await ctx.send(embed=d)

    @commands.check(is_owner)
    @help.command(name="master")
    async def help_master(self, ctx):
        b = discord.Embed(description='Master commands', title='➡️Commands list', color=0xFF0000)
        b.set_thumbnail(url="https://cdn.discordapp.com/attachments/476653267036930049/498859365046943745/1538964466545.png")
        b.add_field(name=f'<{prefiximg}>`say <channel> <text>`', value='Talk through me !')
        b.add_field(name=f'<{prefiximg}>`shutdown`', value='Shut me down...')
        try:
            await ctx.send(embed=b)
        except:
            await ctx.send("Access denied ! Y~you're not my master !")


    @help.command(name='all')
    async def help_all(self, ctx):
        c = discord.Embed(description='All the commands', color=0x003366)
        c.set_thumbnail(url="https://cdn.discordapp.com/emojis/471044511804686348.gif?v=1")
        c.add_field(name="`help`, `info`, `ping`, `kick <member/id>`,`ban <member/id> <reason>`, `clear <amount of messages>`, `clear <amount of messages>`, `pp <user>`, `qr <link>`, `shorten <link>`, `roll <number>`, `hug <user>`, `pat <user>`, `facts`, `why`", value='Full command list')
        c.add_field(name="`info`, `utilities`, `moderator`, `fun`", value='Help categories')
        await ctx.send(embed=c)
    
    @commands.command(aliases=['utilities', 'moderator', 'all', 'master'])
    async def fun(self, ctx):
        await ctx.send("Please type `k!help <name of the category>` to get specific help about a category. Don't forget the `help` !")

def setup(bot):
    bot.add_cog(Help(bot))
