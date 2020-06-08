# Udacity Solution
def tower_of_Hanoi_soln(num_disks, source, destination, auxiliary):

    if num_disks == 0:
        return

    if num_disks == 1:
        print(f'{source} {destination}')
        return

    tower_of_Hanoi_soln(num_disks - 1, source, auxiliary, destination)
    print(f'{source} {destination}')
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, destination, source)


def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'D', 'A')
    print('-----------')


tower_of_Hanoi(2)
tower_of_Hanoi(3)
tower_of_Hanoi(4)
