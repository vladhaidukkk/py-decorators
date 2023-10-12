import functools


def memoize(fn):
    cache = {}

    @functools.wraps(fn)
    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]

    return inner
