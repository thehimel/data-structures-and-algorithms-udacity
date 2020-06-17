"""
Problem Statement
Given arrival and departure times of trains on a single day in a railway
station, find out the minimum number of platforms required so that no train
has to wait for the other(s) to leave. In other words, when a train is about
to arrive, at least one platform must be available to accommodate it.

You will be given arrival and departure times both in the form of a list.
The size of both the lists will be equal, with each common index representing
the same train. Note: Time hh:mm would be written as integer hhmm for e.g.
9:30 would be written as 930. Similarly, 13:45 would be given as 1345

Example:
Input: A schedule of 6 trains:

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
Expected output: Minimum number of platforms required = 3

The greedy approach:
Sort the schedule, and make sure when a train arrives or depart, keep track of
the required number of platforms. We will have iterator i and j traversing the
arrival and departure lists respectively. At any moment, the difference (i - j)
will provide us the required number of platforms.

At the time of either arrival or departure of a train, if i^th arrival is
scheduled before the j^th departure, increment the platform_required and i.
Otherwise, decrement platform_required count, and increase j.
Keep track of the max value of platform_required ever, as the expected result.

Complexity Analysis:
TC: O(n) + T(Python Sort: Tim Sort) => O(n) + O(nlogn) => O(nlogn)
TC: O(nlogn)
"""


def min_platforms(arrival, departure):
    # Mismatch in the length of the lists
    if(len(arrival) != len(departure)):
        return -1

    array_length = len(arrival)

    # Sort both the lists.
    arrival.sort()
    departure.sort()

    # Count of platforms required when comparing i^th arrival
    # and j^th departure
    platform_required = 1

    # Keep track of the max value of platform_required
    max_platform_required = 1

    # Iterate such that (i-j) will represent platform_required at that moment
    # Assume the first train has arrived
    i = 1
    j = 0

    # Traverse the arrival list with iterator `i`, and departure with `j`
    while i < array_length and j < array_length:

        # if i^th arrival is scheduled before than j^th departure,
        # increment platform_required and i as well.
        if arrival[i] < departure[j]:
            platform_required += 1
            i += 1

            # Update the max value of platform_required
            if platform_required > max_platform_required:
                max_platform_required = platform_required

        # Otherwise, decrement platform_required count, and increase j.
        else:
            platform_required -= 1
            j += 1

    return max_platform_required


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)
arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
