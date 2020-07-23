import discord
from discord.ext import commands 

class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        "This event is triggered when an error is raised"
    
        ignored = (commands.CommandNotFound, commands.UserInputError)

        if isinstance(error, ignored):
            return
    
        elif isinstance(error, commands.MissingPermissions):
            ctx.send(f"You are missing Permissions to use {ctx.command}")

        elif isinstance(error, commands.MissingRequiredArgument):
            ctx.send(f"Pass through all the arguements for {ctx.command}")
        
        elif isinstance(error, commands.NotOwner):
            ctx.send(f"You must be the owner of this discord to use {ctx.command}")

        elif isinstance(error, commands.)
def setup(bot):
    bot.add_cog(ErrorHandler(bot))