"""
Implementing fixed-sized queue with "static" array
Of course in Python lists are dynamic arrays but you might simulate the fixed size array.
"""
from collections.abc import Iterator
from typing import TypeVar

from src.linear_container import LinearContainer

T = TypeVar("T")


class ArrayQueue(LinearContainer[T]):
    DEFAULT_CAP = 5
    DEFAULT_FULL_CONTAINER_MSG = "Queue is full!"
    DEFAULT_EMPTY_CONTAINER_MSG = "Queue is empty!"

    def __init__(self, capacity: int = DEFAULT_CAP) -> None:
        self._front = 0
        super().__init__(capacity)

    def enqueue(self, item: T) -> None:
        super().insert(item)

    def pop(self) -> T:
        if self._count == 0:
            raise ValueError("Empty queue!")

        val = self._data[self._front % self._capacity]
        assert val is not None

        self._data[self._front % self._capacity] = None
        self._front += 1
        self._count -= 1
        return val
