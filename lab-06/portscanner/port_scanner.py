import socket

def scan_ports(target, ports):
    """Quét các cổng trên một địa chỉ IP nhất định."""
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Thời gian timeout 1 giây
        result = sock.connect_ex((target, port))  # Kết quả trả về 0 nếu cổng mở
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    target = input("Nhập IP hoặc hostname cần quét: ")
    ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]  # Danh sách cổng phổ biến

    open_ports = scan_ports(target, ports)  # Gọi hàm quét port

    if open_ports:  
        print(f"Các cổng mở trên {target}: {', '.join(map(str, open_ports))}")
    else:
        print(f"Không tìm thấy cổng mở trên {target}.")

if __name__ == "__main__":
    main()
