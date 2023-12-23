from copy import copy

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

grid = puzzle_input.splitlines()

start_position = (0, grid[0].find("."))
end_position = (len(grid) - 1, grid[-1].find("."))


def get_longest_path(start_pos, visited, count):
    other_max = 0
    while start_pos != end_position:
        next_available = (
            (start_pos[0] + 1, start_pos[1]),
            (start_pos[0] - 1, start_pos[1]),
            (start_pos[0], start_pos[1] + 1),
            (start_pos[0], start_pos[1] - 1)
        )
        match grid[start_pos[0]][start_pos[1]]:
            case "v":
                next_available = [next_available[0]]
            case "^":
                next_available = [next_available[1]]
            case ">":
                next_available = [next_available[2]]
            case "<":
                next_available = [next_available[3]]
        next_available = [pos for pos in next_available if pos not in visited and grid[pos[0]][pos[1]] != "#"]
        if len(next_available) == 0:
            return other_max
        start_pos = next_available[0]
        visited.add(start_pos)
        count += 1
        if len(next_available) > 1:
            other_max = max(*[get_longest_path(pos, copy(visited), count) for pos in next_available[1:]], other_max)
    return max(count, other_max)

visited = set()
visited.add(start_position)

print(get_longest_path(start_position, visited, 0))
