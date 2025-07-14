from scapy.all import sniff, IP

def demo_packet_handler(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"📦 Packet captured:")
        print(f"   🔹 Source IP:      {ip_layer.src}")
        print(f"   🔹 Destination IP: {ip_layer.dst}")
        print(f"   🔹 Protocol:       {ip_layer.proto}")
        print("-" * 40)

def main():
    print(" Capturing 5 packets...")

    # Capture only 5 packets (demo mode)
    sniff(count=5, prn=demo_packet_handler, store=False)

    print("Packet capture complete!")

if __name__ == "__main__":
    main()
