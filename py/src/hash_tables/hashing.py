class NaiveHashMap:
    def __init__(self, size: int) -> None:
        self._arr = [0] * (size + 1)
        self._hash = [0] * (size + 1)

    def add(self, value: int) -> None:
        self._arr[value] = value
        self._hash[value] += 1

    def remove(self, value: int) -> int:
        if value in self._arr:
            val = self._arr[value]
            self._arr[value] = 0
            self._hash[value] -= 1
            return val

    def is_in(self, value: int) -> int:
        return self._hash[value]
