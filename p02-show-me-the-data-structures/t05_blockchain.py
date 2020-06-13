"""
Every block has some data: data, timestamp, hash, and previous hash.

Every block node consists a block and a next pointer to the next block.

Representation:
block_node: {
    block: {
        data,
        timestamp,
        hash,
        previous_hash hash
    }
    next
}
N.B. It is shown like an object but in reality it is not an object.
Rather, it's a node that can be represented as:
block_node( block( data, timestamp, hash, previous_hash hash ), next )

Blockchain is a linkedlist containing block nodes.
Representation:
block_node1 -> block_node2 -> block_node3


Complexity Analysis:
n = number of total block nodes in the block chain.

Time Complexity:
Append: O(1).
We are keeping track of the tail node, thus it takes constant time.

Traverse: O(n).
We traverse trough the each node of the blockchain.

Space Complexity:
Append: O(1)
Traverse: O(n)
"""

import hashlib
import datetime


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.hash = self._calc_hash(self.data)
        self.previous_hash = previous_hash
        self.timestamp = self._get_time()

    def _calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def _get_time(self):
        return datetime.datetime.now()

    def _format_time(self, timestamp):
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")


class BlockNode:
    def __init__(self, data, previous_hash):
        self.block = Block(data, previous_hash)
        self.next = None


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        previous_hash = self._get_previous_hash()
        new_block_node = BlockNode(data, previous_hash)

        if self.head is None:
            self.head = new_block_node
            self.tail = self.head
            return

        self.tail.next = new_block_node
        self.tail = new_block_node
        return

    def _get_previous_hash(self):
        if self.tail is None:
            return 0

        return self.tail.block.hash

    def traverse(self):
        if self.head is None:
            return None

        block_node = self.head
        count = 0
        while block_node:
            data = block_node.block.data
            time = self._format_time(block_node.block.timestamp)
            hash = block_node.block.hash
            previous_hash = block_node.block.previous_hash

            print(f'Block: {count}, Data: {data}, Time: {time}, \
                \nSHA256 Hash: {hash}, \nPrevious Hash: {previous_hash}\n')

            count += 1
            block_node = block_node.next

    def _format_time(self, timestamp):
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")


# Test Block
data = 'Hello Block'
block = Block(data, 0)
print(block.data, block.hash)

# Test BlockNode
data = 'Hello BlockNode'
block_node = BlockNode(data, 0)
print(block_node.block.data, block_node.block.hash)
print()

# Test BlockChain
blockchain = BlockChain()
blockchain.append("Apple")
blockchain.append("Orange")
blockchain.append("Banana")

blockchain.traverse()
