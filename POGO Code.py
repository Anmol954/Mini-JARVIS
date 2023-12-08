import speech_recognition as sr
import os
import webbrowser
import numpy as np
import pyttsx3
import datetime
import openai
import subprocess

# Set your OpenAI API key here
api_key = "Your-Open-AI-Key"
chat_str = ""


# Initialize the OpenAI API client
openai.api_key = api_key


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5)
            say("Recognizing")
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            say("Could not understand the audio.")
            print("Could not understand the audio.")
    return "Some Error Occurred. Sorry from POGO"

print("-----Welcome to POGO's world-----")
say('Welcome to POGOs world')

while True:
    say("Give me your command Sir.")
    print("Listening")
    query = takeCommand()
    print(query)

    if "text chat" in query.lower():
        # Start a text chat session
        say("Text chat mode activated. You can start typing your questions or commands.")
        chat_str = ""
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit" or user_input.lower() == "end":
                break
            chat_str += f"You: {user_input}\n"
            response = openai.Completion.create(
                engine="davinci",
                prompt=chat_str,
                max_tokens=100,
                stop=None,
                temperature=0.7,
            )
            chat_str += f"AI: {response.choices[0].text}\n"
            print(f"AI: {response.choices[0].text}")
            say(response.choices[0].text)
    else:
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"],["gpt", "https://chat.openai.com/"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "go away".lower() in query.lower():
            say("It was a great interaction sir, bye bye")
            break
        elif "current time" in query.lower():
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The current time is {current_time}.")
        elif "open notepad" in query.lower():
            subprocess.Popen("notepad.exe")
            say("Opening Notepad.")
        elif "open calculator" in query.lower():
            subprocess.Popen("calc.exe")
            say("Opening Calculator")
        elif "open spotify" in query.lower():
            spotify_path = "C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.222.982.0_x64__zpdnekdrzrea0\Spotify.exe"
            if os.path.exists(spotify_path):
                say("Opening Spotify...")
                subprocess.Popen(spotify_path)
            else:
                say("Spotify app not found on your system.")

        elif "open discord" in query.lower():
            discord_path = "C:/Users/anmol\AppData\Local\Discord/app-1.0.9022\Discord.exe"
            if os.path.exists(discord_path):
                say("Opening Discord...")
                subprocess.Popen(discord_path)
            else:
                say("Discord app not found on your system.")

        elif "open WhatsApp" in query.lower():
            WhatsApp_path = "C:/Users/anmol\OneDrive\Desktop/WhatsApp.exe"
            if os.path.exists(WhatsApp_path):
                say("Opening WhatsApp...")
                subprocess.Popen(WhatsApp_path)
            else:
                say("WhatsApp app not found on your system.")