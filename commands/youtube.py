import discord
from discord.ext import commands
import asyncio

class Notifications(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    

def setup(bot):
    bot.add_cog(Giveaway(bot))