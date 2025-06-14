# int - integer
from asyncio.windows_events import INFINITE

a = 1

# float - floating point
b = 2.0
c = 2.
d = -2.0
e = -2.
f = 0.0000000000000000000

# complex
g = 1 + 2j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# decimal
"""
From: https://docs.python.org/3/library/decimal.html#decimal.Decimal

• Decimal numbers can be represented exactly.
In contrast, numbers like 1.1 and 2.2 do not have exact representations in binary floating point.
End users typically would not expect 1.1 + 2.2 to display as 3.3000000000000003 as it does with binary floating point.

• The exactness carries over into arithmetic.
In decimal floating point, 0.1 + 0.1 + 0.1 - 0.3 is exactly equal to zero.
In binary floating point, the result is 5.5511151231257827e-017.
While near to zero, the differences prevent reliable equality testing and differences can accumulate.
For this reason, decimal is preferred in accounting applications which have strict equality invariants.
"""

# Equivalent of BigDecimal in Java
from decimal import Decimal

h = Decimal("3.45")
i = Decimal("5.67")
print(h + i)

j = Decimal('Infinity')
k = Decimal('Infinity')
l = (j + k)
print(l)

"""
If value is a tuple, it should have three components,
a sign (0 for positive or 1 for negative), a tuple of digits, and an integer exponent.
For example, Decimal((0, (1, 4, 1, 4), -3)) returns Decimal('1.414').

as_tuple() - Return a named tuple representation of the number: DecimalTuple(sign, digits, exponent).
"""

# fractions
from fractions import Fraction
m = Fraction(16, -10)
n = Fraction(123)
o = Fraction('3/7')
print(m)
print(n)

"""
class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(float)
class fractions.Fraction(decimal)
class fractions.Fraction(string)
"""
