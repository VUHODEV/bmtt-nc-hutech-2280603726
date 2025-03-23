import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Tạo hash SHA-256 cho block"""
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block #{self.index}\nTimestamp: {self.timestamp}\nTransactions: {self.transactions}\n" \
               f"Proof: {self.proof}\nPrevious Hash: {self.previous_hash}\nHash: {self.hash}\n"
