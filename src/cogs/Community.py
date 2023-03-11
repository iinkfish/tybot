import random

import discord
from discord.ext import commands


class Community(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(guild_ids=["1044668454646587453", "941802797702209546"])  # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond(f"Goodbye {ctx.author.mention} !")

    @discord.slash_command(description="give another member a hug <3", guild_ids=["1044668454646587453", "941802797702209546"])
    async def hug(self, ctx, member: discord.Member):
        await ctx.respond(f" {ctx.author} gives {member.mention} a fat hug <3.")

    @discord.slash_command(aliases=['8ball', '8bal'])
    async def eightball(self, ctx, *, question):
        responses = ["All signs point to yes...", "Yes!", "My sources say nope.", "You may rely on it.", "Concentrate and ask again...", "Outlook not so good...", "It is decidedly so!", "Better not tell you.", "Very doubtful.", "Yes - Definitely!", "It is certain!", "Most likely.", "Ask again later.", "No!", "Outlook good.", "Don\"t count on it."]
        await ctx.respond(f"**Question: ** {question} \n**Answer: ** {random.choice(responses)}")

    @discord.slash_command(description="Call another member cute :)", guild_ids=["1044668454646587453", "941802797702209546"])
    async def cute(self, ctx, member: discord.Member):
        await ctx.respond(
            f"Can we please talk about what a cutiepie {member.mention} is? Can yall believe how cute they are?")

    @discord.slash_command(description="Get the chance of love between you and someone else",
                           guild_ids=["1044668454646587453", "941802797702209546"])
    async def love(self, ctx, member: discord.Member):
        # sneaky way to always get 100 % love with someone you want :)
        isUser1 = (member.id == 714055601340284969) or (member.id == 679022772336328754)
        isUser2 = (ctx.author.id == 714055601340284969) or (ctx.author.id == 679022772336328754)
        print(isUser2, isUser1)
        if isUser1 and isUser2:
            await ctx.respond(
                f"There is a 100 % chance of love between {ctx.author.mention} and {member.mention} <3")
        else:
            await ctx.respond(
                f"There is a {random.randint(1, 100)} % chance of love between {ctx.author.mention} and {member.mention} <3")

    @discord.slash_command(description="Send hate to a random member")
    async def hate(self, ctx):
        member = random.choice(ctx.guild.members)
        await ctx.respond(f"Oh wow {member.mention} kinda sucks huh?")

    @discord.user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')

    @commands.Cog.listener()  # we can add event listeners to our cog
    async def on_member_join(self, member):  # this is called when a member joins the server
        # you must enable the proper intents
        # to access this event.
        # See the Popular-Topics/Intents page for more info
        await member.send('Welcome to the server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        await channel.send(f"Goodbye  {member.mention} ({member.name})")


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(Community(bot))  # add the cog to the bot
