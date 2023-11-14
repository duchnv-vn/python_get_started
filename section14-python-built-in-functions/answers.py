## QUESTION 1
widgets = [f'w{i}' for i in range(1, 21)]
skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]

zipped_data = {index: value for (index, value) in zip(widgets, skus)}

# print(f'zipped_data: {zipped_data}')
## ------------------------------------------
## QUESTION 2
suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

list_of_card = [
  (number, letter)
  for letter in suits
    for number in ranks
]

total_cards = 52
suits_2 = sorted(suits * round(52/len(suits)), reverse=True)
ranks_2 = ranks * round(52/len(ranks))

list_of_card_2 = list(
  list(
    zip(ranks_2[(len(ranks)*i):(len(ranks)*(i+1))], suits_2))
      for i in range(len(suits)
  )
)

# print(f'list_of_card: {list_of_card}') zip(ranks_2,suits_2)
# print(f'length of list_of_card: {len(list_of_card)}')

# print(f'ranks_2: {ranks_2}')
print(f'list_of_card_2: {list_of_card_2}')

## ------------------------------------------
## QUESTION 3