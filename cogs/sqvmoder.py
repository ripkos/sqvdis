import random

import discord
from discord.ext import commands

from cogs.util.sqlight import SQLite

from cogs.util.forumutil import *
import cogs.util.on_reactions as afaf


class sqvmoder(commands.Cog):
    # init
    def __init__(self, bot):
        self.bot = bot
        self.db = SQLite('./res/forum.db')

    # Commands

    @commands.command(brief='название сервера (sqv servers)')
    async def frog(self, ctx, sname, arg1=''):
        sname = sname.lower()
        if len(self.db.check_server(sname)) > 0:
            await ctx.send(
                '**===============================================\nПоиск открытых тем в разделе ' + self.db.get_server_name(sname) + ' :**'
            )
            response = parse_forum_short((self.db.get_server_link(sname)))
            if response != False:
                topics = len(response)
                for topic in response:
                    msg = await ctx.send(construct_short(topic))
                    if arg1 == 'open':
                        await afaf.reaction_downarrow_force(msg)
                    else:
                        await msg.add_reaction('⏬')
                await ctx.send('**Найдено ' + str(topics) + ' открытых тем\n===============================================**')
            else:
                await ctx.send('**БОТА ЗАБАНИЛИ СЕРЕГА ИЗВИНЯЙСЯ**')
        else:
            await ctx.send('Нет такого сервера! Пиши sqv servers')

    @commands.command(brief='название сервера (sqv servers)')
    async def f(self, ctx, snames, arg1=''):
        if len(self.db.check_all_servers(snames + '%')) > 0:
            ffs = self.db.get_all_servers(snames + '%')
            for asd in ffs:
                await self.frog(ctx, asd[0], arg1)
        else:
            await ctx.send('Нет таких серверов! Пиши sqv servers')

    @commands.command(brief='тоже самое что жб + обж')
    async def ff(self, ctx, arg1=''):
        await self.frog(ctx, 'жб', arg1)
        await self.frog(ctx, 'обж', arg1)

    @commands.command(brief='список всех категорий доступных для парсинга')
    async def servers(self, ctx):
        text = '```\n'
        response = self.db.get_server_list()
        for d in response:
            text = text + d[0] + ' - ' + d[1] + '\n'
        text = text + '```'
        await ctx.send(text)

    # end


def setup(client):
    client.add_cog(sqvmoder(client))
