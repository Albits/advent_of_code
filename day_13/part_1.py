import itertools

from puzzle_input import value as puzzle_input

patterns = puzzle_input.split("\n\n")
print(patterns[0])

patterns_rocks_coordinates = []


def check_x_mirror(pattern_lines, x_mirror_index, width):
    top_line_index = x_mirror_index - width
    bot_line_index = x_mirror_index + width - 1
    if top_line_index < 0 or bot_line_index >= len(pattern_lines):
        return True
    if pattern_lines[bot_line_index] != pattern_lines[top_line_index]:
        return False
    else:
        return check_x_mirror(pattern_lines, x_mirror_index, width + 1)


def check_y_mirror(pattern_lines, y_mirror_index, width):
    left_col_index = y_mirror_index - width
    right_col_index = y_mirror_index + width - 1
    if left_col_index < 0 or right_col_index >= len(pattern_lines[0]):
        return True
    if [pattern_lines[i][left_col_index] for i in range(len(pattern_lines))] != [pattern_lines[i][right_col_index] for i in range(len(pattern_lines))]:
        return False
    else:
        return check_y_mirror(pattern_lines, y_mirror_index, width + 1)


x_mirrors = []
y_mirrors = []

for pattern in patterns:
    lines = pattern.splitlines()
    rocks_coordinates = []
    for x_index, y_index in itertools.product(range(len(lines)), range(len(lines[0]))):
        if lines[x_index][y_index] == "#":
            rocks_coordinates.append((x_index, y_index))

    for x_mirror in range(1, len(lines)):
        if check_x_mirror(lines, x_mirror, 0):
            x_mirrors.append(x_mirror)

    for y_mirror in range(1, len(lines[0])):
        if check_y_mirror(lines, y_mirror, 0):
            y_mirrors.append(y_mirror)

print(100*sum(x_mirrors) + sum(y_mirrors))
