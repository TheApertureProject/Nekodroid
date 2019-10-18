import os

import aiohttp
import discord
from discord.ext import commands

osu_api_key = os.environ["OSUTOKEN"]
dis_api_key = os.environ["DISCOURSETOKEN"]
redcross = '<:white_cross_mark:612474623333761031>'


class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config
    
    @commands.group()
    async def osu(self, ctx, player_id):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://osu.ppy.sh/api/get_user", params={"k": osu_api_key, "u": player_id}) as resp:
                resp.raise_for_status()
                payload = await resp.json()
        if len(payload) == 0:
            await ctx.send(f'{redcross} | Couldn\'t find any user matching this name / ID.')
        else:
            user = payload[0]

            USERNAME = user["username"]
            USERID = user["user_id"]
            JOINDATE = user["join_date"]
            PLAYCOUNT = user["playcount"]
            PPRAW = user["pp_raw"]
            PPRANK = user["pp_rank"]
            COUNTRYRANK = user["pp_country_rank"]
            LEVEL = user["level"]
            COUNTRY = user["country"]

            country = COUNTRY.lower()
            a0 = float(LEVEL)
            a1 = int(a0)
            b0 = float(PLAYCOUNT)
            b1 = int(b0)
            c0 = float(PPRAW)
            c1 = int(c0)

            userinfo=f"""Joined {JOINDATE}
Level : `{a1}`
Ranked games count : `{b1}`"""
            
            ranking=f"""Total performance points : `{c1}`
Global ranking : `#{PPRANK}`
Country ranking : `#{COUNTRYRANK}`"""
            
            e = discord.Embed(title = f':flag_{country}: {USERNAME}', description=f':id: {USERID}', url = f'https://osu.ppy.sh/users/{USERID}', color = 0xFF69B4)
            e.set_author(name="osu! profile info", icon_url='https://media.discordapp.net/attachments/612394933294202891/613790628878221357/1566409482107.png')
            e.add_field(name='User information', value=userinfo)
            e.add_field(name='Ranking', value=ranking)
            e.set_thumbnail(url=f'https://a.ppy.sh/{USERID}')
            await ctx.send(embed = e)

    @commands.command(aliases = ['forumuser', 'forum', 'aperture', 'apertureuser', 'aperuser'])
    async def aper(self, ctx, user_name):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://forum.apertureproject.me/users", params={"username": user_name}) as resp:
                resp.raise_for_status()
                payload = await resp.json()
        if len(payload) == 0:
            await ctx.send(f'{redcross} | Couldn\'t find any user matching this name on aper.me.')
        else:
            user = payload[0]

            USERNAME = user["username"]
            USERID = user["id"]
            JOINEDAT = user["created_at"]
            LASTPOSTED = user["last_posted_at"]
            LASTSEEN = user["last_seen_at"]
            TRUSTLEVEL = user["trust_level"]
            BADGECOUNT = user["badge_count"]
            WEBSITE = user["website_name"]

            userinfo=f"""Joined {JOINEDAT}
Last posted at {LASTPOSTED}
Last seen at {LASTSEEN}
Trust level : `{TRUSTLEVEL}`
Badge count : `{BADGECOUNT}`
Personal website : `{WEBSITE}`"""

            e = discord.Embed(title = f'👥 {USERNAME}', description=f':id: {USERID}', url = f'https://forum.apertureproject.me/u/{USERNAME}', color = 0x00fad1)
            e.set_author(name="aper.me profile info", icon_url='https://forum.apertureproject.me/uploads/default/original/1X/402bed02389225af6e0777113915126691b88483.png')
            e.add_field(name='User information', value=userinfo)
            await ctx.send(embed = e)

def setup(bot):
    bot.add_cog(Stats(bot))
