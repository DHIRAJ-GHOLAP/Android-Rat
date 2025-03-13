import asyncio
import websockets

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            response = input("Enter command for mobile: ")
            await websocket.send(response)
    except Exception as e:
        print(f"Client disconnected: {e}")
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)  # Adjust host/port as needed
    print("Server running on ws://0.0.0.0:8765")
    await server.wait_closed()

asyncio.run(main())
