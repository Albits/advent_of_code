import itertools
from math import sqrt, isclose

from scipy.special import h1vp

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

hailstones = []
for line in puzzle_input.splitlines():
    pos, speed = line.split(" @ ")
    pos = tuple(int(val) for val in pos.split(","))
    speed = tuple(int(val) for val in speed.split(","))
    hailstones.append((pos, speed))

count = 0


def vector_product(vect_1, vect_2):
    x = vect_1[1] * vect_2[2] - vect_1[2] * vect_2[1]
    y = vect_1[2] * vect_2[0] - vect_1[0] * vect_2[2]
    z = vect_1[0] * vect_2[1] - vect_1[1] * vect_2[0]

    return x, y, z


def dot_product(vect_1, vect_2):
    return sum(a*b for b, a in zip(vect_1, vect_2))


def get_plan_coordinates(normal_coords, point_coords):
    d = - sum(n*p for n, p in zip(normal_coords, point_coords))
    return *normal_coords, d


def normalize(vector):
    x = vector[0] / sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    y = vector[1] / sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    z = vector[2] / sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    return x, y, z


def crossing(h1, h2):
    x1, y1, z1 = h1[0]
    dx1, dy1, dz1 = h1[1]
    x2, y2, z2 = h2[0]
    dx2, dy2, dz2 = h2[1]

    try:
        left_term = (dx2 - dy2) / (dx1 - dy1) * ((y1 - y2) / dy2 - (x1 - x2) / dx2)
        right_term = (dx2 - dz2) / (dx1 - dz1) * ((z1 - z2) / dz2 - (x1 - x2) / dx2)
    except ZeroDivisionError:
        return False

    return isclose(left_term, right_term)


# Find two parallel vectors
solution_found = False
for h1, h2 in itertools.combinations(hailstones, 2):
    if isclose(abs(h1[1][0] / h2[1][0]), (h1[1][1] / h2[1][1])) and isclose(abs(h1[1][1] / h2[1][1]), (h1[1][2] / h2[1][2])):
        print("Parallel found")
        solution_found = True
        break
    elif crossing(h1, h2):
        print("Crossing found")
        solution_found = True
        break


assert solution_found, "Solution not found"

other_vector = tuple(a - b for a, b in zip(h1[0], h2[0]))
normal_vector = vector_product(h1[1], other_vector)
# normal_vector = normalize(normal_vector)

plan = get_plan_coordinates(normal_vector, hailstones[1][0])
print(plan)

forbidden_indices = [hailstones.index(h1), hailstones.index(h2)]
forbidden_indices.sort()
other_h1 = hailstones[forbidden_indices[0] - 1]
other_h2 = hailstones[forbidden_indices[1] + 1]
# h1 = hailstones[0]
# h2 = hailstones[4]

t1 = -(plan[0] * other_h1[0][0] + plan[1] * other_h1[0][1] + plan[2] * other_h1[0][2] + plan[3]) / (plan[0] * other_h1[1][0] + plan[1] * other_h1[1][1] + plan[2] * other_h1[1][2])
t2 = -(plan[0] * other_h2[0][0] + plan[1] * other_h2[0][1] + plan[2] * other_h2[0][2] + plan[3]) / (plan[0] * other_h2[1][0] + plan[1] * other_h2[1][1] + plan[2] * other_h2[1][2])

vect_coords = tuple((c2 + d2*t2 - c1 - d1*t1) / (t2 - t1) for c1, d1, c2, d2 in zip(*other_h1, *other_h2))
origin_coords = tuple(c + t1 * (d - dr) for c, d, dr in zip(*other_h1, vect_coords))
print(vect_coords)
print(origin_coords)

check_pos = (24, 13, 10)
check_vect = (-3, 1, 2)

print(check_pos[0] * plan[0] + check_pos[1] * plan[1] + check_pos[2] * plan[2] + plan[3])
print(dot_product(normal_vector, check_vect))
print(t1, t2)
