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
        try:
            if reason==None:
                await member.ban()
                await ctx.send('Member'+member+'was successfully banned ! Good bye !')
                await ctx.send('And dont come back !')
            else:
                await member.ban(reason=reason)
                await ctx.send(f'Member'+member+'was successfully banned for the following reason : {reason} ! Good bye !')
        except Exception as e:
            print(e.args)
            await ctx.send('An error occured. Check your permissions & the way you wrote the username.')

    @commands.guild_only()    
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, *, member: discord.Member):
        try:
            await member.kick()
            await ctx.send('Member', member, 'was successfully kicked ! Babaï !')
        except Exception as e:
            print(e.args)
            await ctx.send('An error occured. Check your permissions & the way you wrote the username.')

    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()
        try:
            deleted = await ctx.channel.purge(limit=amount)
            await ctx.send(f"`{len(deleted)}` messages successfully deleted !", delete_after = 5)
        except:
            await ctx.send("Something went wrong. Please retry indicating positive numbers only, and check your permissions.")

def setup(bot):
    bot.add_cog(Moderator(bot))
