import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit
import random
import psutil
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def currentTime():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
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
    currentTime()
    date()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Emma. Please tell me how can I help you?")


def introduction():
    speak("I am Emma, AI voice assistant , "
          "I am created by Team Venom , "
          "I can help you in various regards , "
          "I can search for you on the Internet , "
          "I can also grab definitions for you from wikipedia , "
          "In layman terms , I can try to make your life a bed of roses , "
          "Where you just have to command me , and I will do it for you , ")


def creator():
    speak("I am created by Team Venom ,"
          "Team Venom is an extra-ordinary group ,"
          "They have a passion for Robotics, Artificial Intelligence and Machine Learning ,"
          "They are very co-operative ,"
          "If you are facing any problem regarding the 'Emma', They will be glad to help you ")


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak("percent")


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
            currentTime()

        elif 'date' in query:
            date()

        elif 'how are you' in query:
            speak("I am fine, Sir thanks for asking.")

        elif 'who are you' in query or 'tell me about youself' in query:
            introduction()

        elif 'creator' in query:
            creator()

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about it, may be you should give me more times.")

        elif "i love you" in query:
            speak("It's hard to understand. I am still trying to figure this out.")

        elif 'cpu' in query:
            cpu()

        elif 'who am I' in query:
            speak("If you can talk, then definitely you are a human")

        elif 'what is love' in query or 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
                  "And I think it is just a mere illusion , "
                  "It is waste of time")

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
                rand = random.randint(1, 50)
                os.startfile(os.path.join(songs_dir, songs[rand]))
                continue

        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        elif 'play in youtube' in query:
            song = query.replace('play in youtube', '')
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

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = takeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = takeCommand()
            speak("You asked me to remember that" + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remember that" + remember.read())

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            answer = int(takeCommand())
            time.sleep(answer)
            print(answer)

        elif 'offline' in query:
            speak("going Offline")
            quit()
