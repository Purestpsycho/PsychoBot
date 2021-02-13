#Importing Libraries
import discord
import os
import io
import aiohttp

from discord.ext import commands

#Set the URL for the think image
think = 'https://cdn.shopify.com/s/files/1/2136/9235/products/8584_8ba8501b-ed11-4bee-91eb-1b629076ca08_1024x1024.jpg?v=1609922305'
yeehaw = 'https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Ffacebook%2F000%2F028%2F682%2FDt2WrakU0AA1ScI.jpg'
hawyee = 'https://i.imgur.com/3ZN9pGW.jpg'

#Confirm login in the Console
client = discord.Client()
print('Logged in as Psycho Bot')

#Doesn't send a message if from itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return

#Howdy Pardners
    elif message.content.startswith('Hey'):
        await message.channel.send('Howdy Pardner :cowboy:')

#Attempt to download an send an image
    elif message.content.startswith('Think'):
        async with aiohttp.ClientSession() as session:
          async with session.get(think) as resp:
            if resp.status != 200:
              return await message.channel.send('Try again later')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'think.png'))

#Same as above, but for a different Image
    elif message.content.startswith('Yeehaw'):
        async with aiohttp.ClientSession() as session:
          async with session.get(yeehaw) as resp:
            if resp.status != 200:
              return await message.channel.send('Try again later')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'yeehaw.png'))

#Second verse, same as the first
    elif message.content.startswith('Hawyee'):
        async with aiohttp.ClientSession() as session:
          async with session.get(hawyee) as resp:
            if resp.status != 200:
              return await message.channel.send('Try again later')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'hawyee.png'))

#List of commands            
    if message.content.startswith('!commands'):
        await message.channel.send('Find a list of my commands here: https://pastebin.com/YktDLjBn')

#Set Discord Status
        

#Start the bot and attempt to keep it alive
client.run ('TOKEN')
