import tornado.web
import tornado.websocket
import tornado.ioloop
import random

# Danh sách các client đang kết nối
connected_clients = set()

class WebSocketServer(tornado.websocket.WebSocketHandler):
    def open(self):
        """Khi client kết nối"""
        print("New client connected")
        connected_clients.add(self)

    def on_message(self, message):
        """Nhận tin nhắn từ client"""
        print(f"Received from client: {message}")
        self.write_message(f"Server: {random_word_selector()}")

    def on_close(self):
        """Khi client đóng kết nối"""
        print("Client disconnected")
        connected_clients.remove(self)

def random_word_selector():
    """Hàm chọn ngẫu nhiên một từ từ danh sách"""
    words = ["banana", "apple", "orange", "grape"]
    return random.choice(words)

def send_random_word():
    """Gửi từ ngẫu nhiên đến tất cả client mỗi 3 giây"""
    if connected_clients:
        word = random_word_selector()
        for client in connected_clients:
            client.write_message(f"Server: {word}")
        print(f"Sending message grape to: {word}")

def main():
    """Khởi chạy WebSocket server"""
    app = tornado.web.Application([(r"/websocket", WebSocketServer)])
    app.listen(8765)  # Server lắng nghe trên cổng 8765
    print("WebSocket Server started on ws://localhost:8765/websocket")

    # Thiết lập gửi tin nhắn tự động mỗi 3 giây
    periodic_callback = tornado.ioloop.PeriodicCallback(send_random_word, 3000)
    periodic_callback.start()

    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()