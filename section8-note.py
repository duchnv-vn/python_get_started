d = {
    'a': 1,
    'b': 2
}

d['a'] = 0

d['c'] = 3

del d['b']

print('d', d, type(d))
print(d['a'])