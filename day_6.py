import re
from math import sqrt, floor, ceil

from day_6_input import value as puzzle_input

lines = puzzle_input.splitlines()

times = [int(time_value) for time_value in re.findall("\d+", lines[0])]
records = [int(distance_value) for distance_value in re.findall("\d+", lines[1])]


def get_winning_ways(time, record):
    high_win = (time + sqrt(time ** 2 - 4 * record)) / 2.0
    low_win = (time - sqrt(time ** 2 - 4 * record)) / 2.0
    num_winning_ways = floor(high_win) - ceil(low_win) + 1
    return num_winning_ways


result = 1
for time, record in zip(times, records):
    result *= get_winning_ways(time, record)

print(f"First part solution: {result}")

real_time = ""
real_record = ""
for time, record in zip(times, records):
    real_time += str(time)
    real_record += str(record)
real_time = int(real_time)
real_record = int(real_record)

print(f"Second part solution: {get_winning_ways(real_time, real_record)}")
