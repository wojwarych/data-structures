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
        self._min = None

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

    def peek(self) -> T:
        if not self.is_empty():
            return self._head.value

    def pprint(self) -> None:
        node = self._head
        if node:
            while node.next != None:
                print("NODE: ", node.value)
                node = node.next
            print("NODE: ", node.value)
        print("Linked List is empty!")


class MinStack:
    def __init__(self) -> None:
        self._stack = Stack()
        self._min_stack = Stack()

    def push(self, value: T) -> None:
        if self._stack.is_empty():
            self._stack.push(value)
            self._min_stack.push(value)
        else:
            self._stack.push(value)
            self._min_stack.push(min(value, self._min_stack.peek()))

    def pop(self) -> T:
        self._min_stack.pop()
        return self._stack.pop()

    def get_min(self) -> T:
        return self._min_stack.peek()

    def top(self) -> T:
        return self._stack.peek()


if __name__ == "__main__":
    ms = MinStack()
    values = [3, 8, 1, 10, 22]
    for v in values:
        ms.push(v)
    print(ms.get_min())

    ms.pop()
    ms.pop()
    ms.pop()

    print(ms.get_min())

    ms.push(-45)

    print(ms.get_min())
