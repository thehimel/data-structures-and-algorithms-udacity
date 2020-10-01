def prod(a, b):
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output

        # Hint: i is a successive integer and n is the previous product
        n = output
        i += 1


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(f'{i}! = {next(my_gen)}')

# Correct result when num = 5:
# 0! = 1
# 1! = 2
# 2! = 6
# 3! = 24
# 4! = 120
