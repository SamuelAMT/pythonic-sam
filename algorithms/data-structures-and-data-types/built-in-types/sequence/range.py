# range

"""
The range type represents an immutable sequence of numbers and is commonly used for
looping a specific number of times in for loops.
"""

# Note: Using list(range(...)) defeats range's memory efficiency by materializing all elements as a list.

# Empty range: start=0, stop=0 → no elements
range_1 = range(0)
print(list(range_1))  # []

range_2 = range(5)
print(list(range_2))

range_3 = range(2, 7)
print(list(range_3))

range_4 = range(1, 10, 2)
print(list(range_4))

range_5 = range(10, 0, -2)
print(list(range_5))

range_6 = range(1_000_000_000) # This takes the same memory as range(10)
print(range_6[123456])  # Just-in-time access to an element

# It's printed as a list because range() expects integers, not an iterable.

"""
Ranges implement all of the common sequence operations except concatenation and repetition
(due to the fact that range objects can only represent sequences that follow a strict pattern
and repetition and concatenation will usually violate that pattern).
"""

"""
The advantage of the range type over a regular list or tuple is that
a range object will always take the same (small) amount of memory,
no matter the size of the range it represents
(as it only stores the start, stop and step values,calculating individual items and subranges as needed).
"""
