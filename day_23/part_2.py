from copy import copy
from datetime import datetime

print(f"Started at {datetime.now()}")

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

grid = puzzle_input.splitlines()

start_position = (0, grid[0].find("."))
end_position = (len(grid) - 1, grid[-1].find("."))

def get_longest_path(start_pos, visited, count, depth=0):
    other_max = 0
    while start_pos != end_position:
        next_available = (
            (start_pos[0] + 1, start_pos[1]),
            (start_pos[0] - 1, start_pos[1]),
            (start_pos[0], start_pos[1] + 1),
            (start_pos[0], start_pos[1] - 1)
        )
        next_available = [pos for pos in next_available if pos not in visited and grid[pos[0]][pos[1]] != "#"]
        if len(next_available) == 0:
            return other_max
        if len(next_available) > 1:
            for pos in next_available[1:]:
                new_visited = copy(visited)
                new_visited.add(pos)
                current_max = get_longest_path(pos, new_visited, count, depth + 1)
                other_max = max(other_max, current_max)
        count += 1
        start_pos = next_available[0]
        visited.add(start_pos)
        # print(f"Took {paths_taken} paths, count {count}")
        # for line in grid:
        #     print(line)
    # print(f"End reached with count {count} and depth {depth}")
    return max(count, other_max)

visited = set()
visited.add(start_position)

# walkers = [[start_position, visited, 0]]
#
# current_max = 0
# while walkers[0][0] != end_position:
#     walkers_to_add = []
#     walkers_to_pop = []
#     for walker_index, walker in enumerate(walkers):
#         if walker[0] == end_position:
#             current_max = max(current_max, walker[2])
#             walkers_to_pop.append(walker_index)
#             continue
#         start_pos = walker[0]
#         next_available = (
#             (start_pos[0] + 1, start_pos[1]),
#             (start_pos[0] - 1, start_pos[1]),
#             (start_pos[0], start_pos[1] + 1),
#             (start_pos[0], start_pos[1] - 1)
#         )
#         try:
#             next_available = [pos for pos in next_available if pos not in walker[1] and grid[pos[0]][pos[1]] != "#"]
#         except IndexError:
#             print(f"Error for {next_available}")
#         if len(next_available) == 0:
#             walkers_to_pop.append(walker_index)
#             continue
#         walker[0] = next_available[0]
#         walker[1].add(start_pos)
#         walker[2] += 1
#         if len(next_available) > 1:
#             for pos in next_available[1:]:
#                 walkers_to_add.append([pos, copy(visited), walker[2]])
#     for pop_index in reversed(walkers_to_pop):
#         walkers.pop(pop_index)
#     for walker in walkers_to_add:
#         walkers.append(walker)
#     print(len(walkers))
#
#     walkers.sort(key=lambda elem: elem[2], reverse=True)

print(get_longest_path(start_position, visited, 0))
print(f"Ended at {datetime.now()}")

