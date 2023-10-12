import functools
import sys


DEBUG = True


def debug(stream=sys.stdout):
    def decorator(fn):
        if not DEBUG:
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

    return decorator


@debug(sys.stderr)
def minmax(first, *rest):
    min_result = max_result = first
    for arg in rest:
        min_result = arg if arg < min_result else min_result
        max_result = arg if arg > max_result else max_result
    return min_result, max_result


minmax(1, 3, 9, 5, 7)
