from decorators import memoize, profile


@profile
@memoize
def repeat(n):
    for i in range(n):
        pass


repeat(100_000_000)
print(repeat.__total_time__)
repeat(100_000_000)
print(repeat.__total_time__)
