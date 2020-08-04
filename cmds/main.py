import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import random
import json
import math

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('hi!')

#listall function
    @commands.command()
    async def listall(self, ctx):
        embed=discord.Embed(title="useable command", description="Please add + before using the command")
        embed.add_field(name="help", value="show discord command list", inline=True)
        embed.add_field(name="listall", value="show this list", inline=True)
        embed.add_field(name="rand_squad", value="random squad", inline=True)
        embed.add_field(name="D&D 5E 中文化", value="show D&D 5E 中文化 website information", inline=True)
        embed.add_field(name="gdrive", value="show google drive ", inline=True)
        embed.add_field(name="clean", value="Clean message", inline=True)
        embed.add_field(name="bosslist", value="show a list of boss ID and name", inline=True)
        embed.add_field(name="boss", value="Show boss hp", inline=True)
        embed.add_field(name="attack", value="Attack boss", inline=True)
        embed.add_field(name="heal", value="Heal boss", inline=True)
        await ctx.send(embed=embed)

#列出指令
    @commands.command()
    async def 列出指令(self, ctx):
        embed=discord.Embed(title="可用的指今", description="在指令前請加+")
        embed.add_field(name="help", value="呼叫官方的指今表 ", inline=True)
        embed.add_field(name="列出指令", value="呼叫這個指今表", inline=True)
        embed.add_field(name="分隊", value="隨機組隊", inline=True)
        embed.add_field(name="D&D 5E 中文化", value="呼叫D&D 5E 中文化網頁的資訊", inline=True)
        embed.add_field(name="雲端", value="呼叫雲端硬件", inline=True)
        embed.add_field(name="清除", value="清除指定數量的信訊", inline=True)
        await ctx.send(embed=embed)

#L.L.ver_COC
    @commands.command()
    async def example(self, ctx):
        await ctx.send("https://docs.google.com/spreadsheets/d/18REjYeUMsbq3PJuy59I0bkrXsycf85ieji6P9rMUkcY/edit#gid=1351844922")

#call gdrive
    @commands.command()
    async def gdrive(self, ctx):
        embed=discord.Embed(title="Google Drive", description="google drive", url="https://drive.google.com/drive/folders/1fJjWGzDPiEZwNvPOdJD0vRO0UkhzBgTf?usp=sharing")
        await ctx.send(embed=embed)

#呼叫雲端硬件
    @commands.command()
    async def 雲端(self, ctx):
        embed=discord.Embed(title="呼叫雲端硬件", description="google drive", url="https://drive.google.com/drive/folders/1fJjWGzDPiEZwNvPOdJD0vRO0UkhzBgTf?usp=sharing")
        await ctx.send(embed=embed)

#request role
    @commands.command()
    async def request(self, ctx):
        embed=discord.Embed(title="Available request", description="Please click on the emoji to join the role")
        embed.add_field(name="冒險家", value="<:litotter:733875102512316456>", inline=True)
        embed.add_field(name="魔法師", value="<:angerpeach:733875102126702625>", inline=True)
        await ctx.send(embed=embed)

