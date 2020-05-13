import speech_recognition as sr
import os
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "sample.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
# recognize speech using Google Speech Recognition
try:
    print("Audio to text: " + r.recognize_google(audio))
    first_line = r.recognize_google(audio)
    with open("audio.srt", "w") as f:
        f.write(first_line)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
