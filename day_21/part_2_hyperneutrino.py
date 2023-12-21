from collections import deque


with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

lines = puzzle_input.splitlines()
start_x, start_y = next((x, y) for x, line in enumerate(lines) for y, character in enumerate(line) if character == "S")
total_steps = 26501365

assert len(lines) == len(lines[0])
size = len(lines)
assert start_x == start_y == size // 2
assert total_steps % size == size // 2

print(start_x, start_y)

def fill(start_x, start_y, steps):
    ans = set()
    seen = {start_x, start_y}

    queue = deque([(start_x, start_y, steps)])

    while queue:
        x, y, c_steps = queue.popleft()
        if c_steps % 2 == 0:
            ans.add((x, y))
        if c_steps == 0:
            continue

        for next_x, next_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if not 0 <= next_x < len(lines) or not 0 <= next_y < len(lines[0]) or lines[next_x][next_y] == "#" or (next_x, next_y) in seen:
                continue
            seen.add((next_x, next_y))
            queue.append((next_x, next_y, c_steps - 1))

    return len(ans)


big_grid_width = total_steps // size - 1
num_odd_grids = (big_grid_width // 2 * 2 + 1)**2
num_even_grids = ((big_grid_width + 1) // 2 * 2)**2

odd_points = fill(start_x, start_y, size * 2 + 1)
even_points = fill(start_x, start_y, size * 2)

num_steps_extremities = size - 1
corner_top = fill(size - 1, start_y, num_steps_extremities)
corner_right = fill(start_x, 0, num_steps_extremities)
corner_bottom = fill(0, start_y, num_steps_extremities)
corner_left = fill(start_x, size - 1, num_steps_extremities)

num_steps_rem_small_corner = size // 2 - 1
small_top_right = fill(size - 1, 0, num_steps_rem_small_corner)
small_bot_right = fill(0, 0, num_steps_rem_small_corner)
small_bot_left = fill(0, size - 1, num_steps_rem_small_corner)
small_top_left = fill(size - 1, size - 1, num_steps_rem_small_corner)

num_steps_rem_big_corner = 3 * size // 2 - 1
big_top_right = fill(size - 1, 0, num_steps_rem_big_corner)
big_bot_right = fill(0, 0, num_steps_rem_big_corner)
big_bot_left = fill(0, size - 1, num_steps_rem_big_corner)
big_top_left = fill(size - 1, size - 1, num_steps_rem_big_corner)

num_small_corners = big_grid_width + 1
num_big_corners = big_grid_width

print(big_grid_width)
print(num_small_corners)
print(num_big_corners)

print(
    num_odd_grids * odd_points
    + num_even_grids * even_points
    + corner_top + corner_right + corner_bottom + corner_left
    + num_small_corners * (small_top_right + small_bot_right + small_bot_left + small_top_left)
    + num_big_corners * (big_top_right + big_bot_right + big_bot_left + big_top_left)
)
