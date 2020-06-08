# https://youtu.be/buWXDMbY3Ww
# https://en.wikipedia.org/wiki/Tower_of_Hanoi


def move(n, source, destination, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, destination)  # sad

        # Move the nth disk from source to destination
        destination.append(source.pop())

        # Display our progress
        print(S, D, A, '---------', sep='\n')

        # Move the n - 1 disks that we left on auxiliary onto destination
        move(n - 1, auxiliary, destination, source)  # ads


S = [3, 2, 1]
D = []
A = []
# Initiate call from source A to destination C with auxiliary B
move(3, S, D, A)
