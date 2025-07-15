# raise

"""
The raise statement throws an exception to signal an error.
It can raise built-in or custom exceptions.
Used in error handling or to enforce program constraints.
"""

def raise_division_exception(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

print(raise_division_exception(10, 2))
print(raise_division_exception(10, 0))  # Raises ZeroDivisionError

def raise_set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")

raise_set_age(25)
raise_set_age(-3)   # Raises ValueError

try:
    int("abc")
except ValueError:
    print("Conversion failed")
    raise  # Re-raises the same ValueError


class CustomError(Exception):
    pass

def raise_trigger():
    raise CustomError("Something went wrong")

raise_trigger()  # Raises CustomError
