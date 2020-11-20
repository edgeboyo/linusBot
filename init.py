from bot import DiscordClient

from ast import literal_eval

import discord
from discord.ext import commands

def sanitize(s):
	while s[-1] == '\n':
		s = s[:-1]
	return literal_eval("'%s'" % s)

def init():
    with open("discord.token", "r") as f:
        dtoken = f.readline()

    dtoken = sanitize(dtoken)
    print(dtoken)


    client = DiscordClient()
    client.run(dtoken)



if __name__ == "__main__":
    init()

