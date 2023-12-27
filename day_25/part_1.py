import itertools
from collections import defaultdict

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

nodes = defaultdict(list)

for line in puzzle_input.splitlines():
    src, destinations = line.split(":")
    destinations = destinations.split()
    for dest in destinations:
        if dest not in nodes[src]:
            nodes[src].append(dest)
        if src not in nodes[dest]:
            nodes[dest].append(src)


def get_shortest_path(begin, end):
    seen = {begin}
    current_nodes = [begin]
    visited_nodes = [[begin]]

    while end not in seen:
        next_nodes = []
        next_visited_nodes = []
        for i, node in enumerate(current_nodes):
            for destination in nodes[node]:
                if destination not in seen:
                    next_nodes.append(destination)
                    next_visited_nodes.append(visited_nodes[i] + [destination])
                    seen.add(destination)
        current_nodes = next_nodes
        visited_nodes = next_visited_nodes

    return visited_nodes[current_nodes.index(end)]


def count_nodes(begin):
    seen = {begin}
    current_nodes = [begin]
    count = 1

    while True:
        next_nodes = []
        break_loop = True
        for node in current_nodes:
            for destination in nodes[node]:
                if destination not in seen:
                    break_loop = False
                    next_nodes.append(destination)
                    seen.add(destination)
                    count += 1
        current_nodes = next_nodes
        if break_loop:
            break

    return count


vertices_count = defaultdict(int)
for node_a, node_b in itertools.pairwise(nodes.keys()):
    visited_nodes = get_shortest_path(node_a, node_b)
    for va, vb in itertools.pairwise(visited_nodes):
        vertices = [va, vb]
        vertices.sort()
        vertices_count[tuple(vertices)] += 1
vertices_count = {v: c for v, c in sorted(vertices_count.items(), key=lambda item: item[1], reverse=True)}

del_vertices = [pair for pair in vertices_count.keys()][:3]
print(del_vertices)

for src, dest in del_vertices:
    nodes[src].pop(nodes[src].index(dest))
    nodes[dest].pop(nodes[dest].index(src))


print(count_nodes(del_vertices[0][0]) * count_nodes(del_vertices[0][1]))
