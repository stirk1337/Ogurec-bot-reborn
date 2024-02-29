import asyncio
import random

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
] + [''] * 20

gpt_answer = ''


class GptBot:
    def __init__(self, fun_cog):
        self.fun_cog = fun_cog


def gpt_answer_updated() -> bool:
    return gpt_answer != ''


async def send_gpt_message(message: str) -> str:
    global gpt_answer
    await app.send_message(GPT_TELEGRAM_NAME_STR,
                           f'{message}. Начинай текст со знака доллара. {random.choice(BOT_MOODS)}')
    await asyncio.sleep(7)
    if gpt_answer_updated():
        answer = gpt_answer[1:]
        gpt_answer = ''
        return answer


@app.on_message()
async def listen_for_gpt_answers(client, message: Message):
    global gpt_answer
    try:
        if message.from_user.username == GPT_TELEGRAM_NAME_STR and message.text[0] == '$':
            gpt_answer = message.text
    except:
        pass
