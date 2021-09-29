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
    if member == None:
        await ctx.channel.send(f'Usage should be `!admin <member tagged>`')
        return
    admin_role = None
    for role in ctx.guild.roles:
        if role.name == "Admin":
            admin_role = role
    if admin_role == None :
        admin_perm = discord.Permissions(administrator=True)
        admin_role = await ctx.guild.create_role(name='Admin', permissions=admin_perm)
    await member.add_roles(admin_role)
    await ctx.channel.send(f'{member} is now an admin')

@bot.command(name="mute")
async def mute (ctx, member : discord.User=None): # When !mute xxx is called / disabling all textual channels permissions
    ghost_role = discord.utils.get(ctx.guild.roles, name="GHOST")
    if not ghost_role :
        mute_perm = discord.Permissions(send_messages=False)
        ghost_role = await ctx.guild.create_role(name="GHOST", permissions=mute_perm)
        for channel in ctx.guild.channels:
            await channel.set_permissions(ghost_role, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    r = False
    for role in member.roles : 
        if role.name == "GHOST" :
            r = True
    if r :
        await member.remove_roles(ghost_role)
        await ctx.channel.send(f'{member} is now a human again')
    else :
        await ctx.channel.send(f'{member} is now a ghost')
        await member.add_roles(ghost_role)


@bot.command(name="ban")
async def ban (ctx, member : discord.User=None, reason = None):
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")

token = DISCORD_TOKEN
bot.run(token)  # Starts the bot