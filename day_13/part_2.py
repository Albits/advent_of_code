import itertools

from puzzle_input import value as puzzle_input

patterns = puzzle_input.split("\n\n")
print(patterns[0] + "\n")

patterns_rocks_coordinates = []


def get_diff(line_1, line_2):
    assert len(line_1) == len(line_2)
    num_diffs = 0
    diff_index = None
    replaced_line = ""
    for i in range(len(line_1)):
        if line_1[i] != line_2[i]:
            num_diffs += 1
            diff_index = i
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
        return True
    if pattern_lines[bot_line_index] != pattern_lines[top_line_index]:
        if smudge_remaining:
            replaced_line = get_diff(pattern_lines[top_line_index], pattern_lines[bot_line_index])
            if replaced_line is not None:
                pattern_lines[top_line_index] = replaced_line
                return check_x_mirror(pattern_lines, x_mirror_index, width + 1, False)
            else:
                return False
        else:
            return False
    else:
        return check_x_mirror(pattern_lines, x_mirror_index, width + 1, smudge_remaining)

x_mirrors = []

for pattern in patterns:
    lines = pattern.splitlines()
    rocks_coordinates = []
    for x_index, y_index in itertools.product(range(len(lines)), range(len(lines[0]))):
        if lines[x_index][y_index] == "#":
            rocks_coordinates.append((x_index, y_index))

    smudge_remaining = True
    for x_mirror in range(1, len(lines)):
        if check_x_mirror(lines, x_mirror, 0, smudge_remaining):
            smudge_remaining = False
            x_mirrors.append(x_mirror)
            print(x_mirror)

print(patterns[0])
print(100*sum(x_mirrors))
