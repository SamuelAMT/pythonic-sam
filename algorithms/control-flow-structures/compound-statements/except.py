# except

"""
The except block is used to handle individual exceptions raised in a try block.
The except* block, introduced in Python 3.11, handles exception groups in parallel contexts.
Both allow graceful error handling and recovery.
"""

try:
    value = int("abc")
except ValueError:
    print("Cannot convert string to int") # except block handling a specific exception


try:
    result = 10 / int("zero")
except (ValueError, ZeroDivisionError):
    print("Invalid operation") # except block handling a tuple of exceptions


try:
    x = int("abc")
except ValueError as e:
    print("Error message:", str(e)) # except block using as alias


# except* (Python 3.11+)
try:
    raise ExceptionGroup("Multiple errors", [ValueError("Invalid"), TypeError("Wrong type")])
except* ValueError as ve:
    print("Caught ValueError(s):", ve)
except* TypeError as te:
    print("Caught TypeError(s):", te) # except* block with ExceptionGroup


def throw_errors():
    raise ExceptionGroup("Errors", [
        ValueError("Missing value"),
        ValueError("Negative number"),
        RuntimeError("Unknown error")
    ])

try:
    throw_errors()
except* ValueError as e:
    print("Handled ValueErrors:", e)
except* BaseException as e:
    print("Other unhandled errors:", e) # except* block handling multiple exceptions in parallel contexts

"""
exception* requires ExceptionGroup, specially used in async concurrent programming with
asyncio, threading, taskgroups, etc.
The except* block is evaluated in parallel, differently from traditional except block.
"""
