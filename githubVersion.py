#Importing Libraries
import discord
import os
import io
import aiohttp
import random
from discord.ext import commands, tasks
import webbrowser

#Set the command prefix
client = commands.Bot(command_prefix = '!')

#Bot in Ready State
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('YOUR GAME HERE'))
    print(f'Psycho Bot Online! Latency is: {round(client.latency * 1000)} ms')

#An event that triggers when a member is invited to the Discord channel
@client.event
async def on_member_join(member, ctx):
    print(f'{member} is unlucky enough to be here. F in the chat.')

#An event that triggers when a member leaves the Discord channel, kick, ban, etc.
@client.event
async def on_member_remove(member, ctx):
    print(f'{member} is gone! Feel free to spill the tea!')
#Code for pictures
Conch = 'https://steamuserimages-a.akamaihd.net/ugc/847089849187712504/97C81F4E925A8959CAC1233B406B4E9E649D5A58/'
Think = 'https://cdn.shopify.com/s/files/1/2136/9235/products/8584_8ba8501b-ed11-4bee-91eb-1b629076ca08_1024x1024.jpg?v=1609922305'
Expert = 'https://cdn.discordapp.com/attachments/799895766705504286/823751377871175680/Screenshot_20210305-160409.png'

#Expert Image
@client.command()
async def expert(ctx):
    async with aiohttp.ClientSession() as session:
         async with session.get(Expert) as resp:
             if resp.status != 200:
                 return await ctx.send('Try again later')
             data = io.BytesIO(await resp.read())
         await ctx.send(file=discord.File(data, 'expert.png'))

#The infamous THINK image
@client.command()
async def think(ctx):
    async with aiohttp.ClientSession() as session:
         async with session.get(Think) as resp:
             if resp.status != 200:
                 return await ctx.send('Try again later')
             data = io.BytesIO(await resp.read())
         await ctx.send(file=discord.File(data, 'think.png'))


#Call the class from earlier to slap someone
@client.command()
async def slap(ctx, *, reason='error: please @ someone'):
    user = ctx.author.mention
    await ctx.send(f'{user} slapped {reason}')

#Simple message to queue the playlist from Rythm Bot
@client.command()
async def music(ctx):
    await ctx.send('!play https://youtube.com/playlist?list=PL42p2170oC5J87HeEpt8tL7SWsYA1OFPR')

#Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'latency is: {round(client.latency * 1000)} ms')


#Magic Conch Command with a matching gif
@client.command(aliases=['conch'])
async def magic_conch(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrade and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    async with aiohttp.ClientSession() as session:
            async with session.get(Conch)as resp:
                if resp.status != 200:
                    return await ctx.send('Try again later')
                data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'conch.gif'))

#Coin Flip Command
@client.command()
async def flip(ctx):
#flip a coin, 0 = heads, 1 = tails
    heads = 0
    tails = 1
    flip = random.randint(0,1)
    if (flip == 0):
        await ctx.send('Heads')
    else:
        await ctx.send('Tails')


#Clear message commands
@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, amount = 0):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"cleared {amount} message(s).")
#Kick user
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been kicked. Time to spill the tea sis!')

#lists commands
@client.command()
async def commands(ctx):
    await ctx.send('```Help for the bot commands! \n!think: Displays commands. \n!expert: Sends the funny picture.' +
        '\n!slap: Slaps a user you mention, provide a reason if you want to. \n!music: Serves the command to get the poppin off playlist!' +
        '\n!ping: Displays the bot latency to the server. \n!conch: Ask the magic conch a question :o \n!flip: Flips a coin \n!nuke: Clears (x) amount of chat messages.'+
        '\n!kick: Kicks a non-mod user. You must have the correct permissions to use this.```')

#Run the bot
client.run ('YOUR BOT TOKEN HERE!')
