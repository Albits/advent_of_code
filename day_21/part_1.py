with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


lines = puzzle_input.splitlines()

start_position = (0, 0)
for x, line in enumerate(lines):
    for y, character in enumerate(line):
        if character == "S":
            start_position = (x, y)

blocks_reached = [[start_position]]

for _ in range(64):
    next_positions = []
    for start_position in blocks_reached[-1]:
        next_available_positions = [
            (start_position[0] + 1, start_position[1]),
            (start_position[0] - 1, start_position[1]),
            (start_position[0], start_position[1] - 1),
            (start_position[0], start_position[1] + 1)
        ]
        next_positions += [pos for pos in next_available_positions if lines[pos[0]][pos[1]] != "#" and pos not in next_positions]
    blocks_reached.append(next_positions)

print(len(blocks_reached[-1]))
