from collections import deque
from math import lcm

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

(into_rx,) = [name for name, module in modules.items() if "rx" in module.outputs]
pre_pre_rx = [name for name, module in modules.items() if into_rx in module.outputs]
pre_pre_rx_counter = {}
for key in pre_pre_rx:
    pre_pre_rx_counter[key] = 0
count_low = 0
count_high = 0
rx_reached = False
press_counter = 0
while not all(value != 0 for value in pre_pre_rx_counter.values()):
    rx_counter = 0
    press_counter += 1
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
                queue.extend([(target, dest, new_pulse) for dest in module.outputs])
        elif module.type == "&":
            module.memory[origin] = pulse
            if all([item == "high" for item in module.memory.values()]):
                new_pulse = "low"
            else:
                new_pulse = "high"
            queue.extend([(target, dest, new_pulse) for dest in module.outputs])
        else:
            raise ValueError("No valid input")
        if origin in pre_pre_rx_counter and pulse == "high":
            pre_pre_rx_counter[origin] = press_counter

print(press_counter)
print(pre_pre_rx_counter)
print(lcm(*[value for value in pre_pre_rx_counter.values()]))
