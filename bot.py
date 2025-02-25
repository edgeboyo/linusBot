import discord
import requests
import time

from datetime import datetime

from getQuotes import getRandom

class DiscordClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.tlimit = time.time()

    async def on_message(self, message):
        text = message.content
        if text[0] == '$':
            text = text[1:]
        else:
            return
        if text == "RANT":
            await message.channel.send(getRandom(False))
        if text == "LONGRANT":
            await message.channel.send(getRandom(True))

    async def on_reaction_add(self, reaction, user):
        if user.id == 257130372213506048:
            return
        emoji = reaction.emoji
        print(reaction.message.channel.name)
        if reaction.message.channel.name == "general" and time.time() - self.tlimit > 20 and reaction.custom_emoji and (emoji.id == 779415235735322656 or emoji.id == 779415413280473108):
            await reaction.message.channel.send(getRandom(False))
            self.tlimit = time.time()
        # if emoji.is_custom_emoji() and emoji.id == 779413738054352946:
