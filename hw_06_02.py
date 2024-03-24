import networkx as nx

# Функція DFS для знаходження усіх шляхів
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Функція BFS для знаходження усіх шляхів
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Створення графа зі зв'язками між особами
G = nx.Graph()
relationships = [("Anna", "Bob"), ("Anna", "Charlie"), ("Bob", "Diana"), ("Charlie", "Diana"),
                 ("Edward", "Fiona"), ("Fiona", "George"), ("George", "Hannah"), ("Hannah", "Edward"),
                 ("Anna", "Fiona"), ("Charlie", "Edward"), ("Diana", "George"), ("Bob", "Hannah")]
G.add_edges_from(relationships)

# Використання DFS і BFS для знаходження шляхів від "Anna" до "George"
start, goal = "Anna", "George"
print("DFS шляхи:")
dfs_result = list(dfs_paths(G, start, goal))
for path in dfs_result:
    print(path)

print("\nBFS шляхи:")
bfs_result = list(bfs_paths(G, start, goal))
for path in bfs_result:
    print(path)
