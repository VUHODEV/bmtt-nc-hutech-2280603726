from scapy.all import *

def modify_icmp_packet(packet):
    """ Thay đổi gói tin ICMP """
    if packet.haslayer(ICMP):
        icmp_packet = packet[ICMP]
        print("Original ICMP Packet:")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Type: {icmp_packet.type}")
        print(f"Code: {icmp_packet.code}")
        print(f"ID: {icmp_packet.id}")
        print(f"Sequence: {icmp_packet.seq}")
        
        # Kiểm tra nếu gói tin có payload
        load_data = icmp_packet.load if hasattr(icmp_packet, "load") else b"No Data"

        print(f"Load: {load_data}")

        # Thay đổi nội dung gói tin
        new_load = b"This is a modified ICMP packet"
        new_packet = IP(src=packet[IP].dst, dst=packet[IP].src) / \
                     ICMP(type=icmp_packet.type, code=icmp_packet.code, id=icmp_packet.id, seq=icmp_packet.seq) / \
                     new_load

        print("\nModified ICMP Packet:")
        print(f"Source IP: {new_packet[IP].src}")
        print(f"Destination IP: {new_packet[IP].dst}")
        print(f"Type: {icmp_packet.type}")
        print(f"Code: {icmp_packet.code}")
        print(f"ID: {icmp_packet.id}")
        print(f"Sequence: {icmp_packet.seq}")
        print(f"Load: {new_load}")
        print("=" * 30)

        # Gửi gói tin ICMP đã thay đổi
        send(new_packet)

def main():
    print("Listening for ICMP packets...")
    sniff(filter="icmp", prn=modify_icmp_packet, store=0)

if __name__ == "__main__":
    main()
