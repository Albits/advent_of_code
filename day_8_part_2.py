import re
from math import lcm

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

end_with_a_indices = [i for i in range(len(nodes)) if nodes[i].endswith("A")]


def get_loop_length(ghost_index):
    loop_index = 0
    current_node_index = end_with_a_indices[ghost_index]
    instruction_index = 0
    while not nodes[current_node_index].endswith("Z"):
        instruction = instructions[instruction_index]
        if instruction == "L":
            current_node_index = nodes.index(directions[current_node_index][0])
        else:
            current_node_index = nodes.index(directions[current_node_index][1])
        loop_index += 1
        instruction_index += 1
        instruction_index = instruction_index % len(instructions)
    return loop_index


loop_lengths = [get_loop_length(ghost_index) for ghost_index in range(len(end_with_a_indices))]

print(lcm(*loop_lengths))
