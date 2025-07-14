# list

"""Lists are mutable sequences, typically used to store collections of homogeneous items"""

"""
Lexical (lexicographic) comparison compares sequences element by element, in order.
Two sequences are equal if they have the same type, same length, and all corresponding elements are equal.
If elements differ, the comparison result is based on the first unequal pair.
"""

"""
Forward and reversed iterators over mutable sequences use indexing to access elements.
They continue iterating even if the sequence is modified, stopping only on IndexError or StopIteration.
An IndexError occurs if the index moves outside the bounds of the sequence.
"""

list_1 = [] # empty list
list_2 = [1, 2, 3] # traditional list with integers
list_3 = [x for x in range(10)] # list comprehension
list_4 = list("Hello") # list from string, each character is an element
print(list_3)

"""Both sorting approaches use Timsort under the hood"""
list_5 = sorted([5, 4, 3, 2, 1]) # sorted list, returns a new sorted list
print(list_5)

list_6 = sorted([5, 4, 3, 2, 1], key=None, reverse=False) # it's the same as above, but with explicit parameters
print(list_6)

list_7 = [5, 1, 24, 6, 7, 6]
list_7.sort() # sorts the list in place

"""
Differences between sorted and sort:
- `sorted()` returns a new sorted list, leaving the original list unchanged.
- `sort()` sorts the list in place and returns None.
- `sorted()` can be used on any iterable, while `sort()` is a method of list objects.
"""

"""Lists implement all of the common and mutable sequence operations + sort method."""
