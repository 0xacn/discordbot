import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount=15):
      await ctx.channel.purge(limit=amount)
    
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked by {message.author}")

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned by {message.author}")

    @commands.has_permissions(mute_members=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        await member.mute(reason=reason)
        await ctx.send(f"{member.mention} has been muted by {message.author}")

    @commands.has_permissions(mute_members=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        await member.unmute(reason=reason)
        await ctx.send(f"{member.mention} has been unmuted by {message.author}")


def setup(bot):
    bot.add_cog(Mod(bot))