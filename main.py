#
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
  def check(msg):
    return msg.author == message.author
  if message.author != intents.user:

    if message.content.startswith('/mess'):
        await message.channel.send(message.author)
        
        wait_message = await intents.wait_for("message",check=check)
        await message.channel.send(wait_message.content)
        
intents.run('token',log_handler=handler)
