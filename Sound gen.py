import speech_recognition as sr
from gtts import gTTS
import playsound
text = input("What you want me to say ")
storage = input("By what name to store it ")
tts = gTTS(text=text, lang="en")
filename = str(storage)+".mp3"
tts.save(filename)
playsound.playsound(filename)
