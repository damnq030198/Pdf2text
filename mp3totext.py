from pydub import AudioSegment # uses FFMPEG
import speech_recognition as sr
from pathlib import Path
#from pydub.silence import split_on_silence
#import io
#from pocketsphinx import AudioFile, Pocketsphinx

def process(filepath, chunksize=60000):
    #0: load mp3
    sound = AudioSegment.from_mp3(filepath)

    #1: split file into 60s chunks
    def divide_chunks(sound, chunksize):
        # looping till length l
        for i in range(0, len(sound), chunksize):
            yield sound[i:i + chunksize]
    chunks = list(divide_chunks(sound, chunksize))
    print(f"{len(chunks)} chunks of {chunksize/1000}s each")

    r = sr.Recognizer()
    #2: per chunk, save to wav, then read and run through recognize_google()
    string_index = {}
    for index,chunk in enumerate(chunks):
        #TODO io.BytesIO()
        chunk.export('File1.wav', format='wav')
        with sr.AudioFile('File1.wav') as source:
            audio = r.record(source)
        #s = r.recognize_google(audio, language="en-US") #, key=API_KEY) --- my key results in broken pipe
        s = r.recognize_google(audio, language="en-US")
        print(s)
        string_index[index] = s
        break
    return string_index

text = process('File1.mp3')