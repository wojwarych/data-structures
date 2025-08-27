"""
Implementation of doubly linked lists in Python
"""

from typing import TypeVar

from src.linked_list.node import NextPrevNode

T = TypeVar("T")


class DoublyLinkedList[T]:
    def __init__(self, value: T) -> None:
        node = NextPrevNode(value)
        self._head: NextPrevNode[T] = node
        self._tail: NextPrevNode[T] = node

    @property
    def head(self) -> T:
        return self._head.value

    @property
    def tail(self) -> T:
        return self._tail.value

    def add_tail(self, value: T) -> None:
        node = NextPrevNode(value)
        tail_node = self._tail
        tail_node.next = node
        node.prev = tail_node
        self._tail = node

    def add_head(self, value: T) -> None:
        node = NextPrevNode(value)
        head_node = self._head
        head_node.prev = node
        node.next = head_node
        self._head = node

    def remove_tail(self) -> T:
        prev_tail = self._tail
        new_tail = prev_tail.prev
        new_tail.next = None
        self._tail = new_tail
        return prev_tail.value

    def remove_head(self) -> T:
        if self._head.next:
            prev_head = self._head
            new_head = prev_head.next
            new_head.prev = None
            self._head = new_head
            return prev_head.value
        prev_head = self._head
        self._head = None
        self._tail = None
        return prev_head.value

    def traverse(self) -> None:
        node = self._head
        while node.next != None:
            print("NODE: ", node.value)
            node = node.next
        print("NODE: ", node.value)

    def reverse(self) -> None:
        node = self._tail
        while node.prev != None:
            print("NODE: ", node.value)
            node = node.prev
        print("NODE: ", node.value)
