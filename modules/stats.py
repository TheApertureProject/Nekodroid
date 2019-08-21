import discord
from discord.ext import commands
import requests
import json
import os

osu_api_key = os.environ["OSUTOKEN"]

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
            await bot.send('error')
        USERNAME=payload["user_name"]
        USERID=payload["user_id"]
        JOINDATE=payload["join_date"]
        PLAYCOUNT=payload["playcount"]
        PPRAW=payload["pp_raw"]
        PPRANK=payload["pp_rank"]
        LEVEL=payload["level"]
        COUNTRY=payload["country"]
        e = discord.Embed(title = f'osu! Profile for user {user_name}', description=f'Player ID : {user_id}', url = f'https://osu.ppy.sh/users/{user_id}', color = 0xFF69B4)
        await ctx.send(embed = e)

def setup(bot):
    bot.add_cog(Stats(bot))
