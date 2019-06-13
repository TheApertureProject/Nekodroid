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
        except HTTPException:
            await ctx.send("❎ | I'm sorry, nya ! I can not clear messages older than two weeks.")

def setup(bot):
    bot.add_cog(Moderator(bot))
