## question 1
values = []

try:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
except IndexError as ex:
    # print(f'Found exception: {ex}')
    minimum = 0

# print(f'Minimum is: {minimum}')

## --------------------------------------
## question 2
try:
    raise ValueError('custom message')
except ValueError as ex:
    print(f'Found exception: {ex}')