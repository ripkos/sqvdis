async def pepper(payload, bot):
    channel=bot.get_channel(payload.channel_id)
    await channel.send('gg')