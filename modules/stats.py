import discord
from discord.ext import commands
import json
import os

osu_api_key = os.environ["OSUTOKEN"]

class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    @commands.command()
    async def osu(self, ctx, player_id):
        r = requests.get(url=f'https://osu.ppy.sh/p/api/get_user?k={osu_api_key}&u={player_id}')
        data = (await r.json())[0]
        user_name=data["user_name"]
        user_id=data["user_id"]
        join_date=data["join_date"]
        playcount=data["playcount"]
        pp_raw=data["pp_raw"]
        pp_rank=data["pp_rank"]
        level=["level"]
        country=["country"]
        e = discord.Embed(title = f'osu! Profile for user {user_name}', description=f'Player ID : {user_id}', url = f'https://osu.ppy.sh/users/{user_id}', color = 0xFF69B4)
        await ctx.send(embed = e)

def setup(bot):
    bot.add_cog(Stats(bot))
