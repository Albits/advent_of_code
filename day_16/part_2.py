# Energyzing status: .NESW

with open("puzzle_input.txt") as input_file:
    puzzle_input = input_file.read()

r"""N E S W
/  E N W S
\  W S E N
|  N NS S NS
-  EW E EW W
"""
directions = "NESW"
grid_elements = r"./\|-"
new_directions = [
    ["N", "E", "S", "W"],
    ["E", "N", "W", "S"],
    ["W", "S", "E", "N"],
    ["N", ["N", "S"], "S", ["N", "S"]],
    [["E", "W"], "E", ["E", "W"], "W"]
]

lines = puzzle_input.splitlines()


class Beam:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y


def advance_beam(beam: Beam):
    if beam.direction == "N":
        beam.x -= 1
    elif beam.direction == "E":
        beam.y += 1
    elif beam.direction == "S":
        beam.x += 1
    elif beam.direction == "W":
        beam.y -= 1


def update_grid_status(beam: Beam, grid_status):
    if 0 <= beam.x < len(grid_status) and 0 <= beam.y < len(grid_status[0]) and beam.direction not in grid_status[beam.x][beam.y]:
        grid_status[beam.x][beam.y] += beam.direction
        return False
    else:
        return True


def iterate_beams(beams: list[Beam], grid_status):
    popping_list = []
    pushing_list = []
    for beam_index, beam in enumerate(beams):
        advance_beam(beam)
        if update_grid_status(beam, grid_status):
            popping_list.append(beam_index)
        else:
            grid_element = lines[beam.x][beam.y]
            new_direction = new_directions[grid_elements.index(grid_element)][directions.index(beam.direction)]
            beam.direction = new_direction[0]
            if len(new_direction) == 2:
                pushing_list.append(Beam(new_direction[1], beam.x, beam.y))

    for beam_index in reversed(popping_list):
        beams.pop(beam_index)
    for beam in pushing_list:
        beams.append(beam)


def iterate_beam(origin_beam):
    x_size = len(lines)
    y_size = len(lines[0])

    grid_status = [["." for _ in range(y_size)] for _ in range(x_size)]
    beams = [origin_beam]

    while len(beams) > 0:
        iterate_beams(beams, grid_status)

    num_energized = 0
    for line in grid_status:
        for character in line:
            num_energized += 1 if len(character) > 1 else 0
    return num_energized


def main():
    east_initial_beams = [Beam("E", x_index, -1) for x_index in range(len(lines))]
    south_initial_beams = [Beam("S", -1, y_index) for y_index in range(len(lines[0]))]
    west_initial_beams = [Beam("W", x_index, len(lines[0])) for x_index in range(len(lines))]
    north_initial_beams = [Beam("N", x_index, len(lines)) for x_index in range(len(lines[0]))]

    initial_beams = east_initial_beams + south_initial_beams + west_initial_beams + north_initial_beams
    max_energized = 0
    for initial_beam in initial_beams:
        max_energized = max(max_energized, iterate_beam(initial_beam))
    print(max_energized)


if __name__ == '__main__':
    main()
