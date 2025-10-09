adjacency_list = [
    [1, 4],
    [0, 2, 5],
    [1, 3, 6],
    [2, 7],
    [0, 5, 8],
    [1, 4, 6, 9],
    [2, 5],
    [3, 9],
    [4],
    [5, 7],
]


class BFSAdjacencyList:
    def __init__(self, adjacency_list: list[list[int]]) -> None:
        self._adj_list: list[list[int]] = adjacency_list
        self._length = len(self._adj_list)
        self._visited: list[bool] = self._length * [False]
        self._prev: list[int | None] = self._length * [None]
        self._queue: list[int] = []

    def run(self, start: int, end: int) -> list[int | None]:
        def solve(start):
            self._queue.append(start)
            self._visited[start] = True

            while self._queue:
                node = self._queue.pop(0)
                neighbours = self._adj_list[node]

                for n in neighbours:
                    if not self._visited[n]:
                        self._queue.append(n)
                        self._visited[n] = True
                        self._prev[n] = node
            return self._prev

        self._prev = solve(start)

        def reconstruct(start, end, prev):
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


bfs_adj = BFSAdjacencyList(adjacency_list)
print(bfs_adj.run(1, 6))
