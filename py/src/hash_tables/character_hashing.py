class CharacterNaiveHashMap:
    def __init__(self, string: str) -> None:
        self._string = string
        self._hash = [0] * 27
        self._precompute(string)

    def _precompute(self, string: str) -> None:
        for char in string:
            self.add(char)

    def add(self, char: str) -> None:
        self._string += char
        self._hash[ord(char) - 97] += 1

    def is_in(self, char: str) -> int:
        return self._hash[ord(char) - 97]


if __name__ == "__main__":
    a_string ="justsomechars"
    cnhm = CharacterNaiveHashMap(a_string)
    print(cnhm.is_in("s"))
