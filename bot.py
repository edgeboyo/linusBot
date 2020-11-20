import discord
import requests

from getQuotes import getRandom

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

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
        if reaction.custom_emoji and (emoji.id == 779415235735322656 or emoji.id == 779415413280473108):
            await reaction.message.channel.send(getRandom(False))
        # if emoji.is_custom_emoji() and emoji.id == 779413738054352946:
