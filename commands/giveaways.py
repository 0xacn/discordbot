import discord
from discord.ext.commands import commands


class Giveaway(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Giveaway(bot))