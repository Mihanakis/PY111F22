import networkx as nx


def stairway_path(path):
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param path: массив стоимости путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    graph = nx.DiGraph()
    queue = list(path)[::-1]

    n = 0
    while queue:
        weight = queue.pop()
        if n == 0:
            graph.add_weighted_edges_from([(n, n + 1, weight)])
        else:
            graph.add_weighted_edges_from([(n, n + 1, weight), (n - 1, n + 1, weight)])
        n += 1

    _, coasts = nx.dijkstra_predecessor_and_distance(graph, 0)
    return coasts[n]


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    print(stairway_path(stairway))  # 72
