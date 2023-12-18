with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


directions = {3: (-1, 0), 1: (1, 0), 2: (0, -1), 0: (0, 1)}

lines = puzzle_input.splitlines()
polygon = [(0, 0)]
boundary_length = 0
for line in lines:
    _, _, color = line.split()
    color = color[1:-1]
    direction = int(color[-1])
    steps = int(color[1:-1], base=16)
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
