import itertools
from copy import deepcopy

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


workflows_str, _ = puzzle_input.split("\n\n")
workflows = {}
for workflow in workflows_str.splitlines():
    key, rules = workflow.split("{")
    rules = rules[:-1]
    rules = rules.split(",")
    workflows[key] = rules

parts_ranges = {
    "x": [1, 4000],
    "m": [1, 4000],
    "a": [1, 4000],
    "s": [1, 4000],
    "next_workflow": "in"
}

ranges_to_test = [parts_ranges]
accepted_ranges = []


while len(ranges_to_test) > 0:
    new_ranges = []
    for test_range in ranges_to_test:
        rules = workflows[test_range["next_workflow"]]
        for rule in rules:
            result = rule.split(":")
            if len(result) == 1:
                destination = result[0]
                if destination == "A":
                    accepted_ranges.append(test_range)
                elif destination not in "AR":
                    test_range["next_workflow"] = result[0]
                    new_ranges.append(test_range)
                break
            condition, destination = result
            characteristic = condition[0]
            op = condition[1]
            value = int(condition[2:])
            new_range = deepcopy(test_range)
            if op == "<":
                new_range[characteristic][1] = value - 1
                test_range[characteristic][0] = value
            elif op == ">":
                new_range[characteristic][0] = value + 1
                test_range[characteristic][1] = value
            if destination not in "AR":
                new_range["next_workflow"] = destination
                new_ranges.append(new_range)
            elif destination == "A":
                accepted_ranges.append(new_range)
    ranges_to_test = new_ranges

total_sum = 0
for accepted_range in accepted_ranges:
    cum_prod = 1
    for key in "xmas":
        cum_prod *= accepted_range[key][1] - accepted_range[key][0] + 1
    total_sum += cum_prod
print(total_sum)
