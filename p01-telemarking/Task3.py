"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# Task A
def getCodeFromTelemarketer(number):
    if number[0:3] == '140':
        return '140'


def getCodeFromMobile(number):
    if '(' not in number:
        return number[0:4]


"""
Bug in the regex declaration of getCodeFromFixedLine(). If number is a
fixed line number like '(080)33118033', code = 080. But if number is a
telephone number like 78130 00821, code = 78130. If number = 7813000821,
code = 7813000821
"""


def getCodeFromFixedLine(number):
    return re.search(r"(\d+)", number).group(0)


def isBangalore(number):
    return getCodeFromFixedLine(number) == '080'


def getCode(number):
    code = getCodeFromTelemarketer(number)
    # if the number is not a telemarketer, code = None
    if not code:
        code = getCodeFromMobile(number)
        # if the number is not a mobile, code = None
        if not code:
            code = getCodeFromFixedLine(number)
    return code


"""
TestCalls = [
    ['0123 40118', '(080)33118033'],
    ['140 40118', '(080)33118033'],
    ['4567 40118', '(020)33118033'],
    ['(010101) 40118', '(080)33118033'],
    ['(020202) 40118', '(0820)33118033'],
]
"""
uniqueAreaCodes = []

for call in calls:
    caller = call[0]
    receiver = call[1]
    if isBangalore(receiver):
        code = getCode(caller)
        if code not in uniqueAreaCodes:
            uniqueAreaCodes.append(code)

uniqueAreaCodes = sorted(uniqueAreaCodes)
for code in uniqueAreaCodes:
    print(code)


"""
TC: O(n^2)
SC: O(n) | Reason: texts and calls list
"""


# Task B
def getPercentage(n, m):
    return n/m*100


totalCalls = 0
callsInBangalore = 0

for call in calls:
    caller = call[0]
    receiver = call[1]
    if isBangalore(caller):
        totalCalls += 1
        if isBangalore(receiver):
            callsInBangalore += 1

# upto 2 decimal places
percentage = round(getPercentage(callsInBangalore, totalCalls), 2)
print(f'{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

"""
TC: O(n)
SC: O(n) | Reason: texts and calls list
"""
