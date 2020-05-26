# Example function 1: return the sum of two numbers.
def sum(a, b):
    return a+b


print(sum(2, 3))


# Example function 2: return the size of list,
# and modify the list to now be sorted.
def list_sort(my_list):
    my_list.sort()
    return len(my_list), my_list


print(list_sort([9, 4, 3]))
