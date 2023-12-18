from math import inf

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()


class Node:
    def __init__(self, value):
        self.value = value
        self.weights = {}

    def __str__(self):
        return f"({self.value}, {min(weight for weight in self.weights.values()):3})"


class Walker:
    def __init__(self, x_coord, y_coord, direction, walk_counter=0, weight=0):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.direction = direction
        self.weight = weight
        self.walk_counter = walk_counter


def advance_walker(walker: Walker, nodes_map):
    if walker.direction == "N":
        walker.x_coord -= 1
    elif walker.direction == "E":
        walker.y_coord += 1
    elif walker.direction == "S":
        walker.x_coord += 1
    elif walker.direction == "W":
        walker.y_coord -= 1
    walker.walk_counter += 1
    if not 0 <= walker.x_coord < len(nodes_map) or not 0 <= walker.y_coord < len(nodes_map[0]) or walker.walk_counter > 10:
        return "kill"
    walker.weight += nodes_map[walker.x_coord][walker.y_coord].value
    if walker.x_coord == len(nodes_map) - 1 and walker.y_coord == len(nodes_map[0]) - 1 and walker.walk_counter < 4:
        return "kill"
    current_node = nodes_map[walker.x_coord][walker.y_coord]
    walker_key = (walker.direction, walker.walk_counter)
    if walker_key not in current_node.weights.keys() or current_node.weights[walker_key] > walker.weight:
        current_node.weights[walker_key] = walker.weight
        if walker.walk_counter < 4:
            return "continue"
        else:
            return "spawn"
    else:
        return "kill"


def iterate_walkers(walkers, node_map):
    pop_list = []
    push_list = []
    for w_index, walker in enumerate(walkers):
        result = advance_walker(walker, node_map)
        if result == "kill":
            pop_list.append(w_index)
        elif result == "spawn":
            walker_directions = "NS" if walker.direction in "WE" else "WE"
            push_list.append(Walker(walker.x_coord, walker.y_coord, walker_directions[0], weight=walker.weight))
            push_list.append(Walker(walker.x_coord, walker.y_coord, walker_directions[1], weight=walker.weight))
    for w_index in reversed(pop_list):
        walkers.pop(w_index)
    walkers += push_list


def main():
    puzzle_lines = puzzle_input.splitlines()
    nodes_map = [[Node(int(character)) for character in line] for line in puzzle_lines]
    walkers = [Walker(0, 0, "E"), Walker(0, 0, "S")]

    i = 0
    while len(walkers) > 0:
        walkers.sort(key=lambda walker: walker.weight)
        iterate_walkers(walkers, nodes_map)
        print(f"Loop {i}, {len(walkers)} walkers")
        i += 1

    for line in nodes_map:
        print([str(node) for node in line])


if __name__ == '__main__':
    main()
