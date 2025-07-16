# import

"""
The import statement imports modules or functions from other files.
It allows the user to use code defined elsewhere, promoting code reuse and organization.
"""

# Import entire module
import math
print(math.sqrt(16))
print(math.pi)

# Import specific functions from a module
from random import randint, choice
print(randint(1, 10))
print(choice(['apple', 'banana', 'cherry']))

# Import a module with an alias
import datetime as dt
now = dt.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Import all from a module (not recommended)
from os import *
print(getcwd())

# Importing from a custom module (assuming utils.py exists)
#from utils import explicit_return_function
#print(explicit_return_function(5, 10))

# Future imports (not applicable in this context)
# from __future__ import annotations  # For type hinting in future versions of Python
# Importing a module conditionally
