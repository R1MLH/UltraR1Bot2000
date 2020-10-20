from discord.ext import commands



class UltraR1Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", pass_context=True)
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command(name="pong", pass_context=True)
    async def pong(self, ctx, number: int):
        for i in range(number):
            await ctx.send('pong')
            
    @commands.command(name="pingus", pass_context=True)
    async def pingus(self, ctx):
        await ctx.send('pongus')

    @commands.command(name="test", pass_context=True)
    async def test(self, ctx):
        await ctx.send('test ok')

def setup(bot):
    print("Loading Commands Cog")
    bot.add_cog(UltraR1Commands(bot))

def teardown(bot):
    print('Removing commands Cog')
    bot.remove_cog('UltraR1Commands')
