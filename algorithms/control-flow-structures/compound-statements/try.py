# try

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


