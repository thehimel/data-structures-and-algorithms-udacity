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


def test(text):
    if len(text) == 0:
        print("Text is empty. No need to encode or decode.")
        return

    print(f"Data: {text}")
    print(f"Data Size: {sys.getsizeof(text)}")

    encoded_data, tree = huffman_encoding(text)

    print(f"Encoded Data: {encoded_data}")
    print(f"Encoded Data Size: {sys.getsizeof(int(encoded_data, base=2))}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"Decoded Data: {decoded_data}")
    print(f"Decoded Data Size: {sys.getsizeof(decoded_data)}\n")


if __name__ == "__main__":
    text = "The bird is the word."
    test(text)

    text = "Python is beautiful."
    test(text)

    text = ""
    test(text)
