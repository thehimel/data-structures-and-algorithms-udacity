"""
Problem Statement
Design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used
entry when the cache memory reaches its limit. For the current problem,
consider both get and set operations as a use operation.

While doing the get() operation, if the entry is found in the cache,
it is known as a cache hit. If, however, the entry is not found,
it is known as a cache miss.

Your job is to use an appropriate data structure(s) to implement the cache.
- In case of a cache hit, your get() operation should return the value.
- In case of a cache miss, your get() should return -1.
- While putting an element in the cache, your put() / set() operation
    must insert the element. If the cache is full, you must write code
    that removes the least recently used entry first
    and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Solution Logic:
Use python ordered dictionary which works as map data structure
to keep the (key, value) pair in the cache.

Maintain a variable to keep track of the last key.
If the max cache size is reached, pop that key from the cache.

Solution Time Complexity:
Set: O(1)
Get: O(1)
Pop: O(1)

Reason: Set, get, and pop operations in python dictionary takes constant time.
During the removal of the oldest key, we are just performing the pop operation.
"""


import collections


class LRU_Cache(object):
    # Initialize class variables
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.cache_size = 0
        self.max_cache_size = 5
        self.lru_key = None

    # Retrieve item from provided key. Return -1 if nonexistent.
    def get(self, key):
        if key in self.cache:
            # Update the LRU Key
            self.lru_key = self.cache[key]
            return self.cache[key]
        return -1

    def set(self, key, value):
        # If the cache is at capacity remove the oldest item.
        if self.cache_size == self.max_cache_size:
            # print(f'Cache size over. Removing last recently used cache.')
            self.cache.pop(self.lru_key)
            self.cache_size -= 1

        # Update the value if the key is present in the cache.
        if key in self.cache:
            self.cache[key] = value
            self.lru_key = key
            # print(f'Overwritten {key}')

        # Set the value if the key is not present in the cache.
        else:
            self.cache[key] = value
            self.cache_size += 1
            self.lru_key = key
            # print(f'size = {self.cache_size}')

    def __str__(self):
        out_string = ''
        for key in self.cache:
            out_string += str(key) + '->'
        out_string += 'End'

        return out_string

    def get_lru_key(self):
        return self.lru_key


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache)
print(f'LRU Key: {our_cache.get_lru_key()}')

print(our_cache.get(1))  # returns 1
print(f'LRU Key: {our_cache.get_lru_key()}')

print(our_cache.get(2))  # returns 2
print(f'LRU Key: {our_cache.get_lru_key()}')

print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
print(f'LRU Key: {our_cache.get_lru_key()}')

our_cache.set(5, 5)
print(our_cache.get(5))
print(f'LRU Key: {our_cache.get_lru_key()}')

our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity
# and 5 was the least recently used entry
print(our_cache.get(5))
print(f'LRU Key: {our_cache.get_lru_key()}')

print(our_cache.get(6))
print(our_cache)
print(f'LRU Key: {our_cache.get_lru_key()}')

our_cache.set(0, 0)
print(our_cache)
print(f'LRU Key: {our_cache.get_lru_key()}')

our_cache.set(-1, -1)
print(our_cache)
print(f'LRU Key: {our_cache.get_lru_key()}')
