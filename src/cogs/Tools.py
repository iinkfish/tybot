import random
import string
import os  # default module
import discord
import requests
from discord.ext import commands


class Tools(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="Convert any length",
                           guild_ids=["1044668454646587453", "941802797702209546"])
    async def convertunits(self, ctx, value: discord.Option(float), unit: discord.Option(str)):
        unit_conversions = {
            'ft': {
                'm': value / 3.281,
                'km': (value / 3.281) / 1000,
                'cm': (value / 3.281) * 100,
                'inch': value * 12,
                'mm': (value / 3.281) * 1000,
                'miles': value / 5280
            },
            'm': {
                'ft': value * 3.281,
                'km': value / 1000,
                'cm': value / 100,
                'mm': value * 1000,
                'inch': value * 39.37
            },
            'f': {
                'celsius': (value - 32) * (5 / 9),
                'kelvin': (value - 32) * (5 / 9) + 273.15
            },
            'celsius': {
                'f': (value * (9 / 5)) + 32,
                'kelvin': value + 273.15
            }
        }
        await ctx.respond(
            unit_conversions.get(unit, "No conversion available. Available for m, ft, f (for fahrenheit) and celsius"))


print(os.getenv('OPENAI_API_KEY'))


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(Tools(bot))  # add the cog to the bot
