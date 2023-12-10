import re
from math import inf

from day_5_input import value as puzzle_input

lines = puzzle_input.splitlines()

seeds = [int(seed) for seed in re.findall("\d+", lines[0])]

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
        current_map.append((range(source_range, source_range + range_length), target_range))


def map_value(input_value, map):
    output_value = input_value
    for map_range, target_range in map:
        if input_value in map_range:
            output_value = input_value - map_range.start + target_range
    return output_value


def get_location(seed):
    soil = map_value(seed, seed_soil_map)
    fertilizer = map_value(soil, soil_fertilizer_map)
    water = map_value(fertilizer, fertilizer_water_map)
    light = map_value(water, water_light_map)
    temperature = map_value(light, light_temperature_map)
    humidity = map_value(temperature, temperature_humidity_map)
    location = map_value(humidity, humidity_location_map)
    return location

result = inf
for seed in seeds:
    location = get_location(seed)
    if location < result:
        result = location

print(result)
