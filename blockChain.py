import hashlib


class NeuralCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
t1 = "Alice sends 2 NC to Fred"
t2 = "Bob sends 4.1 NC to Fred"
t3 = "Fred sends 3.2 NC Eve"
t4 = "David sends 1 NC to James"
t5 = "Fred sends 5.4 NC to Jennifer"
t6 = "Fred sends 5.4 NC to David"

initial_block = NeuralCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)