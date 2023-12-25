import itertools
from math import sqrt, isclose

import sympy

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

hailstones = []
for line in puzzle_input.splitlines():
    pos, speed = line.split(" @ ")
    pos = tuple(int(val) for val in pos.split(","))
    speed = tuple(int(val) for val in speed.split(","))
    hailstones.append((pos, speed))

count = 0

xr, yr, zr, dxr, dyr, dzr = sympy.symbols("xr, yr, zr, dxr, dyr, dzr")

equations = []

for h in hailstones:
    x0, y0, z0 = h[0]
    dx, dy, dz = h[1]
    equations.append((xr - x0) * (dy - dyr) - (yr - y0) * (dx - dxr))
    equations.append((xr - x0) * (dz - dzr) - (zr - z0) * (dx - dxr))

solution = sympy.solve(equations)[0]
print(solution[xr] + solution[yr] + solution[zr])
