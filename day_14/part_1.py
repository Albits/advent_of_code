import itertools
from copy import copy

from puzzle_input import value as puzzle_input

lines = puzzle_input.splitlines()

# Rotate so that north is on the right
rotated_lines = [""] * len(lines[0])
for column_index in range(len(lines)):
    for row_index in range(len(lines[0])):
        rotated_lines[row_index] += lines[-column_index-1][row_index]

# Roll balls and compute load
total_load = 0
for line in rotated_lines:
    rocks = line.split("#")
    shifted = ""
    for rock_block in rocks:
        num_balls = rock_block.count("O")
        num_points = len(rock_block) - num_balls
        shifted += "." * num_points + "O" * num_balls
        shifted += "#"
    shifted = shifted[:-1]
    for i in range(len(shifted)):
        if shifted[i] == "O":
            total_load += i + 1

print(total_load)
