import os
import discord
from discord.ext import commands

WELCOME_CHANNEL = os.getenv("WELCOME_CHANNEL", "general")

class Bienvenida(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name=WELCOME_CHANNEL)
        if channel:
            embed = discord.Embed(
                title="🎉 ¡Bienvenido/a!",
                description=f"Hola {member.mention}, bienvenido/a a **{member.guild.name}**.\n¡Esperamos que la pases genial! 😄",
                color=0x00ff00
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            await channel.send(embed=embed)
        else:
            print(f"⚠️ No se encontró el canal '{WELCOME_CHANNEL}' en {member.guild.name}")

async def setup(bot):
    await bot.add_cog(Bienvenida(bot))
