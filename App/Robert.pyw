import pyttsx3
import speech_recognition as sr
import os
import random

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            statement = r.recognize_google(audio, language='en-in')
            print("the command is printed=", statement)

        except Exception as e:
            print(e)
            print("Say that again sir")
            speak("Sir press hotkey again to give command")
            print("Sir press hotkey again to give command")
            return "None"

        return statement


def take_speak_command():
    wishMe()
    speak("Nice To See You Again")
    statement = takeCommand().lower()
    if statement == 0

       
if __name__ == "__main__":
    take_speak_command()
