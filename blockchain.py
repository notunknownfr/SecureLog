import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + str(self.timestamp) + self.data + self.previous_hash
        return hashlib.sha256(content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis()]

    def create_genesis(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, data):
        last = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, last.hash)
        self.chain.append(new_block)
