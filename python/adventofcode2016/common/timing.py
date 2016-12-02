import time
import contextlib


@contextlib.contextmanager
def print_timing_data(name):
    start = time.time()
    yield
    print '{name}: {elapsed:0.6f}'.format(
        name=name,
        elapsed=time.time() - start,
    )
