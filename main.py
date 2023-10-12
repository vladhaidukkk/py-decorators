from decorators import debug, once


@debug
@once
def minmax(first, *rest):
    min_result = max_result = first
    for arg in rest:
        min_result = arg if arg < min_result else min_result
        max_result = arg if arg > max_result else max_result
    return min_result, max_result


if minmax(1, 3, 9, 5, 7) == minmax(2, 4, 10, 6, 8):
    print("The same returned value")
