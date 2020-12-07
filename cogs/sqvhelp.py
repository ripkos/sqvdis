import random
from discord.ext import commands


class sqvhelp(commands.Cog):
    # init
    def __init__(self, bot):
        self.bot = bot
        file = open('./res/sqv.txt', "r")
        self.content = file.readlines()
        self.size = len(self.content)

    # Commands
    @commands.command()
    async def helpme(self, ctx):
        num = random.randint(0, self.size)
        await ctx.send(self.content[num])

    @commands.command()
    async def clear(self, ctx, lim: int = 1):
        await ctx.channel.purge(limit=lim)

    # end


def setup(client):
    client.add_cog(sqvhelp(client))
