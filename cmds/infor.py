import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Infor(Cog_Extension):
    @commands.command()
    async def DnD5E中文化(self, ctx):
        embed=discord.Embed(title="D&D 5E 中文化", url="https://trpgtdnd.weebly.com")
        embed.add_field(name="+聖騎士", value="聖騎士的相關資料", inline=True)
        embed.add_field(name="+精靈", value="精靈的相關資料", inline=True)
        embed.add_field(name="+兼職規則", value="兼職規則的相關資料", inline=True)
        embed.add_field(name="+怪物種類", value="怪物種類的相關資料", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Infor(bot))