with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


workflows_str, parts_str = puzzle_input.split("\n\n")
workflows = {}
for workflow in workflows_str.splitlines():
    key, rules = workflow.split("{")
    rules = rules[:-1]
    rules = rules.split(",")
    workflows[key] = rules

parts = []
for part in parts_str.splitlines():
    characteristics = part[1:-1].split(",")
    part_dict = {}
    for characteristic in characteristics:
        key, value = characteristic.split("=")
        part_dict[key] = int(value)
    parts.append(part_dict)

total_score = 0
for part in parts:
    next_workflow = "in"
    while next_workflow not in "AR":
        rules = workflows[next_workflow]
        for rule in rules:
            x, m, a, s = part["x"], part["m"], part["a"], part["s"]
            result = rule.split(":")
            if len(result) == 1:
                next_workflow = result[0]
                break
            else:
                rule, next_workflow = result
            if eval(rule):
                break
            else:
                continue
    if next_workflow == "A":
        total_score += sum([value for value in part.values()])

print(total_score)
