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


class DFSAdjacencyMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        self._matrix = matrix
        self._length = len(self._matrix)
        self._visited = [False] * self._length

    def run(self, start: int) -> list[int]:
        order = []
        if self._visited[start]:
            return []
        self._visited[start] = True
        order.append(start)

        for row_idx, _ in enumerate(self._matrix[start]):
            if (
                self._matrix[start][row_idx] == 1
                and not self._visited[row_idx]
            ):
                order += self.run(row_idx)
        return order


dfs_matrix = DFSAdjacencyMatrix(adjacency_matrix)
print(dfs_matrix.run(0))
