import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import re

with open('setting.json','r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel=self.bot.get_channel(int(jdata['welcome_channel']))
        await channel.send(f'{member} join!!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel=self.bot.get_channel(int(jdata['leave_channel']))
        await channel.send(f'{member} leave!!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword=['apple','pie','abc']
        if msg.content in keyword and msg.author!=self.bot.user:
            await msg.channel.send('apple')

def setup(bot):
    bot.add_cog(Event(bot))