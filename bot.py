import discord
from discord.ext import commands
from decouple import config

# from apikeys import *
from dotenv import load_dotenv
from utils import *

def bot_functionality():

    load_dotenv()
    discord_api_key = config('DISCORD_BOT_TOKEN')

    # initialize bot
    client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    # here, on_ready() tells that bot is ready to receive command
    # This is for testing
    @client.event
    async def on_ready():
        print("The bot is now ready for use")
        print("-----------------------------")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        message_str = str(message.content).split("\n")
        print(message_str)
        response = await fomatting_check(message_str)
        await message.channel.send(response)

    @client.event
    async def on_message_edit(before, after):
        if after.author == client.user:
            return
        message_str = str(after.content).split("\n")
        response = await fomatting_check(message_str)
        await after.channel.send (response)

    # it tells the bot to run
    client.run(discord_api_key)


