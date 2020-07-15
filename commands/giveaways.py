import discord
from discord.ext.commands import commands


class Giveaway(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    def start(ctx, days=days title=title)
        embed = discord.Embed(
            title= f"{title}"
        )


def setup(bot):
    bot.add_cog(Giveaway(bot))