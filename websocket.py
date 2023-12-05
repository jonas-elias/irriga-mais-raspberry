import asyncio
from websockets import connect

async def webSocketConnect(websocket):
    while True:
        message = await websocket.recv()
        print(f"Received: {message}")
        await asyncio.sleep(1)

async def main():
    uri = "ws://localhost:8000/ws/pivo/0ba0bc7a016a873a5250abf65d4fdc0/"
    async with connect(uri) as websocket:
        await webSocketConnect(websocket)

if __name__ == "__main__":
    asyncio.run(main())