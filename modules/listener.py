import asyncio
import json
import arrow
import discord
from discord.ext import commands
from discord.ext.commands import Cog
import datetime
from datetime import datetime
from datetime import date

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

PREFIX = config["prefix"]
MSERV_ID = config["main_server_id"]
SJCHAN_ID = config["server_join_channel"]
SCCHAN_ID = config["server_count_channel"]
ERPCHAN_ID = config["error_reports_channel"]
redcross = '<:white_cross_mark:612474623333761031>'


class Listeners(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        # Nekodroid support server welcomer
        if member.guild.id == 612342503089242182:
            e = discord.Embed(
                description="Thanks for joining my support server ! Please make sure you've read the <#612699815662452785> before chatting with other members. Hope you'll enjoy your stay here !",
                title=f'Welcome, {member.name} !', color=0xdb90f4)
            e.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/476653267036930049/528247247574401025/WindowKamuis.gif')
            e.set_image(
                url='https://media.discordapp.net/attachments/612394933294202891/612403670713368606/unknown-31.png?width=400&height=226')
            await member.send(embed=e)
            role = discord.utils.get(member.guild.roles, name='Members')
            await member.add_roles(role)

    @Cog.listener()
    async def on_guild_join(self, guild):
        join = self.bot.get_channel(612353294718730240)
        try:
            invite_url = await self.bot.get_channel(self.bot.get_guild(guild.id).system_channel).create_invite()
            invite = f"[Join this server]({invite_url.url})"
        except:
            invite = "Couldn't generate any invite for this server."
        a = f"""Owned by **`{guild.owner}`**
Member count : `{guild.member_count}`
Created at `{guild.created_at}`
Guild Nr. `{len(self.bot.guilds)}`
{invite}"""
        e = discord.Embed(description=guild.name, title='Server Joined', color=1565439, timestamp=datetime.utcnow())
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name='Info', value=a)
        await join.send(embed=e)
        e = discord.Embed(
            description=f"Hey {guild.owner.name}, I just wanted to thank you for adding me here on your guild ! Feel free to join my [support server](https://discord.gg/wxBGu5f). Type `nya help` for more information about me & my commands ~",
            title='Thanks !', color=0xdb90f4)
        e.set_thumbnail(
            url='https://media.discordapp.net/attachments/612394933294202891/612403535979610142/JPEG_20190817_220553.jpg?width=300&height=300')
        try:
            await guild.owner.send(embed=e)
        except Exception as e:
            print(e.args)
        servchan = self.bot.get_channel(612343524658118665)
        await servchan.edit(name=f'{len(self.bot.guilds)} servers')

    @Cog.listener()
    async def on_guild_remove(self, guild):
        join = self.bot.get_channel(612353294718730240)
        a = f"""Owned by **{guild.owner}**
Member count : `{guild.member_count}`
Created at `{guild.created_at}`
Guild Nr. `{len(self.bot.guilds)}`"""
        e = discord.Embed(description=guild.name, title='Server Left', color=16744448, timestamp=datetime.utcnow())
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name='Info', value=a)
        await join.send(embed=e)
        servchan = self.bot.get_channel(612343524658118665)
        await servchan.edit(name=f'{len(self.bot.guilds)} servers')

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f'{redcross} | Check your input and try again.')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('❓')
            await asyncio.sleep(15)
            await ctx.message.remove_reaction(emoji='❓', member=ctx.guild.me)
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f'{redcross} | Your\'not allowed to use this command.')
        elif isinstance(error, commands.NotOwner):
            await ctx.send(f'{redcross} | You\'re not the bot owner.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{redcross} | A required argument is missing.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{redcross} | You\'re not allowed to use this command.')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'{redcross} | I can\'t execute this command.')
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f'{redcross} | You can\'t use this command in DM\'s.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{redcross} | This command is not usable right know due to a bug.')
        else:
            embedbasic = discord.Embed(color=discord.Color.red(),
                                       description='⚠ An unknown error occured! The error will be fixed as soon as possible. Please join our **[support server](https://discord.gg/wxBGu5f)** if you think you can give us details about the error c:')
            errorembed = discord.Embed(color=discord.Color.red(),
                                       title=f'Error caused by `{ctx.author}` ({ctx.author.id})',
                                       description=f'```py\n{error}\n```')
            errorembed.add_field(name='Server', value=f'**`{ctx.guild.name}`** ({ctx.guild.id})', inline=True)
            errorembed.add_field(name='Command', value=f'**{ctx.command.name}**')
            channel = ctx.bot.get_channel(612358161826840708)
            await ctx.send(embed=embedbasic)
            await channel.send(embed=errorembed)


def setup(bot):
    bot.add_cog(Listeners(bot))
