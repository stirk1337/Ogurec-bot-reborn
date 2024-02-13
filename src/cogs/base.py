from discord import Client
from discord.ext import commands


class BaseCog(commands.Cog):
    def __init__(self, bot: Client):
        self.bot = bot
    