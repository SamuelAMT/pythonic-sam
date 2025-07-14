# Bytearray Objects

"""
bytearray objects are a mutable counterpart to bytes objects.
"""

bytearray_1 = bytearray() # empty bytearray
bytearray_2 = bytearray(10) # bytearray of size 10, initialized with zeroes
bytearray_3 = bytearray(range(20)) # bytearray from an iterable, each element is a byte
bytearray_4 = bytearray(b'samuel') # bytearray from bytes object

"""
Bytearray objects can be modified in place, allowing for changes to individual bytes.
They are useful when needed a mutable sequence of bytes, such as when working with binary data
"""

bytearray_5 = bytearray(b'samuel')
bytearray_5[0] = 83  # Change the first byte to 'S'
print(bytearray_5)
