import speech_recognition as sr
import pyttsx3
"""

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                      
    speak("Hello")
    print("listening...")
    audio = r.record(source,duration=3)
    try:
        str=r.recognize_google(audio)
        print(str)
    except:
        print("some error occurred!") 
"""   

a = 0
a = not a
print(a)