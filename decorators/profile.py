import functools
import time


def profile(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        inner.__n_calls__ += 1
        inner.__total_time__ += elapsed
        return result

    inner.__n_calls__ = 0
    inner.__total_time__ = 0
    return inner
