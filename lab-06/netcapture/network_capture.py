import subprocess
from scapy.all import sniff, get_if_list, Raw

def get_interfaces():
    """ Lấy danh sách các giao diện mạng """
    return get_if_list()

def packet_handler(packet):
    """ Xử lý gói tin khi bắt được """
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(packet[Raw].load)

# Lấy danh sách giao diện mạng
interfaces = get_interfaces()

print("Danh sách các giao diện mạng:")
for i, iface in enumerate(interfaces, start=1):
    print(f"{i}. {iface}")

# Chọn giao diện mạng
while True:
    try:
        choice = int(input("Chọn giao diện mạng (số): "))
        if 1 <= choice <= len(interfaces):
            selected_iface = interfaces[choice - 1]
            break
        else:
            print("Vui lòng nhập số hợp lệ!")
    except ValueError:
        print("Vui lòng nhập số!")

print(f"Bắt đầu sniff trên giao diện: {selected_iface}")

# Bắt gói tin trên giao diện được chọn
sniff(iface=selected_iface, prn=packet_handler, filter="tcp")
