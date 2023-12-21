from collections import deque


with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

lines = puzzle_input.splitlines()
start_x, start_y = next((x, y) for x, line in enumerate(lines) for y, character in enumerate(line) if character == "S")

print(start_x, start_y)

ans = set()
seen = {start_x, start_y}

queue = deque([(start_x, start_y, 64)])

while queue:
    x, y, steps = queue.popleft()
    if steps % 2 == 0:
        ans.add((x, y))
    if steps == 0:
        continue

    for next_x, next_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if not 0 <= next_x < len(lines) or not 0 <= next_y < len(lines[0]) or lines[next_x][next_y] == "#" or (next_x, next_y) in seen:
            continue
        seen.add((next_x, next_y))
        queue.append((next_x, next_y, steps - 1))

print(len(ans))
