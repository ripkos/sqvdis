import discord
import os
from cogs.util.util import *
from cogs.util.reactions_moder import *
from discord.ext import commands
from cogs.util.reactions_switcher import switch

bot = commands.Bot(command_prefix='sqv ')
debug_mode = False


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def echo(ctx, response):
    await ctx.send("💮")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def debug(ctx):
    global debug_mode
    debug_mode = not debug_mode


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# events
@bot.event
async def on_member_update(before, after):
    channel = bot.get_channel(756870330609303654)
    if isinstance(after.activity, discord.BaseActivity):
        if after.activity.name == 'Dota 2':
            if after.id == 245957141083455489 or after.id == 270229741942997003:
                msg = ('<@' + str(after.id) + '> ВЫЙДИ ИЗ ДОТЫ')
                await channel.send(msg)
    if isinstance(before.activity, discord.BaseActivity):
        if before.activity.name == 'Dota 2':
            if before.id == 245957141083455489 or before.id == 270229741942997003:
                msg = ('<@' + str(after.id) + '> УДАЛИ ЭТУ ПОМОЙКУ И БОЛЬШЕ В НЕЁ НЕ ЗАХОДИ')
                await channel.send(msg)


@bot.event
async def on_message(message):
    if message.channel.name == 'bot':
        await bot.process_commands(message)


@bot.event
async def on_raw_reaction_add(payload):
    if debug_mode:
        print(payload.emoji.name)
    if payload.member.bot:
        return
    else:
        await switch(payload, bot)




# run bot
bot.run(os.environ['TOKEN'])
