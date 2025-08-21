class CharacterNaiveHashMap:
    def __init__(self, string: str) -> None:
        self._string = string
        self._hash = [0] * 27
        self._precompute(string)

    def _precompute(self, string: str) -> None:
        if not self._is_ascii(string):
            raise TypeError("Can only hash map ASCII characters!")
        for char in string:
            self.add(char)

    def _is_ascii(self, string: str) -> bool:
        return all(ord(c) < 128 for c in string)

    def add(self, char: str) -> None:
        if not self._is_ascii(char):
            raise TypeError("Can only hash map ASCII characters!")
        self._string += char
        self._hash[ord(char) - 97] += 1

    def is_in(self, char: str) -> bool:
        return bool(self._hash[ord(char) - 97])
