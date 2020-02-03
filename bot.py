import sys
from typing import Dict

import os
import random
import discord
from discord.errors import Forbidden
from discord.guild import Guild
from discord.message import Message
from discord.reaction import Reaction
from discord.user import User
from discord.ext import commands
from discord.colour import Colour

from warning import get_warning
from warning import WARNINGS

from dotenv import load_dotenv

bot = discord.Client()

load_dotenv()
botToken = os.getenv('TOKEN')
print(botToken)

@bot.event
async def on_message(message):
    #if message.author == bot.user:
    #    await message.add_reaction("❎")
    #    return

    # Bad word check
    data = get_warning(message.content)
    if data is not None:
        await message.add_reaction("🙊")

    # Bot Test
    if message.content == "!!!languagebot":
        await message.channel.send(message.content)

@bot.event
async def on_reaction_add(reaction, user):
        reactionCount = reaction.count
        if reaction.me:
            reactionCount = reactionCount - 1
        #if reaction.message.author == bot.user:
        #    if reactionCount > 0 and reaction.emoji == "❎":
        #        await reaction.message.delete()
        if reactionCount > 0 and reaction.emoji == "🙊":
            #await reaction.message.remove_reaction("🙊", bot.user)
            #await reaction.message.remove_reaction("🙊", user)
            embed = get_embed_message(get_warning(reaction.message.content))
            await user.send(embed=embed)
            #await reaction.message.channel.send(embed=embed)

def get_embed_message(warning):
    colour = discord.Colour(random.randint(0, 0xFFFFFF))
    new_colour = discord.Colour.from_rgb(*(round(c * 0.7) for c in colour.to_rgb()))
    embed = discord.Embed(title="Language Suggester", description=warning + "\n\nThis bot exists simply to ask you to reflect on your word choices, and will never moderate or punish people for activating it" + "\n\nIf you have an issue with the bot, a change for a words description or additional words for the bot please message @Nyght#4732", color=new_colour)
    return embed

bot.run(botToken)
