from puzzle_input import value as puzzle_input

lines = puzzle_input.splitlines()

line_length = len(lines[0])

start_index = puzzle_input.index("S")
# Take into accound EOL characters
begin_x = start_index // (line_length + 1)
begin_y = start_index % (line_length + 1)


def get_next_node(previous_x, previous_y, current_x, current_y):
    delta_x = current_x - previous_x
    delta_y = current_y - previous_y
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


if lines[begin_x + 1][begin_y] in "|LJ":
    current_x = begin_x + 1
    current_y = begin_y
elif lines[begin_x - 1][begin_y] in "|7F":
    current_x = begin_x - 1
    current_y = begin_y
elif lines[begin_x][begin_y + 1] in "-J7":
    current_x = begin_x
    current_y = begin_y + 1
elif lines[begin_x][begin_y - 1] in "-LF":
    current_x = begin_x
    current_y = begin_y - 1
else:
    raise ValueError("Nowhere to go")


num_steps = 0
previous_x = begin_x
previous_y = begin_y
while lines[current_x][current_y] != "S":
    temp_x, temp_y = current_x, current_y
    current_x, current_y = get_next_node(previous_x, previous_y, current_x, current_y)
    previous_x, previous_y = temp_x, temp_y
    num_steps += 1

print((num_steps + 1) / 2)
