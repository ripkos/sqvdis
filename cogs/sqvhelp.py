from discord.ext import commands


class sqvhelp(commands.Cog):
    # init
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command()
    async def clear(self, ctx, lim: int = 1):
        await ctx.channel.purge(limit=lim)

    # end


def setup(client):
    client.add_cog(sqvhelp(client))
