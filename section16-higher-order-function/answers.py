import math
from time import perf_counter

## QUESTION 1
f1 = lambda x: x ** 2 -1
f2 = lambda x: abs(x - 2)
f3 = lambda x: math.sin(x)

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

import_points = import_list_func(points)

result_1 = import_points(for_func, handle_each)
result_2 = import_points(comprehension_func, handle_each)
result_3 = import_points(map_func, handle_each)

# print(f'result_1: {result_1}')
# print(f'result_2: {result_2}')
# print(f'result_3: {result_3}')

## ------------------------------------------
## QUESTION 3

## ------------------------------------------
## QUESTION 4