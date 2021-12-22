#importing libraries (the keep_alive will be explained later)
from keep_alive import keep_alive
import discord
import random
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    #this will report in the console when your bot is ready
    print('We have logged in as {0.user}'.format(client))
    #this will change your bot's status
    await client.change_presence(activity=discord.Game(name="$commands"))
   

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #basic command line 
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
     
keep_alive()
client.run('your token here')
