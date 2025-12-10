from aes_layer import AESCipher
from blockchain import Blockchain
from ids_engine import detect_suspicious
from scapy.all import sniff

aes = AESCipher()
chain = Blockchain()

def process_packet(packet):
    alert = detect_suspicious(packet)
    if alert:
        print(alert)
        encrypted = aes.encrypt(alert)
        chain.add_block(encrypted)
        print("[+] Alert encrypted & added to blockchain.")

print("SecureLog Running...")
sniff(filter="tcp", prn=process_packet, store=False)
