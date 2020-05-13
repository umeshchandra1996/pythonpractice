import speech_recognition as sr
import os 
from os import path
filename=path.join(path.dirname(path.realpath(__file__)), "sample_v.mp4")
os.system("ffmpeg -i output.wav".format(filename))
r = sr.Recognizer()
with sr.AudioFile('output.wav') as source:
    audio = r.record(source)
try:
    print("Audio to text: " + r.recognize_google(audio))
    first_line = r.recognize_google(audio)
    with open("video.srt", "w") as f:
        f.write(first_line)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



