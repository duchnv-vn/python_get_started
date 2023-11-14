## round function
round_num = round(3.324, 2)

# print(f'round_num: {round_num}')

## --------------------------------------------
## sorted function
list_of_numbers = (5,3,4,1,2)
list_of_strings = ['Big', 'city', 'boy']

sorted_1 = sorted(list_of_numbers, reverse=True)
sorted_2 = sorted(list_of_strings)

# print(f'sorted_1: {sorted_1}')
# print(f'sorted_2: {sorted_2}')

## --------------------------------------------
## min function
min_1 = min(list_of_numbers, default=0)
min_2 = min([], default=0)

# print(f'min_1: {min_1}')
# print(f'min_2: {min_2}')

## --------------------------------------------
## max function
max_1 = max(list_of_numbers)
max_2 = max((), default=100)

# print(f'max_1: {max_1}')
# print(f'max_2: {max_2}')

## --------------------------------------------
## zip function
list_1_zip = ['a', 'b', 'c', 'd']
list_2_zip = (1, 2, 3)
# list_3_zip = (True, False)

zipped_1 = zip(list_1_zip, list_2_zip)

# print(f'zipped_1 1: {dict(zipped_1)}')
# print(f'zipped_1 2: {list(zipped_1)}')

data = [
  ('item1', 10, 100.0),
  ('item2', 5, 25.0),
  ('item3', 100, 0.2)
]

schema = ('widget', 'num_sold', 'unit_price')

d = {row[0]: dict(zip(schema[1:],row[1:])) for row in data}

print('d', d)
