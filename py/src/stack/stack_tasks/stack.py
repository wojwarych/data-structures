"""
Stack implementation in Python on a single linked list basis
"""

from collections.abc import Iterator
from typing import TypeVar, Self

T = TypeVar("T")


class Node:
    def __init__(self, val: T) -> None:
        self._value = val
        self.next = None

    @property
    def value(self) -> T:
        return self._value


class Stack[T](Iterator):
    def __init__(self) -> None:
        self._head = None
        self._curr = self._head

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> T:
        val = self._curr
        if not val:
            raise StopIteration
        ret_val = self._curr.value
        self._curr = self._curr.next
        return ret_val

    def push(self, value: T) -> None:
        new_head = Node(value)
        prev_head = self._head
        self._head = new_head
        self._curr = self._head
        self._head.next = prev_head

    def pop(self) -> T:
        if not self.is_empty():
            prev_head = self._head
            self._head = prev_head.next
            self._curr = self._head
            return prev_head.value
        raise IndexError("Stack is empty")

    def is_empty(self) -> bool:
        return self._head is None

    def pprint(self) -> None:
        node = self._head
        if node:
            while node.next is None:
                print("NODE: ", node.value)
                node = node.next
            print("NODE: ", node.value)
        print("Linked List is empty!")


class CanonicalPath:
    def __init__(self, path: str) -> None:
        self._stack = Stack()
        self._path = path

    def traverse_path(self) -> None:
        for sub_path in self._path.split("/"):
            if sub_path == "..":
                if not self._stack.is_empty():
                    self._stack.pop()
                    continue
            elif sub_path == "." or sub_path == "":
                continue
            else:
                self._stack.push(sub_path)

        path = "/" + "/".join(self._stack)
        return path

    def pprint(self) -> None:
        self._stack.pprint()


if __name__ == "__main__":
    cp = CanonicalPath("/home/wojtek//tmp//./")
    ret = cp.traverse_path()
    print(ret)
