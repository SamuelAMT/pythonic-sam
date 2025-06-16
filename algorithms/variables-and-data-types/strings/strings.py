# str
a, b = "A String", 'doesn\'t care much about single or double quotes'
print(a, b)
c = '"This is quoted by double quotes wrapped by single quotes"'
print(c)
d = "They said, \"yes\"!"
print(d)

"""
To avoid characters prefaced by \ to be interpreted as special characters,
we can use raw strings by adding an r before the first quote:
"""
e = 'C:\sam\name'
print(e)
f = r'C:\sam\name'
print(f)
g, h = "Sam", " Miranda"
print(g + h)

i = "SamuelMiranda"
print(i[0:3])
print(i[-7:])
print(f"The length of my name and last name without space is {len(i)}")