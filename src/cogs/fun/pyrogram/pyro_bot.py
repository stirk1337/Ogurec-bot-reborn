import random
from typing import List

import discord
from pyrogram import Client
from pyrogram.types import Message

from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, GPT_TELEGRAM_NAME_STR

app = Client("my_account", api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH)

BOT_MOODS = [
                'Пиши как футболист',
                'Пиши как программист',
                'Пиши как гопник',
                'Пиши с жестким негативом',
                'Пиши как гопник с жестким негативом',
                'Пиши положительно',
                'Пиши как политик',
                'Пиши как ведьмак',
                'Пиши как геймер',
                'Пиши как анимешник',
                'Пиши как военный',
                'Пиши как полицейский',
                'Пиши с негативом',
                'Пиши с жестким негативом',
                'Пиши как певица',
                'Пиши с негативом',
                'Пиши как агресивный гопник'
            ] + [''] * 20

gpt_stack: List[Message] = []


class GptBot:
    def __init__(self, fun_cog):
        self.fun_cog = fun_cog


async def send_gpt_message(message: str, use_moods: bool = False):
    await app.send_message(GPT_TELEGRAM_NAME_STR,
                           f'{message} {random.choice(BOT_MOODS) if use_moods else ""}')


async def gpt_answer_receive(answer: str):
    try:
        message = gpt_stack[-1]
        await message.channel.send(answer, reference=message)
        gpt_stack.pop()
    except:  # reklama or empty lst
        pass


@app.on_message()
async def listen_for_gpt_answers(client, message: Message):
    if message.from_user.username == GPT_TELEGRAM_NAME_STR:
        await gpt_answer_receive(message.text)
