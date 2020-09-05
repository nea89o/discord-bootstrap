from discord.ext import commands

from bot.config import Config

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

name = "Bot Name"
description = "Bot Description"


@bot.command()
async def hello(ctx: commands.Context):
    await ctx.send('Hello, World')


def main():
    bot.run(Config.token)
