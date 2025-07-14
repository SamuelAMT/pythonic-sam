# frozenset

"""
A set object is an unordered collection of distinct hashable objects.
Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations
such as intersection, union, difference, and symmetric difference.
"""

"""
Sets do not support indexing, slicing, or other sequence-like behavior.
The set type is mutable, the contents can be changed using methods like add() and remove().
"""

frozenset_1 = {'samuel', 'miranda'} # frozenset literal
print(frozenset_1)

frozenset_2 = {s for s in 'sam' if s not in 'uel'} # frozenset comprehension
print(frozenset_2)

frozenset_3 = frozenset() # frozenset constructor
frozenset_4 = frozenset('samuel') # frozenset constructor
frozenset_5 = frozenset([1, 2, 3, 4, 5]) # frozenset constructor from a list

print(frozenset_3, frozenset_4, frozenset_5, f'length: {len(frozenset_5)}')

frozenset_6 = {'google', 'microsoft', 'apple'}
frozenset_7 = {'home depot', 'lowe\'s', 'walmart'}
frozenset_8 = frozenset.union(frozenset(frozenset_6), frozenset(frozenset_7))
print(f'union: {frozenset_8}, type: {(type(frozenset_8))}')

"""
Instances of set are compared to instances of frozenset based on their members.
For example, set('abc') == frozenset('abc') returns True and so does set('abc') in set([frozenset('abc')]).
"""
