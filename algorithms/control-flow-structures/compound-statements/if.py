# if

"""
The if statement allows conditional execution of code blocks.
It runs only if the given condition is true.
Often used with `elif` and `else` to handle multiple paths.
"""

x = 10

if x > 5:
    print("x is greater than 5") # basic if statement


age = 17

if age >= 18:
    print("Adult")
else:
    print("Minor") # classic if-else statement


temperature = 25

if temperature > 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold") # classic if-elif-else statement


is_logged_in = True

if is_logged_in:
    print("Welcome!") # if statement with a boolean condition


x = 15

if x > 10:
    if x < 20:
        print("x is between 10 and 20") # nested if statement


x = 15

if x > 10:
    if x < 20:
        print("x is between 10 and 20") # if statement with logical operators
