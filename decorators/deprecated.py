import functools
import warnings


def deprecated(fn=None, *, replacement=None):
    if fn is None:
        return functools.partial(deprecated, replacement=replacement)

    @functools.wraps(fn)
    def inner(*args, **kwargs):
        warnings.warn(
            f"{fn.__name__} is deprecated{f', use {replacement.__name__} instead' if replacement else ''}",
            category=DeprecationWarning
        )
        return fn(*args, **kwargs)

    return inner
