import itertools

from puzzle_input import value as puzzle_input

lines = puzzle_input.splitlines()
x_length = len(lines)
y_length = len(lines[0])

insertion_x_indices = [i for i in range(x_length) if all([character == "." for character in lines[i]])]
insertion_y_indices = [i for i in range(y_length) if all([lines[j][i] == "." for j in range(y_length)])]

compensation_increment = 0
for insertion_index in insertion_x_indices:
    new_line = "." * y_length
    lines.insert(insertion_index + compensation_increment, new_line)
    compensation_increment += 1
x_length += compensation_increment

lines = [list(line) for line in lines]
compensation_increment = 0
for insertion_index in insertion_y_indices:
    for line in lines:
        line.insert(insertion_index + compensation_increment, ".")
    compensation_increment += 1
y_length += compensation_increment

galaxies = []
for x_index, y_index in itertools.product(range(x_length), range(y_length)):
    if lines[x_index][y_index] == "#":
        galaxies.append((x_index, y_index))

total_distances = 0
for first_galaxy, second_galaxy in itertools.combinations(galaxies, 2):
    total_distances += abs(first_galaxy[0] - second_galaxy[0]) + abs(first_galaxy[1] - second_galaxy[1])
print(total_distances)
