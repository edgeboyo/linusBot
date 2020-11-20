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
