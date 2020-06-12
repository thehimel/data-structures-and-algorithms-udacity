from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray

text = "HAPPY HAPPY"

freq_lib = defaultdict(int)    # generate a default library
for ch in text:                # count each letter and record into the frequency library
    freq_lib[ch] += 1

print(freq_lib)

heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]  # '' is for entering the huffman code later
print(heap)

heapify(heap) # transform the list into a heap tree structure
print(heap)

while len(heap) > 1:
    right = heappop(heap)  # heappop - Pop and return the smallest item from the heap
    print('right = ', right)
    left = heappop(heap)
    print('left = ', left)

    for pair in right[1:]:
        pair[1] = '0' + pair[1]   # add zero to all the right note
    for pair in left[1:]:
        pair[1] = '1' + pair[1]   # add one to all the left note
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])  # add values onto the heap. Eg. h = []; heappush(h, (5, 'write code')) --> h = [(5, 'write code')]

huffman_list = right[1:] + left[1:]
print(huffman_list)
huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}
print(huffman_dict)


encoded_text = bitarray()
encoded_text.encode(huffman_dict, text)
print(encoded_text)

padding = 8 - (len(encoded_text) % 8)


decoded_text = bitarray()

decoded_text = encoded_text  # remove padding

decoded_text = decoded_text.decode(huffman_dict)
decoded_text = ''.join(decoded_text)

print(decoded_text)
