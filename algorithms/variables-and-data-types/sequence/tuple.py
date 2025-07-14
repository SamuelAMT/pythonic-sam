# tuple

tuple_1 = () # empty tuple
tuple_2 = (1, 2 , 3) # traditional tuple with integers
tuple_3 = tuple(x for x in range(10)) # tuple comprehension
tuple_4 = tuple("Hello") # tuple from string, each character is an element

tuple_5 = sorted((3, 6, 1, 8, 2))
print(tuple_5)

tuple_6 = (4, 7, 5, 1, 10)
tuple_6.sort()
print(tuple_6)  # This will raise an AttributeError because tuples do not have a sort method.

"""It's the comma, not the parentheses, that defines a tuple in Python."""
tuple_7 = 1,2,3
print(type(tuple_7))

"""Parentheses are useful when defining empty tuples or when grouping elements."""
tuple_8 = ()
tuple_9 = (1 + 2, 3 + 4) # tuple with expressions
print(type(tuple_9))

"""This also matters in function calls, where parentheses are used to group arguments."""
def show_person_info(first_name, last_name, age):
    print(f"Name: {first_name} {last_name}, Age: {age}")

# Passing 3 separate arguments
show_person_info("Samuel", "Miranda", 21)

def show_person_info_from_tuple(info_tuple):
    first_name, last_name, age = info_tuple
    print(f"Name: {first_name} {last_name}, Age: {age}")

# Passing 1 tuple with 3 elements
show_person_info_from_tuple(("Samuel", "Tavares", 21))

"""Tuples implement all of the common sequence operations."""
