# type parameter lists

"""
Type parameter lists allow defining generics directly in function, class, and
type alias declarations. They enhance type safety and reusability across different types.
"""

from typing import TypeVar, Generic, Callable

# --------------------------------------------------
# Generic Function
# --------------------------------------------------

T = TypeVar("T")

# Type parameter directly in function definition
def identity[T](value: T) -> T:
    return value

print(identity(42))
print(identity("hello"))


# --------------------------------------------------
# Generic Class
# --------------------------------------------------

U = TypeVar("U")

class Box[U]:
    def __init__(self, content: U):
        self.content = content

    def get(self) -> U:
        return self.content

int_box = Box(123)
str_box = Box("abc")

print(int_box.get())
print(str_box.get())


# --------------------------------------------------
# Generic Type Alias
# --------------------------------------------------

V = TypeVar("V")

type Mapper[V] = Callable[[V], V]  # Alias for a function that maps a value to itself

def square(x: int) -> int:
    return x * x

def echo(x: str) -> str:
    return x

int_mapper: Mapper[int] = square
str_mapper: Mapper[str] = echo

print(int_mapper(4))
print(str_mapper("ok"))
