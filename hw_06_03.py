import networkx as nx

def add_weighted_edges(G, edges_with_weights):
    for edge in edges_with_weights:
        G.add_edge(edge[0], edge[1], weight=edge[2])

def dijkstra_shortest_path(G, start, goal):
    # Використовуємо алгоритм Дейкстри з бібліотеки NetworkX
    path = nx.dijkstra_path(G, source=start, target=goal, weight='weight')
    return path

# Створення графа і додавання вершин з вагами
G = nx.Graph()
edges_with_weights = [
    ("Anna", "Bob", 1), ("Anna", "Charlie", 2), ("Bob", "Diana", 2),
    ("Charlie", "Diana", 1), ("Edward", "Fiona", 3), ("Fiona", "George", 2),
    ("George", "Hannah", 1), ("Hannah", "Edward", 2), ("Anna", "Fiona", 3),
    ("Charlie", "Edward", 4), ("Diana", "George", 2), ("Bob", "Hannah", 3)
]
G.add_weighted_edges_from(edges_with_weights)

# Застосування алгоритму Дейкстри для кожної вершини
for source in G.nodes():
    print(f"Найкоротші шляхи від {source}:")
    lengths = nx.single_source_dijkstra_path_length(G, source)
    paths = nx.single_source_dijkstra_path(G, source)
    for target in lengths:
        print(f"  До {target}: довжина {lengths[target]}, шлях {paths[target]}")
    print("\n")
