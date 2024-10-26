from discord.ext import commands
from config import TOKEN
from config import prefix, intents
from commands.info import info
from commands.on_message import message_chat
from functions.get_channel import get_channel


# Crear una instancia de bot
bot = commands.Bot(command_prefix= prefix, intents= intents)


# Evento de inicio
@bot.event
async def on_ready():
    for guild in bot.guilds:
        bot_channel = await get_channel(guild)
        print(f"Bot conectado correctamente en {guild}")
        await bot_channel.send("¡IA bot se ha conectado al servidor en el canal especializado!")
        

#Procesar cada mensaje como una pregunta para la IA
@bot.event
async def on_message(message):

    #Ignorar mensaje del propio bot
    if message.author == bot.user:  
        return
    
    #Obtener el canal
    bot_channel = await get_channel(message.guild)

    #Llama a la IA si el mensaje no comienza con el simbolo que se usa para los comandos ("$")
    if not message.content.startswith("$") and bot_channel and message.channel == bot_channel:
        await message_chat(message)

    #revisa si el mensaje coincide con algún comando del bot y lo ejecuta si es necesario.
    await bot.process_commands(message) 


# Agregar un comando de información
@bot.command(name="info")
async def info_chat(ctx):
    bot_channel = await get_channel(ctx.guild)
    if bot_channel and ctx.channel == bot_channel:
        await info(ctx)


# Ejecutar el bot
bot.run(TOKEN)