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
hash_sum = 0

for step in sequence_steps:
    hash_sum += aoc_hash(step)

print(hash_sum)
