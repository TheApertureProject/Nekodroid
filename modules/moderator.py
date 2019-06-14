import discord
from discord.ext import commands

class Moderator(commands.Cog):
    
    conf = {}
	
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        if reason==None:
            await member.ban()
            await ctx.send('✅ | Member'+member+'was successfully banned ! Good bye !')
        else:
            await member.ban(reason=reason)
            await ctx.send(f'✅ | Member {member} was successfully banned for the following reason : {reason} ! Good bye !')

    @commands.guild_only()    
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, *, member: discord.Member):
        await member.kick()
        await ctx.send('Member', member, 'was successfully kicked ! Babaï !')

    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()
        try:
            deleted = await ctx.channel.purge(limit=amount)
            await ctx.send(f"✅ | `{len(deleted)}` messages successfully deleted !", delete_after = 5)
        except discord.HTTPException:
            await ctx.send(f"❎ | I'm sorry, but I can't delete messages older than two weeks. Nya !")


    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mute(self, ctx, member=discord.Member, reason):
        muted = discord.utils.get(ctx.guild.roles, name='Muted')
        if muted is not None:
            await ctx.send('❎ | The `Muted` role was created already, nya.')
        else:
            guild = ctx.guild
            await guild.create_role(name="Muted")
            await ctx.send('✅ | The `Muted` role was succesfully created !')


    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mute(self, ctx, member=discord.Member, reason):
        muted = discord.utils.get(ctx.guild.roles, name='Muted')
        if muted is not None:
            role = discord.utils.get(name="Muted", ctx.guild.roles)
            await member.add_roles(role)
            if reason == None:
                await ctx.send(f'✅ | Member `{member}` successfully muted, nya !')
            else:
                await ctx.send(f'✅ | Member `{member}` successfully muted for the following reason :```{reason}``` Nya !')
        else:
            await ctx.send('❎ | The `Muted` role doesn\'t exist. Please create it first, or let me do that for you by typing `nya!setmute`.')

def setup(bot):
    bot.add_cog(Moderator(bot))
