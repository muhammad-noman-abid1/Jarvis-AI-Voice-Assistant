# Jarvis - AI Powered Voice Assistant

Jarvis is a Python based desktop voice assistant built as my first major Python project.

It combines voice recognition, text to speech, web automation, music playback, news retrieval, and AI powered question answering into a single voice controlled assistant.

The main purpose of this project is to apply Python programming concepts to a real world application while learning about APIs, AI integration, automation, and software development.

## Features

### Voice Interaction

Wake word detection using "Jarvis"
Speech recognition using Google Speech Recognition
Text to speech using pyttsx3
Voice based command execution
Concise AI responses designed for voice interaction

### Website Commands

Jarvis can open websites through voice commands.

Supported websites include:

- Google
- YouTube
- Facebook
- Instagram
- GitHub
- LinkedIn
- Gemini
- Canva
- ChatGPT

Example:

"Jarvis, open YouTube"

### Games Commands

Jarvis can open Games through voice commands.
Supported Games include:

- Deadshot.io
- Ping Pong game

### Music Player

Jarvis includes a custom music library stored in `musicLibrary.py`.
Songs can be played using voice commands.

Examples:

"Jarvis, play music Skyfalls"

### News

Jarvis can retrieve recent news using the NewsAPI service.

Example:

"Jarvis, tell me the news"

### AI Powered Question Answering

Jarvis can answer general questions using AI.
The project currently integrates:

- Groq API
- Google Gemini API

Groq is currently used as the primary AI provider.
Gemini has also been integrated and tested as an additional AI provider.

Example:

"Jarvis, what is quantum computing?"

Jarvis sends the question to the AI service and speaks the response.

### Conversation Context

The AI system can maintain conversation context during an active session.

For example:

User:
"My name is Nomi."

Jarvis:
"Nice to meet you, Nomi."

User:
"What is my name?"

Jarvis can use the previous conversation context to answer.

### API Key Security

The `.env` file is included in `.gitignore` so API keys are not uploaded to GitHub.

## How Jarvis Works

The basic workflow is:

User
↓
Microphone
↓
Speech Recognition
↓
Wake Word Detection
↓
Command Processing
↓
Local Command or AI Question
↓
Action or AI Response
↓
Text to Speech
↓
User

Jarvis separates normal commands from AI questions.

For example:

"Open YouTube"

This is handled directly by Python and does not require an AI request.

## Project Structure

```text
Jarvis/
│
├── main.py
├── client.py
├── client_groq.py
├── musicLibrary.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
