import cogs.sqvrofl


async def pepper(payload, bot):
    channel = bot.get_channel(payload.channel_id)
    await cogs.sqvrofl.sqvrofl.gg(channel)
