from re import M
import discord
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import datetime
class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}毫秒')
    
    @commands.command()
    async def hi(self,ctx):
        await ctx.send('12457rredwqdsfsefwqfdawdaw5')
    
    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="aswqdq", url="https://www.pixiv.net/", description="dwdwdw", color=0xc91818,
        timestamp= (datetime.datetime.now()+datetime.timedelta(hours=-8)))
        embed.set_author(name="gert", url="https://memes.tw/gif/796", icon_url="https://memes.tw/gif/796")
        embed.set_thumbnail(url="https://memes.tw/gif/804")
        embed.add_field(name="asdw", value="11", inline=False)
        embed.add_field(name="ddd", value="55", inline=True)
        embed.add_field(name="wdwq333", value="5757", inline=True)
        embed.add_field(name="wdqd", value="556", inline=True)
        embed.set_footer(text="13265958")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=(num+1))


def setup(bot):
    bot.add_cog(Main(bot))