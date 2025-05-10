
import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # ใช้ Token จาก Zeabur environment variable

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้วในชื่อ {bot.user}")

bot.run(TOKEN)
