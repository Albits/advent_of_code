from day_4_input import value as input_values

lines = input_values.splitlines()
num_original_cards = len(lines)
num_cards = [1] * num_original_cards
total_num_cards = 0

for line_index, line in enumerate(lines):
    winning_numbers, card_numbers = line.split(": ")[1].split("|")
    winning_numbers = winning_numbers.split()
    card_numbers = card_numbers.split()
    num_matches = 0
    for card_number in card_numbers:
        num_matches += 1 if card_number in winning_numbers else 0
    for i in range(num_matches):
        num_cards[line_index + i + 1] += num_cards[line_index]
    total_num_cards += num_cards[line_index]

print(total_num_cards)
