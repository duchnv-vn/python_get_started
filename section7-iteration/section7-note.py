r = range(10)

# print('range', r, list(r))

e = enumerate([15,25,35])

print('enumerate', e, list(e))

data = [15,25,35,45,55]

for t in enumerate(data):
  index, value = t
  # print('index', index)
  # print('value', value)