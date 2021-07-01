from re import M
import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}毫秒')
    
    @commands.command()
    async def hi(self,ctx):
        await ctx.send('12457rredwqdsfsefwqfdawdaw5')

def setup(bot):
    bot.add_cog(Main(bot))