"""
Time complexities:
Insert: O(1)
Search: O(1)
Delete: O(1)

Note: We need to travers the linked list inside every bucket and
in worst case, the traversal through the linked list takes O(n) time.
But the highest size of the linked list for each bucket = n/b.
Here, bucket size = b and total number of elements in the bucket = n.
So, the TC for the traversal becomes O(n/b). But still, for b << n,
it becomes O(n). But the aim of the hashmap is to keep the TC O(1).
Rather, for the most part, we can safely assume that
the time complexity of put and get operations will be O(1).

For detailed time complexity, review the jupyter notebook file.

Abbreviation:
(key: value) pair = KV pair

A KV pair comes.
From the key, with the help of the hash function, we calculate
the bucket_index in the bucket_array and put that KV pair on that bucket_index.
So, TC for get and set becomes O(1) for the simple array set and get operation.
Elements in the bucket_index are kept as Node of key and value.

Inside the hash funtion, we compress the values with value % bucket_size
so that the bucket_index doesn't go beyond the bucket_size. Logic: m % n < n
Example: 5 % 2 = 1, 6 % 2 = 0, 3 % 2 = 1
Note: While rehashing, bucket_size is increased. Thus, for each element,
we need to calculate the new bucket_index to put it in the new bucket_array.

Same bucket_index may come for multiple KV pair. For that reason,
every bucket is a linked list and for multiple elements with same index,
we add the element to that linked list.


Imagine a real world bucket, and you are allowed to fill water upto the 70%
of the bucket. After 70% is filled, if some new water comes, we'll take a new
bucket with the more size than the present bucket. Eg. double the size.

Now, come back to the concept.
Let bucket size = b and total number of elements in the bucket = n.
Then n/b is called the load factor. We will fill the bucket_array upto 70%.
That means our load factor is 0.7 and if for any new entry the load factor
increases, we'll increase the size of the bucket_array and move the elements
from the present bucket to the new bucket and it is called rehashing.
"""


class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, initial_size=15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry
        #   and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  # compress coefficient
        return hash_code % num_buckets  # one last compression before returning

    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)  # we can use our put() method to rehash
                head = head.next

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next

        return output


# Check the bucket_index for 2 different strings
# made with same set of characters
hash_map = HashMap()

bucket_index = hash_map.get_bucket_index("one")
print(bucket_index)

bucket_index = hash_map.get_bucket_index("neo")
print(bucket_index)  # Collision might occur


# Test Rehashing
# We have reduced the size of the hashmap array
#   to increase the load factor (> 0.7)
# and hence trigger the rehash() function
hash_map = HashMap(5)

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))
print()

hash_map  # call to the helper function to see the hashmap

# Test delete operation
hash_map = HashMap(7)

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))
hash_map  # call to the helper function to see the hashmap


hash_map.delete("one")
hash_map  # call to the helper function to see the hashmap

print(hash_map.get("one"))
print(hash_map.size())
