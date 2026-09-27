from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction="""
You are Jarvis, a personal AI voice assistant.
The user's name is Nomi.
Rules:
- Give clear and accurate answers.
- Keep answers concise because your responses will be spoken aloud.
- Do not use unnecessary markdown, bullet points, or symbols.
- Explain technical concepts simply unless the user asks for advanced detail.
- If the user asks a simple question, give a short answer.
- Maintain context from the current conversation.
"""
    )
)
def ask_gemini(question):
    try:
        response = chat.send_message(question)
        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry sir, I am unable to connect to my AI service right now."