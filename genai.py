import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Inicializa la IA
genai.configure(api_key=os.getenv("gemini_bot_key"))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])