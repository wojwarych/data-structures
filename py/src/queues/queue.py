"""
Queue implementation in Python with usage of Doubly Linked List
"""

from typing import TypeVar

from src.linked_list import DoublyLinkedList


T = TypeVar("T")


class Queue[T]:
    def __init__(self, value: T) -> None:
        self._dl = DoublyLinkedList(value)

    def enqueue(self, value: T) -> None:
        self._dl.add_tail(value)

    def dequeue(self) -> T:
        return self._dl.remove_head()

    def peek(self) -> T:
        return self._dl.head
