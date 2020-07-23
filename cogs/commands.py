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
      member = ctx.author
      voice_state = member.voice
      if voice_state is None:
        await ctx.send('You must be in a voice channel to use this command.')
      else: 
        voice_channel = voice_state.channel       
        await voice_channel.connect()
      
    @commands.command()
    async def leave(self, ctx):
      guild = ctx.message.guild
      voice_client = guild.voice_client
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
    async def randomnumber(self, ctx, minimum: int, maximum: int):
      await ctx.send(random.randint(minimum, maxium))

        # Help/Utilites
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Nerb Bot info")
        embed.add_field(name="Music Commands", value="n!n join [Joins the vc] n!n play [plays a song of your choice] n!n leave [leaves the vc] n!n stop[stops the current song] n!n resume [resumes the song you have stopped]", inline=False)
        embed.add_field(name="Admin commands (only high ranks can use these) n!n clear [clears a certain amount of messages from the channel] n!n kick [member] n!n ban [member] n!n mute [member] n!n [unmute]")
        embed.add_field(name="Fun commands!")
        
def setup(bot):
    bot.add_cog(Commands(bot))


