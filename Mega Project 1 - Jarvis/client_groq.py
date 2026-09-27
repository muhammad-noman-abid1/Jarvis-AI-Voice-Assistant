import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_groq(question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": """You are Jarvis, a personal AI voice assistant.
The user's name is nomi.
Rules:
- Give clear and accurate answers.
- Keep answers concise because your responses will be spoken aloud.
- Do not use unnecessary markdown, bullet points, or symbols.
- Explain technical concepts simply unless the user asks for advanced detail.
- If the user asks a simple question, give a short answer.
- Maintain context from the current conversation."""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content