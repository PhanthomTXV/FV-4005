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



print("Server Running.")
bot.run(token)
