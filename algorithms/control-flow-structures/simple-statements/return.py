# return

"""The return statement exits the current function and returns a value.
It can return any expression or None if omitted.
"""

def explicit_return_function(a, b):
    return a + b

print(explicit_return_function(10.2, 20.3)) # explicit return

def implicit_return_function():
    print("Hello!")

result = implicit_return_function()
print(result)  # implicit return, result is None

def early_return_function(c):
    if c < 0:
        return "Negative value"
    return "Non-negative value"

print(early_return_function(7))
print(early_return_function(-3))  # early return

def testing_return_fuction(d, e):
    f = d * e
    return f

print(testing_return_fuction(5, 6))

def less_lines_return_function(g, h):
    return g + h

i = less_lines_return_function(3, 4)
print(less_lines_return_function(7, 10))
