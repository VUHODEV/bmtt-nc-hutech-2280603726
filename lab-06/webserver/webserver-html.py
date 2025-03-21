import socket
import os

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8', errors='ignore')
    print(f"Received request:\n{request_data}")
    
    request_lines = request_data.split("\n")
    if len(request_lines) > 0:
        request_line = request_lines[0]
        parts = request_line.split()
        if len(parts) >= 2:
            requested_file = parts[1]
        else:
            requested_file = "/"
    else:
        requested_file = "/"

    if requested_file == "/":
        requested_file = "/index.html"
    elif requested_file == "/admin":
        requested_file = "/admin.html"
    
    file_path = f".{requested_file}"
    
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, "rb") as f:
            content = f.read()
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(content)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode('utf-8') + content
    else:
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n"
            "\r\n"
            "<html><body><h1>404 Not Found</h1></body></html>"
        ).encode('utf-8')
    
    client_socket.sendall(response)
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(5)
    
    print("Server listening on http://127.0.0.1:8080")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_request(client_socket)

if __name__ == "__main__":
    main()