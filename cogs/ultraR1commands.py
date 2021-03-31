from discord.ext import commands
import discord
import json
import yaml
import datetime
 
import asyncio



class UltraR1Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", pass_context=True)
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command(name="pasta", aliases=['copypasta', "cp"], pass_context=True)
    async def pasta(self, ctx, pasta):
        await ctx.send("WIP")

    @commands.command(name="remind", pass_context=True)
    async def remind(self, ctx, reminder, time:int): 
        self.bot.bg_task = self.bot.loop.create_task(self.timer(datetime.timedelta(seconds=time).seconds,reminder,ctx))
        print('added reminder task')


    @commands.command(name="changeActivity", pass_context=True)
    async def changeActivity(self, ctx, Acttype:int, lolxd):
        await self.bot.change_presence(activity=discord.Activity(name=lolxd, type=Acttype))
        await ctx.send('voila')


    async def timer(self,timestamp,reminder,context):
        await self.bot.wait_until_ready()
        await asyncio.sleep(timestamp)
        await context.send(reminder)


    @commands.command(name="reminderDebug",pass_context=True)
    async def reminderDebug(self,ctx):
        reminders=self.checkDate(datetime.date.today())
        for message in reminders:
            await ctx.send(message)
    
    @commands.command(name="remindMe",pass_context=True)
    async def remindMe(self,ctx,date,message):
        try:
            datetime.date.fromisoformat(date)
            with open("./data/reminders.yaml",'a') as f:
                 f.write("  - !!python/tuple [{},{}]\n".format(date,message))
            await ctx.send("Reminder set: {}, {}".format(date,message))
        except:
            await ctx.send("La date doit etre au format YYYY-MM-DD")
        


    def checkDate(self,date):
        with open("./data/reminders.yaml") as f:
            reminders = yaml.load(f)
        return [x[1] for x in reminders if x[0]==date]     


def setup(bot):
    print("> Loading Commands Cog")
    bot.add_cog(UltraR1Commands(bot))
    print("> Command Cog Loaded")

def teardown(bot):
    print("> Removing Commands Cog")
    bot.remove_cog('UltraR1Commands')
    print("> Commands Cog Removed")
