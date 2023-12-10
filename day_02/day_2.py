import re

from day_2_input import value as input_values


lines = input_values.splitlines()
num_red = 12
num_green = 13
num_blue = 14

result_sum = 0

for line in lines:
    line = line.replace("Game ", "")
    line = line.replace(":", ";")
    tokens = line.split(";")
    game_number = tokens.pop(0)
    game_valid = True
    min_red = 0
    min_green = 0
    min_blue = 0
    for current_search in tokens:
        current_red_find = re.search("([0-9]+) red", current_search)
        if current_red_find is not None:
            current_red = int(current_red_find.groups()[0])
        else:
            current_red = 0
        current_green_find = re.search("([0-9]+) green", current_search)
        if current_green_find is not None:
            current_green = int(current_green_find.groups()[0])
        else:
            current_green = 0
        current_blue_find = re.search("([0-9]+) blue", current_search)
        if current_blue_find is not None:
            current_blue = int(current_blue_find.groups()[0])
        else:
            current_blue = 0
        min_red = max(min_red, current_red)
        min_green = max(min_green, current_green)
        min_blue = max(min_blue, current_blue)
    game_power = min_red * min_green * min_blue
    result_sum += game_power

print(result_sum)
