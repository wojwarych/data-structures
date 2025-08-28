from src.stack.array_stack import ArrayStack

import pytest


def test_array_stack_empty_setup() -> None:
    array_stack: ArrayStack[int] = ArrayStack()

    assert array_stack.capacity == array_stack.DEFAULT_CAP
    assert array_stack.count == 0
    assert array_stack.data == [None] * array_stack.DEFAULT_CAP


def test_array_stack_push() -> None:
    array_stack: ArrayStack[int] = ArrayStack()

    array_stack.push(4)

    assert array_stack.capacity == array_stack.DEFAULT_CAP
    assert array_stack.count == 1
    assert array_stack.top() == 4


def test_array_stack_push_full_cap_raises_error() -> None:
    array_stack: ArrayStack[int] = ArrayStack()

    for i in range(array_stack.capacity):
        array_stack.push(i)

    with pytest.raises(ValueError):
        array_stack.push(6)

        assert array_stack.capacity == array_stack.DEFAULT_CAP
        assert array_stack.count == 5
        assert array_stack.top() == 0


def test_array_stack_top_empty_stack() -> None:
    array_stack: ArrayStack[int] = ArrayStack()

    with pytest.raises(ValueError):
        array_stack.top()

        assert array_stack.capacity == array_stack.DEFAULT_CAP
        assert array_stack.count == 0
        assert array_stack.data == [None] * array_stack.DEFAULT_CAP


def test_array_stack_pop_empty_stack_raises_error() -> None:
    array_stack: ArrayStack[int] = ArrayStack()

    with pytest.raises(ValueError):
        array_stack.pop()

        assert array_stack.capacity == array_stack.DEFAULT_CAP
        assert array_stack.count == 0
        assert array_stack.data == [None] * array_stack.DEFAULT_CAP


def test_array_stack_pop_returns_correct_item() -> None:
    array_stack: ArrayStack[int] = ArrayStack()

    array_stack.push(4)
    array_stack.push(10)

    ret = array_stack.pop()

    assert ret == 10
    assert array_stack.top() == 4
    assert array_stack.capacity == array_stack.DEFAULT_CAP
    assert array_stack.count == 1


def test_array_stack_traversal_iterates() -> None:
    array_stack: ArrayStack[int] = ArrayStack()

    array_stack.push(4)
    array_stack.push(10)
    array_stack.push(33)
    array_stack.push(55)

    expected_order = [4, 10, 33, 55]

    for item in array_stack.traverse():
        assert item == expected_order.pop(0)
