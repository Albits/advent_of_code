from day_12.puzzle_input import value as puzzle_input


lines = puzzle_input.splitlines()

memo = {}


def count_arrangements(conditions, rules):
    if not rules:
        return 0 if "#" in conditions else 1
    if not conditions:
        return 1 if not rules else 0

    if (conditions, rules) in memo.keys():
        return memo[(conditions, rules)]

    result = 0

    if conditions[0] in ".?":
        ret_value = count_arrangements(conditions[1:], rules)
        result += ret_value
    if conditions[0] in "#?":
        if (
            rules[0] <= len(conditions)
            and "." not in conditions[: rules[0]]
            and (rules[0] == len(conditions) or conditions[rules[0]] != "#")
        ):
            ret_value = count_arrangements(conditions[rules[0] + 1:], rules[1:])
            result += ret_value

    memo[(conditions, rules)] = result

    return result


solution1 = 0
solution2 = 0
for line in lines:
    conditions, rules = line.split()
    rules = eval(rules)
    solution1 += count_arrangements(conditions, rules)

    conditions = "?".join([conditions] * 5)
    rules = rules * 5
    solution2 += count_arrangements(conditions, rules)

print(memo)
print("Solution 1:", solution1)
print("Solution 2:", solution2)