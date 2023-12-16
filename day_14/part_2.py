from puzzle_input import value as puzzle_input

lines = puzzle_input.splitlines()

# Rotate so that north is on the right
def rotate(lines):
    rotated_lines = [""] * len(lines[0])
    for column_index in range(len(lines)):
        for row_index in range(len(lines[0])):
            rotated_lines[row_index] += lines[-column_index-1][row_index]
    return rotated_lines


# Roll balls
def roll(lines):
    total_load = 0
    shifted_lines = []
    for line in lines:
        rocks = line.split("#")
        shifted = ""
        for rock_block in rocks:
            num_balls = rock_block.count("O")
            num_points = len(rock_block) - num_balls
            shifted += "." * num_points + "O" * num_balls
            shifted += "#"
        shifted = shifted[:-1]
        shifted_lines.append(shifted)
    return shifted_lines


# Compute load
def get_load(lines):
    load = 0
    for line in lines:
        for i in range(len(line)):
            if line[i] == "O":
                load += i + 1
    return load


lines = rotate(lines)
loads_history = {}
for i in range(200):
    for j in range(4):
        lines = roll(lines)
        lines = rotate(lines)
    load = get_load(lines)
    if load not in loads_history.keys():
        loads_history[load] = [i + 1]
    else:
        loads_history[load].append(i + 1)
    # print(f"Iteration {i} done, load {load}")


# Item: [load, last_seen_index, loop_size]
likely_loads = []
for load, appearances in loads_history.items():
    if appearances[-1] > 150:
        likely_loads.append([load, appearances[-1], appearances[-1] - appearances[-2]])

num_total_cycles = 1000000000

for likely_load in likely_loads:
    if (num_total_cycles - likely_load[1]) % likely_load[2] == 0:
        print(f"load {likely_load[0]} candidate")
