import discord
from discord.ext import commands


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    async def ready(self):
        print(f"Succesfully Logged in As {self.user} to {len(self.guild)} guild")
        self.welcome = self.guild.get_channel(723211438474133614)
        self.guild = self.get_guild(721364747353587743)
        
    @commands.Cog.listener()  
    async def on_member_join(self, member):
        await self.wait_until_ready()
        if member.guild.id == 721364747353587743:
            await self.welcome(f"Welcome to the Nerb-Discord {member.mention}!")


            

def setup(client):
    client.add_cog(Welcome(client))

