# match

"""
The match statement is used for pattern matching.
Pattern matching takes a pattern as input and a subject value.
The pattern (which may contain subpatterns) is matched against the subject value.
"""

# --------------------------------------------
# Match Statement Overview
# --------------------------------------------

value = 2

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Default")


# --------------------------------------------
# Guards
# --------------------------------------------

user = {"name": "Alice", "age": 17}

match user:
    case {"name": name, "age": age} if age >= 18:
        print(f"{name} is an adult")
    case {"name": name, "age": age}:
        print(f"{name} is underage")


# --------------------------------------------
# Irrefutable Case Blocks
# --------------------------------------------

value = (10, 20)

match value:
    case (x, y):  # This pattern always matches
        print(f"Always matches: {x=}, {y=}")


# --------------------------------------------
# OR Patterns
# --------------------------------------------

animal = "cat"

match animal:
    case "dog" | "cat":
        print("It is a pet")
    case _:
        print("Unknown animal")


# --------------------------------------------
# AS Patterns
# --------------------------------------------

point = (1, 2)

match point:
    case (x, y) as p:
        print(f"x={x}, y={y}, full point={p}")


# --------------------------------------------
# Literal Patterns
# --------------------------------------------

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")


# --------------------------------------------
# Capture Patterns
# --------------------------------------------

data = [1, 2, 3]

match data:
    case x:
        print(f"Captured: {x}")  # Captures the whole list


# --------------------------------------------
# Wildcard Patterns
# --------------------------------------------

def handle(value):
    match value:
        case 1:
            print("One")
        case _:
            print("Anything else")  # Used when the value doesn't care about specific cases

handle(99)


# --------------------------------------------
# Value Patterns
# --------------------------------------------

status = 200

match status:
    case 404:
        print("Not Found")
    case 200:
        print("OK")  # This will run


# --------------------------------------------
# Group Patterns
# --------------------------------------------

pair = (0, 1)

match pair:
    case ((0, x) | (x, 0)):
        print(f"One item is zero: {x}")  # Pattern grouped using | and ()


# --------------------------------------------
# Sequence Patterns
# --------------------------------------------

elements = [1, 2, 3]

match elements:
    case [1, x, 3]:
        print(f"Middle element is {x}")  # Matches
    case _:
        print("No match")


# --------------------------------------------
# Mapping Patterns
# --------------------------------------------

config = {"debug": True, "port": 8000}

match config:
    case {"debug": True}:
        print("Debug mode enabled")  # Matches
    case _:
        print("Default config")


# --------------------------------------------
# Class Patterns
# --------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(3, 4)

match pt:
    case Point(x=3, y=y_val):
        print(f"Point with x=3 and y={y_val}")  # Matches
    case _:
        print("No match")
