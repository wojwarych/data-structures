from typing import TypeVar


T = TypeVar("T")


class Node[T]:
    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T) -> None:
        self._value = value


