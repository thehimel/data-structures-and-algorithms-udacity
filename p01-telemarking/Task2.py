"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds,
on the phone during September 2016.".

In other words, find the total time a number spent on phone,
to calculate this you need to sum all call time for each number
(E.g. "78298 91466" has called 21 times during September 2016,
so you need to sum all the 3 call times and store it in some data structure.)
and then you need to find the maximum out of these.

Also you need to update the receiver time also as both the caller and
the receiver were on phone on each call.
"""
# Dictionary of all unique telephone numbers with duration.
"""
callDuration = {
    '78130 00821': '186'
    '98453 94494': '186'
    '78298 91466': '2093'
    '(022)28952819': '2093'
}
"""
callDuration = {}


def addToCallDuration(number, duration):
    if number in callDuration:
        callDuration[number] += duration
    else:
        callDuration[number] = duration
    return callDuration[number]


def main():
    # Take the 1st element to this variable
    maxCallNumber = [calls[0][0], int(calls[0][3])]

    for call in calls:
        caller = call[0]
        receiver = call[1]
        duration = int(call[3])

        callerDuration = addToCallDuration(caller, duration)
        if maxCallNumber[1] < callerDuration:
            maxCallNumber = [caller, callerDuration]

        receiverDuration = addToCallDuration(receiver, duration)
        if maxCallNumber[1] < receiverDuration:
            maxCallNumber = [receiver, receiverDuration]

    # print(callDuration)
    print(f'{maxCallNumber[0]} spent the longest time, {maxCallNumber[1]} seconds, on the phone during September 2016.')


if __name__ == '__main__':
    main()

"""
TC: O(n^2) | Reason: Inside the for loop there is a search operation
SC: O(n) | Reason: texts and calls list
"""
