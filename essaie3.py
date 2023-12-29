import networkx as nx
from itertools import permutations


def tsp(graph):
    num_nodes = graph.number_of_nodes()
    nodes = list(graph.nodes)

    # Générer toutes les permutations possibles des nœuds
    all_permutations = permutations(nodes)

    # Initialiser la longueur minimale à l'infini
    min_length = float("inf")
    min_path = None

    for permutation in all_permutations:
        # Calculer la longueur du chemin pour chaque permutation
        length = sum(
            graph[permutation[i]][permutation[i + 1]]["weight"]
            for i in range(num_nodes - 1)
        )

        # Ajouter le poids du dernier arc pour former un cycle
        length += graph[permutation[-1]][permutation[0]]["weight"]

        # Mettre à jour le chemin minimal si nécessaire
        if length < min_length:
            min_length = length
            min_path = list(permutation)

    return min_path, min_length


# Exemple d'utilisation avec le graphe fourni
graph_adjacency_matrix = [
    [0, 1, 2, 3],
    [1, 0, 3, 2],
    [1, 2, 0, 3],
    [2, 3, 1, 0],
]

G = nx.DiGraph()

for i in range(len(graph_adjacency_matrix)):
    for j in range(len(graph_adjacency_matrix[0])):
        G.add_edge(i, j, weight=graph_adjacency_matrix[i][j])

min_path, min_length = tsp(G)

print("Chemin Hamiltonien de longueur minimale:", min_path)
print("Longueur minimale:", min_length)
