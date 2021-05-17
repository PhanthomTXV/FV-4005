import discord
from discord import Intents
from discord.ext import commands
import os

token = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
bot = commands.Bot(command_prefix='*', intents=intents)


@bot.command(name='ping', help='The bot responds with pong.')
async def ping_(ctx):
    await ctx.send("pong!!")


@bot.command(name='kick', help='Usage *kick @user reason')
@commands.has_permissions(kick_members=True)
async def kick_(ctx, user: discord.Member, reason= None):
    channel = bot.get_channel(843356905337651230)
    if not reason:
        await user.kick()
        await channel.send(f"**{user}** has been kicked for **{reason}**.")
    else:
        await user.kick(reason=reason)
        await channel.send(f"**{user}** has been kicked for **{reason}**.")


@bot.command(name='ban', help='Usage *ban @user reason')
@commands.has_permissions(ban_members=True)
async def ban_(ctx, user: discord.Member, reason= None):
    channel = bot.get_channel(843356905337651230)
    if not reason:
        await user.create_dm()
        await user.dm_channel.send(f"You have been banned for **{reason}**. You are now Banned from PhantomTXV's Streaming Community")
        await user.ban()
        await channel.send(f"**{user}** has been banned for **{reason}**.")
    else:
        await user.create_dm()
        await user.dm_channel.send(f"You have been banned for **{reason}**. You are now Banned from PhantomTXV's Streaming Community")
        await user.ban()
        await channel.send(f"**{user}** has been banned for **{reason}**.")


@bot.command(name='warn', help='Usage *warn @user reason', pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn_(ctx, user: discord.Member, reason=None):
    if not reason:
        await ctx.send(f"**{user}** has been warned for **{reason}**.")
        msg = ctx.message
    else:
        await ctx.send(f"**{user}** has been warned for **{reason}**.")
        msg = ctx.message


@bot.event
async def on_message(message):
    try:
        banned_words = {"shit", "bitch", "fuck", "cunt", "nigger", "niger", "pussy", "gay", "jizz", "semen", "puss",
                        "pussie", "gae", "bitches", "bitchin", "bitching", "dick", "dicks", "penis", "asshole", "ass",
                        "hoe", "fucked", "fuckd", "bitched", "bitchd"}
        for word in banned_words:
            if word in message.content.lower():
                await message.delete()
                await message.channel.send("You said a no no word!! So I deleted it... WITH MY RAYGUN")
    except Exception as e:
        print(e)

    try:
        deleted_commands = {"*kick", "*ban", "*warn"}
        for word in deleted_commands:
            if word in message.content.lower():
                await message.delete()
    except Exception as e:
        print(e)

    await bot.process_commands(message)

print("Server Running.")
bot.run(token)
