import asyncio
import websockets
from prometheus_client import start_http_server, Counter

class WebSocketServer:
    def __init__(self):
        # Set WebSocket server address and port
        self.address = 'localhost'
        self.port = 5000

    async def websocket_handler(self, websocket, path):
        while True:
            data = await self.data_manager.get_latest_data()
            await websocket.send(data)
            await asyncio.sleep(1)  # Update interval

    def start(self):
        # Start Prometheus metrics server
        start_http_server(8080)

        # Define and register metrics
        websocket_connections = Counter('websocket_connections', 'Number of WebSocket connections')

        async def register(websocket):
            # Increment the counter when a new connection is established
            websocket_connections.inc()

        async def unregister(websocket):
            # Decrement the counter when a connection is closed
            websocket_connections.dec()

        async def handler(websocket, path):
            await register(websocket)
            try:
                await self.websocket_handler(websocket, path)
            finally:
                await unregister(websocket)

        start_server = websockets.serve(handler, self.address, self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
