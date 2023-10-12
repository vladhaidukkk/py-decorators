import functools
import os
import sys


def debug(fn=None, *, stream=sys.stdout):
    if fn is None:
        return functools.partial(debug, stream=stream)

    if not os.getenv("DEBUG"):
        return fn

    @functools.wraps(fn)
    def inner(*args, **kwargs):
        params = ", ".join(
            [str(arg) for arg in args] + [f"{key}={value}" for key, value in kwargs.items()]
        )
        print(f"{fn.__name__}({params}) = ?", file=stream)
        result = fn(*args, **kwargs)
        print(f"{fn.__name__}({params}) = {result}", file=stream)
        return result

    return inner
