import re
from math import inf

from day_8_input import value as puzzle_input

lines = puzzle_input.splitlines()

instructions = lines[0]
nodes = []
directions = []
for line in lines:
    nodes_values = re.findall("[A-Z]{3}", line)
    if len(nodes_values) == 3:
        nodes.append(nodes_values[0])
        directions.append((nodes_values[1], nodes_values[2]))

current_node_index = nodes.index("AAA")
instruction_index = 0
steps_taken = 0

while nodes[current_node_index] != "ZZZ":
    instruction = instructions[instruction_index]
    if instruction == "L":
        current_node_index = nodes.index(directions[current_node_index][0])
    else:
        current_node_index = nodes.index(directions[current_node_index][1])
    steps_taken += 1
    instruction_index += 1
    instruction_index = instruction_index % len(instructions)

print(steps_taken)
