import os
import speech_recognition as sr
from pydub import AudioSegment
import subprocess

def transcription(path):
    #file = os.getfilename(path)
    mp4_file = path.endswith('.mp4')
    mp3_file = path.endswith('.mp3')
    wav_file = path.endswith('.wav')

    if (mp4_file):
        p = path.split("\\")
        le = len(p)
        n = p[le - 1].split(".")

        newWav = n[0] + ".wav"

        command = "ffmpeg -i "+ path +" -ab 160k -ac 2 -ar 44100 -vn "+newWav
        subprocess.call(command, shell=True)
        f = os.path.abspath(newWav)
        wavTranscription(f)
    elif(mp3_file):
        sound = AudioSegment.from_mp3(path)
        f = sound.export("mp3.wav", format="wav")
        p = os.path.abspath("mp3.wav")
        wavTranscription(p)
    elif(wav_file):
        wavTranscription(path)
    else:
        print("Sorry cannot convert this file into text")


def wavTranscription(path):
    r = sr.Recognizer()
    hellow = sr.AudioFile(path)

    p = path.split("\\")
    le = len(p)
    n = p[le-1].split(".")

    textFile = n[0] + ".txt"


    with hellow as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print(s)
        text_file = open(textFile, "w")
        text_file.write(s)
        text_file.close()
    except Exception as e:
        print("Exception: "+str(e))

if __name__ == '__main__':
    path = "C:\\Users\\jesus\\OneDrive\\Desktop\\wav.wave"
    transcription(path)


