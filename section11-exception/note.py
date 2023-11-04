a = 1
b = 0

# try:
#     c = a / b
# except Exception as ex:
#     print(ex, type(ex), type(ex) == ZeroDivisionError)
#     c = 0

l = [1,2,3,4,5]

while len(l) > 0:
    print(l.pop())
    print('l', l)

print('done')

# print('c', c)

# valErr = ValueError('value must be at least 5 characters.')

# raise valErr

# print(valErr)
# print(repr(valErr))

# name = input('Enter name (5 characters min): ')

# if len(name) < 5:
#     raise ValueError(f'{name} is not 5 characters or more...')

# print(f'Hello {name}!')

