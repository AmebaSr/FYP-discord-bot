import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot (command_prefix='+')

@bot.event
async def on_ready(): 
    print(" >> SC_Bot ONLINE <<")

#load
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')
#載入
@bot.command()
async def 載入(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'載入 {extension} 成功.')

#unload
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')
    
#解除
@bot.command()
async def 解除(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'解除 {extension} 成功.')

#reload
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done.')
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
