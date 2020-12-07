import cogs.sqvrofl
from cogs.util.jediutil import trash


async def pepper(payload, bot):
    ctx = bot.get_channel(payload.channel_id)
    tosend = trash()
    await ctx.send(tosend)
    msg = await ctx.send("Next? 🌶️")
    await msg.add_reaction('🌶️')
