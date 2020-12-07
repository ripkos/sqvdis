import discord
from discord.ext import *
from discord.ext import commands

from cogs.util.reactions_moder import *
from cogs.util.reactions_rofl import *


async def switch(payload, bot):
    await moder(payload, bot)
    await rofl(payload, bot)


async def moder(payload, bot):
    if payload.emoji.name == '⏬':
        await reaction_downarrow(payload, bot)
        return
    if payload.emoji.name == '0️⃣':
        await reaction_number(payload, bot, 0)
        return
    if payload.emoji.name == '1️⃣':
        await reaction_number(payload, bot, 1)
        return
    if payload.emoji.name == '2️⃣':
        await reaction_number(payload, bot, 2)
        return
    if payload.emoji.name == '3️⃣':
        await reaction_number(payload, bot, 3)
        return
    if payload.emoji.name == '4️⃣':
        await reaction_number(payload, bot, 4)
        return
    if payload.emoji.name == '5️⃣':
        await reaction_number(payload, bot, 5)
        return
    if payload.emoji.name == '6️⃣':
        await reaction_number(payload, bot, 6)
        return
    if payload.emoji.name == '7️⃣':
        await reaction_number(payload, bot, 7)
        return
    if payload.emoji.name == '8️⃣':
        await reaction_number(payload, bot, 8)
        return
    if payload.emoji.name == '9️⃣':
        await reaction_number(payload, bot, 9)
        return


async def rofl(payload, bot):
    if payload.emoji.name == '🌶️':
        msg = await Messageable.fetch_message(bot.get_channel(payload.channel_id), id=payload.message_id)
        if msg.author.bot:
            await pepper(payload, bot)
