import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Створення графа
G = nx.Graph()

# Додавання вершин
people = ["Anna", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah"]
G.add_nodes_from(people)

# Додавання ребер (взаємозв'язків)
relationships = [("Anna", "Bob"), ("Anna", "Charlie"), ("Bob", "Diana"), ("Charlie", "Diana"),
                 ("Edward", "Fiona"), ("Fiona", "George"), ("George", "Hannah"), ("Hannah", "Edward"),
                 ("Anna", "Fiona"), ("Charlie", "Edward"), ("Diana", "George"), ("Bob", "Hannah")]
G.add_edges_from(relationships)

# Візуалізація графа
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=1, font_size=15, font_weight='bold')
plt.title("Соціальна мережа спільноти")
plt.show()

# Аналіз основних характеристик мережі
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [val for (node, val) in G.degree()]
avg_degree = np.mean(degrees)
max_degree = np.max(degrees)
min_degree = np.min(degrees)

# Виведення основних характеристик
print(f"Кількість вершин (учасників мережі): {num_nodes}")
print(f"Кількість ребер (взаємозв'язків): {num_edges}")
print(f"Середній ступінь вершин: {avg_degree}")
print(f"Максимальний ступінь вершин: {max_degree}")
print(f"Мінімальний ступінь вершин: {min_degree}")
