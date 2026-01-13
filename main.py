import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # ⭐ مهم بزاف

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

bot.run(os.getenv("TOKEN"))
