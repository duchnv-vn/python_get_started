l = [1,2,3,4,5]

i = iter(l)

# i.__next__()
# i.__next__()
# i.__next__()
# i.__next__()
# i.__next__()

# print('i', i)
# print(i.__next__())

try:
    raise KeyError('custom message')
except KeyError as ex:
    print('1', ex)
    pass
except Exception as ex:
    print('2', ex)
