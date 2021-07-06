# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:38:21 2021

@author: Admin
"""

import discord
from discord import channel
from discord import file
from discord.ext import commands
from discord.flags import Intents
import json
import random
import os

with open('setting.json','r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.default()
intents.members=True
intents.presences=False
bot= commands.Bot(command_prefix='[',intents=intents)


@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'un-loaded {extension} done.')

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done.')
    
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f're-loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if__name__="__main__"        
bot.run(jdata['TOKEN'])