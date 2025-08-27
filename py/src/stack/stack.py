"""
Stack implementation in Python on a single linked list basis
"""

from typing import TypeVar
from src.linked_list import LinkedList

T = TypeVar("T")


class Stack[T]:
    def __init__(self, value: T) -> None:
        self._ll: LinkedList[T] = LinkedList(value)

    def push(self, value: T) -> None:
        self._ll.add_head(value)

    def pop(self) -> T:
        return self._ll.remove_head()

    def top(self) -> T:
        return self._ll.head
