import hashlib
import json
import time

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'prev_hash': self.prev_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'prev_hash': self.prev_hash,
            'hash': self.hash
        }

    @classmethod
    def from_dict(cls, data):
        block = cls(data['index'], data['data'], data['prev_hash'])
        block.timestamp = data['timestamp']
        block.hash = data['hash']
        return block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), data, last_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash() or current.prev_hash != previous.hash:
                return False
        return True

    def to_list(self):
        return [block.to_dict() for block in self.chain]

    @classmethod
    def from_list(cls, data_list):
        blockchain = cls()
        blockchain.chain = [Block.from_dict(b) for b in data_list]
        return blockchain
