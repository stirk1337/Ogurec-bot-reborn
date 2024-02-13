import datetime
from random import shuffle

import discord
from discord import app_commands

from src.cogs.base import BaseCog
from src.google_docs.google_docs import get_table
from src.utils.role_utils import get_all_users_with_role

UNO_LOGO_URL = ('https://media.discordapp.net/attachments/1043248714652860477/1206889284242772019'
                '/1740671508_preview_1280px-UNO_Logo_svg.png?ex=65dda63c&is=65cb313c&hm'
                '=63bf1c5c79afd8c3a14f9b9c528a23cd0a50d308cfc1a6df69725ba7c6ef6be7&=&format=webp&quality=lossless'
                '&width=833&height=585')

GOOGLE_SPREADSHEETS_LOGO_URL = ('https://media.discordapp.net/attachments/1043248714652860477/1206901181079748618'
                                '/be52957fc0b0ec8.webp?ex=65ddb150&is=65cb3c50&hm'
                                '=81f134804f73570f2409022106c6b367ca4045418234c625003ef16f0399dc44&=&format=webp'
                                '&width=585&height=585')


class Uno(BaseCog):
    @app_commands.command(description='Отобразить таблицу UNO из Google Таблицы')
    async def uno(self, interaction: discord.Interaction):
        values = get_table()['values']
        embed = discord.Embed(title='Результаты UNO',
                              color=discord.Color.random(),
                              timestamp=datetime.datetime.now())
        embed.set_author(name=interaction.user.display_name,
                         icon_url=interaction.user.avatar)
        embed.set_thumbnail(url=UNO_LOGO_URL)
        embed.set_footer(text="Google Таблицы",
                         icon_url=GOOGLE_SPREADSHEETS_LOGO_URL)
        for score in values[1:7]:
            embed.add_field(name=f'**{score[0]}**',
                            value=f'> Шансㅤ \t{score[1]}\n> Победы {score[2]}\n> Лузы ㅤ\t{score[3]}',
                            )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description='Случайный порядок игроков с ролью UNO')
    async def uno_shuffle(self, interaction: discord.Interaction):
        uno_players = get_all_users_with_role(interaction, 'Uno')
        shuffle(uno_players)
        embed = discord.Embed(title='UNO Шаффл!',
                              color=discord.Color.random())
        embed.set_thumbnail(url=UNO_LOGO_URL)
        for player in uno_players:
            embed.add_field(name='', value=player, inline=False)
        await interaction.response.send_message(embed=embed)
