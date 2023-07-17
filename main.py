from gtts import gTTS as gt
from playsound import playsound as ps
import pyttsx3 as pyt
import speech_recognition as sr
import pyttsx3 as pys
import wikipedia as wiki
# from googlesearch import search
import time

# # strings = "I am driving a car"
# # a = gt(text=strings, lang="en", slow=False)
# # a.save('Driving.mp3')
# # time.sleep(1)
# ps('Driving.mp3')


def Speech(speak):
    a = pys.init()
    a.say(speak)
    a.runAndWait()


recog = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as microphone:
            print("Listening")
            recog.adjust_for_ambient_noise(microphone, 3)
            audio = recog.listen(microphone)
            time.sleep(1.5)
            text = recog.recognize_google(audio)
            print(text)
            Speech(text)
    except sr.UnknownValueError:
        Speech("Sadly I can not hear you.")

# text = input("a")
# Speech(text)

# python venv -m envvv
# cd envvv/Scripts
# activate