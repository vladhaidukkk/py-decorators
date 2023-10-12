from decorators import debug, once, deprecated


@deprecated
@debug
@once
def minmax(first, *rest):
    min_result = max_result = first
    for arg in rest:
        min_result = arg if arg < min_result else min_result
        max_result = arg if arg > max_result else max_result
    return min_result, max_result


minmax(2, 4, 10, 6, 8)
