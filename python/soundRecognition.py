import speech_recognition as sr
import ctypes

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        word = "terminate"
        audio_data = r.record(source, duration=5)
        text = r.recognize_google(audio_data)
        if word in text.lower():
            break

ctypes.windll.user32.LockWorkStation()
