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


class DFSAdjacencyList:
    def __init__(self, adj_list: list[list[int]]) -> None:
        self._adj_list = adj_list
        self._length = len(self._adj_list)
        self._visited = [False] * self._length

    def run(self, node: int) -> list[int]:
        order = []
        if self._visited[node]:
            return []
        self._visited[node] = True
        order.append(node)

        neighbours = self._adj_list[node]

        for neighbour in neighbours:
            if not self._visited[neighbour]:
                order += self.run(neighbour)
        return order


dfs_adj = DFSAdjacencyList(adjacency_list)
print(dfs_adj.run(0))

n = 5
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3],
}
count = 0
visited = [False] * n
components = [None] * n


def find_components():
    global n
    global graph
    global count
    global visited
    global components

    def dfs(at):
        visited[at] = True
        components[at] = count

        for node in graph[at]:
            if not visited[node]:
                dfs(node)

    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return (count, components)
