import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

# Intents para eventos de miembros y mensajes
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Evento: Bot listo
@bot.event
async def on_ready():
    print(f"✅ DogBot conectado como {bot.user}")
    await bot.load_extension("cogs.bienvenida")  # Cargar módulo de bienvenida

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ ERROR: No se encontró el token del bot en las variables de entorno.")
