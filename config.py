import os
import discord
from dotenv import load_dotenv

load_dotenv()

# Reemplaza 'tu_token_aquí' con el token de tu bot
TOKEN = os.getenv("discord_api_key")

#Prefijo del bot
prefix = "$"

#ID del canal del Bot
channel_id = 1299455211064000532


# Intents son necesarios para algunas características del bot
intents = discord.Intents.default()
intents.message_content = True  # Si necesitas leer el contenido de los mensajes
intents.presences = True  # Si necesitas rastrear el estado de los usuarios
intents.members = True  # Si necesitas acceder a la lista de miembros