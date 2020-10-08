import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='?>')

@bot.event
async def on_ready() :
    print("Bot Started!")

@bot.event
async def on_message(message) :
    if message.content.startswith('?>ping') :
       await message.channel.send('Pong ~ Meow ><')

bot.run(TOKEN)