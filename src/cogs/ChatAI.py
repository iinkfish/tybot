import discord
import openai
import os
from discord.ext import commands


class ChatAI(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="Ask tyBot anything you wish")
    async def answer(self, ctx, prompt: discord.Option(str)):
        await ctx.defer()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0.7,
          max_tokens=1000,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0,
        )

        await ctx.followup.send(response.choices[0].text.replace('![alt text]', '[How about this?]'))

    @discord.slash_command(description="Write a description of the image you want to create", guild_ids=["1044668454646587453"])
    async def create(self, ctx, prompt: discord.Option(str)):
        await ctx.defer()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        await ctx.followup.send(response['data'][0]['url'])

def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(ChatAI(bot))  # add the cog to the bot
