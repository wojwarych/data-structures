"""
Implementing fixed-sized stack with "static" array
Of course in Python lists are dynamic arrays but you might simulate the fixed size array.
"""
from typing import TypeVar

T = TypeVar("T")


class ArrayStack:
    def __init__(self, capacity: int = 5) -> None:
        self._data = [None] * capacity
        self._capacity = capacity
        self._count = 0
        self._rear = 0

    def push(self, item: T) -> None:
        if self._count == self._capacity:
            raise ValueError("Stack is full!")
        self._data[self._rear % self._capacity] = item
        self._rear += 1
        self._count += 1

    def pop(self) -> T:
        if self._count == 0:
            raise ValueError("Empty stack!")
        val = self._data[self._rear - 1]
        self._data[self._rear - 1] = None
        self._rear -= 1
        self._count -= 1
        return val

    def top(self) -> T:
        if self._count == 0:
            raise ValueError("Empty stack!")
        return self._data[self._rear % self._capacity]

    def traverse(self) -> None:
        for item in range(self._rear):
            print(self._data[item % self._capacity], "-->")


if __name__ == "__main__":
    aq = ArrayStack()
    aq.push(3)
    aq.push(4)
    aq.push(5)
    aq.push(6)
    aq.push(7)
    aq.pop()
    aq.pop()
    aq.traverse()
    aq.push(8)
    aq.push(9)
    aq.traverse()
    aq.pop()
    aq.traverse()
