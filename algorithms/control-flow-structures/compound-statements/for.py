# for

"""
The for statement is used to iterate over the elements of a sequence
(such as a string, tuple or list) or other iterable object.
"""

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) # classic for loop iterating over a list


for i in range(20):
    print(i) # for loop using range to iterate over numbers


for i in range(3):
    if i == 3:
        break
    print(i) # for loop with break condition


for i in range(5):
    if i == 2:
        continue
    print(i) # for loop with continue condition


for i in range(10):
    print(i)
else:
    print("Loop ended normally") # for loop with else clause


person = {"name": "Samuel", "age": 21, "favorite_country_singer": "Merle Haggard"}

for key, value in person.items():
    print(f"{key}: {value}")
