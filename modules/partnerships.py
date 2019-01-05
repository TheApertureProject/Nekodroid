import discord
from discord.ext import commands

class Partnership:

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    def is_communitymanager(ctx):
        whitelisted = [520312070256984087, 458586186328571913]
        if ctx.author.id in whitelisted:
            return True
        else:
            return False

    
    @commands.check(is_communitymanager)
    @commands.command()
    async def extpartnership(self, ctx, chan: discord.TextChannel, mentionning):
        a = """***[__The Aperture Project__](https://discord.gg/JEUUM8c)***

Rejoignez dès maintenant Aperture, le tout nouveau serveur dédié aux anime, au kawaii et à la photographie !

🤙 Une communauté **active**, à qui parler du **moindre de vos problèmes** ! **_(et des câlins x3)_**

🍋 Des **emotes** inédites et originales !

👌 Un design **esthétique** et **innovant** !

🆘 Un staff actif et à l'écoute !

💮 Du **kawaii** et des **animes** !

🔣 La flopée de **rôles self-attribuables** pour montrer aux autres vos passions et jeux vidéos ! 

🎉 Des **giveaways** !

🤖 Un bot dédié au serveur, accessible à tous :3"""
        e = discord.Embed(name='Join server', description=a, color=0x1a53ff, url='https://discord.gg/JEUUM8c')
        e.set_image(url='https://cdn.discordapp.com/attachments/466600971213209602/473418748959653888/20180730_111606.gif')
        e.set_thumbnail(url='https://cdn.discordapp.com/attachments/489041727697584148/503466180481384448/1528224039633.png')
        await chan.send(embed=e)
        if mentionning == 'here':
            await chan.send('@here')
        elif mentionning == 'everyone':
            await chan.send('@everyone')
        else :
            pass

def setup(bot):
    bot.add_cog(Partnership(bot))
