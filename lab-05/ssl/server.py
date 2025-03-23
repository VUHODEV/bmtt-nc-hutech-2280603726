import socket
import ssl
import threading

# Địa chỉ và cổng server
server_address = ("localhost", 12345)

def handle_client(conn):
    """Xử lý kết nối từ client"""
    try:
        print("🔗 New client connected")
        conn.sendall(b"Welcome to Secure Server!")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"📩 Received: {data.decode()}")
            conn.sendall(b"Server received your message!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()
        print("❌ Client disconnected")

def start_server():
    """Khởi động server SSL"""
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain("certificates/server-cert.crt", "certificates/server-key.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print(f"🚀 Secure Server started at wss://{server_address[0]}:{server_address[1]}")

    while True:
        client_socket, addr = server_socket.accept()
        secure_conn = context.wrap_socket(client_socket, server_side=True)
        threading.Thread(target=handle_client, args=(secure_conn,)).start()

if __name__ == "__main__":
    start_server()
