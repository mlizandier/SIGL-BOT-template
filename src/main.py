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
async def name (ctx):  # When !name is called
    response = ctx.message.author
    await ctx.message.channel.send(response)

@bot.command(name="admin")
@commands.has_permissions(manage_roles=True)
async def admin (ctx, member : discord.User=None):
    admin_role = None
    for role in ctx.guild.roles:
        if role.name == "ADMIN":
            admin_role = role
    await member.add_roles(admin_role)
    await ctx.channel.send(f'{member} is now an admin')

@bot.command(name="mute")
async def mute (ctx, member : discord.User=None): # When !mute xxx is called / disabling all textual channels permissions
    ghost_role = None
    for role in ctx.guild.roles:
        if role.name == "GHOST":
            ghost_role = role
        else : 
            perms = 
            ctx.guild.create_role(name="GHOST", permissions=perms)
    await member.add_roles(ghost_role)
    await ctx.channel.send(f'{member} is now a ghost')
    # print("test 0")
    # if role : 
    #     print("test 1")
    #     if Ghost in member.roles: 
    #         await member.delete_roles(member, get(member.guild.roles, name="Ghost"))
    #     else:
    #         await member.add_roles(member, get(member.guild.roles, name="Ghost"))
    # else :
    #     print("test 2")
    #     await ctx.create_role(ctx.guild, name='Ghost', permissions=perms)
    #     await member.add_roles(member, get(member.guild.roles, name="Ghost"))

@bot.command(name="ban")
async def ban (ctx, member : discord.User=None, reason = None):
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")

token = DISCORD_TOKEN
bot.run(token)  # Starts the bot