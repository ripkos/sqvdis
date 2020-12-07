from discord.ext import commands
import random
from cogs.util.jediutil import parse, trash


class sqvrofl(commands.Cog):
    # init
    def __init__(self, bot):
        self.bot = bot
        file = open('./res/sqv.txt', "r")
        self.content = file.readlines()
        self.size = len(self.content)

    # Commands
    @commands.command()
    async def q(self, ctx):
        num = random.randint(0, self.size)
        await ctx.send(self.content[num])

    @commands.command()
    async def jedi(self, ctx, pagenum=1):
       # tosend = "номер должен быть 1, 2 или 3"
        #if pagenum == 3:
        tosend = trash()
        await ctx.send(tosend)

    # end


def setup(client):
    client.add_cog(sqvrofl(client))
