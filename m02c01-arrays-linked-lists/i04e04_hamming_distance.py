"""
Exercise 4. Hamming Distance
In information theory, the Hamming distance between two strings of equal length
is the number of positions at which the corresponding symbols are different.
Calculate the Hamming distace for the following test cases.


Calculate the hamming distance of the two strings
Args:
    str1(string),str2(string): Strings to be used
        for finding the hamming distance
Returns:
    int: Hamming Distance
"""


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return None

    count = 0
    for char in range(len(str1)):
        if str1[char] != str2[char]:
            count += 1

    return count


def test(str1, str2, output):
    print("Pass" if hamming_distance(str1, str2) == output else "Fail")


test('0000', '1111', 4)
test('0101', '0000', 2)
test('ACTTGACCGGG', 'GATCCGGTACA', 10)
test('shove', 'stove', 1)
test('Slot machines', 'Cash lost in me', None)
test('A gentleman', 'Elegant men', 9)
test('0101010100011101', '0101010100010001', 2)
