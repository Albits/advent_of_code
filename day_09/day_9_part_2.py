import re
from math import comb

from day_9_input import value as puzzle_input

lines = puzzle_input.splitlines()

numbers_sequences = []

for line in lines:
    numbers = re.findall("-?\d+", line)
    numbers = [int(number) for number in numbers]
    numbers_sequences.append(numbers)

result = 0
for number_sequence in numbers_sequences:
    sequence_length = len(number_sequence)
    current_sign = (-1)**(sequence_length-1)
    previous_value = 0
    number_sequence.reverse()
    for index, number in enumerate(number_sequence):
        previous_value += current_sign * comb(sequence_length, index) * number
        current_sign *= -1
    result += previous_value

print(result)


"""
-d+4c-6b+4a a b c d
d-4c+6b-3a b-a c-b d-c
-d+4c-5b+2a c-2b+a d-2c+b
d-3c+3b-a 
"""
