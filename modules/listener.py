import discord
from discord.ext import commands
import asyncio
import discord
import json
from datetime import datetime

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

PREFIX = config["prefix"]

class Listeners:
	
    def __init__(self, bot):
        self.bot = bot

#    async def on_message(self, message):     
#        if self.bot.user.mentioned_in(message):   
#            await message.channel.send(f'My prefix here is `{PREFIX}`.')
   
    async def on_member_join(self, member):
        if member.guild.id == 462871882916560896:
            role = discord.utils.get(member.guild.roles, name='Members')
            await member.add_roles(role)
            e=discord.Embed(description="Thanks for joining my support server !", title=f'Welcome, {member.name} !', color=0xdb90f4)
            e.set_thumbnail(url='https://cdn.discordapp.com/attachments/476653267036930049/528247247574401025/WindowKamuis.gif')
            e.set_image(url='https://cdn.discordapp.com/attachments/476653267036930049/528247286598467614/train-girl.jpg')
            await member.send(embed=e)

    async def on_guild_join(self, guild):
        join = self.bot.get_channel(462875598184775700)
        a = f"""Owned by **{guild.owner}**
Member count : `{guild.member_count}`
Created at `{guild.created_at}`
Guild Nr. `{len(self.bot.guilds)}`"""
        e = discord.Embed(description=guild.name, title='Server Joined', color=1565439, timestamp=datetime.utcnow())
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name='Info', value=a)
        await join.send(embed=e)
        e = discord.Embed(description=f"Hey {guild.owner.name}, I just wanted to thank you for adding me here on your guild ! Feel free to join my [support server](https://discord.gg/PTT9UpZ). Type `k!help` for more information about me & my commands ~", title='Thanks !', color=0xdb90f4)
        e.set_thumbnail(url='https://cdn.discordapp.com/attachments/476653267036930049/526223217749393417/458776090752843786.png')
        try:
            await guild.owner.send(embed=e)
        except Exception as e:
            print(e.args)
        servchan=self.bot.get_channel(527180509542088704)
        await servchan.edit(name=f'{len(self.bot.guilds)} servers')

    async def on_guild_remove(self, guild):
        join = self.bot.get_channel(462875598184775700)
        a = f"""Owned by **{guild.owner}**
Member count : `{guild.member_count}`
Created at `{guild.created_at}`
Guild Nr. `{len(self.bot.guilds)}`"""
        e = discord.Embed(description=guild.name, title='Server Left', color=16744448, timestamp=datetime.utcnow())
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name='Info', value=a)
        await join.send(embed=e)
        servchan=self.bot.get_channel(527180509542088704)
        await servchan.edit(name=f'{len(self.bot.guilds)} servers')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f'⚠ Check your input and try again.')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction('❓')
            await asyncio.sleep(15)
            await ctx.message.remove_reaction(emoji='❓', member=ctx.guild.me)
        elif isinstance(error, commands.CheckFailure):
            await ctx.send('⚠ Your\'not allowed to use this command.')
        elif isinstance(error, commands.NotOwner):
            await ctx.send('⚠ You\'re not the bot owner.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('⚠ A required argument is missing.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('⚠ You\'re not allowed to use this command.')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('⚠ I can\'t execute this command.')
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('⚠ You can\'t use this command in DM\'s.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('⚠ This command is not usable right know due to a bug.')
        else:
            embedbasic = discord.Embed(color=discord.Color.red(), description='⚠ An unknown error occured! The error will be fixed as soon as possible. Please join our **[support server](https://discord.gg/PTT9UpZ)** if you think you can give us details about the error c:')
            errorembed = discord.Embed(color=discord.Color.red(), title=f'Error caused by {ctx.author} ({ctx.author.id})', description=f'```py\n{error}\n```')
            errorembed.add_field(name='Server', value=f'**{ctx.guild.name}** ({ctx.guild.id})', inline=True)
            errorembed.add_field(name='Command', value=f'**{ctx.command.name}**')
            channel = ctx.bot.get_channel(462876207097053195)
            await ctx.send(embed=embedbasic)
            await channel.send(embed=errorembed)

def setup(bot):
    bot.add_cog(Listeners(bot))
