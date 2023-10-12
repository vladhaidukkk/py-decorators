DEBUG = True


def update_wrapper(wrapper, wrapped):
    for attr in ["__name__", "__doc__", "__module__"]:
        setattr(wrapper, attr, getattr(wrapped, attr))
    wrapper.__wrapped__ = wrapped
    return wrapper


def wraps(fn):
    def decorator(wrapper):
        update_wrapper(wrapper, fn)
        return wrapper

    return decorator


def debug(fn):
    if not DEBUG:
        return fn

    @wraps(fn)
    def inner(*args, **kwargs):
        params = ", ".join(
            [str(arg) for arg in args] + [f"{key}={value}" for key, value in kwargs.items()]
        )
        print(f"{fn.__name__}({params}) = ?")
        result = fn(*args, **kwargs)
        print(f"{fn.__name__}({params}) = {result}")
        return result

    return inner


@debug
def minmax(first, *rest):
    min_result = max_result = first
    for arg in rest:
        min_result = arg if arg < min_result else min_result
        max_result = arg if arg > max_result else max_result
    return min_result, max_result


minmax(1, 3, 9, 5, 7)
