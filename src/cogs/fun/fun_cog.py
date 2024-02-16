import asyncio
import random

import discord
from discord import app_commands, Message
from discord.ext import commands
from discord.ext.commands import Bot

from src.cogs.base import BaseCog
from src.cogs.fun.eight_ball import EIGHT_BALL
from src.cogs.fun.game_reviews import GAME_REVIEWS
from src.utils.emoji_utils import get_random_formatted_emoji, get_random_sticker


class Fun(BaseCog):
    def __init__(self, bot: Bot):
        super().__init__(bot)
        self.on_message_counter = 0
        self.ON_MESSAGE_GUARANTEE = 750
        self.game_reviews = GAME_REVIEWS
        self.answers = EIGHT_BALL

    async def answer_question(self, message: Message) -> bool:
        if len(message.content) > 0 and self.bot.user.mentioned_in(message):
            if message.content[-1] == '?':
                async with message.channel.typing():
                    await asyncio.sleep(random.randint(2, 10))
                    await message.channel.send(random.choice(self.answers), reference=message)
                    return True
        return False

    async def answer_ping(self, message: Message):
        if self.bot.user.mentioned_in(message):
            async with message.channel.typing():
                await asyncio.sleep(random.randint(2, 6))
                random_number = random.randint(1, 4)
                if random_number == 1:  # 25%
                    await message.channel.send(stickers=[get_random_sticker(message.channel.guild)], reference=message)
                else:
                    formatted_emoji = get_random_formatted_emoji(
                        message.channel.guild)
                    await message.channel.send(formatted_emoji, reference=message)

    async def send_random_emoji(self, message: Message) -> bool:
        random_number = random.randint(1, 300)
        if random_number in [1, 2] or self.on_message_counter == self.ON_MESSAGE_GUARANTEE:
            if not self.bot.user.mentioned_in(message):
                self.on_message_counter = 0
            async with message.channel.typing():
                await asyncio.sleep(random.randint(2, 6))
                formatted_emoji = get_random_formatted_emoji(
                    message.channel.guild)
                await message.channel.send(formatted_emoji, reference=message)
            return True
        return False

    async def send_random_sticker(self, message: Message) -> bool:
        random_number = random.randint(1, 300)
        if random_number in [1, 2] or self.on_message_counter == self.ON_MESSAGE_GUARANTEE:
            if not self.bot.user.mentioned_in(message):
                self.on_message_counter = 0
            async with message.channel.typing():
                await asyncio.sleep(random.randint(2, 6))
                await message.channel.send(stickers=[get_random_sticker(message.channel.guild)], reference=message)
            return True
        return False

    async def set_random_reaction(self, message: Message):
        random_number = random.randint(1, 300)
        if 3 <= random_number <= 10:
            await asyncio.sleep(random.randint(1, 4))
            await message.add_reaction(random.choice(message.guild.emojis))

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.id in [self.bot.user.id]:
            return
        question = await self.answer_question(message)
        if question:
            return

        ping = await self.answer_ping(message)
        if ping:
            return

        sticker = await self.send_random_sticker(message)
        if sticker:
            return

        emoji = await self.send_random_emoji(message)
        if emoji:
            return

        await self.set_random_reaction(message)
        self.on_message_counter += 1

    @app_commands.command(description='Получить оценку игры. Примечание: я конченный')
    @app_commands.describe(game="Игра")
    async def rgame(self, interaction: discord.Interaction, game: str):
        await interaction.response.send_message(f'Запросили оценку {game}. Жёстко анализирую...')
        async with interaction.channel.typing():
            await asyncio.sleep(random.randint(1, 10))
            await interaction.followup.send(self.game_reviews[random.randint(0, len(self.game_reviews) - 1)])
