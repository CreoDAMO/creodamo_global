import websockets
from prometheus_client import Counter
from config import AppConfig

class WebSocketServer:

    def __init__(self):
        self.config = AppConfig()
        self.connections_counter = Counter('websocket_connections', 'Number of WebSocket connections')

    async def handler(self, websocket, path):
        self.connections_counter.inc()
        try:
            pass
        finally:
            self.connections_counter.dec()
