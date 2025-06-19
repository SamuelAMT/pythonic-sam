# str

# String Methods
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

j = "spam" "across"
print(j)

"""
Strings support two styles of string formatting
1. One providing large degree of flexibility and customization;

2. The second based on C printf style formatting that handles a narrower
range of types and slightly harder to use correctly but is often faster.   
"""

k = "sam".capitalize()
print(k)

l = 'Python'.encode()
print(type(l))
print(l)

m = "The sum of 1 + 2 = {}".format(1+2)
print(m)

n = '123'.isdigit()
print(n)

o = 'Big'.islower()
print(o)

p = '123'.isnumeric()
print(p)

q = ' '.isspace()
print(q)

r = 'test'.join('123')
print(r)

s = 'AnyString'.lower()
print(s)

t = 'www.mysite.com'.lstrip('w.')
print(t)

u = 'www.mysitetwo.com'.removeprefix('www.')
print(u)

v = 'Sam'.replace('Sam', 'TheNewSam')
print(v)

w = 'Sam Came back, Again.'.split(sep=',', maxsplit=0)
print(w)

x = 'Goat'.startswith('Go')
print(x)

z = 'strING'.swapcase()
print(z)

aa = 'sam is SUCH a nice guy'.title()
print(aa)

ab = 'Sam_Strings'.upper()
print(ab)

# Formatted String Literals (f-strings)
"""
An f-string is a string literal that is prefixed with f or F.
This type of string allows embedding arbitrary Python expressions within
replacement fields, which are delimited by curly brackets ({}).

These expressions are evaluated at runtime, similarly to str.format(), and
are converted into regular str objects.
"""

who = 'nobody'
nationality = 'Brazilian'
print(f'{who.title()} expects the {nationality} Inquisition!')

ac = 42
print(f'{{x}} is {ac}!')

name = 'Samuel Miranda - às cão'
print(f'{name!a}')

ad = 'Sam'
print(f'Hi, welcome {ad}')

# printf-style String Formatting
"""
Basically old print, more like C style.
It's being replaced by f and .format
"""