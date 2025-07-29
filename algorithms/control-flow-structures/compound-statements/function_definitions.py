# function definitions

"""
Function definitions in Python use the def keyword to create reusable blocks of code.
They can accept parameters, return values, and include optional annotations for types.
Functions can also be nested or defined using async def for asynchronous operations.
"""

# Basic function definition
def greet(name):
    return f"Hello, {name}!"

print(greet("Samuel"))


# Function with type annotations
def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))


# Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))


# Function with *args and **kwargs
def describe(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

describe(1, 2, 3, name="Alice", age=30)


# Nested function
def outer():
    def inner():
        return "Inner!"
    return inner()

print(outer())
