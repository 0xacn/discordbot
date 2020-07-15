import discord
from discord.ext import commands
import youtube_dl
import random

class Commands(commands.Cog):
    players = {}
  
    def __init__(self, client):
        self.bot = bot

    # Music Commands
    @commands.command()
    async def play(self, ctx, url):
      guild = ctx.message.guild 
      voice_client = client.voice_client_in(guild)
      player = await voice_client.create_ytdl_player(url)
      players[guild.id] = player
      players.play()
      
  
    @commands.command()
    async def join(self, ctx):
      channel = ctx.message.author.voice.channel(channel)
      await bot.join_voice_channel(channel)

    @commands.command()
    async def leave(self, ctx):
      guild = ctx.message.guild
      voice_client = bot.voice_client_in(guild)
      await voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
      id = ctx.message.guild.id
      players[id].pause()

    @commands.command()
    async def resume(self,ctx):
      id = ctx.message.guild.id
      players[id].resume()
  
    @commands.command()
    async def stop(self, ctx):
      id = ctx.message.guild.id
      players[id].stop()


    # Fun Commands
    @commands.command()
    async def randomnumber(self, ctx, minimum=None, maximum=None):
      await ctx.send(random.randint(minimum, maxium))

        # Help/Utilites
    @commands.command()
    async def help(self, ctx):
        pass

def setup(bot):
  client.add_cog(Commands(bot))


