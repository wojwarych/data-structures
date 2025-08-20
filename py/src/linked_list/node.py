from __future__ import annotations
from typing import TypeVar


T = TypeVar("T")


class Node[T]:
    def __init__(self, value: T) -> None:
        self._value = value
        self._next: Node | None = None

    @property
    def value(self) -> T:
        return self._value

    @property
    def next(self) -> Node | None:
        return self._next

    @next.setter
    def next(self, next_: Node | None) -> None:
        self._next = next_



class NextPrevNode[T](Node):
    def __init__(self, value: T) -> None:
        self._prev: NextPrevNode | None = None
        super().__init__(value)

    @property
    def prev(self) -> NextPrevNode | None:
        return self._prev

    @prev.setter
    def prev(self, prev_: NextPrevNode | None) -> None:
        self._prev = prev_
