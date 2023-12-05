import websockets
import asyncio
import unittest

class TestWebSocket(unittest.TestCase):

  async def test_connect(self):
    async with websockets.connect("http://localhost:8765") as ws:  
      response = await ws.recv()
      data = json.loads(response)
      self.assertEqual(data["key"], "value")

if __name__ == "__main__":
  unittest.main()
