"""
Stack implementation in Python on a single linked list basis
"""
from typing import TypeVar, Self

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
        if not self.is_empty():
            prev_head = self._head
            self._head = prev_head.next
            return prev_head.value
        raise IndexError("Stack is empty")

    def is_empty(self) -> bool:
        return self._head is None

    def pprint(self) -> None:
        node = self._head
        if node:
            while node.next != None:
                print("NODE: ", node.value)
                node = node.next
            print("NODE: ", node.value)
        print("Linked List is empty!")

    def peek(self) -> T:
        if not s.is_empty():
            return self._head.value


if __name__ == "__main__":
    redundant = "(a+b+c)"
    not_redundant = "({a+b}-(d*f))"

    bracket_mapping = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    operators = "+-*/%"

    results = []
    tests = [redundant, not_redundant]
    for t in tests:
        s = Stack()
        for char in t:
            if char not in ")}]":
                s.push(char)
            else:
                count = 0
                while s.peek() != bracket_mapping[char]:
                    print(char)
                    v = s.pop()
                    if v in "+-*/":
                        count += 1
                s.pop()

                if count == 0:
                    results.append(False)
                    break
        else:
            results.append(True)

    print(results)
