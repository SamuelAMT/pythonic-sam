# nonlocal

"""
The nonlocal statement allows the user to assign a value to a variable in an enclosing scope (not global).
It is used to work with variables in nested functions,
allowing modification of variables in the nearest enclosing scope that is not global.
"""

def outer_function():
    nonlocal_var = "I am a nonlocal variable"

    def inner_function():
        nonlocal nonlocal_var
        nonlocal_var = "Nonlocal variable modified"
        print("Inner function:", nonlocal_var)

    print("Before inner function:", nonlocal_var)
    inner_function()
    print("After inner function:", nonlocal_var)

outer_function()

def nested_function_example():
    outer_var = "Outer variable"

    def inner_function():
        nonlocal outer_var
        outer_var = "Modified outer variable"
        print("Inner function:", outer_var)

    print("Before inner function:", outer_var)
    inner_function()
    print("After inner function:", outer_var)

nested_function_example()
