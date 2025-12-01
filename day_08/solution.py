import networkx as nx
import numpy as np

with open("day_08/input.txt") as f:
    data = f.readlines()

# Parse coordinates
coords = [tuple(map(int, line.split(','))) for line in data]

# Build graph with squared Euclidean distances as weights
G = nx.Graph()
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        dist = sum((a - b) ** 2 for a, b in zip(coords[i], coords[j]))
        G.add_edge(i, j, weight=dist)

# Get the 1000 edges with the smallest weights
edges = sorted(G.edges(data=True), key=lambda x: x[2]["weight"])[:1000]

# Create a new graph with these edges
H = nx.Graph()
H.add_edges_from(edges)

# Find the three largest connected components
components = sorted(nx.connected_components(H), key=len, reverse=True)
sizes = [len(c) for c in components[:3]]

# Calculate the product of their sizes
part_one = np.prod(sizes)

# Create spanning tree from G
T = nx.minimum_spanning_tree(G)

# Find the edge with the maximum weight in the spanning tree
max_edge = max(T.edges(data=True), key=lambda x: x[2]["weight"])

# Multiply the X coordinates of the two nodes connected by this edge
part_two = coords[max_edge[0]][0] * coords[max_edge[1]][0]

print(part_one)
print(part_two)
