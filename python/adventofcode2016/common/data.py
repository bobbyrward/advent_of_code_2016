import os


def get_data_content(day, problem):
    filename = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'data',
        'data_{:02d}_{:02d}.txt'.format(day, problem),
    )

    filename = os.path.normpath(filename)

    with open(filename, 'rb') as data_fp:
        return data_fp.read()
