import os
from datetime import timezone, timedelta

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD_ID = os.getenv('GUILD_ID')
TIME_ZONE = timezone(timedelta(hours=5))  # Russia, Ekaterinburg
BOT_CHAT_ID = 749662464538443948
MAIN_CHAT_ID = 670981415306788870
