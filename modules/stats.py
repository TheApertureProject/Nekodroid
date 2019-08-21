import discord
from discord.ext import commands
import aiohttp
import json
import os

osu_api_key = os.environ["OSUTOKEN"]
redcross = '<:white_cross_mark:612474623333761031>'

class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    @commands.command()
    async def osu(self, ctx, player_id):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://osu.ppy.sh/api/get_user", params={"k": osu_api_key, "u": player_id}) as resp:
                resp.raise_for_status()
                payload = await resp.json()
        if len(payload) == 0:
            await ctx.send(f'{redcross} | Couldn\'t find any user matching this name / ID.')
        user=payload[0]
        USERNAME=user["username"]
        USERID=user["user_id"]
        JOINDATE=user["join_date"]
        PLAYCOUNT=user["playcount"]
        PPRAW=user["pp_raw"]
        PPRANK=user["pp_rank"]
        LEVEL=user["level"]
        COUNTRY=user["country"]
        e = discord.Embed(title = f'osu! Profile for user {USERNAME}', description=f'Player ID : {USERID}', url = f'https://osu.ppy.sh/users/{USERID}', color = 0xFF69B4)
        await ctx.send(embed = e)

def setup(bot):
    bot.add_cog(Stats(bot))
