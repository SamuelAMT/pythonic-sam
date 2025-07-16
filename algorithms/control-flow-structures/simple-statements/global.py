# global

"""
The global statement declares a variable as global,
allowing it to be accessed and modified across different scopes.
"""

def global_variable_example():
    global global_var
    global_var = "I am a global variable"
    print(global_var)

def access_global_variable():
    print("Accessing global variable:", global_var)

def modify_global_variable():
    global global_var
    global_var = "Global variable modified"
    print("Modified global variable:", global_var)

global_var = "Initial global variable"
global_variable_example()  # Declare and initialize global variable
access_global_variable()  # Access global variable
modify_global_variable()  # Modify global variable
access_global_variable()  # Access modified global variable
