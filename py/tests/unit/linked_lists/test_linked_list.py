from src import LinkedList

import pytest


@pytest.fixture
def ll() -> LinkedList:
    return LinkedList(66)


def test_linked_list() -> None:
    ll: LinkedList[int] = LinkedList(3)

    assert ll.head == 3


def test_linked_list_add_tail(ll: LinkedList) -> None:
    ll.add_tail(23)
    ll.add_tail(55)

    assert ll.tail() == 55


def test_linked_list_remove_tail(ll: LinkedList) -> None:
    ll.add_tail(458)
    ll.add_tail(9872)

    ret = ll.remove_tail()

    assert ret == 9872
    assert ll.tail() == 458


def test_linked_list_add_head(ll: LinkedList) -> None:
    ll.add_head(23)

    assert ll.head == 23


def test_linked_list_remove_head(ll: LinkedList) -> None:
    ll.add_head(879)
    ll.add_head(234)

    ret = ll.remove_head()

    assert ret == 234
    assert ll.head == 879
