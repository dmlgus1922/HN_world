from urllib import parse
import urllib.request
import websockets
import asyncio
import ssl
import pyaudio
import numpy as np
import websocket

CHUNK = 2**10
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16, rate=RATE, input=True, 
    frames_per_buffer=CHUNK, channels=1
    )

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.load_cert_chain('C:/Temp/openssl-0.9.8e_X64/private.crt', keyfile='C:/Temp/openssl-0.9.8e_X64/private.key')

encoded = parse.quote('김의현')

# print(encoded)

url =  '' + encoded

async def test():
    async with websockets.connect(url, ssl=ssl_context) as websocket:
        rec = []
        while True:
            # data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
            data = stream.read(CHUNK)
            # print(int(np.average(np.abs(data))))

            websocket.send(data)
            # print('123')
            re = websocket.recv()
            
            print(re)


asyncio.get_event_loop().run_until_complete(test())