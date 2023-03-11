import discord
from discord.ext import commands
import os  # default module
from dotenv import load_dotenv

load_dotenv()  # load all the variables from the env file
bot = discord.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


@bot.slash_command(description="Sends the bot's latency.")  # this decorator makes a slash command
async def ping(ctx):  # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")


@bot.message_command(name="Get Message ID")
# creates a global message command. use guild_ids=[] to create guild-specific commands.
async def get_message_id(ctx, message: discord.Message):  # message commands return the message
    await ctx.respond(f"Message ID: `{message.id}`")


@bot.command(description="adds two numbers")
# pycord will figure out the types for you
async def add(ctx, first: discord.Option(int), second: discord.Option(int)):
    # you can use them as they were actual integers
    sum = first + second
    await ctx.respond(f"The sum of {first} and {second} is {sum}.")


@bot.slash_command(description="multiplies two numbers", guild_ids=["1044668454646587453"])
# pycord will figure out the types for you
async def multiply(ctx, first: discord.Option(int), second: discord.Option(int)):
    # you can use them as they were actual integers
    sum = first * second
    await ctx.respond(f"The sum of {first} and {second} is {sum}.")


@bot.slash_command(guild_ids=["1044668454646587453", "941802797702209546"])
async def getid(ctx, member: discord.Member):
    await ctx.respond(f"Author ID: {ctx.author.id}\n MemberID: {member.id}")


cogs_list = [
    'Community',
    'GameAPI',
    'Tools',
    'ChatAI'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(os.getenv('TOKEN'))  # run the bot with the token
