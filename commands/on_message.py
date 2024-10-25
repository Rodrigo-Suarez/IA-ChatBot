from genai import chat

async def message_chat(message):
    
    pregunta = message.content

    try:
        response =  chat.send_message(pregunta)
        response_texto = response.text
        partes =  [response_texto[i:i+2000] for i in range(0, len(response_texto), 2000)]
        for parte in partes:
            await message.channel.send(parte)
        
    except Exception as e:
            print(f"Error en on_message: {e}")
            
    