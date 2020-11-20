import discord
import requests

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        text = message.content
        if text[0] == '$':
            text = text[1:]
        else:
            return
        await message.channel.send("Pong!")