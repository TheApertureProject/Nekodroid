import asyncio
import aiohttp
  
token = 'xxx'

class Update(commands.Cog): 
  
    def __init__(self, bot):
        self.bot = bot 
        self.session = aiohttp.ClientSession(loop=self.bot.loop) 
  
    async def update(self):
        guild_count = len(self.bot.guilds)
        payload = json.dumps({
        'server_count': guild_count
        })
  
        headers = {
            'authorization': token,
            'content-type': 'application/json'
        }
  
        url = 'https://divinediscordbots.com/bots/{}/stats'.format(self.bot.user.id)
        
    async with self.session.post(url, data=payload, headers=headers) as resp:
        print('divinediscordbots statistics returned {} for {}'.format(resp.status, payload))
 
    async def on_guild_join(self, guild): 
        await self.update()
  
    async def on_guild_remove(self, guild): 
        await self.update()
  
    async def on_ready(self):
        await self.update()
  
def setup(bot):
    bot.add_cog(Update(bot))
