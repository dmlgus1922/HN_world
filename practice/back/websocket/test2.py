from websocket import WebSocketApp
from threading import Thread
import json
import time
def on_message(ws, msg):
    msg = json.loads(msg.decode('utf-8'))
    print(msg)
def on_error(ws, msg):
    print(msg)
def on_close(ws):
    print("close")
def on_open(ws):
    def run(*args):
        request = '[{"ticket":""},{"type":"ticker","codes":["KRW-BTC"]}]'
        ws.send(request)
        time.sleep(5)
        ws.close()
    th = Thread(target=run, daemon=True)
    th.start()

if __name__ == "__main__":
    ws = WebSocketApp("wss://api.upbit.com/websocket/v1",
                      on_message=on_message,
                      on_error=on_error,
                      on_close=on_close,
                      on_open=on_open)
    ws.run_forever()