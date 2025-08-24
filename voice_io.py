import os
import time
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv


load_dotenv()


class VoiceIO:
def __init__(self):
self.recognizer = sr.Recognizer()
self.engine = pyttsx3.init()
# Optional tuning from .env
rate = int(os.getenv("VOICE_ENGINE_RATE", 180))
vol = float(os.getenv("VOICE_ENGINE_VOLUME", 0.9))
self.engine.setProperty('rate', rate)
self.engine.setProperty('volume', vol)


def say(self, text: str):
self.engine.say(text)
self.engine.runAndWait()


def listen(self, timeout: float = 5.0, phrase_time_limit: float = 8.0) -> str:
with sr.Microphone() as source:
self.recognizer.adjust_for_ambient_noise(source, duration=0.4)
audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
try:
return self.recognizer.recognize_google(audio)
except sr.WaitTimeoutError:
return ""
except sr.UnknownValueError:
return ""
except sr.RequestError:
# network issue for Google Web Speech API
return ""