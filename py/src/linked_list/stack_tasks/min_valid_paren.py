class Node:
    def __init__(self, value: int) -> None:
        self._value = value
        self._next = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = value

    @property
    def next(self) -> "Node | None":
        return self._next

    @next.setter
    def next(self, n: "Node") -> None:
        self._next = n


class Stack:
    def __init__(self) -> None:
        self._head = None
        self._length = 0

    def push(self, value: int) -> None:
        node = Node(value)
        prev_head = self._head
        self._head = node
        self._head.next = prev_head
        self._length += 1

    def peek(self) -> int | None:
        if self._head:
            return self._head.value
        return None

    def pop(self) -> int:
        prev_head = self._head
        self._head = prev_head.next
        self._length -= 1
        return prev_head.value

    def __getitem__(self, index):
        if index >= self._length:
            raise IndexError("Index out of bounds!")
        node = self._head
        if index == 0 and self._head:
            return self._head.value
        i = 0
        while node:
            if i == index:
                return node.value
            node = node.next
            i += 1
        return node

    def __setitem__(self, index, value):
        if index >= self._length:
            raise IndexError("Index out of bounds!")
        node = self._head
        if index == 0 and self._head:
            self._head.value = value
        i = 0
        while node:
            if i == index:
                node.value = value
            node = node.next
            i += 1


if __name__ == "__main__":
    parens_ = "[t(an)((i{sh}]q)]"
    parens_map = {"(": ")", "{": "}", "[": "]"}
    s = Stack()
    is_ok = Stack()
    for _ in parens_:
        is_ok.push(0)

    for idx, ch in enumerate(parens_):
        if ch in "({[":
            s.push(idx)
        elif ch in ")}]":
            if s.peek() is not None and parens_map[parens_[s.peek()]] == ch:
                is_ok[s.pop()] = 1
                is_ok[idx] = 1
            else:
                continue
        else:
            continue

    ans = ""
    for idx, ch in enumerate(parens_):
        if ch in "({[)}]":
            if is_ok[idx]:
                ans += ch
        else:
            ans += ch

    print(parens_)
    print(ans)
