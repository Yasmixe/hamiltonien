from typing import Dict, Set, List
from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph: Dict[int, Set] = defaultdict(set)
        self.visited = defaultdict(lambda: False)

        self.make_graph()

        self.visited_nodes = 0
        self.total_nodes = len(self.graph.keys())

    def make_graph(self) -> None:
        for vertices in self.edges:
            for i in range(len(vertices) - 1):
                u, v = vertices[i], vertices[i + 1]
                self.graph[u].add(v)
                self.graph[v].add(u)

    def visit(self, node):
        self.visited[node] = True
        self.visited_nodes += 1

    def un_visit(self, node):
        self.visited[node] = False
        self.visited_nodes -= 1

    def all_nodes_are_visited(self) -> bool:
        return self.visited_nodes == self.total_nodes

    def get_hamiltonian_path(self, start) -> List[List[int]]:
        self.visit(start)

        all_paths = []

        if self.all_nodes_are_visited():
            all_paths.append([start])

        for node in self.graph[start]:
            if self.visited[node]:
                continue
            paths = self.get_hamiltonian_path(node)
            for path in paths:
                if path:
                    path.append(start)
                    all_paths.append(path)

        self.un_visit(start)
        return all_paths


if __name__ == "__main__":
    edges = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 2, 0, 3], [2, 3, 1, 0]]
    graph = Graph(edges)
    hamiltonian_path = graph.get_hamiltonian_path(start=1)

    for path in hamiltonian_path:
        print("->".join(map(str, reversed(path))))
