with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

lines = puzzle_input.splitlines()
polygon = [(0, 0)]
boundary_length = 0
for line in lines:
    direction, steps, color = line.split()
    steps = int(steps)
    boundary_length += steps
    # Draw polygon
    increment_v, increment_h = directions[direction]
    increment_v *= steps
    increment_h *= steps
    new_point_h = polygon[-1][0] + increment_h
    new_point_v = polygon[-1][1] + increment_v
    polygon.append((new_point_h, new_point_v))


def shoelace(vertices):
    area = 0
    for i in range(len(vertices)):
        area += vertices[i][0] * (vertices[(i + 1) % len(vertices)][1] - vertices[i - 1][1])
    return area / 2


def pick(area, boundary_length):
    return area - boundary_length / 2 + 1


polygon_area = shoelace(polygon)
inside_area = pick(polygon_area, boundary_length)
total_area = inside_area + boundary_length

print(polygon)
print(total_area)
