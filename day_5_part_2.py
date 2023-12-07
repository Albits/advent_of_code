import re
from copy import copy

from day_5_input import value as puzzle_input

lines = puzzle_input.splitlines()

seeds = [int(seed) for seed in re.findall("\d+", lines[0])]
seeds_ranges = []
for i in range(len(seeds) // 2):
    seeds_ranges.append([seeds[2 * i], seeds[2 * i + 1]])


current_map = None

seed_soil_map = []
soil_fertilizer_map = []
fertilizer_water_map = []
water_light_map = []
light_temperature_map = []
temperature_humidity_map = []
humidity_location_map = []


for line in lines:
    if line == "seed-to-soil map:":
        current_map = seed_soil_map
    elif line == "soil-to-fertilizer map:":
        current_map = soil_fertilizer_map
    elif line == "fertilizer-to-water map:":
        current_map = fertilizer_water_map
    elif line == "water-to-light map:":
        current_map = water_light_map
    elif line == "light-to-temperature map:":
        current_map = light_temperature_map
    elif line == "temperature-to-humidity map:":
        current_map = temperature_humidity_map
    elif line == "humidity-to-location map:":
        current_map = humidity_location_map

    if current_map is not None and len(regex_match := re.findall("\d+", line)) > 0:
        target_range, source_range, range_length = [int(match) for match in regex_match]
        current_map.append((source_range, range_length, target_range))


def map_ranges(input_ranges, maps):
    next_iteration_ranges = input_ranges
    output_ranges = []
    for current_map in maps:
        current_iteration_ranges = copy(next_iteration_ranges)
        next_iteration_ranges = []
        for range_index, current_range in enumerate(current_iteration_ranges):
            range_end = sum(current_range)
            map_end = sum(current_map[0:2])
            pre_length = max(0, min(range_end, current_map[0]) - current_range[0])
            effect_length = max(0, min(map_end, range_end) - max(current_map[0], current_range[0]))
            post_length = max(0, range_end - max(map_end, current_range[0]))
            if pre_length > 0:
                next_iteration_ranges.append([current_range[0], pre_length])
            if post_length > 0:
                next_iteration_ranges.append([current_range[0] + pre_length + effect_length, post_length])
            if effect_length > 0:
                output_start = current_map[2] - current_map[0] + current_range[0] + pre_length
                output_ranges.append([output_start, effect_length])
    return output_ranges + next_iteration_ranges


def get_locations(seeds_ranges):
    soils = map_ranges(seeds_ranges, seed_soil_map)
    fertilizers = map_ranges(soils, soil_fertilizer_map)
    waters = map_ranges(fertilizers, fertilizer_water_map)
    lights = map_ranges(waters, water_light_map)
    temperatures = map_ranges(lights, light_temperature_map)
    humidities = map_ranges(temperatures, temperature_humidity_map)
    locations = map_ranges(humidities, humidity_location_map)
    return locations


output_ranges = get_locations(seeds_ranges)
output_ranges.sort(key=lambda elem: elem[0])

print(output_ranges[0][0])
