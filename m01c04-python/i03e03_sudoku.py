correct = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]]

incorrect = [
    [1, 2, 3, 4],
    [2, 3, 1, 3],
    [3, 1, 2, 3],
    [4, 4, 4, 4]]

incorrect2 = [
    [1, 2, 3, 4],
    [2, 3, 1, 4],
    [4, 1, 2, 3],
    [3, 4, 1, 2]]

incorrect3 = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2]]

incorrect4 = [
    ['a', 'b', 'c'],
    ['b', 'c', 'a'],
    ['c', 'a', 'b']]

incorrect5 = [
    [1, 1.5],
    [1.5, 1]]


# Define a function check_sudoku() here:
def check_sudoku(square):
    # Horizontal checking
    # Create a list with the integers 1, 2, ..., n.
    # We will check that each number in the row is in the list
    # and remove the numbers from the list once they are verified
    # to ensure that each number only occurs once in the row.
    for row in square:
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i in check_list:
                check_list.remove(i)
            else:
                return False

    # Vertical checking
    # n goes from 0 to len and for every row, row[n] is checked
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] in check_list:
                check_list.remove(row[n])
            else:
                return False

    return True


print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False
