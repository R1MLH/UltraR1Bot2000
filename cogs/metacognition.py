from discord.ext import commands
import discord
import subprocess


class MetaCognition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ls", pass_context=True)
    async def ls(self, ctx):
        lf = subprocess.run(["git","status"],stdout=subprocess.PIPE,text=True)
        await ctx.send(lf.stdout)


def setup(bot):
    print("> Loading Meta Commands Cog")
    bot.add_cog(MetaCognition(bot))
    print("> Meta Command Cog Loaded")

def teardown(bot):
    print("> Removing Meta Commands Cog")
    bot.remove_cog('MetaCognition')
    print("> Meta Commands Cog Removed")
