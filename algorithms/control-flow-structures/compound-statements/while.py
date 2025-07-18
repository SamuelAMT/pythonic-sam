# while

"""
The while statement repeats a block of code while a condition remains true.
"""

count = 0

while count < 3:
    print("Counting:", count)
    count += 1 # basic while loop with counter


n = 0

while True:
    if n == 3:
        break
    print(n)
    n += 1 # while loop with break condition


x = 0

while x < 5:
    x += 1
    if x == 3:
        continue
    print(x) # while loop with continue condition


password = ""

while password != "1234":
    password = input("Enter password: ")

print("Access granted") # while loop with user input condition, dynamic condition


x = 0

while x < 3:
    print(x)
    x += 1
else:
    print("Finished normally") # while loop with else clause, executes after loop completes without break
