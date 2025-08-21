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

    def push(self, value: str) -> None:
        node = Node(value)
        prev_head = self._head
        self._head = node
        self._head.next = prev_head

    def peek(self) -> str | None:
        if self._head:
            return self._head.value
        return None

    def pop(self) -> str:
        prev_head = self._head
        self._head = prev_head.next
        return prev_head.value


if __name__ == "__main__":
    infix = "(a+b)/c*d-e"
    bodmas = {
        "^": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0
    }

    def infix_2_postfix(infix: str):

        ans = ""
        stack = Stack()

        for ch in infix:
            if ch == "(":
                stack.push(ch)
            elif ch == ")":
                while stack.peek() != "(":
                    ans += stack.pop()
                stack.pop()
            elif ch not in "*/+-":
                ans += ch
            else:
                while stack.peek() and bodmas[stack.peek()] >= bodmas[ch]:
                    ans += stack.pop()
                stack.push(ch)

        while stack.peek():
            ans += stack.pop()
        return ans

    # evaluate postfix notation with stack

    eval_stack = Stack()
    infix = "(1+2)/3*3-9"
    postfix = infix_2_postfix(infix)
    expected = 0

    for c in postfix:
        if c not in "^*/+-":
            eval_stack.push(c)
        else:
            second = eval_stack.pop()
            first = eval_stack.pop()
            eval_ = eval(f"{first}{c}{second}")
            eval_stack.push(eval_)

    print(eval_stack.peek())
