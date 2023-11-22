import math
from time import perf_counter

## QUESTION 1
# f1 = lambda x: x ** 2 -1
# f2 = lambda x: abs(x - 2)
# f3 = lambda x: math.sin(x)

## ------------------------------------------
## QUESTION 2
points = [
    (0, 0),
    (1, 1),
    (10, 20),
    (math.pi, math.e)
]

def handle_each(item):
    return math.hypot(*item)

def import_list_func(points):
    def inner(loop_f, each_f):
        start = perf_counter()
        output = loop_f(points, each_f)
        end = perf_counter()
        spent_time = end - start

        print(f'spent_time of {loop_f.__name__}: {spent_time}')

        return output

    return inner

def for_func(points, f):
    output = []
    for item in points:
        result = f(item)
        output.append(result)

    return output

def comprehension_func(points, f):
    return [f(item) for item in points]

def map_func(points, f):
    return map(f, points)

import_points = import_list_func(points * 1_000_000)

# result_1 = import_points(for_func, handle_each)
# result_2 = import_points(comprehension_func, handle_each)
# result_3 = import_points(map_func, handle_each)

# print(f'result_1: {result_1}')
# print(f'result_2: {result_2}')
# print(f'result_3: {result_3}')

## ------------------------------------------
## QUESTION 3
def partial_func(f, *args, **kwargs):
    def inner(a):
        return f(a, *args, **kwargs)

    return inner

def power(a, n):
    return a ** n

# squares = partial_func(power, 2)
# result_squares = squares(3)

# cubes = partial_func(power, 3)
# result_cubes = cubes(3)

# print(f'result_squares: {result_squares}')
# print(f'result_cubes: {result_cubes}')
## ------------------------------------------
## QUESTION 4
def log_time(f):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = f(*args, **kwargs)
        end = perf_counter()
        print(f'elapsed time: {end - start}')
        return result
    return inner

def norm(x, y):
    return math.sqrt(x**2 + y**2)

def find_index_min(seq):
    min_ = min(seq)
    return seq.index(min_)

# norm_logged = log_time(norm)
# norm_result = norm_logged(1, 1)

# print(f'norm_result: {norm_result}')