# import discord
from discord.ext import commands
import os
import random
# import asyncio

token = os.getenv("DISCORD_BOT_TOKEN")
client = commands.Bot(command_prefix=".")
# client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user.name} is ready!")

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("pong!")
    elif message.content == 'raise-exception':
        raise discord.DiscordException
'''

@client.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    if number_of_dice <= 0:
        await ctx.channel.send("I need at least one dice, man.")
    elif number_of_sides <= 0:
        await ctx.channel.send("Such dice does not exist.")

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.channel.send(', '.join(dice))

@client.command(name='ping', help='Display your ping.')
async def ping(ctx):
    await ctx.channel.send(f"{str(round(client.latency, 2))}s")

@client.command(name='clear', help='Clear texts in a channel with a given amount.')
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

client.run(token)
