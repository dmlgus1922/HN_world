from urllib import parse
import urllib.request
import websockets
import asyncio
import ssl
import pyaudio
import numpy as np
import websocket
import _thread
import time
import rel

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# ssl_context.load_cert_chain('C:/Temp/openssl-0.9.8e_X64/private.crt', keyfile='C:/Temp/openssl-0.9.8e_X64/private.key')
# ssl_context.load_verify_locations('C:/Temp/openssl-0.9.8e_X64/private.crt')
# print(type(ssl_context))

# ssl_context = ssl.create_default_context()
# ssl_context.load_verify_locations()

def on_message(ws, message):
    print(message)
    # print(1)
    # pass

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):

    print("receive thread Opened connection")



encoded = parse.quote('김의현')

url =  'wss:' + encoded

# websocket.enableTrace(True)
ws = websocket.WebSocketApp(
    url,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
    )

ws.run_forever(
               sslopt={
                "cert_reqs": ssl.CERT_NONE,
                "check_hostname": False,
                "ssl_version": ssl.PROTOCOL_TLSv1_2,
                # 'certfile' : 'C:/Temp/openssl-0.9.8e_X64/private.crt',
                # 'keyfile' : 'C:/Temp/openssl-0.9.8e_X64/private.key'
               }
            # context = ssl_context
               )  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
# rel.signal(2, rel.abort)  # Keyboard Interrupt
# rel.dispatch()


