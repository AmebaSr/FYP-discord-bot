import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

#加入
class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(jdata['Welcome_channel'])
        await channel.send(f'{member} join!')
#離開
    @commands.Cog.listener()
    async def on_member_remove(self, member):
     channel = self.bot.get_channel(jdata['Left_channel'])
     await channel.send(f'{member} left!')  

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content in jdata['keyword'] and msg.author !=self.bot.user:
            await msg.channel.send('Lets start!')
        elif msg.content in jdata['chkeyword'] and msg.author !=self.bot.user:
            await msg.channel.send('讓我們開始吧！')

#通用錯誤
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return 
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("你倒是把話說完啊？")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("我沒見過這指令喔")
        else:
            await ctx.send("成功地失敗了")

#新增身份組
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        # add role
        if data.message_id == 734397919758778408:
            if str(data.emoji) == '<:litotter:733875102512316456>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(733867542421962883)
                await data.member.add_roles(role)
                await data.member.send(f"You are now a {role}！")
                await data.member.send("Now you can see 真理之塔！")
            if str(data.emoji) == '<:angerpeach:733875102126702625>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(733864565191868466)
                await data.member.add_roles(role)
                await data.member.send(f"You are now a part of {role}！")
                await data.member.send("冒險家之家's door is open for you！")
        #新增身份組    
        if data.message_id == 733968290443034665:
            if str(data.emoji) == '<:litotter:733875102512316456>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(733867542421962883)
                await data.member.add_roles(role)
                await data.member.send(f"你成為了了一個{role}！")
                await data.member.send("你可以進入真理之塔了！")
            if str(data.emoji) == '<:angerpeach:733875102126702625>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(733864565191868466)
                await data.member.add_roles(role)
                await data.member.send(f"你成為了一個{role}！")
                await data.member.send("冒險家之家的大門為你打開！")
                
              
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        #drop role
        if data.message_id == 734397919758778408:
            if str(data.emoji) == '<:litotter:733875102512316456>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(733867542421962883)
                await user.remove_roles(role)
                await user.send(f"You lose {role} identity...")
            if str(data.emoji) == '<:angerpeach:733875102126702625>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(733864565191868466)
                await user.remove_roles(role)
                await user.send(f"You lose {role} identity...")
        #失去身份組
        if data.message_id == 733968290443034665:
            if str(data.emoji) == '<:litotter:733875102512316456>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(733867542421962883)
                await user.remove_roles(role)
                await user.send(f"你失去了了{role}的身份...")
            if str(data.emoji) == '<:angerpeach:733875102126702625>':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(733864565191868466)
                await user.remove_roles(role)
                await user.send(f"你失去了{role}的身份...")


def setup(bot):
    bot.add_cog(Event(bot))
    