from src.queues.array_queue import ArrayQueue

import pytest


def test_array_queue_empty_setup() -> None:
    aq: ArrayQueue[int] = ArrayQueue()

    assert aq.capacity == aq.DEFAULT_CAP
    assert aq.count == 0
    assert aq.data == [None] * aq.DEFAULT_CAP


def test_array_queue_enqueue() -> None:
    aq: ArrayQueue[int] = ArrayQueue()

    aq.enqueue(4)

    assert aq.capacity == aq.DEFAULT_CAP
    assert aq.count == 1
    assert aq.top() == 4


def test_array_queue_enqueue_full_cap_raises_error() -> None:
    aq: ArrayQueue[int] = ArrayQueue()

    for i in range(aq.capacity):
        aq.enqueue(i)

    with pytest.raises(ValueError):
        aq.enqueue(6)

        assert aq.capacity == aq.DEFAULT_CAP
        assert aq.count == 5
        assert aq.top() == 0


def test_array_queue_top_empty_queue_raises_error() -> None:
    aq: ArrayQueue[int] = ArrayQueue()

    with pytest.raises(ValueError):
        aq.top()

        assert aq.capacity == aq.DEFAULT_CAP
        assert aq.count == 0
        assert aq.data == [None] * aq.DEFAULT_CAP


def test_array_queue_pop_empty_queue_raises_error() -> None:
    aq: ArrayQueue[int] = ArrayQueue()

    with pytest.raises(ValueError):
        aq.pop()

        assert aq.capacity == aq.DEFAULT_CAP
        assert aq.count == 0
        assert aq.data == [None] * aq.DEFAULT_CAP


def test_array_queue_pop_returns_correct_item() -> None:
    aq: ArrayQueue[int] = ArrayQueue()

    aq.enqueue(4)
    aq.enqueue(10)

    ret = aq.pop()

    assert ret == 4
    assert aq.top() == 10
    assert aq.capacity == aq.DEFAULT_CAP
    assert aq.count == 1


def test_array_queue_traversal_iterates() -> None:
    aq: ArrayQueue[int] = ArrayQueue()

    aq.enqueue(4)
    aq.enqueue(10)
    aq.enqueue(33)
    aq.enqueue(55)

    expected_order = [4, 10, 33, 55]

    for item in aq.traverse():
        assert item == expected_order.pop(0)
