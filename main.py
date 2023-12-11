#a
import discord
from discord.ext import commands
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents = discord.Client(intents=intents)

@intents.event
async def on_ready():
    print(f'We have logged in as {intents.user}')
    
@intents.event
async def on_message(message):
    if message.author != intents.user:
        await message.channel.send(message.author)
        
intents.run('token',log_handler=handler)
