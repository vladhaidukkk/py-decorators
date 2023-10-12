import sys

from decorators import debug, once, deprecated, memoize, profile


@debug(stream=sys.stderr)
def minmax(*args):
    min_result = max_result = float("-inf")
    for arg in args:
        min_result = arg if arg < min_result else min_result
        max_result = arg if arg > max_result else max_result
    return min_result, max_result


@once
def init_logger():
    pass


@deprecated(replacement=init_logger)
def activate_logger():
    pass


@profile
@memoize
def repeat(n):
    for _ in range(n):
        pass
