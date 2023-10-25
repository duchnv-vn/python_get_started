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

t0 = []
t0.extend(t1)
t0.extend(t2)
t0.extend(t3)

for i in range(0, len(t0),2):
  t0[i] = 0

# print('t0', t0)

t00 = []
t00.extend(t1[1::2])
t00.extend(t2[1::2])
t00.extend(t3[1::2])

print('t00', t00)