import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from client_groq import ask_groq
from dotenv import load_dotenv
import os

load_dotenv()

newsapi = os.getenv("NEWS_API_KEY")
# pip install SpeechRecognition

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    c = c.lower().strip()
    if c.startswith("play music"):
        song = c.replace("play music", "", 1).strip()
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry sir, that song is not in my music library.")
        return
    if "open google" in c.lower():
        speak("Opening Google sir")
        webbrowser.open("https://www.google.com")
        return
    elif "open deadshot game" in c.lower():
        speak("Opening Deadshot Game sir")
        webbrowser.open("https://deadshot.io/")
        return
    elif "i want to play ping pong game" in c.lower():
        speak("Opening Ping Pong Game sir")
        webbrowser.open("https://poki.com/en/g/ping-pong-html5")
        return
    elif "open youtube" in c.lower():
        speak("Opening YouTube sir")
        webbrowser.open("https://www.youtube.com")
        return
    elif "open facebook" in c.lower():
        speak("Opening Facebook sir")
        webbrowser.open("https://www.facebook.com")
        return
    elif "open instagram" in c.lower():
        speak("Opening Instagram sir")
        webbrowser.open("https://www.instagram.com")
        return
    elif "open github" in c.lower():
        speak("Opening GitHub sir")
        webbrowser.open("https://www.github.com")
        return
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn sir")
        webbrowser.open("https://www.linkedin.com")
        return
    elif "open gemini" in c.lower():
        speak("Opening Gemini sir")
        webbrowser.open("https://www.gemini.com")
        return
    elif "open canva" in c.lower():
        speak("Opening Canva")
        webbrowser.open("https://www.canva.com")
        return
    elif "open chatgpt" in c.lower():
        speak("Opening ChatGPT sir ")
        webbrowser.open("https://chat.openai.com")
        return
    elif c.lower().startswith("play music"):
        song = c.lower().split(" ", 2)[2]
        if song in musicLibrary.music:
            speak(f"Playing {song} sir")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry sir, that song is not in my music library.")

    elif "news" in c.lower():
        try:
            r = requests.get(
                f"https://newsapi.org/v2/everything?q=Pakistan&sortBy=publishedAt&language=en&apiKey={newsapi}",
                timeout=10
                )

            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])

                for article in articles[:5]:
                    speak(article["title"])
            else:
                speak("Sorry sir, I couldn't fetch the news.")

        except Exception as e:
            print("News Error:", e)
            speak("Sorry sir, I couldn't connect to the news service.")

        return

    else:
        answer = ask_groq(c)
        speak(answer)

if __name__ == "__main__":
    # my main code logic here
    speak("initialising jarvis.....")
    while True:
        # listen for the wake word "jarvis" 
        # obtain audio from the microphone
        r = sr.Recognizer()       
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print("You said:", word)
            if word.lower() in ["jarvis", "jar", "jervis","vis",]:
                print("Wake word detected!")
                speak("Ya Nomi")
             
            
                        
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                processCommand(command)
                
        except Exception as e:
            print("Error:", type(e).__name__, e)