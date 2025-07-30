# memoryview

"""
Memoryview objects allow Python code to access the internal data of an object that supports
the buffer protocol without copying.
"""

"""
They are useful for efficiently slicing, modifying, or passing large binary data 
without creating new objects in memory.
"""

# Creating a memoryview from a bytes object (immutable)
bytes_obj = b"samuel"
memview_1 = memoryview(bytes_obj)
print(memview_1[0])

# Creating a memoryview from a bytearray (mutable)
bytearray_obj = bytearray(b"samuel")
memview_2 = memoryview(bytearray_obj)
memview_2[0] = ord('S')  # Modify the first byte via memoryview
print(bytearray_obj)

# Slicing a memoryview (no copy happens here)
memview_3 = memview_2[1:4]
print(memview_3.tobytes())

# Converting memoryview back to bytes
print(memview_2.tobytes())

# Getting information about the memory layout
print(memview_2.format)
print(memview_2.shape)

"""
Memoryview is especially useful for zero-copy access when working with large binary data,
such as files, images, sockets, or when integrating with low-level libraries or extensions.
"""
