# yield

"""
The yield statement can be used to omit the parentheses that would otherwise
be required in the equivalent yield expression statement.
Used to produce values one at a time in a generator function.
"""

def yield_count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in yield_count_up_to(5):
    print(number)

def yield_even_numbers_up_to(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print(list(yield_even_numbers_up_to(11)))
