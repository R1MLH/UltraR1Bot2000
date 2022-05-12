import random
from discord.ext import commands
import os
import discord


print("██╗   ██╗██╗  ████████╗██████╗  █████╗ ██████╗  ██╗██████╗  ██████╗ ████████╗")
print("██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗███║██╔══██╗██╔═══██╗╚══██╔══╝")
print("██║   ██║██║     ██║   ██████╔╝███████║██████╔╝╚██║██████╔╝██║   ██║   ██║   ")
print("██║   ██║██║     ██║   ██╔══██╗██╔══██║██╔══██╗ ██║██╔══██╗██║   ██║   ██║   ")
print("╚██████╔╝███████╗██║   ██║  ██║██║  ██║██║  ██║ ██║██████╔╝╚██████╔╝   ██║   ")
print(" ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═╝╚═════╝  ╚═════╝    ╚═╝   ")
print("                                                                             ")
print("=============================================================================")
print("> Initializing prefixes")

prefix = ('¤', 'UltraR1Bot le bot superieur, ', 'nique ta mere ','URB, ','URB ')

bot = commands.Bot(command_prefix=prefix)

print("> Done")
print("> Loading Base Commands")
bot.load_extension('cogs.ultraR1commands')
print("> Loading Meta Commands")
bot.load_extension('cogs.metacognition')
print("> Initialization complete")

@bot.command(name="reload", pass_context=True)
async def reload(ctx):
        bot.reload_extension('cogs.ultraR1commands')
        bot.reload_extension('cogs.metacognition')
        await ctx.send("reload terminé")


token = os.environ['DISCORDTOKEN']


bot.run(token)
