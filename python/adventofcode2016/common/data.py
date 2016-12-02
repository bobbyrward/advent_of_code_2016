import os


def get_data_filename(day, problem):
    return os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        'data',
        'data_{:02d}_{:02d}.txt'.format(day, problem),
    )

    return filename


def get_data_content(day, problem):
    with open(get_data_filename(day, problem), 'rb') as data_fp:
        return data_fp.read()


def get_data_lines(day, problem):
    with open(get_data_filename(day, problem), 'rb') as data_fp:
        return data_fp.readlines()
