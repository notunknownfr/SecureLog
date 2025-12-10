from scapy.all import sniff, TCP, IP
from collections import defaultdict

syn_counter = defaultdict(int)

def detect_suspicious(packet):
    if packet.haslayer(TCP):
        src = packet[IP].src

        if packet[TCP].flags == "S":
            syn_counter[src] += 1

            if syn_counter[src] > 10:
                return f"[ALERT] Possible SYN scan detected from {src}"

    return None
