from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

class AESCipher:
    def __init__(self, key=None):
        self.key = key if key else get_random_bytes(32)

    def pad(self, data):
        pad_len = 16 - (len(data) % 16)
        return data + pad_len * chr(pad_len)

    def encrypt(self, plaintext):
        plaintext = self.pad(plaintext).encode()
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(plaintext)
        return base64.b64encode(iv + encrypted).decode()
