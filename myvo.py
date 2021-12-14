import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def whishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good Morning!")

    elif hour >= 12 and hour < 18:
        speak("good Afternoon ")

    else:
        speak("good Evening")
    speak("I am myvo sir. How may i help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recgonizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("say that again please...")
        return "none"
    return query


if __name__ == "__main__":
    whishMe()
    takeCommand()
