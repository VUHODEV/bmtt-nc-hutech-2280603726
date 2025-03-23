import socket
import ssl

# Địa chỉ server
server_address = ("localhost", 12345)

def connect_to_server():
    """Kết nối đến server SSL"""
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Không kiểm tra chứng chỉ (Self-signed cert)

    with socket.create_connection(server_address) as sock:
        with context.wrap_socket(sock, server_hostname="localhost") as secure_sock:
            print(f"✅ Connected to Secure Server at {server_address}")

            welcome_message = secure_sock.recv(1024)
            print(f"📩 Server: {welcome_message.decode()}")

            while True:
                msg = input("Bạn: ")
                secure_sock.sendall(msg.encode())
                response = secure_sock.recv(1024)
                print(f"📩 Server: {response.decode()}")

if __name__ == "__main__":
    connect_to_server()
