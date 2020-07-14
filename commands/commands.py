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
      await client.join_voice_channel(channel)

    @commands.command()
    async def leave(self, ctx):
      guild = ctx.message.guild
      voice_client = client.voice_client_in(guild)
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
    async def randomnumber(self, ctx, minimum=minimum, maximum=maximum):
      await ctx.send(random.randint(minimum, maxium))

        # Help/Utilites
    @commands.command()
    async def help(self, ctx):
      embed = discord.Embed(
      title = "Commands For Nerb"
      description = "All the commands use the prefix n!n"
      colour = discord.Colour.orange()
      
      )
    
      embed.set_footer("Thank you for reading :D")
      embed.set_thumbnail(url="")
      embed.add_field(name="Music", value="1. n!n join [Makes the bot join the voice channel] 2. n!n play [songname/ytlink] 3. n!n stop [Stops the song] n!n pause [Pauses the song] n!n resume [Resumes the song]")
      embed.add_field(name="Utilites", value="1.n!n help [Gives you information about the bot], 2. n!n ping - Pong!")
      embed.add_field(name="AutoMod", value="1. n!n kick (member) (reason) [Kicks a specific user with a reason] 2. n!n ban [Bans a specific user with a reason]")

    await ctx.author.send(embed=embed)

def setup(bot):
  client.add_cog(Commands(bot))


