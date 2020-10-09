import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from expense import ExpenseTracker
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?>')
tracker = ExpenseTracker()
tracker.connect("Tracking")
@bot.event
async def on_ready() :
    print("Bot Started!")

@bot.event
async def on_message(message) :
    if message.content.startswith('?>ping') :
      await message.channel.send('Pong ~ Meow ><')

    if message.content.startswith('?>expense') :
      result_message = tracker.add("EXPENSE", message.content)
      await message.channel.send(result_message)
    
    if message.content.startswith('?>income') :
      result_message = tracker.add("INCOME", message.content)
      await message.channel.send(result_message)

bot.run(DISCORD_TOKEN)