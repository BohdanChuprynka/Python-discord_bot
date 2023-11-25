import discord
import os

from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

#intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is now running')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    #only for debugging
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message} ({channel})"')
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel("put the id of your channel, where you want your bot to send the message")
    if channel is not None:
        await channel.send(f'Hello {member.mention}. Welcome to the Ukraine server!')

@bot.event
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    print("Token not found")
else:
    bot.run(TOKEN)
