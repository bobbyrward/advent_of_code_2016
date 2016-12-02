from .common import data
from .common.timing import print_timing_data

from itertools import izip, cycle


def easter_bunny_distance(data_tokens):
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

    for movement, dimension in izip(data_tokens, cycle((0, 1))):
        direction = movement[0]
        distance = int(movement[1:])

        if current_orientation % 2 == 0:
            pos[0] += orientations[current_orientation][0] * translate_direction[direction] * distance
        else:
            pos[1] += orientations[current_orientation][1] * translate_direction[direction] * distance

        current_orientation = (current_orientation + translate_direction[direction]) % 4

    return abs(pos[0]) + abs(pos[1])


def get_test_data():
    return (
        (
            ('R2', 'R3'),
            5
        ),
        (
            ('R2', 'R2', 'R2'),
            2
        ),
        (
            ('R5', 'L5', 'R5', 'R3'),
            12
        ),
    )


def run_test_data():
    for idx, (tokens, expected) in enumerate(get_test_data()):
        with print_timing_data('test data {}'.format(idx)):
            result = easter_bunny_distance(tokens)

        print 'Test {}: Excepted {}, Actual {}'.format(idx, expected, result)


def run_solution():
    tokens = data.get_data_content(1, 1).split(', ')

    with print_timing_data('Solution'):
        result = easter_bunny_distance(tokens)

    print 'Solution: {}'.format(result)


def main():
    run_test_data()
    run_solution()


if __name__ == '__main__':
    main()
