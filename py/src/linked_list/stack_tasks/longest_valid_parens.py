class Node:
    def __init__(self, value: str) -> None:
        self._value = value
        self._next = None

    @property
    def value(self) -> str:
        return self._value

    @property
    def next(self) -> "Node | None":
        return self._next

    @next.setter
    def next(self, node: "Node") -> None:
        self._next = node


class Stack:
    def __init__(self) -> None:
        self._head = None

    def push(self, value) -> None:
        node = Node(value)
        prev = self._head
        self._head = node
        self._head.next = prev

    def pop(self) -> str:
        prev = self._head
        self._head = prev.next
        return prev.value

    def peek(self) -> str | None:
        if self._head:
            return self._head.value
        return None


if __name__ == "__main__":
    parens = "()(((()"
    parens_2 = "()((("
    parens_3 = "(())(((((()))"
    parens4 = ")))))))"
    s = Stack()

    best = 0
    cnt = 0
    for c in parens_3:
        if c == "(":
            cnt = 0
            s.push(c)
        elif c == ")":
            if s.peek() == "(":
                cnt += 2
                best = max(best, cnt)
                s.pop()

    # can be also implemented with `is_ok` stack that is an arr of len of word with 0s
    # and changed to 1s if it is a valid parenthesis pair
    print(best)
