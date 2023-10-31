s = set()

s.add(1)
s.add('a')
s.add(False)
s.add('b')
s.add((1,4))
s.add(3.14)

s2 = set([3, frozenset({2, 'c', True}), True])

s3 = {1,2,0}
s4 = {'a','b'}

# print('s', s)
# print('s2', s2)
print('s3', s3)
print('s4', s4)
print('isdisjoint', s3.isdisjoint(s4))
# print('compare sets', {1,2,4}>{1,2,2})
# print('union', s | s2)
# print('intersection', s & s2)
# print('difference', s - s2)