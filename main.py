import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Discord token from the environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Set up logging to a file
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.getLogger().addHandler(handler)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Define a custom bot class to handle setup
class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.vsGradeCalc")


bot = MyBot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(DISCORD_TOKEN)