#職業申請
    @commands.command()
    async def 職業申請(self, ctx):
        embed=discord.Embed(title="職業申請", description="請加入表情，以申請職業")
        embed.add_field(name="冒險家", value="<:litotter:733875102512316456>", inline=True)
        embed.add_field(name="魔法師", value="<:angerpeach:733875102126702625>", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

#clean
    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

#清除
    @commands.command()
    async def 清除(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

#rand_squad
    @commands.command()
    async def rand_squad(self, ctx, playernum:int, matenum:int):
        self.playernum = playernum
        self.matenum = matenum
        
        online = []
        for member in ctx.guild.members:
            if str(member.status) == 'online': 
            #and member.bot == False:
                online.append(member.name)
        if (self.playernum % self.matenum) == 0:
            self.range = (self.playernum // self.matenum)
            #await ctx.send(f"{self.range}")
            random_online = random.sample(online, k=self.playernum)
            for squad in range(self.range):
                a = random.sample(random_online, k=self.matenum)
                await ctx.send(f"Squad{squad+1}"+str(a))
                for name in a:
                    random_online.remove(name)
        else: 
            await ctx.send(f"{self.playernum} cannot group to {self.range} team(s)")

#分隊
    @commands.command()
    async def 分隊(self, ctx, playernum:int, matenum:int):
        self.playernum = playernum
        self.matenum = matenum
        
        online = []
        for member in ctx.guild.members:
            if str(member.status) == 'online': 
            #and member.bot == False:
                online.append(member.name)
        if (self.playernum % self.matenum) == 0:
            self.range = (self.playernum // self.matenum)
            #await ctx.send(f"{self.range}")
            random_online = random.sample(online, k=self.playernum)
            for squad in range(self.range):
                a = random.sample(random_online, k=self.matenum)
                await ctx.send(f"第{squad+1}小隊"+str(a))
                for name in a:
                    random_online.remove(name)
        else: 
            await ctx.send(f"{self.playernum} 不能分成完整的{self.matenum}人小隊")



    @rand_squad.error
    async def rand_squad_error(self, ctx, error):
            await ctx.send("分不到隊啦！")

#random dice
    @commands.command()
    async def randice(self, ctx, maxnum:int, dicenum:int):
        self.maxresult = 0
        for i in range(dicenum):
            self.result = 0
            self.result = random.randint(1, maxnum)
            await ctx.send(f"Dice{i+1} result is {self.result}" )
            self.maxresult += self.result
        await ctx.send(f"The result is {self.maxresult}")

#roll compare
    @commands.command()
    async def compare(self, ctx, maxnum:int, dicenum:int, taget:int):
        self.maxresult = 0
        for i in range(dicenum):
            self.result = 0
            self.result = random.randint(1, maxnum)
            self.maxresult += self.result
        if self.maxresult >= taget:
            await ctx.send("Success")
        else:
            await ctx.send("Fail")

#boss list
    @commands.command()
    async def bosslist(self, ctx):
        for i in range(3):
            self.name = jdata['boss'][i]
            await ctx.send(f"Boss NO.{i} : {self.name}")
        

#show boss
    @commands.command()
    async def boss(self, ctx, num:int):
        self.name = jdata['boss'][num]
        self.bosshp = jdata[f'{self.name}'][0]
        if self.bosshp > 0:
            await ctx.send(f"{self.name} still have {self.bosshp} hp")
        else:
            self.killer = jdata[self.name][1]
            await ctx.send(f"{self.name} is dead, killed by {self.killer}")


#attack
    @commands.command()
    async def attack(self, ctx, bossnum:int, maxnum:int, dicenum:int):
        self.name = jdata['boss'][bossnum]
        self.bosshp = jdata[self.name][0]
        self.maxresult = 0
        self.attacker = ctx.message.author.name
        if self.bosshp > 0 :
            for i in range(dicenum):
                self.result = 0
                self.result = random.randint(1, maxnum)
                self.maxresult += self.result
                await ctx.send(f"Dice{i+1} result is {self.result}" )
            await ctx.send(f"{self.maxresult}")
            self.bosshp -=self.maxresult 
            await ctx.send(f"You have make {self.maxresult} damage to {self.name}" )

            if self.bosshp > 0 :
                await ctx.send(f"{self.name} still have {self.bosshp} hp") 
                jdata[self.name][0] = self.bosshp
                with open('setting.json','w', encoding='utf8') as jfile:
                    json.dump(jdata, jfile, indent=4)
            else:
                await ctx.send(f"{self.name} is dead, killed by {self.attacker}")
                jdata[self.name][1] = self.attacker
                with open('setting.json','w', encoding='utf8') as jfile:
                    json.dump(jdata, jfile, indent=4)
                jdata[self.name][0] = 0
                with open('setting.json','w', encoding='utf8') as jfile:
                    json.dump(jdata, jfile, indent=4)
                await ctx.send(f"You have kill{self.name} !")
        else:
            self.killer = jdata[self.name][1]
            await ctx.send(f"{self.name} is already dead, killed by {self.killer}")

    #heal
    @commands.command()
    async def heal(self, ctx, bossnum:int, heal:int ):
        self.name = jdata['boss'][bossnum]
        self.bosshp = jdata[self.name][0]
        self.healed = heal
        self.bosshp += self.healed
        jdata[self.name][0] = self.bosshp
        with open('setting.json','w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send(f"You heal{self.name} for {self.healed} hp!")
        await ctx.send(f"{self.name} now have {self.bosshp} hp!")


        
        

        


def setup(bot):
    bot.add_cog(Main(bot))