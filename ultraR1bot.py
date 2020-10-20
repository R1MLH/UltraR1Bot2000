import random
from discord.ext import commands
import os
import discord


prefix = ('¤', 'UltraR1Bot le bot superieur, ', 'nique ta mere ')

bot = commands.Bot(command_prefix=prefix)

bot.load_extension('ultraR1commands')


@bot.command(name="reload", pass_context=True)
async def reload(ctx):
        bot.reload_extension('ultraR1commands')


token = os.environ['DISCORDTOKEN']


bot.run(token)
