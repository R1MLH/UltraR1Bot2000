from discord.ext import commands
import discord
import json
from datetime import datetime, timedelta
 
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
        self.bot.bg_task = self.bot.loop.create_task(self.timer(timedelta(seconds=time).seconds,reminder,ctx))
        print('added reminder task')


    @commands.command(name="changeActivity", pass_context=True)
    async def changeActivity(self, ctx, Acttype:int, lolxd):
        await self.bot.change_presence(activity=discord.Activity(name=lolxd, type=Acttype))
        await ctx.send('voila')


    async def timer(self,timestamp,reminder,context):
        await self.bot.wait_until_ready()
        await asyncio.sleep(timestamp)
        await context.send(reminder)

            


def setup(bot):
    print("Loading Commands Cog")
    bot.add_cog(UltraR1Commands(bot))

def teardown(bot):
    print('Removing commands Cog')
    bot.remove_cog('UltraR1Commands')
