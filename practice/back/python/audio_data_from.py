import pyaudio
import numpy as np
import streamlit as st


CHUNK = 1024
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16, rate=RATE, input=True, 
    frames_per_buffer=CHUNK, channels=1
    )

data = stream.read(CHUNK)
waveform = np.frombuffer(data, dtype=np.int16)
waveform = np.append(waveform, -5)
waveform = np.insert(waveform, 0, -5)
waveform = waveform[100:800]
print(type(waveform), len(waveform), '\n', waveform)

p.close(stream)