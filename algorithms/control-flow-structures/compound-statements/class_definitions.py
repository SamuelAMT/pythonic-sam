# class_definitions

"""
Class definitions in Python use the class keyword to create new user-defined types.
A class can contain methods, attributes, and special functions like __init__.
They support inheritance, encapsulation, and polymorphism.
"""

# Basic class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

p = Person("Samuel", 29)
print(p.greet())


# Class with class and static methods
class Math:
    PI = 3.14159

    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius ** 2

    @staticmethod
    def add(x, y):
        return x + y

print(Math.circle_area(5))
print(Math.add(2, 3))


# Inheritance
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())
