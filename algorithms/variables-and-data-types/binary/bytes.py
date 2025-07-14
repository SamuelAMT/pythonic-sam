# Bytes Objects

"""
Bytes objects are immutable sequences of single bytes.
"""

"""
The syntax for bytes literals is largely the same as that for string literals,
except that a b prefix is added
"""
bytes_1 = b'samuel'
print(bytes_1)

bytes_2 = b"samuel double quotes"
print(bytes_2)

bytes_3 = b"""samuel triple quotes"""
print(bytes_3)

"""
Bytes Objects can make the same work that strings do, but with bytes instead of characters.
They share the same methods as strings, but they operate on bytes.
"""

bytes_5 = b'Samuel Miranda'.removeprefix(b"Samuel ")
print(bytes_5)