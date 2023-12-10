import re

from day_3_input import value as input_value


class Star:
    def __init__(self, x_index, y_index):
        self.x_index = x_index
        self.y_index = y_index
        self.num_adjacent_numbers = 0
        self.adjacent_numbers = []


lines = input_value.splitlines()
stars = []
for x_index, line in enumerate(lines):
    for y_index, character in enumerate(line):
        if character == "*":
            stars.append(Star(x_index, y_index))

for x_index, line in enumerate(lines):
    find_iterator = re.finditer("[0-9]+", line)
    for found_number in find_iterator:
        start_index, end_index = found_number.span()
        for star in stars:
            if x_index - 1 <= star.x_index <= x_index + 1 and start_index -1 <= star.y_index <= end_index:
                star.num_adjacent_numbers += 1
                star.adjacent_numbers.append(int(found_number.group()))

result_sum = 0
for star in stars:
    if star.num_adjacent_numbers == 2:
        result_sum += star.adjacent_numbers[0] * star.adjacent_numbers[1]

print(result_sum)
