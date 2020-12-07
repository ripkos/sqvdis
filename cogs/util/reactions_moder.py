import discord
from discord.abc import Messageable
from cogs.util.util import *
from cogs.util.forumutil import *
from cogs.sqvmoder import *

disc_cache = []


async def reaction_downarrow(payload, bot):
    msg = await Messageable.fetch_message(bot.get_channel(payload.channel_id), id=payload.message_id)
    await reaction_downarrow_force(msg)


async def reaction_downarrow_force(msg):
    if msg.author.bot:
        url = get_url_from_msg(msg.content)
        api = url_to_api(url)
        rawdisc = parse_disc(api)
        if rawdisc not in disc_cache:
            disc_cache.append(rawdisc)
        newmsg = construct_message(rawdisc)
        await msg.edit(content=str(newmsg))
        await clear_and_add(msg, len(rawdisc) - 1)


async def reaction_number(payload, bot, number):
    msg = await Messageable.fetch_message(bot.get_channel(payload.channel_id), id=payload.message_id)
    if msg.author.bot:
        raw = None
        url = get_url_from_msg(msg.content)
        for disc in disc_cache:
            if disc[0]['link'] == url:
                raw = disc
        if raw is None:
            api = url_to_api(url)
            raw = parse_disc(api)
        newmsg = construct_message(raw, number)
        await msg.edit(content=str(newmsg))


async def clear_and_add(msg, postCount):
    await msg.clear_reactions()
    if postCount > 1:
        await msg.add_reaction('0️⃣')
        await msg.add_reaction('1️⃣')
    if postCount > 2:
        await msg.add_reaction('2️⃣')
    if postCount > 3:
        await msg.add_reaction('3️⃣')
    if postCount > 4:
        await msg.add_reaction('4️⃣')
    if postCount > 5:
        await msg.add_reaction('5️⃣')
    if postCount > 6:
        await msg.add_reaction('6️⃣')
    if postCount > 7:
        await msg.add_reaction('7️⃣')
    if postCount > 8:
        await msg.add_reaction('8️⃣')
    if postCount > 9:
        await msg.add_reaction('9️⃣')
    await msg.add_reaction('⏬')
