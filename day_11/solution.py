from functools import cache

import networkx as nx

with open("day_11/input.txt") as f:
    data = f.read().replace(':', '').splitlines()

# Parse the input data into a directed graph
G: nx.DiGraph = nx.parse_adjlist(data, create_using=nx.DiGraph)


@cache
def paths(u, v):
    """Return the number of paths from u to v in the directed acyclic graph G."""
    if u == v:
        return 1
    total = 0
    for neighbor in G.successors(u):
        total += paths(neighbor, v)
    return total


# Part One
part_one = paths("you", "out")
print(part_one)

# Part Two
part_two = 1
sequence = ["svr", "fft", "dac", "out"]
for i in range(len(sequence) - 1):
    part_two *= paths(sequence[i], sequence[i + 1])
print(part_two)
