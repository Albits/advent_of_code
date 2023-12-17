import itertools

from .sample_input import value as puzzle_input


lines = puzzle_input.splitlines()


def get_memo_key(groups, total_size):
    return str(groups) + str(total_size)


memo = {}


def get_single_possible_groups(group_size, total_size):
    """Does not check bounds"""
    group = "#" * group_size
    possibilities = []
    for i in range(total_size - group_size + 1):
        possibility = "." * i + group + "." * (total_size - group_size - i)
        possibilities.append(possibility)
    return possibilities


def get_possible_values_from_groups(groups_sizes, total_size, all_values: list, current_incremented_value):
    current_group_size = groups_sizes[0]
    after_groups_size = sum(groups_sizes[1:]) + len(groups_sizes)
    last_available_position = total_size - after_groups_size - current_group_size + 1
    if len(groups_sizes) > 1:
        for i in range(last_available_position + 1):
            current_value = "." * i + "#" * current_group_size
            get_possible_values_from_groups(groups_sizes[1:], total_size - current_group_size - 1 - i, all_values, current_incremented_value + current_value + ".")
    else:
        possible_values = get_single_possible_groups(current_group_size, total_size)
        for possible_value in possible_values:
            all_values.append(current_incremented_value + possible_value)


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


def get_possible_values_from_map(spring_map, num_springs, groups_sizes):
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
        modified_groups = modified_map.split(".")
        modified_groups_sizes = [len(group) for group in modified_groups if group != ""]
        if modified_groups_sizes == groups_sizes:
            print(modified_map)
            possible_values.append(modified_map)
    return possible_values


result = 0

max_possible_from_map = 0
max_possible_from_groups = 0
for line in lines:
    # spring_map, groups_sizes = line.split()
    # groups_sizes = [int(value) for value in groups_sizes.split(",")]
    origin_map, origin_groups_sizes = line.split()
    print(origin_map)
    origin_groups_sizes = [int(value) for value in origin_groups_sizes.split(",")]
    spring_map = ""
    groups_sizes = []
    for i in range(5):
        spring_map += origin_map + "?"
        groups_sizes += origin_groups_sizes
    spring_map = spring_map[:-1]
    print(spring_map)
    print(origin_groups_sizes, groups_sizes)

    # print(f"{spring_map}, {groups_sizes}")
    # possible_values_from_map = get_possible_values_from_map(spring_map, sum(groups_sizes), groups_sizes)
    # print("Map ok")
    # possible_values_from_groups = []
    # get_possible_values_from_groups(groups_sizes, len(spring_map), possible_values_from_groups, "")
    # if len(possible_values_from_groups) > max_possible_from_groups:
    #     max_possible_from_groups = len(possible_values_from_groups)
    # print("Groups ok")
    # springs, dots = get_unambiguous_values(possible_values_from_groups)
    # print(springs, dots)
    #
    #
    # if len(possible_values_from_map) > max_possible_from_map:
    #     max_possible_from_map = len(possible_values_from_map)
    # final_possible_values = [value for value in possible_values_from_map if value in possible_values_from_groups]
    # result += len(final_possible_values)

print(result)
print(f"{max_possible_from_groups}, {max_possible_from_map}")
# print(memo)

"""
.??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##. 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3,
????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####. 1,6,5
?###??????????###??????????###??????????###??????????###???????? 3,2,1 10 possibilities -> 12 per block
"""
