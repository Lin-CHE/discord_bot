# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:38:21 2021

@author: Admin
"""

import discord
from discord import channel
from discord.ext import commands
from discord.flags import Intents
intents=discord.Intents.default()
intents.members=True
intents.presences=False
bot= commands.Bot(command_prefix='[',intents=intents)


@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(860064974302609429)
    await channel.send(f'{member} join!!')
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(860065136219521045)
    await channel.send(f'{member} leave!!')

bot.run('ODYwMDQxNDk5OTA3NTg4MDk2.YN1eEA.FGii3vKbbAGnsi6RzL83v3KwI_Y')