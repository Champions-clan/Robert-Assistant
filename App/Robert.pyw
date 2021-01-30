import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import wolframalpha
import os
import random
import matplotlib.pyplot as plt
from PIL import ImageGrab


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



def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        speak("The day is " + day_of_the_week)


def grabPhoto():
    try:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
        else:
            ret = False
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        speak('Image Captured!')
        print(green + '\n\tDone!' + reset)
        plt.imshow(img1)
        plt.title('Image Camera-1')
        plt.xticks([])
        plt.yticks([])
        plt.show()
        cap.release()
    except Exception as e:
        print(red + '\n\tUnable to Grab Image!' + reset)
        speak('Unable to Grab Image!')


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def playMusic():
    try:
        music_dir = input("Enter your file Directory: ")
        songNum = random.randint(0, 159)
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[songNum]))
        print(green + '\n\tPlaying Music! ' + reset)
        speak('Playing Music!')
    except Exception as e:
        speak('Unable to Play Music From Your Device!')
        print(red + '\n\tUnable to Play Music!' + reset)

def take_speak_command():
    #wishMe()
    speak("Nice To See You Again")
    statement = takeCommand().lower()
    if statement == 0:

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'date' in statement:
            speak(date.today().day)

        elif 'day' in statement:
            tellDay()

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Robert your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or scientific questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Champions Clan for timathon")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'open cmd' in statement or 'command prompt' in statement:
            print(yellow + '\n\tOpening COMMAND PROMPT!' + reset)
            speak('Opening Command Promt')
            os.startfile('C:\\Windows\\System32\\cmd.exe')

        elif 'open calculator' in statement:
            print(yellow + '\n\tOpening CALCULATOR' + reset)
            speak('Opening Calculator!')
            os.startfile('C:\\Windows\\System32\\calc.exe')

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'screenshot' in statement or 'screen shot' in statement:
            speak("Grabbing Screenshot!")
            print(yellow + '\n\tDone!' + reset)
            img = ImageGrab.grab()
            speak("Done!")
            img.show()

        elif 'play music' in statement or 'play song' in statement:
            playMusic()

        elif 'open notepad' in statement:
            print(yellow + '\n\tOpening NOTEPAD!' + reset)
            speak('Opening Notepad')
            os.startfile('C:\\Windows\\system32\\notepad.exe')

        elif "Start Power Mode" in statement:
            speak('I can answer to Computational and Scientific questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.statement(question)
            answer = next(res.results).text
            speak(answer)


if __name__ == "__main__":
    take_speak_command()
