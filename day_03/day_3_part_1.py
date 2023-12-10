import re

from day_3_input import value as input_value


# Get symbols
symbols = []
for character in input_value:
    if not character.isdigit() and character not in ("\n", ".") and character not in symbols:
        symbols.append(character)

lines = input_value.splitlines()
symbols_indices = []
for x_index, line in enumerate(lines):
    for y_index, character in enumerate(line):
        if character in symbols:
            symbols_indices.append((x_index, y_index))

result_sum = 0
for x_index, line in enumerate(lines):
    find_iterator = re.finditer("[0-9]+", line)
    for found_number in find_iterator:
        start_index, end_index = found_number.span()
        for symbol_index in symbols_indices:
            if x_index - 1 <= symbol_index[0] <= x_index + 1 and start_index -1 <= symbol_index[1] <= end_index:
                result_sum += int(found_number.group())

print(result_sum)
