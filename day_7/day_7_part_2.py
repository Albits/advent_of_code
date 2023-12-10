import re

from day_7_input import value as puzzle_input


card_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

class Card:
    def __init__(self, string_value, bid):
        self.string_value = string_value
        self.bid = int(bid)
        self.groups = []

        for card in self.string_value:
            card_assigned = False
            for group_index, group in enumerate(self.groups):
                if card in group and card != "J":
                    self.groups[group_index] = group + card
                    card_assigned = True
            if not card_assigned and card != "J":
                self.groups.append(card)
        num_jokers = self.string_value.count("J")
        self.groups.sort(key=lambda elem: len(elem), reverse=True)
        if len(self.groups) > 0:
            self.groups[0] += "J"*num_jokers
        else:
            self.groups = ["J" * num_jokers]

    def __lt__(self, other):
        num_groups = len(self.groups)
        other_num_groups = len(other.groups)
        if num_groups != other_num_groups:
            return num_groups > other_num_groups
        # Identical number of groups: the one with the biggest group wins
        biggest_group = max([len(group) for group in self.groups])
        other_biggest_group = max([len(group) for group in other.groups])
        if biggest_group != other_biggest_group:
            return biggest_group < other_biggest_group
        # Identical hand type: find first with greatest card number
        for card, other_card in zip(self.string_value, other.string_value):
            if card != other_card:
                return card_order.index(card) < card_order.index(other_card)


lines = puzzle_input.splitlines()
cards = [Card(*line.split(" ")) for line in lines]
cards.sort()

score = 0
for card_index, card in enumerate(cards):
    score += (card_index + 1) * card.bid

print(score)
