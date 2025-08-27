"""
Implementing fixed-sized stack with "static" array
Of course in Python lists are dynamic arrays but you might simulate the fixed size array.
"""

from typing import TypeVar

from src.linear_container import LinearContainer

T = TypeVar("T")


class ArrayStack[T](LinearContainer[T]):
    DEFAULT_FULL_CONTAINER_MSG = "Stack is full!"
    DEFAULT_EMPTY_CONTAINER_MSG = "Stack is empty!"

    def push(self, item: T) -> None:
        super().insert(item)

    def pop(self) -> T:
        if self._count == 0:
            raise ValueError("Empty stack!")

        val = self._data[self._rear - 1]
        assert val is not None

        self._data[self._rear - 1] = None
        self._rear -= 1
        self._count -= 1
        return val
