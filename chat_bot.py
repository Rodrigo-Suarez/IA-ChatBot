import os
import google.generativeai as genai  #pip install google-generativeai
from dotenv import load_dotenv
from google.generativeai import Content

load_dotenv()

genai.configure(api_key=os.getenv("gemini_bot_key"))

history = []

while True:
    pregunta = input("Preguntame lo que quieras >>>  ")

    if pregunta.lower() == "salir":
        break

    # Create the model configuration
    generation_config = {
        "temperature": 0.5,  #Que tan especifica es la respuesta. Va del 0 al 1
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 300,
        "response_mime_type": "text/plain",
    }

    # Create the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

    # Start the conversation
    chat_session = model.start_chat(
        history= [Content(text=p) for p in history]
    )

    # Send the question
    response = chat_session.send_message(pregunta)
    
    history.append(pregunta)
    history.append(response.text)

    # Print the answer
    print(response.text)