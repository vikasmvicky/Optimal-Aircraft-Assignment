import hashlib
import json
from datetime import datetime


class Block:

    def __init__(self, index, timestamp, data, previous_hash):

        self.index = index

        self.timestamp = timestamp

        self.data = data

        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()

    def calculate_hash(self):

        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()


class Blockchain:

    def __init__(self):

        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):

        return Block(
            0,
            str(datetime.now()),
            "Genesis Block",
            "0"
        )

    def get_latest_block(self):

        return self.chain[-1]

    def add_block(self, data):

        latest_block = self.get_latest_block()

        new_block = Block(
            len(self.chain),
            str(datetime.now()),
            data,
            latest_block.hash
        )

        self.chain.append(new_block)

    def display_chain(self):

        chain_data = []

        for block in self.chain:

            chain_data.append({
                "Index": block.index,
                "Timestamp": block.timestamp,
                "Data": block.data,
                "Hash": block.hash[:12],
                "Previous Hash": block.previous_hash[:12]
            })

        return chain_data