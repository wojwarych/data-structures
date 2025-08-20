"""
Implementing fixed-sized queue with "static" array
Of course in Python lists are dynamic arrays but you might simulate the fixed size array.
"""
from typing import TypeVar

T = TypeVar("T")


class ArrayQueue:
    def __init__(self, capacity: int = 5) -> None:
        self._data = [None] * capacity
        self._capacity = capacity
        self._count = 0
        self._front = 0
        self._rear = 0

    def enqueue(self, item: T) -> None:
        if self._count == self._capacity:
            raise ValueError("Queue is full!")
        self._data[self._rear % self._capacity] = item
        self._rear += 1
        self._count += 1

    def top(self) -> T:
        if self._count == 0:
            raise ValueError("Empty queue!")
        return self._data[self._front % self._capacity]

    def pop(self) -> T:
        if self._count == 0:
            raise ValueError("Empty queue!")
        val = self._data[self._front % self._capacity]
        self._data[self._front % self._capacity] = None
        self._front += 1
        self._count -= 1
        return val

    def traverse(self) -> None:
        for item in range(self._front, self._rear):
            if (val := self._data[item % self._capacity]) is not None:
                print(val)


if __name__ == "__main__":
    aq = ArrayQueue()
    aq.enqueue(3)
    aq.enqueue(4)
    aq.enqueue(5)
    aq.enqueue(6)
    aq.enqueue(7)
    aq.pop()
    aq.pop()
    aq.enqueue(8)
    aq.enqueue(9)
    aq.traverse()
    aq.pop()
    aq.traverse()
