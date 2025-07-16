# type

"""
Introduced in Python 3.12, the type statement defines a new structured type.
It provides a concise way to declare fields and create objects with named attributes.
"""

# Creating a simple type
type Point:
    x: int
    y: int

p = Point(x=1, y=2)
print(p.x, p.y)

# Accessing attributes
type User:
    name: str
    age: int

u = User(name="Alice", age=30)
print(u.name.upper())

"""
Requires Python 3.12+
"""