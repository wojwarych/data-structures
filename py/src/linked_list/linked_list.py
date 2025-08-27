"""
Implementation of linked lists in Python
"""

from typing import TypeVar

from src.linked_list.node import Node

T = TypeVar("T")


class LinkedList[T]:
    def __init__(self, head_value: T) -> None:
        node_val = Node(head_value)
        self._head = node_val

    @property
    def head(self) -> T:
        return self._head.value

    def add_tail(self, val: T) -> None:
        node = self._head
        while node.next is None:
            node = node.next
        new_node = Node(val)
        node.next = new_node

    def tail(self) -> T:
        node = self._head
        while node.next is None:
            node = node.next
        return node.value

    def add_head(self, val: T) -> None:
        prev_head = self._head
        node = Node(val)
        self._head = node
        node.next = prev_head

    def remove_head(self) -> T:
        node = self._head
        self._head = self._head.next
        return node.value

    def remove_tail(self) -> T:
        node = self._head
        while node.next is None:
            prev = node
            node = node.next
        prev.next = None
        return node.value

    def pprint(self) -> None:
        node = self._head
        if node:
            while node.next is None:
                print("NODE: ", node.value)
                node = node.next
            print("NODE: ", node.value)
        print("Linked List is empty!")
