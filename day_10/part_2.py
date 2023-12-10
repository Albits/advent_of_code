from puzzle_input import value as puzzle_input
import itertools

lines = puzzle_input.splitlines()

line_length = len(lines[0])

start_index = puzzle_input.index("S")
# Take into accound EOL characters
begin_x = start_index // (line_length + 1)
begin_y = start_index % (line_length + 1)


def get_next_node(previous_x, previous_y, current_x, current_y):
    delta_x = current_x - previous_x
    delta_y = current_y - previous_y
    increment_left = 0
    increment_right = 0
    match lines[current_x][current_y]:
        case "|":
            next_x = current_x + delta_x
            next_y = current_y
        case "-":
            next_x = current_x
            next_y = current_y + delta_y
        case "L":
            next_x = current_x + delta_x - 1  # 0:-1 ; 1:0
            next_y = current_y + delta_y + 1  # -1:0 ; 0:1
        case "J":
            next_x = current_x + delta_x - 1  # 0:-1 ; 1:0
            next_y = current_y + delta_y - 1  # 1:0 ; 0:-1
        case "7":
            next_x = current_x + delta_x + 1
            next_y = current_y + delta_y - 1
        case "F":
            next_x = current_x + delta_x + 1
            next_y = current_y + delta_y + 1
        case _:
            raise ValueError("Node not valid")
    return next_x, next_y

origin_candidates = ""
if lines[begin_x + 1][begin_y] in "|LJ":
    current_x = begin_x + 1
    current_y = begin_y
    origin_candidates += "|7F"
if lines[begin_x - 1][begin_y] in "|7F":
    current_x = begin_x - 1
    current_y = begin_y
    origin_candidates += "|LJ"
if lines[begin_x][begin_y + 1] in "-J7":
    current_x = begin_x
    current_y = begin_y + 1
    origin_candidates += "-LF"
if lines[begin_x][begin_y - 1] in "-LF":
    current_x = begin_x
    current_y = begin_y - 1
    origin_candidates += "-J7"

characters = "|-LFJ7"
for character in characters:
    if origin_candidates.count(character) == 2:
        origin_character = character

pipe_map = [["." for _ in range(line_length)] for _ in range(len(lines))]

previous_x = begin_x
previous_y = begin_y

pipe_map[begin_x][begin_y] = origin_character
pipe_map[current_x][current_y] = lines[current_x][current_y]

num_steps = 1
while lines[current_x][current_y] != "S":
    pipe_map[current_x][current_y] = lines[current_x][current_y]
    temp_x, temp_y = current_x, current_y
    current_x, current_y = get_next_node(previous_x, previous_y, current_x, current_y)
    previous_x, previous_y = temp_x, temp_y
    num_steps += 1

"""
Transition matrix
state / elem .  |  -  L  7  J  F 
outside      o  i  x  oa x  x  ob
inside       i  o  x  ob x  x  oa
on_pipe_a    x  x  oa x  i  o  x   on pipe with inside above
on_pipe_b    x  x  ob x  o  i  x   on pipe with inside below
"""
characters = ".|-L7JF"

# Index on state on x elem on y
transition_matrix = [
    [0, 1, -1, 2, -1, -1, 3],
    [1, 0, -1, 3, -1, -1, 2],
    [-1, -1, 2, -1, 1, 0, -1],
    [-1, -1, 3, -1, 0, 1, -1]
]

num_inside = 0

for x_coord in range(len(lines)):
    current_state = 0
    for y_coord in range(line_length):
        current_char = pipe_map[x_coord][y_coord]
        if current_state == 1 and current_char == ".":
            pipe_map[x_coord][y_coord] = "I"
            num_inside += 1
        char_index = characters.index(current_char)
        current_state = transition_matrix[current_state][char_index]
        if current_state == -1:
            raise ValueError("Next state invalid")

for line in pipe_map:
    line_as_string = ""
    for character in line:
        line_as_string += character
    print(line_as_string)

print(num_inside)
