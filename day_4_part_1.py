from day_4_input import value as input_values

lines = input_values.splitlines()
result_sum = 0

for line in lines:
    winning_numbers, card_numbers = line.split(": ")[1].split("|")
    winning_numbers = winning_numbers.split()
    card_numbers = card_numbers.split()
    num_matches = 0
    for card_number in card_numbers:
        num_matches += 1 if card_number in winning_numbers else 0
    score = 2**(num_matches - 1) if num_matches > 0 else 0
    result_sum += score

print(result_sum)
