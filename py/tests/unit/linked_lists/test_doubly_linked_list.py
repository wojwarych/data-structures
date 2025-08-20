from src import DoublyLinkedList

import pytest


@pytest.fixture
def dl() -> DoublyLinkedList[int]:
    return DoublyLinkedList(2)


def test_doubly_linked_list() -> None:
    dl = DoublyLinkedList(5)

    assert dl.head == 5
    assert dl.tail == 5


def test_doubly_linked_list_add_tail(dl: DoublyLinkedList[int]) -> None:
    dl.add_tail(4)
    dl.add_tail(55)

    assert dl.tail == 55


def test_doubly_linked_list_add_head(dl: DoublyLinkedList[int]) -> None:
    dl.add_head(4)
    dl.add_head(55)

    assert dl.head == 55


def test_doubly_linekd_list_remove_tail(dl: DoublyLinkedList[int]) -> None:
    dl.add_tail(23)
    dl.add_tail(11)

    ret = dl.remove_tail()

    assert ret == 11


def test_doubly_linekd_list_remove_head_one_item(dl: DoublyLinkedList[int]) -> None:
    ret = dl.remove_head()

    assert ret == 2


def test_doubly_linekd_list_remove_head(dl: DoublyLinkedList[int]) -> None:
    dl.add_head(23)
    dl.add_head(11)

    ret = dl.remove_head()

    assert ret == 11
