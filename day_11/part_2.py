import itertools

from puzzle_input import value as puzzle_input

lines = puzzle_input.splitlines()
x_length = len(lines)
y_length = len(lines[0])

insertion_x_indices = [i for i in range(x_length) if all([character == "." for character in lines[i]])]
insertion_y_indices = [i for i in range(y_length) if all([lines[j][i] == "." for j in range(y_length)])]

galaxies = []
for x_index, y_index in itertools.product(range(x_length), range(y_length)):
    if lines[x_index][y_index] == "#":
        galaxies.append((x_index, y_index))

total_distances = 0
for first_galaxy, second_galaxy in itertools.combinations(galaxies, 2):
    x_augment = 0
    y_augment = 0
    for insertion_index in insertion_x_indices:
        if min(first_galaxy[0], second_galaxy[0]) < insertion_index < max(first_galaxy[0], second_galaxy[0]):
            x_augment += 999999
    for insertion_index in insertion_y_indices:
        if min(first_galaxy[1], second_galaxy[1]) < insertion_index < max(first_galaxy[1], second_galaxy[1]):
            y_augment += 999999
    x_distance = abs(first_galaxy[0] - second_galaxy[0]) + x_augment
    y_distance = abs(first_galaxy[1] - second_galaxy[1]) + y_augment
    total_distances += x_distance + y_distance
print(total_distances)
