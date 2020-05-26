"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but
never send texts, receive texts or receive incoming calls.

A possible approach could be create 4 different set namely,
calls_sent calls_received texts_sent texts_received. Fill the respective sets.
Finally to get the possible telemarketers.

telemarketers = calls_sent - calls_received - texts_sent - texts_received

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic
order with no duplicates.
"""

# Solution
"""
Logic: for each call in calls add the caller in the telemarketers list, and
remove the receiver from the telemarketers list if exists.

for each text in texts remove sender and receiver fromthe telemarketers list
if exist.
"""


def remove_telemarketers(telemarketers, number):
    if number in telemarketers:
        telemarketers.remove(number)


def main():
    telemarketers = []

    for call in calls:
        caller = call[0]
        receiver = call[1]
        if caller not in telemarketers:
            telemarketers.append(caller)
        remove_telemarketers(telemarketers, receiver)

    for text in texts:
        sender = text[0]
        receiver = text[1]
        remove_telemarketers(telemarketers, sender)
        remove_telemarketers(telemarketers, receiver)

    telemarketers = sorted(telemarketers)
    for telemarketer in telemarketers:
        print(telemarketer)


if __name__ == '__main__':
    main()

"""
TC: O(n^2)
SC: O(n) | Reason: texts and calls list
"""
