## list comprehensions

numbers = (1, 2, 3, 4, 5)

sq = [number ** 2 for number in numbers]

even_numbers = [number for number in numbers if number % 2 == 0]

number_types = ['even' for number in numbers if number % 2 == 0]

# print('sq', sq)
# print('even_numbers', even_numbers)
# print('number_types', number_types)

from math import sqrt
vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]

mg = [sqrt(x**2 + y**2) for x, y in vectors]

# print('mg', mg)
## -----------------------------------------------------------------------------
## dictionary & set comprehensions
products = ['item 1', 'item 2', 'item 3', 'item 5']
sales = [10, 5, 15, 0]

dict1 = {products[i]: sales[i] for i in range(len(sales)) if sales[i] > 0}

set1 = {i for i in products if i != 'item 3'}

data = ['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd']

freq = {
  element: len([char for char in data if char == element])
  for element in set(data)
}

from collections import Counter

paragraph = """
“'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation 
of negation) they are a complete set of basic logical operations — all other logical 
operations, no matter how complex, can be obtained by suitable combinations of these.” 
― John von Neumann, The Computer and the Brain
"""

ignored = ",.'\"“ ”()-―—\n"

freq2 = {
  key: value
  for key, value in Counter(paragraph.casefold()).items()
  if key not in ignored
}

print('freq2', freq2)
# print('freq', freq)
# print('dict1', dict1)
# print('set1', set1)