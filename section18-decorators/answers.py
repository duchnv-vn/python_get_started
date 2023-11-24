from functools import lru_cache
from time import sleep
from decimal import Decimal
from time import perf_counter

# QUESTION 1


def log_time(fn):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f'elapsed: {elapsed}')
        return result

    return inner


# @log_time
def add(a, b, c):
    return a+b+c


# result_1 = add(5, 6, 7)

# ---------------------------------------------------
# QUESTION 2

def normalize(precision):
    def decorator (fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            return round(result, ndigits=precision)
        return inner
    return decorator


@normalize(5)
def perc_diff(x, y):
    try:
        return (y-x) / x * 100
    except ZeroDivisionError:
        return 0


# @normalize
def sum_squares(*args):
    return sum(x**2 for x in args)


# @normalize
def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)


# result_perc_diff = perc_diff(2.1233, 9.5555555)
# result_sum_squares = sum_squares(1.111, 2.222, 3.333, 4.444)
# result_avg = avg(1.111, 2.222, 3.333)

# print(f'result_perc_diff: {result_perc_diff}')
# print(f'result_sum_squares: {result_sum_squares}')
# print(f'result_avg: {result_avg}')

# ---------------------------------------------------
# QUESTION 3
@log_time
@lru_cache(maxsize=2)
def add_3(x, y):
    sleep(2)
    return x + y


# result_3_1 = add_3(1, 2)
# result_3_2 = add_3(2, 3)
# result_3_4 = add_3(1, 2)  # Will return cached value without calling function
# ---------------------------------------------------
# QUESTION 4
