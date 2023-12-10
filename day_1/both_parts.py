import re

from puzzle_input import values as input_values


def spelled_to_int(number):
    match number:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case "zero":
            return "0"


def flip_string(input_string):
    output_string = ""
    for character in input_string:
        output_string = character + output_string
    return output_string


lines = input_values.splitlines()

result_sum = 0

forward_regex = "one|two|three|four|five|six|seven|eight|nine|zero"
backward_regex = flip_string(forward_regex)
print(backward_regex)

for line in lines:
    forward_numbers = re.findall(f"{forward_regex}|[0-9]", line)
    backward_numbers = re.findall(f"{backward_regex}|[0-9]", flip_string(line))
    result = ""
    if len(forward_numbers) > 0:
        result += forward_numbers[0] if forward_numbers[0].isdigit() else spelled_to_int(forward_numbers[0])
    if len(backward_numbers) > 0:
        result += backward_numbers[0] if backward_numbers[0].isdigit() else spelled_to_int(flip_string(backward_numbers[0]))
    result_sum += int(result)

print(result_sum)
