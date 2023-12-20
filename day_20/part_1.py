with open("sample_input.txt") as input_file:
    puzzle_input = input_file.read()


class FlipFlop:
    def __init__(self):
        self.input = False
        self.state = False

    def process(self):
        signal = self.input
        if self.state == signal:
            self.state = not self.state
            return self.state
        return signal

    def add_input(self, input_name):
        pass

    def set_input(self, _, input_value):
        self.input = input_value


class Conjunction:
    def __init__(self):
        self.inputs = {}
        self.state = {}

    def process(self):
        for key in self.inputs.keys():
            self.state[key] = self.inputs[key]
        if all(self.state.values()):
            return False
        else:
            return True

    def add_input(self, input_name):
        self.inputs[input_name] = False
        self.state[input_name] = False

    def set_input(self, input_name, input_value):
        self.inputs[input_name] = input_value


graph = {}
# Build graph
for line in puzzle_input.splitlines():
    extract = line.split()
    name = extract[0]
    destinations = extract[2:]
    destinations = [destination.replace(",", "") for destination in destinations]

    if name == "broadcaster":
        broadcaster = destinations
        continue

    node_type = name[0]
    node_name = name[1:]
    if node_type == "%":
        graph[node_name] = (FlipFlop(), destinations)
    elif node_type == "&":
        graph[node_name] = (Conjunction(), destinations)

for destination in broadcaster:
    graph[destination][0].add_input("broadcaster")

for key, value in graph.items():
    destinations = value[1]
    for destination in destinations:
        graph[destination][0].add_input(key)


def get_state(graph):
    return [item[0].state for item in graph.values()]


def process_one_push():
    process_queue = []
    new_process_queue = []
    for destination in broadcaster:
        graph[destination][0].set_input("broadcaster", False)
        process_queue.append(destination)
    for elem in process_queue:
        result = graph[elem][0].process()
    process_queue = new_process_queue
    state_before = get_state(graph)
    state_after = None
    while state_before != state_after:
        state_before = get_state(graph)
        print(state_before)
        new_process_queue = []
        for elem in process_queue:
            result = graph[elem][0].process()
            for destination in graph[elem][1]:
                graph[destination][0].set_input(elem, result)
                new_process_queue.append(destination)
        state_after = get_state(graph)
        process_queue = new_process_queue

# Process once
print(get_state(graph))
process_one_push()
print(get_state(graph))

# print(graph)
