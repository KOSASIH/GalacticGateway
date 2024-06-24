import asyncio
import websockets

class GalacticNetwork:
    def __init__(self, gateway_address: str):
        self.gateway_address = gateway_address

    async def send_data(self, alien_ship: str, data: bytes) -> str:
        # Send data to the alien ship using websockets
        async with websockets.connect(f"ws://{alien_ship}:8080") as websocket:
            await websocket.send(data)
            response = await websocket.recv()
            return response
