"""
Implementing fixed-sized queue with "static" array
Of course in Python lists are dynamic arrays but you might simulate the fixed size array.
"""
from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


class ArrayQueue[T]:
    DEFAULT_CAP = 5

    def __init__(self, capacity: int = DEFAULT_CAP) -> None:
        self._data: list[T | None] = [None] * capacity
        self._capacity = capacity
        self._count = 0
        self._front = 0
        self._rear = 0

    @property
    def data(self) -> list[T | None]:
        return self._data

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def count(self) -> int:
        return self._count

    def enqueue(self, item: T) -> None:
        if self._count == self._capacity:
            raise ValueError("Queue is full!")
        self._data[self._rear % self._capacity] = item
        self._rear += 1
        self._count += 1

    def top(self) -> T:
        if self._count == 0:
            raise ValueError("Empty queue!")

        ret = self._data[self._front % self._capacity]
        assert ret is not None

        return ret

    def pop(self) -> T:
        if self._count == 0:
            raise ValueError("Empty queue!")

        val = self._data[self._front % self._capacity]
        assert val is not None

        self._data[self._front % self._capacity] = None
        self._front += 1
        self._count -= 1
        return val

    def traverse(self) -> Iterator[T]:
        for item in range(self._front, self._rear):
            if (val := self._data[item % self._capacity]) is not None:
                yield val
