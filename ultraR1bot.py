import random
from discord.ext import commands
import os
import discord


print("██╗   ██╗██╗  ████████╗██████╗  █████╗ ██████╗  ██╗██████╗  ██████╗ ████████╗██████╗  ██████╗  ██████╗  ██████╗ ")
print("██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗███║██╔══██╗██╔═══██╗╚══██╔══╝╚════██╗██╔═████╗██╔═████╗██╔═████╗")
print("██║   ██║██║     ██║   ██████╔╝███████║██████╔╝╚██║██████╔╝██║   ██║   ██║    █████╔╝██║██╔██║██║██╔██║██║██╔██║")
print("██║   ██║██║     ██║   ██╔══██╗██╔══██║██╔══██╗ ██║██╔══██╗██║   ██║   ██║   ██╔═══╝ ████╔╝██║████╔╝██║████╔╝██║")
print("╚██████╔╝███████╗██║   ██║  ██║██║  ██║██║  ██║ ██║██████╔╝╚██████╔╝   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝")
print(" ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═╝╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ")
print("                                                                                                                ")
print("================================================================================================================")
print("> Initializing prefixes")

prefix = ('¤', 'UltraR1Bot le bot superieur, ', 'nique ta mere ','URB, ','URB ')

bot = commands.Bot(command_prefix=prefix)

print("> Done")

bot.load_extension('cogs.ultraR1commands')


@bot.command(name="reload", pass_context=True)
async def reload(ctx):
        bot.reload_extension('cogs.ultraR1commands')
        await ctx.send("reload terminé")


token = os.environ['DISCORDTOKEN']


bot.run(token)
