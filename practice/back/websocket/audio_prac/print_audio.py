import numpy as np
import pyaudio

CHUNK = 2**10
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16, rate=RATE, input=True, 
    frames_per_buffer=CHUNK, channels=1
    )

# while True:
#     data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
#     print(int(np.average(np.abs(data))))


# while True:
#     # data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
#     data = stream.read(CHUNK)
#     # print(int(np.average(np.abs(data))))
    
#     print(data)

data = stream.read(CHUNK)
# data = np.fromstring(stream.read(CHUNK), dtype=np.int16)

print(type(data))


stream.stop_stream()
stream.close()



