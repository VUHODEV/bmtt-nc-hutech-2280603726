import hashlib
import json
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(proof=1, previous_hash="0")  # Khởi tạo block đầu tiên (Genesis Block)

    def create_block(self, proof, previous_hash):
        """Tạo block mới và thêm vào blockchain"""
        block = Block(len(self.chain) + 1, self.pending_transactions, previous_hash, proof)
        self.pending_transactions = []  # Xóa danh sách giao dịch đang chờ xử lý
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        """Thêm giao dịch mới vào danh sách chờ"""
        self.pending_transactions.append({"sender": sender, "receiver": receiver, "amount": amount})
        return self.last_block.index + 1

    def proof_of_work(self, last_proof):
        """Bài toán tìm proof-of-work (POW)"""
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """Xác thực proof bằng cách tạo hash có 4 số 0 ở đầu"""
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def last_block(self):
        return self.chain[-1]

    def is_chain_valid(self):
        """Kiểm tra tính hợp lệ của blockchain"""
        for i in range(1, len(self.chain)):
            prev_block = self.chain[i - 1]
            curr_block = self.chain[i]

            if curr_block.previous_hash != prev_block.hash:
                return False

            if not self.valid_proof(prev_block.proof, curr_block.proof):
                return False

        return True
