"""
Dynamic Array implementation in Python.
Yes, the std's list itself implementation is a dynamic array, but to resemble the
behaviour of the dynamic array in C-like language I tried to simulate this.
Aiming at no usage of provided methods for `list` to modify it (other than slicing,
that might change in the future)
"""


class DynamicArray:
    GROWTH_FACTOR = 1.5
    def __init__(self):
        self._data = []
        self._capacity = 0
        self._length = 0

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def length(self) -> int:
        return self._length

    def add(self, item: int) -> None:
        if self._length == self._capacity:
            if self._capacity == 0:
                self._capacity += 1
            else:
                self._capacity = round(self._capacity * self.GROWTH_FACTOR)
            prev_data = self._data
            self._data = [None] * self._capacity

            for idx, p_d in enumerate(prev_data):
                self._data[idx] = p_d

            del prev_data

        self._data[self._length] = item
        self._length += 1

        return None

    def remove(self) -> int:
        if self._length > 0:
            val = self._data[self._length - 1]
            self._data[self._length - 1] = None
            self._length -= 1
            return val
        raise ValueError("Empty array!")

    def remove_at(self, idx: int = None) -> int:
        if not idx:
            idx = self._length - 1
            return self.remove()
        else:
            if idx > self._length:
                raise IndexError("Position out of array current length!")
            pos = idx - 1
            val = self._data[pos]
            self._data[pos] = None
            start_idx = pos
            for item in self._data[idx:self._length]:
                self._data[start_idx] = item
                self._data[start_idx + 1] = None
                start_idx += 1
            self._length -= 1
            return val

    def get(self, pos: int) -> int:
        return self._data[pos - 1]

    def __str__(self) -> str:
        return f"Arr<{self._data}; length: {self._length}; capacity: {self._capacity}>"
