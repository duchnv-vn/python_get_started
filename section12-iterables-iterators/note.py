## ITERABLES & ITERATORS
r = range(0, 10)
iterator = iter(r)

# iterator.__next__()
# iterator.__next__()
# iterator.__next__()

# l = list(iterator)

# print('l', l)

## --------------------------------------------------------
## GENERATORS
g = (i ** 2 for i in range(5))

# g.__next__()

# print('g', g.__next__())
# print('g', g.__next__())
# print('g', g.__next__())
# print('g', g.__next__())
# print('g', g.__next__())

checkItemInGenerator= 3 in g

print('1', checkItemInGenerator)

l = list(g)


print('2', g)
print('3', l)

