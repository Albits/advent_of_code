import itertools
from math import sqrt

from scipy.special import h1vp

with open("sample_input.txt") as input_file:
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


other_vector = tuple(a - b for a, b in zip(hailstones[2][0], hailstones[1][0]))
normal_vector = vector_product(hailstones[1][1], other_vector)
# normal_vector = normalize(normal_vector)

plan = get_plan_coordinates(normal_vector, hailstones[1][0])
print(plan)

h1 = hailstones[0]
h2 = hailstones[4]

t1 = -(plan[0] * h1[0][0] + plan[1] * h1[0][1] + plan[2] * h1[0][2] + plan[3]) / (plan[0] * h1[1][0] + plan[1] * h1[1][1] + plan[2] * h1[1][2])
t2 = -(plan[0] * h2[0][0] + plan[1] * h2[0][1] + plan[2] * h2[0][2] + plan[3]) / (plan[0] * h2[1][0] + plan[1] * h2[1][1] + plan[2] * h2[1][2])

vect_coords = tuple((c2 + d2*t2 - c1 - d1*t1) / (t2 - t1) for c1, d1, c2, d2 in zip(*h1, *h2))
origin_coords = tuple(c + t1 * (d - dr) for c, d, dr in zip(*h1, vect_coords))
# x_coord = (h2[0][0] + h2[1][0] * t2 - h1[0][0] - h1[1][0] * t1) / (t2 - t1)
print(vect_coords)
print(origin_coords)

check_pos = (24, 13, 10)
check_vect = (-3, 1, 2)

print(check_pos[0] * plan[0] + check_pos[1] * plan[1] + check_pos[2] * plan[2] + plan[3])
print(dot_product(normal_vector, check_vect))
print(t1, t2)
