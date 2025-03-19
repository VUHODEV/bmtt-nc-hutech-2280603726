import tornado.websocket
import tornado.ioloop

class WebSocketClient:
    def __init__(self, url):
        self.url = url

    async def connect(self):
        """Kết nối đến WebSocket Server"""
        try:
            self.ws = await tornado.websocket.websocket_connect(self.url)
            print("Connected to server!")

            # Nhận tin nhắn liên tục
            await self.receive_messages()

        except Exception as e:
            print(f"Connection error: {e}")

    async def receive_messages(self):
        """Nhận tin nhắn từ server"""
        while True:
            msg = await self.ws.read_message()
            if msg:
                print(f"Received word from server: {msg}")

def main():
    """Chạy WebSocket Client"""
    client = WebSocketClient("ws://localhost:8765/websocket")
    tornado.ioloop.IOLoop.current().run_sync(client.connect)

if __name__ == "__main__":
    main()