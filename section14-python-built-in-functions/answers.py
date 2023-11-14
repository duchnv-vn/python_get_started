## QUESTION 1
widgets = [f'w{i}' for i in range(1, 21)]
skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]

# zipped_data = {widget: sku for (widget, sku) in zip(widgets, skus)}
zipped_data = dict(zip(widgets, skus))

# print(f'zipped_data: {zipped_data}')
## ------------------------------------------
## QUESTION 2
suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

# Solution 1
def generate_card_dict(*, suits_arg, ranks_arg):
  output = [
    (number, letter)
    for letter in suits_arg
      for number in ranks_arg
  ]
  return output

list_of_card = generate_card_dict(suits_arg=suits, ranks_arg=ranks)

# print(f'list_of_card: {list_of_card}') zip(ranks_2,suits_2)
# print(f'length of list_of_card: {len(list_of_card)}')

# Solution 2
def generate_card_dict_2(*, suits_arg, ranks_arg):
  output = [
    list(zip(ranks_arg, suit * len(ranks_arg)))
    for suit in suits_arg
  ]
  return output

list_of_card_2 = generate_card_dict_2(suits_arg=suits, ranks_arg=ranks)

# print(f'list_of_card_2: {list_of_card_2}')

## ------------------------------------------
## QUESTION 3
def func_3(numbers, *, reverse=False):
  sorted_numbers = sorted(numbers, reverse=reverse)
  min_number = min(numbers)
  max_number = max(numbers)

  return sorted_numbers, min_number, max_number

sorted_numbers, min_number, max_number = func_3([7,5,8,3,5,2,4,1], reverse=True)

# print(f'sorted_numbers: {sorted_numbers}')
# print(f'min_number: {min_number}')
# print(f'max_number: {max_number}')