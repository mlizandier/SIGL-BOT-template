import os
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 0000000  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token = "ODkyODIxNzY0OTE5Mzk4NDYw.YVSfEA.FhP8k4QEeDlOuOXNcNM_hZ50d9c"
bot.run(token)  # Starts the bot