numbers = (1, 2, 3, 4, 5)

sq = [number ** 2 for number in numbers]

even_numbers = [number for number in numbers if number % 2 == 0]

number_types = ['even' for number in numbers if number % 2 == 0]

# print('sq', sq)
# print('even_numbers', even_numbers)
# print('number_types', number_types)

## -----------------------------------------------------------------------------
from math import sqrt
vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]

mg = [sqrt(x**2 + y**2) for x, y in vectors]

print('mg', mg)