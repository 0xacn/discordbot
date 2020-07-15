import discord
from discord.ext import commands
import asyncio

class Giveaway(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    def start(self, ctx, days=None, title=None):
       pass

def setup(bot):
    bot.add_cog(Giveaway(bot))