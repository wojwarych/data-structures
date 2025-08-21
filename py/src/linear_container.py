from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


class LinearContainer[T]:
    DEFAULT_CAP = 5
    DEFAULT_FULL_CONTAINER_MSG = "The container is full!"
    DEFAULT_EMPTY_CONTAINER_MSG = "Then container is empty!"

    def __init__(self, capacity: int = DEFAULT_CAP) -> None:
        self._data: list[T | None] = [None] * capacity
        self._capacity = capacity
        self._count = 0
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

    def top(self) -> T:
        if self._count == 0:
            raise ValueError(self.DEFAULT_EMPTY_CONTAINER_MSG)

        if hasattr(self, "_front"):
            val = self._data[self._front % self._capacity]
        else:
            val = self._data[self._rear - 1]
        assert val is not None

        return val

    def insert(self, item: T) -> None:
        if self._count == self._capacity:
            raise ValueError(self.DEFAULT_FULL_CONTAINER_MSG)
        self._data[self._rear % self._capacity] = item
        self._rear += 1
        self._count += 1

    def traverse(self) -> Iterator[T]:
        if hasattr(self, "_front"):
            r = range(self._front, self._rear)
        else:
            r = range(self._rear)

        for item in r:
            if (val := self._data[item % self._capacity]) is not None:
                yield val
