import re
from math import inf
from copy import copy

from day_5_input import value as puzzle_input

lines = puzzle_input.splitlines()

seeds = [int(seed) for seed in re.findall("\d+", lines[0])]
seeds_ranges = []
for i in range(len(seeds) // 2):
    seeds_ranges.append([seeds[2*i], seeds[2*i+1]])


def custom_sort(lst):
    return sorted(lst, key=lambda elem: elem[0])


seeds_ranges = custom_sort(seeds_ranges)


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

seed_soil_map = custom_sort(seed_soil_map)
soil_fertilizer_map = custom_sort(soil_fertilizer_map)
fertilizer_water_map = custom_sort(fertilizer_water_map)
water_light_map = custom_sort(water_light_map)
light_temperature_map = custom_sort(light_temperature_map)
temperature_humidity_map = custom_sort(temperature_humidity_map)
humidity_location_map = custom_sort(humidity_location_map)


def map_ranges(input_ranges, maps):
    next_iteration_ranges = input_ranges
    output_ranges = []
    for current_map in maps:
        current_iteration_ranges = copy(next_iteration_ranges)
        next_iteration_ranges = []
        for range_index, current_range in enumerate(current_iteration_ranges):
            # current_range_tmp = copy(current_range)
            # low_bound = max(current_range[0], current_map[0])
            # high_bound = min(sum(current_range), sum(current_map[0:2]))
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

            # if high_bound > low_bound:
            #     if low_bound == current_range[0] and high_bound == sum(current_range):
            #         input_ranges.pop(range_index)
            #         index_pad = 0
            #     else:
            #         current_range[1] = low_bound - current_range[0]
            #         index_pad = 1
            #     input_ranges.insert(range_index + index_pad, [low_bound, high_bound - low_bound])
            #     if high_bound < sum(current_range_tmp):
            #         input_ranges.insert(range_index + index_pad + 1, [high_bound, high_bound - current_range_tmp[1]])
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


output_ranges = custom_sort(get_locations(seeds_ranges))

print(output_ranges[0][0])
