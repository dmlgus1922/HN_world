import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f'{name}씨 안녕하세요.'

    await websocket.send(greeting)
    print(f'> {greeting}')


start_server = websockets.serve(hello, 'localhost', 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()