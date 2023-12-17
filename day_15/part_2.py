from puzzle_input import value as puzzle_input


def aoc_hash(input_string: str):
    hash_value = 0
    for character in input_string:
        hexa_char = bytes(character, "ascii").hex()
        int_char = int(hexa_char, base=16)
        hash_value += int_char
        hash_value *= 17
        hash_value %= 256
    return hash_value


sequence_steps = puzzle_input.split(",")


# Box list: [{label: focal_length}, ...]
box_list = [{} for _ in range(256)]
for step in sequence_steps:
    separator = "-" if "-" in step else "="
    label, focal_length = step.split(separator)
    focal_length = int(focal_length) if separator == "=" else None
    target_box = aoc_hash(label)
    if separator == "=":
        box_list[target_box][label] = focal_length
    elif separator == "-":
        try:
            box_list[target_box].pop(label)
        except KeyError:
            pass

result = 0
for box_index, box in enumerate(box_list):
    for lens_index, focal_length in enumerate(box.values()):
        result += (box_index + 1)*(lens_index + 1)*focal_length

print(result)
