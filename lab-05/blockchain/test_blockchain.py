from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Thêm các giao dịch
my_blockchain.add_transaction("Alice", "Bob", 10)
my_blockchain.add_transaction("Bob", "Charlie", 5)

# Tạo block mới với Proof-of-Work
last_proof = my_blockchain.last_block.proof
proof = my_blockchain.proof_of_work(last_proof)
new_block = my_blockchain.create_block(proof, my_blockchain.last_block.hash)

# In thông tin các block
for block in my_blockchain.chain:
    print(block)

# Kiểm tra tính hợp lệ của blockchain
print("Is Blockchain Valid:", my_blockchain.is_chain_valid())
