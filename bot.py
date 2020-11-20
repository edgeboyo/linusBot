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
    async def on_raw_reaction_add(self, payload):
        print("I saw react XD")

    async def on_reaction_add(self, reaction, user):
        reactList = reaction.message.reactions
        print(reactList)
        for i in reactList:
            if i.count > 1:
                await reaction.message.channel.send("Whoa there!")
                await reaction.message.delete()
