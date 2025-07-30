# set

"""
A set object is an unordered collection of distinct hashable objects.
Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations
such as intersection, union, difference, and symmetric difference.
"""

"""
Sets do not support indexing, slicing, or other sequence-like behavior.
The set type is mutable, the contents can be changed using methods like add() and remove().
"""

set_1 = {'samuel', 'miranda'} # set literal
print(set_1)

set_2 = {s for s in 'sam' if s not in 'uel'} # set comprehension
print(set_2)

set_3 = set() # set constructor
set_4 = set('samuel') # set constructor
set_5 = set([1, 2, 3, 4, 5]) # set constructor from a list

print(set_3, set_4, set_5, f'length: {len(set_5)}')

set_6 = {'google', 'microsoft', 'apple'}
set_7 = {"home depot", "lowe's", "walmart"}
set_8 = set.union(set_6, set_7)
print(set_8)

"""
Instances of set are compared to instances of frozenset based on their members.
For example, set('abc') == frozenset('abc') returns True and so does set('abc') in set([frozenset('abc')]).
"""

set_9 = {'money', 'talks'}
set_9.add('jewish') # This is not available in frozenset as it is immutable.
print(set_9)