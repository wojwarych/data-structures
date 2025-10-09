from src.graphs.depth_first_search import DFSAdjacencyList, DFSAdjacencyMatrix


def test_dfs_algos_return_same_result_for_input() -> None:
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

    dfs_matrix = DFSAdjacencyMatrix(adjacency_matrix)
    dfs_adj = DFSAdjacencyList(adjacency_list)

    assert dfs_matrix.run(0) == dfs_adj.run(0)
