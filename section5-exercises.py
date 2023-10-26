## Exercise 1
s = 'FfEeDdCcBbAa'
s2 = s[::-1]
lower = s2[::2]
upper = s2[1::2]

# print('s2', s2)
# print('lower', lower)
# print('upper', upper)

## -------------------------------------------------------------------------------------
## Exercise 2
t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17

t00 = list(t1) + list(t2) + list(t3)

t00[::2] = [0] * len(t00[::2])

t00 = tuple(t00)

# print('t00', t00)

## -------------------------------------------------------------------------------------
## Exercise 3
m0 = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

m0[0][0] = 1
m0[0][2] = 1
m0[1][1] = 1
m0[2][2] = 1
m0[2][0] = 1

# print('m', m)

## -------------------------------------------------------------------------------------
## Exercise 4
from copy import deepcopy
m00 = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

m1 = deepcopy(m00)

m1[0][0] = 1
m1[0][2] = 1
m1[1][1] = 1
m1[2][2] = 1
m1[2][0] = 1

# print('m00', m00)
# print('m1', m1)

## -------------------------------------------------------------------------------------
## Exercise 5
data = [
  (100, 'USD', 'EUR', 0.83),
  (100, 'USD', 'CAD', 1.27),
  (100, 'CAD', 'EUR', 0.65)
]

d0 = data[0]
d1 = data[1]
d2 = data[2]

d0_amount, d0_currency, d0_target_currency, d0_exchange_rate = d0
d1_amount, d1_currency, d1_target_currency, d1_exchange_rate = d1
d2_amount, d2_currency, d2_target_currency, d2_exchange_rate = d2

statement0 = f'{d0_amount} {d0_currency} =  {d0_amount * d0_exchange_rate} {d0_target_currency}'
statement1 = f'{d1_amount} {d1_currency} =  {d1_amount * d1_exchange_rate} {d1_target_currency}'
statement2 = f'{d2_amount} {d2_currency} =  {d2_amount * d2_exchange_rate} {d2_target_currency}'

# print(statement0)
# print(statement1)
# print(statement2)

