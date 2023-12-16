import itertools
from copy import copy

from puzzle_input import value as puzzle_input

patterns = puzzle_input.split("\n\n")
# patterns = patterns[3:4]
# for pattern in patterns:
#     print(pattern)

patterns_rocks_coordinates = []


def rotate(pattern):
    output_pattern = [""] * len(pattern[0])
    for column_index in range(len(pattern)):
        for row_index in range(len(pattern[0])):
            output_pattern[row_index] += pattern[column_index][row_index]
    return output_pattern


def get_diff(line_1, line_2):
    assert len(line_1) == len(line_2)
    num_diffs = 0
    replaced_line = ""
    for i in range(len(line_1)):
        if line_1[i] != line_2[i]:
            num_diffs += 1
            replaced_line += "." if line_1[i] == "#" else "#"
        else:
            replaced_line += line_1[i]
    if num_diffs == 1:
        return replaced_line
    else:
        return None


def check_x_mirror(pattern_lines, x_mirror_index, width, smudge_remaining):
    top_line_index = x_mirror_index - width
    bot_line_index = x_mirror_index + width - 1
    if top_line_index < 0 or bot_line_index >= len(pattern_lines):
        return True, smudge_remaining
    if pattern_lines[bot_line_index] != pattern_lines[top_line_index]:
        if smudge_remaining:
            replaced_line = get_diff(pattern_lines[top_line_index], pattern_lines[bot_line_index])
            if replaced_line is not None:
                fixed_lines = copy(pattern_lines)
                fixed_lines[top_line_index] = replaced_line
                return check_x_mirror(fixed_lines, x_mirror_index, width + 1, False)
            else:
                return False, True
        else:
            return False, True
    else:
        return check_x_mirror(pattern_lines, x_mirror_index, width + 1, smudge_remaining)

x_mirrors = []
y_mirrors = []

for pattern in patterns:
    lines = pattern.splitlines()
    rocks_coordinates = []
    for x_index, y_index in itertools.product(range(len(lines)), range(len(lines[0]))):
        if lines[x_index][y_index] == "#":
            rocks_coordinates.append((x_index, y_index))

    smudge_remaining = True
    num_fixes = 0
    for x_mirror in range(1, len(lines)):
        result, smudge_remaining = check_x_mirror(lines, x_mirror, 0, smudge_remaining)
        if result and not smudge_remaining:
            x_mirrors.append(x_mirror)
            num_fixes += 1
    smudge_remaining = True
    new_lines = rotate(lines)
    for y_mirror in range(1, len(new_lines)):
        result, smudge_remaining = check_x_mirror(new_lines, y_mirror, 0, smudge_remaining)
        if result and not smudge_remaining:
            y_mirrors.append(y_mirror)
            num_fixes += 1
    if num_fixes == 2:
        print(f"Two fixes for indexes {x_mirrors[-1]}, {y_mirrors[-1]}")
        for line in new_lines:
            print(line)

print(len(x_mirrors))
print(len(y_mirrors))
print(len(patterns))
print(100*sum(x_mirrors) + sum(y_mirrors))
