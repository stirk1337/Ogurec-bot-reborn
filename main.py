import discord
from discord.ext.commands import Bot

from config import TOKEN
from src.cogs.help_cog import Help
from src.cogs.uno_cog import Uno

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    await bot.add_cog(Uno(bot))
    await bot.add_cog(Help(bot))
    print(f'We have logged in as {bot.user}')


@bot.command(name="sync")
async def sync(ctx):
    synced = await bot.tree.sync()
    await ctx.send(f"Синхронизировано {len(synced)} команд.")


bot.run(TOKEN)
