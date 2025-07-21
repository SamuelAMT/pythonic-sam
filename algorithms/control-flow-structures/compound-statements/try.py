# try (Statement)

"""
The try statement defines a block where exceptions may occur.
It allows handling errors with except, clean up with finally,
and optionally use else or except* for advanced cases.
"""

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero") # basic try-except block


try:
    value = int("abc")
except ValueError:
    print("Invalid number")
except TypeError:
    print("Wrong type") # try-except with multiple exceptions


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", result) # try-except with else clause, executes if no exception occurs


try:
    print("Running")
    x = 1 / 1
except:
    print("Error")
finally:
    print("Always runs") # try-except with finally clause, always executes after try block


# except (Clause)

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


# except* (Clause) (Python 3.11+)
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


# else (Clause)

"""
The optional else clause is executed if the control flow leaves the try suite,
no exception was raised, and no return, continue, or break statement was executed.
"""

try:
    value = int("10")
except ValueError:
    print("Invalid input")
else:
    print("Conversion successful:", value) # try-except with else clause


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Success")  # try-except with else clause, executes if no exception occurs


try:
    user = {"name": "Samuel"}
    name = user["name"]
except KeyError:
    print("Missing name")
else:
    print("Hello,", name) # try-except with else clause, executes when successful


# finally (Clause)

"""
The finally clause is always executed at the end of a try statement.
It is used to perform cleanup actions regardless of success or failure.
"""

try:
    print("No error here")
finally:
    print("This always runs") # try-finally block


try:
    1 / 0
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Still runs the finally block") # try-except-finally block


try:
    file = open("temp.txt", "w")
    file.write("Hello")
except IOError:
    print("Failed to write")
finally:
    file.close()
    print("File closed") # try-except-finally block with file handling
