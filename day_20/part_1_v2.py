from collections import deque

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "¨%":
            self.memory = "off"
        else:
            self.memory = {}

    def __repr__(self):
        return f"{self.name}, type={self.type}, outputs={','.join(self.outputs)}, memory={self.memory}"

modules = {}
broadcast_targets = []


for line in puzzle_input.splitlines():
    extract = line.split()
    name = extract[0]
    destinations = extract[2:]
    destinations = [destination.replace(",", "") for destination in destinations]

    if name == "broadcaster":
        broadcast_targets = destinations
    else:
        type = name[0]
        module_name = name[1:]
        modules[module_name] = Module(module_name, type, destinations)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "low"

count_low = 0
count_high = 0
for _ in range(1000):
    # Queue [origin, target, pulse]
    queue = deque([("broadcaster", dest, "low") for dest in broadcast_targets])
    count_low += len(broadcast_targets) + 1

    while queue:
        origin, target, pulse = queue.popleft()
        if target not in modules.keys():
            continue
        module = modules[target]
        if module.type == "%":
            if pulse == "low":
                module.memory = "off" if module.memory == "on" else "on"
                new_pulse = "high" if module.memory == "on" else "low"
                if new_pulse == "high":
                    count_high += len(module.outputs)
                else:
                    count_low += len(module.outputs)
                queue.extend([(target, dest, new_pulse) for dest in module.outputs])
        elif module.type == "&":
            module.memory[origin] = pulse
            if all([item == "high" for item in module.memory.values()]):
                new_pulse = "low"
                count_low += len(module.outputs)
            else:
                new_pulse = "high"
                count_high += len(module.outputs)
            queue.extend([(target, dest, new_pulse) for dest in module.outputs])
        else:
            raise ValueError("No valid input")

print(modules)
print(count_low * count_high)
