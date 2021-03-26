import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishMe():
    speak("Welcome sir")
    time()
    date()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Emma. Please tell me how can I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'how are you' in query:
            speak("I am fine, Sir thanks for asking.")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")

        elif 'play songs' in query:
            video = 'F:/Video/Song'
            audio = 'F:/Audio'
            speak("What songs should I play? Audio or Video")
            ans = (takeCommand().lower())
            while (ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (takeCommand().lower())

            if 'audio' in ans:
                songs_dir = audio
                songs = os.listdir(songs_dir)
                print(songs)

            elif 'video' in ans:
                songs_dir = video
                songs = os.listdir(songs_dir)
                print(songs)

            speak("select a random number")
            rand = (takeCommand().lower())
            while ('number' not in rand and rand != 'random'):
                speak("I could not understand you. Please Try again.")
                rand = (takeCommand().lower())

            if 'number' in rand:
                rand = int(rand.replace("number ", ""))
                os.startfile(os.path.join(songs_dir, songs[rand]))
                continue

            elif 'random' in rand:
                rand = random.randint(1, 200)
                os.startfile(os.path.join(songs_dir, songs[rand]))
                continue

        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing...'+song)
            pywhatkit.playonyt(song)

        elif 'search google' in query:
            speak("What should I search?")
            search = takeCommand().lower()
            speak('Searching...')
            webbrowser.open('https://www.google.com/search?q=' + search)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.com/maps/place/" + location + "")

        elif 'offline' in query:
            speak("going Offline")
            quit()
