from copy import copy
from math import inf

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

grid = puzzle_input.splitlines()

start_position = (0, grid[0].find("."))
end_position = (len(grid) - 1, grid[-1].find("."))

paths_taken = 0

points_of_interest = [start_position, end_position]

for r, row in enumerate(grid):
    for c, character in enumerate(row):
        if character == "#":
            continue
        neighbors = 0
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                neighbors += 1
        if neighbors >= 3:
            points_of_interest.append((r, c))

print(len(points_of_interest))

graph = {point: {} for point in points_of_interest}

for start_r, start_c in points_of_interest:
    stack = [(0, start_r, start_c)]
    seen = {(start_r, start_c)}

    while stack:
        n, r, c = stack.pop()

        if n != 0 and (r, c) in points_of_interest:
            graph[(start_r, start_c)][(r, c)] = n
            continue

        for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != "#" and (new_r, new_c) not in seen:
                stack.append((n + 1, new_r, new_c))
                seen.add((new_r, new_c))

print(graph)

visited = set()


def get_longest_path(current_point):
    if current_point == end_position:
        return 0
    max_length = -inf

    visited.add(current_point)
    for next_point in graph[current_point]:
        if next_point not in visited:
            max_length = max(max_length, get_longest_path(next_point) + graph[current_point][next_point])
    visited.remove(current_point)

    return max_length

print(get_longest_path(start_position))
