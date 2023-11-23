## DECORATORS
from time import perf_counter
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s", level=logging.DEBUG
)

logger = logging.getLogger("Custom log")


def log(fn):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        logger.debug(f"called {fn.__name__} | elapsed: {end - start}")
        return result

    return inner


@log
def add(a, b, c):
    return a + b + c


def greet(name):
    return f"Hello {name}!"


## Previous solution
# greet = log(greet)
# greet_result = greet("Masanori")

## Decorator solution
# add_result_2 = add(2, 3, 4)

# print(f"add_result: {add_result}")
# print(f"add_result_2: {add_result_2}")

## LRU Caching
cache = {}


def power(x, n):
    key = (x, n)
    if key in cache:
        print("Value exist")
        return cache[key]

    print("Value no exist")

    result = x**n
    cache[key] = result

    return result


# result = power(2, 5)

# result_2 = power(2, 5)

# print(f"result: {result}")
# print(f"result_2: {result_2}")
### ------------------------------------------


def cache(fn):
    print("initializing cache dict....")
    cache_2 = {}

    def inner(*args):
        if args in cache_2:
            print("Value exist")
            return cache_2[args]

        print("Value no exist")
        result = fn(*args)
        cache_2[args] = result
        return result

    return inner


# @cache
# def add_2(a, b):
#     return a + b


# @cache
# def multi_2(a, b):
#     return a * b


# result_2_1 = add_2(1, 2)
# result_2_2 = add_2(1, 2)
# result_2_3 = multi_2(1, 2)
# result_2_4 = multi_2(1, 2)

# print(f"result_2_1: {result_2_1}")
# print(f"result_2_2: {result_2_2}")
# print(f"result_2_3: {result_2_3}")
# print(f"result_2_4: {result_2_4}")
### ------------------------------------------
from functools import lru_cache


@lru_cache(maxsize=1)
def add_3(a, b):
    print(f"add_3 with a={a} b={b} called...")
    return a + b


# result_3_1 = add_3(1, 2)
# result_3_2 = add_3(2, 3)
# result_3_3 = add_3(1, 2)
# result_3_4 = add_3(3, 4)
# result_3_5 = add_3(4, 5)
# result_3_6 = add_3(1, 2)

# print(f"result_3_1: {result_3_1}")
# print(f"result_3_2: {result_3_2}")
# print(f"result_3_3: {result_3_3}")
# print(f"result_3_4: {result_3_4}")
# print(f"result_3_5: {result_3_5}")
# print(f"result_3_6: {result_3_6}")
