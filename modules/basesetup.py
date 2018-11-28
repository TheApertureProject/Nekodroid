import discord
from discord.ext import commands
import datetime

class BaseSetup:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    MAINSERV = 462871882916560896

    async def on_guild_join(self, guild):
        my_guild = bot.get_guild()
        join = my_guild.get_channel(MAINSERV)
        e = discord.Embed(description='', title=f'Server Joined - {guild.name}', color=1565439, timestamp=datetime.utcnow())
        e.add_field(name=f'Member count : {guild.member_count}', value=f'Created at {guild.created_at}')
        e.set_footer(text='Kanna - The Kawaii Discord bot')
        await join.send(embed=e)

    async def on_guild_remove(self, guild):
        my_guild = bot.get_guild(MAINSERV)
        join = my_guild.get_channel(462875598184775700)
        e = discord.Embed(description='', title='Server left - {guild.name}', color=16744448, timestamp=datetime.utcnow())
        e.add_field(name=f'Member count : {guild.member_count}', value=f'Created at {guild.created_at}')
        e.set_footer(text='Kanna - The Kawaii Discord bot')
        await join.send(embed=e)

    async def on_member_join(self, member):
        if member.guild.id == MAINSERV:
            role = discord.utils.get(member.guild.roles, name='Members')
            await member.add_roles(role)

def setup(bot):
    bot.add_cog(BaseSetup(bot))
