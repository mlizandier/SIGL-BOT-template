import os
from discord.ext import commands
import discord

DISCORD_TOKEN = os.getenv('DISCORD_KEY')

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 238762143485394944  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def mute (ctx, member : discord.User=None, reason = None): # When !mute xxx is called / disabling all textual channels permissions
    perms = discord.Permissions(send_messages=False, read_messages=True)
    role = ctx.get(ctx.guild.roles, name="Ghost")
    print("test 0")
    if role : 
        print("test 1")
        if Ghost in member.roles: 
            await member.delete_roles(member, get(member.guild.roles, name="Ghost"))
        else:
            await member.add_roles(member, get(member.guild.roles, name="Ghost"))
    else :
        print("test 2")
        await ctx.create_role(ctx.guild, name='Ghost', permissions=perms)
        await member.add_roles(member, get(member.guild.roles, name="Ghost"))

@bot.command()
async def ban (ctx, member : discord.User=None, reason = None):
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")

@bot.command()
async def name (ctx):  # When !name is called
    response = ctx.message.author
    await ctx.message.channel.send(response)

token = DISCORD_TOKEN
bot.run(token)  # Starts the bot