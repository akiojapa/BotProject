import discord
from discord.ext import commands


# client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class Test(commands.Cog, name="test"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send("Teste!")


def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))
