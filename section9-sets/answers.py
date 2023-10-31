## question 1
l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']
s = set(l)

# print('s', s)

## ------------------------------------------
## question 2
s2 = set()

for item in l:
    s2.add(item.casefold())

# print('s2', s2)

## ------------------------------------------
## question 3
data = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'b': 20, 'c': 30, 'd': 40},
    'd3': {'d': 100, 'x': 200}
}

result2 = set()

for item in data.values():
    result2 = result2 | item.keys()

# print('result2', result2)