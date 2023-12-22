import itertools
from math import inf
from copy import deepcopy

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


lines = puzzle_input.splitlines()
bricks_snapshot = []
x_min = inf
x_max = 0
y_min = inf
y_max = 0
for line in lines:
    start, end = line.split("~")
    s_x, s_y, s_z = (int(val) for val in start.split(","))
    e_x, e_y, e_z = (int(val) for val in end.split(","))
    assert s_z <= e_z, f"Error for coordinates {s_x}, {s_y}, {s_z}"
    x_min = min(x_min, s_x, e_x)
    x_max = max(x_max, s_x, e_x)
    y_min = min(y_min, s_y, e_y)
    y_max = max(y_max, s_y, e_y)
    bricks_snapshot.append((s_x, e_x, s_y, e_y, s_z, e_z - s_z + 1))

bricks_snapshot.sort(key=lambda elem: elem[4])

assert x_min == y_min == 0

# height, brick number for each "highest floor"
stack_status = [[[0, None] for _ in range(y_max + 1)] for _ in range(x_max + 1)]

# brick number: (coords, bricks_below, supports)
landed_bricks = {}

for brick_index, brick in enumerate(bricks_snapshot):
    stack_span_x = range(brick[0], brick[1] + 1)
    stack_span_y = range(brick[2], brick[3] + 1)
    stack_top = 0
    bricks_below = []
    for x, y in itertools.product(stack_span_x, stack_span_y):
        stack_top = max(stack_top, stack_status[x][y][0])

    for x, y in itertools.product(stack_span_x, stack_span_y):
        if stack_status[x][y][1] not in (*bricks_below, None) and landed_bricks[stack_status[x][y][1]][4] == stack_top:
            bricks_below.append(stack_status[x][y][1])

    landed_bricks[brick_index] = (brick[0], brick[1], brick[2], brick[3], stack_top + brick[5], brick[5], bricks_below, [])

    for x, y in itertools.product(stack_span_x, stack_span_y):
        stack_status[x][y] = [stack_top + brick[5], brick_index]

for brick_index, brick in landed_bricks.items():
    for supporting_brick_index in brick[6]:
        landed_bricks[supporting_brick_index][7].append(brick_index)


def count_disintegration(brick_index, mod_landed_bricks):
    brick = mod_landed_bricks[brick_index]
    disintegration_count = 0
    for supported_brick_index in brick[7]:
        mod_landed_bricks[supported_brick_index][6].pop(mod_landed_bricks[supported_brick_index][6].index(brick_index))
        if len(mod_landed_bricks[supported_brick_index][6]) == 0:
            disintegration_count += 1
            disintegration_count += count_disintegration(supported_brick_index, mod_landed_bricks)
    return disintegration_count


total_disintegration_count = 0
for brick_index, brick in landed_bricks.items():
    modified_landed_bricks = deepcopy(landed_bricks)
    total_disintegration_count += count_disintegration(brick_index, modified_landed_bricks)

print(total_disintegration_count)
