import discord
from discord.ext import commands

redcross = ':white_cross_mark:589227645753884672'

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
            await ctx.send(f"{redcross} | I'm sorry, but I can't delete messages older than two weeks. Nya !")

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def setmute(self, ctx):
        muted = discord.utils.get(ctx.guild.roles, name='Muted'.casefold())
        if muted is not None:
            await ctx.send(f'{redcross} | The `Muted` role was created already, nya.')
        else:
            guild = ctx.guild
            await guild.create_role(name="Muted")
            await ctx.send('✅ | The `Muted` role was succesfully created !')

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mute(self, ctx, usr:discord.Member, REASON = None):
        muted = discord.utils.get(ctx.guild.roles, name='Muted'.casefold())
        if muted is not None:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await usr.add_roles(role)
            if not REASON:
                await ctx.send(f'✅ | Member `{usr}` was successfully muted, nya !')
            else:
                await ctx.send(f'✅ | Member `{usr}` was successfully muted for the following reason :```{REASON}``` Nya !')
        else:
            await ctx.send(f'{redcross} | The `Muted` role doesn\'t exist. Please create it first, or let me do that for you by typing `nya!setmute`.')

    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def unmute(self, ctx, usr:discord.Member):
        mrole = discord.utils.get(ctx.guild.roles, name="Muted".casefold())
        await usr.remove_roles(mrole)
        await ctx.send(f'✅ | Member `{usr}` was successfully unmuted, nya.')

def setup(bot):
    bot.add_cog(Moderator(bot))
