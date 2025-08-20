"""
Stack implementation in Python on a single linked list basis
"""
from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, val: T) -> None:
        self._value = val
        self.next = None

    @property
    def value(self) -> T:
        return self._value


class Stack[T]:
    def __init__(self) -> None:
        self._head = None

    def push(self, value: T) -> None:
        new_head = Node(value)
        prev_head = self._head
        self._head = new_head
        self._head.next = prev_head

    def pop(self) -> T:
        if self._head:
            prev_head = self._head
            self._head = prev_head.next
            return prev_head.value
        raise IndexError("Stack is empty")


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(11)
    print(stack.pop())
    stack.push(666)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


