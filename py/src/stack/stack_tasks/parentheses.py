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
            while node.next is None:
                print("NODE: ", node.value)
                node = node.next
            print("NODE: ", node.value)
        print("Linked List is empty!")


if __name__ == "__main__":
    valid_parens = "{[a*{c+b}/10]}"
    invalid_1 = "["
    invalid_2 = "{]"
    invalid_3 = "{(a)+b]"

    tests = [valid_parens, invalid_1, invalid_2, invalid_3]

    results = []
    for t in tests:
        stack = Stack()
        for char in t:
            if char in ["{", "[", "("]:
                stack.push(char)
            elif char in ["}", "]", ")"]:
                op_paren = stack.pop()
                if char == "]" and op_paren != "[":
                    results.append(False)
                    break
                elif char == "}" and op_paren != "{":
                    results.append(False)
                    break
                elif char == ")" and op_paren != "(":
                    results.append(False)
                    break
        else:
            if stack.is_empty():
                results.append(True)
            else:
                results.append(False)

    print(results)
