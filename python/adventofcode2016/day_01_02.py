from .common import data
from .common.timing import print_timing_data

from itertools import izip, cycle


def easter_bunny_location(data_tokens):
    pos = [0, 0]

    translate_direction = {
        'L': -1,
        'R': +1,
    }

    orientations = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]

    current_orientation = 0
    visited = set()

    for movement, dimension in izip(data_tokens, cycle((0, 1))):
        direction = movement[0]
        distance = int(movement[1:])

        if current_orientation % 2 == 0:
            to_move = [orientations[current_orientation][0] * translate_direction[direction] * distance, 0]
        else:
            to_move = [0, orientations[current_orientation][1] * translate_direction[direction] * distance]

        if to_move[1] == 0:
            dimension = 0
        else:
            dimension = 1

        moved = 0

        if to_move[dimension] > 0:
            move_direction = 1
        else:
            move_direction = -1

        while to_move[dimension] != moved:
            moved += move_direction
            new_pos = pos[:]
            new_pos[dimension] += moved

            new_pos = tuple(new_pos)

            if new_pos in visited:
                return abs(new_pos[0]) + abs(new_pos[1])

            visited.add(new_pos)

        pos[0] += to_move[0]
        pos[1] += to_move[1]

        current_orientation = (current_orientation + translate_direction[direction]) % 4

    raise Exception('Solution not found')


def get_test_data():
    return (
        (
            ('R8', 'R4', 'R4', 'R8'),
            4,
        ),
    )


def run_test_data():
    for idx, (tokens, expected) in enumerate(get_test_data()):
        with print_timing_data('test data {}'.format(idx)):
            result = easter_bunny_location(tokens)

        print 'Test {}: Excepted {}, Actual {}'.format(idx, expected, result)


def run_solution():
    tokens = data.get_data_content(1, 1).split(', ')

    with print_timing_data('Solution'):
        result = easter_bunny_location(tokens)

    print 'Solution: {}'.format(result)


def main():
    run_test_data()
    run_solution()


if __name__ == '__main__':
    main()
