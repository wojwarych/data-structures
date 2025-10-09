from src.graphs.breadth_first_search import BFSAdjacencyList, BFSMatrix


def test_bfs_algos_return_same_result_for_input() -> None:
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

    bfs_matrix = BFSMatrix(adjacency_matrix)
    bfs_adj = BFSAdjacencyList(adjacency_list)

    assert bfs_matrix.run(1, 6) == bfs_adj.run(1, 6)
