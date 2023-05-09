from urllib import parse
import ssl
import pyaudio
import websocket
import threading

def send_audio(name):
    
    def inner_send_audio():     
        CHUNK = 1024
        RATE = 16000

        p = pyaudio.PyAudio()

        stream = p.open(
            format=pyaudio.paInt16, rate=RATE, input=True, 
            frames_per_buffer=CHUNK, channels=1
            )
        
        while True:
            data = stream.read(CHUNK)
            ws.send(data, websocket.ABNF.OPCODE_BINARY)

    send_thread = threading.Thread(target=inner_send_audio)
    send_thread.daemon = True
    
    def on_open(ws):
        print("### wss Opened connection ###")
        send_thread.start()
    
    def on_message(ws, message):
        print(f'받은 메시지: {message}')
        
        if message == '안녕하세요':
            ws.close()
            print('안녕하세요 일치')

    def on_error(ws, error):
        print(error)

    def on_close(ws, close_status_code, close_msg):
        print("### closed ###")

    encoded = parse.quote(name)

    url =  'wss' + encoded

    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
        )
    
    # ws.run_forever(
    #     sslopt={
    #     "cert_reqs": ssl.CERT_NONE,
    #     "check_hostname": False,
    #     "ssl_version": ssl.PROTOCOL_TLSv1_2,
    #     }
    # )
    def wss_run():
            ws.run_forever(
                sslopt={
                "cert_reqs": ssl.CERT_NONE,
                "check_hostname": False,
                "ssl_version": ssl.PROTOCOL_TLSv1_2,
                }
            )
    wss_run_thread = threading.Thread(target=wss_run)
    wss_run_thread.start()
    print('wss end')