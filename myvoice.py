import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
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
    speak("I am myvoice sir. How may i help you?")


if __name__ == "__main__":
    whishMe()
