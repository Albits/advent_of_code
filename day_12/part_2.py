import itertools

from puzzle_input import value as puzzle_input


lines = puzzle_input.splitlines()


def get_memo_key(groups, total_size):
    return str(groups) + str(total_size)


memo = {}


def get_single_possible_groups(group_size, total_size):
    pass

def get_possible_values_from_groups(groups_sizes, total_size, all_values: list, current_incremented_value):
    try:
        memo_list = memo[get_memo_key(groups_sizes, total_size)]
        for value in memo_list:
            all_values.append(current_incremented_value + value)
    except KeyError:
        pass
    current_group_size = groups_sizes[0]
    after_groups_size = sum(groups_sizes[1:]) + len(groups_sizes)
    last_available_position = total_size - after_groups_size - current_group_size + 1
    for i in range(last_available_position + 1):
        current_value = "." * i + "#" * current_group_size
        if len(groups_sizes) > 1:
            get_possible_values_from_groups(groups_sizes[1:], total_size - current_group_size - 1 - i, all_values, current_incremented_value + current_value + ".")
        else:
            set_value = current_incremented_value + current_value
            set_value = set_value + "." * (total_size - len(current_value))
            try:
                if current_value not in memo[get_memo_key(groups_sizes, total_size)]:
                    memo[get_memo_key(groups_sizes, total_size)].append(current_value)
            except KeyError:
                memo[get_memo_key(groups_sizes, total_size)] = [current_value]
            all_values.append(set_value)


def get_unambiguous_values(possible_values):
    unambiguous_springs = [i for i in range(len(possible_values[0]))]
    unambiguous_dots = [i for i in range(len(possible_values[0]))]

    for value in possible_values:
        for index, character in enumerate(value):
            if index in unambiguous_springs and character == ".":
                unambiguous_springs.pop(unambiguous_springs.index(index))
            if index in unambiguous_dots and character == "#":
                unambiguous_dots.pop(unambiguous_dots.index(index))

    return unambiguous_springs, unambiguous_dots


def get_possible_values_from_map(spring_map, num_springs):
    possible_values = []
    num_questions = spring_map.count("?")
    num_springs_in_map = spring_map.count("#")
    num_springs_to_place = num_springs - num_springs_in_map
    for springs_permutation in itertools.combinations(range(num_questions), num_springs_to_place):
        modified_map = spring_map
        for i in range(num_questions):
            if i in springs_permutation:
                modified_map = modified_map.replace("?", "#", 1)
            else:
                modified_map = modified_map.replace("?", ".", 1)
        possible_values.append(modified_map)
    return possible_values


result = 0

max_possible_from_map = 0
max_possible_from_groups = 0
for line in lines:
    spring_map, groups_sizes = line.split()
    groups_sizes = [int(value) for value in groups_sizes.split(",")]
    origin_map, origin_groups_sizes = line.split()
    origin_groups_sizes = [int(value) for value in origin_groups_sizes.split(",")]
    spring_map = ""
    groups_sizes = []
    for i in range(5):
        spring_map += origin_map + "?"
        groups_sizes += origin_groups_sizes
    spring_map = spring_map[:-1]

    print(spring_map)
    print(groups_sizes)
    map_size = len(spring_map)
    possible_values_from_groups = []
    get_possible_values_from_groups(groups_sizes, len(spring_map), possible_values_from_groups, "")
    if len(possible_values_from_groups) > max_possible_from_groups:
        max_possible_from_groups = len(possible_values_from_groups)
    # possible_values_from_map = get_possible_values_from_map(spring_map, sum(groups_sizes))
    # springs, dots = get_unambiguous_values(possible_values_from_groups)
    # if len(possible_values_from_map) > max_possible_from_map:
    #     max_possible_from_map = len(possible_values_from_map)
    # print(possible_values_from_map)
    # print(possible_values_from_sizes)

print(f"{max_possible_from_groups}, {max_possible_from_map}")
# print(memo)
