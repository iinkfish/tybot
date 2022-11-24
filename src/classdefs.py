import discord
from discord import app_commands
from discord.ext import commands

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.sync = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1044668454646587453))
        self.sync = True
        print("Bot is Online")

botSlash = abot()
tree = app_commands.CommandTree(botSlash)