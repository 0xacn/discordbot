import discord
from discord.ext import commands 
from discord import errors

class Errors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Mod command Errors
    @clear.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingPermissions)
            await ctx.send("You must have administrator permmisions to  use this command")
        
    @kick.error()


