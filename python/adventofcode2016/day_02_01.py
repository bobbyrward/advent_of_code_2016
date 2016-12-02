from .common import data
from .common.timing import print_timing_data


KEYPAD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

MOVES = {
    'U': [-1,  0],
    'D': [ 1,  0],
    'L': [ 0, -1],
    'R': [ 0,  1],
}


def keypad_code(data_tokens):
    pos = [1, 1]
    code_coords = []

    for line in data_tokens:
        print 'Next number'
        for move in line:
            translated = MOVES[move]

            new_pos = (
                pos[0] + translated[0],
                pos[1] + translated[1],
            )

            if new_pos[0] < 0 or new_pos[0] > 2:
                print 'skipped', new_pos
                continue

            if new_pos[1] < 0 or new_pos[1] > 2:
                print 'skipped', new_pos
                continue

            print move, new_pos, KEYPAD[new_pos[0]][new_pos[1]]
            pos = new_pos

        code_coords.append(pos)

    return ''.join([KEYPAD[coord[0]][coord[1]] for coord in code_coords])


def get_test_data():
    return (
        (
            (
                'ULL',
                'RRDDD',
                'LURDL',
                'UUUUD',
            ),
            '1985',
        ),
    )


def run_test_data():
    for idx, (tokens, expected) in enumerate(get_test_data()):
        with print_timing_data('test data {}'.format(idx)):
            result = keypad_code(tokens)

        print 'Test {}: Excepted {}, Actual {}'.format(idx, expected, result)


def run_solution():
    lines = [x.strip() for x in data.get_data_lines(2, 1)]

    with print_timing_data('Solution'):
        result = keypad_code(lines)

    print 'Solution: {}'.format(result)


def main():
    run_test_data()
    run_solution()


if __name__ == '__main__':
    main()

