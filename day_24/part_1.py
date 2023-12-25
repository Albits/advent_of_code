import itertools


with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

hailstones = []
for line in puzzle_input.splitlines():
    pos, speed = line.split(" @ ")
    pos = (int(val) for val in pos.split(","))
    speed = (int(val) for val in speed.split(","))
    hailstones.append((*pos, *speed))

test_area_low = 200000000000000
test_area_high = 400000000000000

count = 0

for h1, h2 in itertools.combinations(hailstones, 2):
    h1_a = h1[4] / h1[3]
    h1_b = h1[1] - h1_a*h1[0]

    h2_a = h2[4] / h2[3]
    h2_b = h2[1] - h2_a*h2[0]

    if h1_a != h2_a:
        crossing_x = (h2_b - h1_b) / (h1_a - h2_a)
        crossing_y = h1_a * crossing_x + h1_b

        if (crossing_x - h1[0]) * h1[3] > 0 and (crossing_x - h2[0]) * h2[3] > 0:
            if test_area_low <= crossing_x < test_area_high and test_area_low <= crossing_y < test_area_high:
                count += 1

print(count)
