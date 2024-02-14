import discord
from discord import app_commands
from discord.ext import tasks
from discord.ext.commands import Bot

from config import BOT_CHAT_ID
from src.cogs.base import BaseCog
from src.utils.emoji_utils import get_random_formatted_emoji


class Help(BaseCog):
    def __init__(self, bot: Bot):
        super().__init__(bot)
        self.spam.start()

    @app_commands.command(description='Обычное приветствие')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Привет, {interaction.user.display_name}!')

    @tasks.loop(hours=1)
    async def spam(self):
        channel = self.bot.get_channel(BOT_CHAT_ID)  # main channel
        formatted_emoji = get_random_formatted_emoji(channel.guild)
        await channel.send(formatted_emoji)

