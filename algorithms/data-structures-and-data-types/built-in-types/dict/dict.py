# dict

"""
Dictionaries are mutable mappings of hashable keys to arbitrary values.
Keys must be unique and immutable (e.g., strings, numbers, tuples).
Values can be any object, mutable or immutable.
"""

dict_1 = {}  # empty dictionary
dict_2 = {"name": "Alice", "age": 30}  # traditional dictionary
dict_3 = dict(name="Bob", age=25)  # dict() constructor with keyword arguments
dict_4 = dict([(1, 'one'), (2, 'two')])  # from list of tuples
dict_5 = {x: x**2 for x in range(5)}  # dictionary comprehension
print(dict_5)

print(dict_2["name"])  # direct access by key
print(dict_2.get("age"))  # safe access using get()

dict_2["age"] = 31  # update existing key
dict_2["city"] = "São Paulo"  # add new key-value pair

del dict_2["name"]  # remove key-value by key
removed = dict_2.pop("city", None)  # remove with default if key is missing

print(list(dict_2.keys()))  # list of keys
print(list(dict_2.values()))  # list of values
print(list(dict_2.items()))  # list of (key, value) pairs

print("age" in dict_2)  # check if key exists
print("name" not in dict_2)

dict_6 = {"x": 1, "y": 2}
dict_7 = {"y": 3, "z": 4}
merged = dict_6 | dict_7  # dict_7 overwrites 'y'
print(merged) # merging dictionaries
