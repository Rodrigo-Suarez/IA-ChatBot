from discord.ext import commands
from config import TOKEN
from config import prefix, intents, channel_id
from commands.info import info
from commands.on_message import message_chat

# Crear una instancia de bot
bot = commands.Bot(command_prefix= prefix, intents= intents)


# Evento de inicio
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("IA bot se ha conectado al servidor")


#Procesar cada mensaje como una pregunta para la IA
@bot.event
async def on_message(message):

    #Ignorar mensaje del propio bot
    if message.author == bot.user:  
        return
    
    #Llama a la IA si el mensaje no comienza con el simbolo que se usa para los comandos ("$")
    if not message.content.startswith("$"):
        await message_chat(message)

    #revisa si el mensaje coincide con algún comando del bot y lo ejecuta si es necesario.
    await bot.process_commands(message) 


# Agregar un comando de información
@bot.command(name="info")
async def info_chat(ctx):
    await info(ctx)


# Ejecutar el bot
bot.run(TOKEN)