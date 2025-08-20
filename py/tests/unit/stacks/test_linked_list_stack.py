from src.stack.stack import Stack


def test_stack_push_pop_equals() -> None:
    inp = 10
    stack: Stack[int] = Stack(5)

    stack.push(inp)

    assert stack.pop() == inp
    assert stack.top() == 5
