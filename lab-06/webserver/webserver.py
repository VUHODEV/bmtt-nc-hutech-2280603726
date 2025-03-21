import socket

def handle_request(client_socket):
    request_data = client_socket.recv(1024)  # Nhận dữ liệu raw
    print(f"Received raw data: {request_data}")  # Kiểm tra dữ liệu thật sự

    # Ghi dữ liệu vào file để debug
    with open("request_debug.log", "wb") as f:
        f.write(request_data)

    try:
        request_text = request_data.decode('utf-8', errors='ignore')
        print(f"Decoded request:\n{request_text}")
    except UnicodeDecodeError:
        print("Error decoding request as UTF-8")
        client_socket.close()
        return

    first_line = request_text.split("\n")[0] if request_text else ""

    if "GET /admin" in first_line:
        response_body = "<html><body><h1>Welcome to the admin page!</h1></body></html>"
    else:
        response_body = "<html><body><h1>Hello, this is a simple web server!</h1></body></html>"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{response_body}"
    )

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(5)

    print("Server listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_request(client_socket)

if __name__ == "__main__":
    main()
