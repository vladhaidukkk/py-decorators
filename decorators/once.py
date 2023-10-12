import functools


def once(fn):
    null = []
    result = null

    @functools.wraps(fn)
    def inner(*args, **kwargs):
        nonlocal result
        if result is null:
            result = fn(*args, **kwargs)
            inner.__called__ = True
        return result

    inner.__called__ = False
    return inner
