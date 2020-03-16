import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import json
import os

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

DB_USERNAME = os.environ["DBUSERNAME"]
DB_PASSWORD = os.environ["DBPASSWORD"]

client = MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@kanna-mgpcj.mongodb.net/test?retryWrites=true&w=majority")
db = client.dis_user

class Datacom(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def register(self, ctx):
        z = discord.Embed(title = "<a:loading:684031670520643640> | Creating your profile")
        y = await ctx.send(embed = z)
        
        db = client.profiles
        
        if user1 is not None:
            a = discord.Embed(title="⚠️ | You've already created an account.")
            await y.edit(embed=a)
        else:
            UNAME = ctx.author.name
            UID = ctx.author.id
            UDESC = "I'm a pretty chill person !"
            UMONEY = 1000
            ULEVEL = 1
        
        profile = {'ui' : UID,
        'ud' : UDESC,
        'um' : UMONEY,
        'ul' : URANK,
        }

        db.profiles.insert_one(profile)
        
        a = f"""**{UNAME}**'s profile
        `{UDESC}`
        Balance : {UMONEY} <a:nekocoins:689129268135067648>
        Level : {ULEVEL}"""
        
        e = discord.Embed(title = "✔️ | Neko-profile created !", description = a, color = 0x16c60c)
        
        await y.edit(embed=e)
        
def setup(bot):
    bot.add_cog(Datacom(bot))
