"""
Complexity Analysis:
-------------------

Operation 1: Encoding
.....................
Time Complexity:
The binary tree creation takes O(log(n)) and the operation must be performed
n times. Thus the time complexity is O(nlog(n))

Space Complexity:
The space complexity is depended on the input size and it is lenear. Thus, O(n)

TC: O(nlog(n))
SC: O(n)

Operation 2: Decoding
.....................
Time Complexity:
The while loop is just to terminate the loop, and it's O(1)
For every character it's matching with the begining of the input which takes
O(n) and also slicing the input and that also takes O(n) for each operation.
Thus, overall O(n^2)

Space Complexity:
The space complexity is depended on the input size and it is lenear. Thus, O(n)

TC: O(n^2)
SC: O(n)
"""

import sys


# Creating tree nodes
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return f'{self.left}_{self.right}'


# Main function implementing huffman coding
def huffman_code_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (left, right) = node.children()
    d = dict()
    d.update(huffman_code_tree(left, binString + '0'))
    d.update(huffman_code_tree(right, binString + '1'))
    return d


def huffman_encoding(text):
    # Calculating frequency
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # If the text consists of only one type of letter, e.g. 'AAAAAA',
    # combining 2 nodes is not possible as there is only one node.
    # Thus, just create the huffman_dict manually, and it's very efficient.
    if len(freq) == 1:
        huffman_dict = {text[0]: '0'}

    else:
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        nodes = freq

        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

        huffman_dict = huffman_code_tree(nodes[0][0])

    # print(' Char | Huffman code ')
    # print('----------------------')
    # for (char, frequency) in freq:
    #     print(' %-4r |%12s' % (char, huffman_dict[char]))

    huffman_code = ''
    for char in text:
        huffman_code += huffman_dict[char]

    return huffman_code, huffman_dict


def huffman_decoding(huffman_code, dictionary):
    text = ''
    while len(huffman_code) > 0:
        for char in dictionary:
            char_code = dictionary[char]
            if huffman_code.startswith(char_code):
                text += char
                huffman_code = huffman_code[len(char_code):]
    return text


def test(data):
    if len(data) == 0:
        print("Data is empty. No need to encode or decode.")
        return

    print(f"Data: {data}")
    data_size = sys.getsizeof(data)
    print(f"Data Size: {data_size}")

    encoded_data, tree = huffman_encoding(data)
    encoded_data_size = sys.getsizeof(int(encoded_data, base=2))

    print(f"Encoded Data: {encoded_data}")
    print(f"Encoded Data Size: {encoded_data_size}")
    print(f'Size Reduced: {data_size - encoded_data_size}')

    decoded_data = huffman_decoding(encoded_data, tree)
    decoded_data_size = sys.getsizeof(decoded_data)

    print(f"Decoded Data: {decoded_data}")
    print(f"Decoded Data Size: {decoded_data_size}\n")


if __name__ == "__main__":
    data = "The bird is the word."
    test(data)

    text = "Python is beautiful."
    test(text)

    text = "AAAAAA"
    test(text)

    text = ""
    test(text)
