import pyaudio
import wave

CHUNK = 1024

path = './2dc07975-5001-48fd-931d-7b5a6d00cf03.wav'

with wave.open(path, 'rb') as f:
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(f.getsampwidth()),
        channels=f.getnchannels(),
        rate = f.getframerate(),
        output=True
        )
    
    data = f.readframes(CHUNK)

    while data:
        stream.write(data)
        data = f.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()