## MAP FUNCTION
l = [1,2,3,4,5]

def multiTwo(number):
  print(f'number: {number}')
  return number * 2

# iterator = map(multiTwo, l)

# print(f'iterator: {list(iterator)}')

## ------------------------------------------------------------------
## CLOSURE
from time import perf_counter

def power(n):
  def inner(x):
    return x ** n
  return inner

def time_it(func):
  def inner(*args, **kwargs):
    start = perf_counter()
    result = func(*args, **kwargs)
    end = perf_counter()
    print(f'elapsed: {end - start}')
    return result
  return inner

def matrix(cols, rows, default=1):
  result = [
    [
      default if col == row else 0
      for col in range(cols)
    ]
    for row in range(rows)
  ]
  return result

# matrix_timeit = time_it(matrix)

# result = matrix_timeit(3,3,default=1)

# print(f'result: {result}')