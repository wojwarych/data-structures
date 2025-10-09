adjacency_matrix = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
]


class BFSMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        self._matrix = matrix
        self._len = len(self._matrix)
        self._visited = [False] * self._len
        self._prev: list[int | None] = [None] * self._len

    def run(self, start: int, end: int) -> list:
        def solve(start: int) -> list[int | None]:
            self._visited[start] = True
            for row_idx, visited in enumerate(self._matrix):
                for idx, adjacencies in enumerate(visited):
                    if adjacencies == 0:
                        continue
                    if adjacencies == 1 and not self._visited[idx]:
                        self._visited[idx] = True
                        self._prev[idx] = row_idx
            return self._prev

        self._prev = solve(start)

        def reconstruct(start: int, end: int, prev: list[int | None]) -> list:
            path = []
            at = end
            while at is not None:
                path.append(at)
                at = prev[at]

            path.reverse()

            if path[0] == start:
                return path
            return []

        return reconstruct(start, end, self._prev)


bfs_m = BFSMatrix(adjacency_matrix)
print(bfs_m.run(1, 6))
