import discord
import os
from discord.ext import commands

# Define the intents
intents = discord.Intents.all()
# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Simple command example
@bot.command(name='hello', help='Print a greeting message')
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot with your token
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
my_secret = os.environ['Token']
bot.run(my_secret)
