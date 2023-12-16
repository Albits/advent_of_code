import itertools

from puzzle_input import value as puzzle_input


lines = puzzle_input.splitlines()


def get_binary_value(start_range, end_range):
    """Get int value associated to bytes at 1 from start_range to end_range (exclusive)"""
    result = 0
    for i in range(start_range, end_range):
        result += 2**i
    return result


def get_possible_values_from_groups_sizes(groups, total_size, all_values: list, current_incremented_value):
    current_group = groups[0]
    after_groups_size = sum(groups[1:]) + len(groups)
    last_available_position = total_size - after_groups_size - current_group + 1
    for i in range(last_available_position + 1):
        current_value = get_binary_value(total_size - current_group - i, total_size - i)
        if len(groups) > 1:
            get_possible_values_from_groups_sizes(groups[1:], total_size - current_group - 1 - i, all_values, current_incremented_value + current_value)
        else:
            all_values.append(current_incremented_value + current_value)


def get_unambiguous_values(possible_values, total_size):
    mask = 2**total_size - 1
    unambiguous_springs = mask
    unambiguous_dots = mask

    for value in possible_values:
        unambiguous_springs = unambiguous_springs & value
        unambiguous_dots = unambiguous_dots & (~value & mask)

    unambiguous_springs_positions = []
    unambiguous_dots_positions = []

    for i in range(len(bin(unambiguous_springs))):
        current_index = -(i + 1)
        if bin(unambiguous_springs)[current_index] == "1":
            unambiguous_springs_positions.append(total_size + current_index)
    for i in range(len(bin(unambiguous_dots))):
        current_index = -(i + 1)
        if bin(unambiguous_dots)[current_index] == "1":
            unambiguous_dots_positions.append(total_size + current_index)

    return unambiguous_springs_positions, unambiguous_dots_positions


result = 0

for line in lines:
    spring_map, groups_sizes = line.split()
    # print(spring_map)
    map_size = len(spring_map)
    groups_sizes = [int(value) for value in groups_sizes.split(",")]
    possible_values_from_sizes = []
    get_possible_values_from_groups_sizes(groups_sizes, len(spring_map), possible_values_from_sizes, 0)
    # print([bin(value) for value in possible_values_from_sizes])
    unambiguous_springs_positions, unambiguous_dots_positions = get_unambiguous_values(possible_values_from_sizes, map_size)

    spring_map = list(spring_map)
    for index in unambiguous_springs_positions:
        spring_map[index] = "#"
    for index in unambiguous_dots_positions:
        spring_map[index] = "."

    binary_powers_springs = [map_size - i - 1 for i in range(map_size) if spring_map[i] == "#"]
    spring_value = 0
    for power in binary_powers_springs:
        spring_value += 2**power
    binary_powers_questions = [map_size - i - 1 for i in range(map_size) if spring_map[i] == "?"]
    questions_iterator_helper = [range(2)] * len(binary_powers_questions)
    possible_values_from_map = []
    for current_set in itertools.product(*questions_iterator_helper):
        current_value = 0
        for index, value in enumerate(current_set):
            current_value += 2**(binary_powers_questions[index]) * value
        possible_values_from_map.append(current_value + spring_value)

    final_possible_values = [value for value in possible_values_from_map if value in possible_values_from_sizes]
    # print([bin(value) for value in final_possible_values])
    result += len(final_possible_values)

print(result)


"""Possible values 3, 2, 1 len:
111011010000
111001101000
111000110100
111000011010
111000001101"""
