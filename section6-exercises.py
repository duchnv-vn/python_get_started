## Question 1
str = 'a, b, c'
strRemoveSpace = str.replace(' ', '')
lowerList = strRemoveSpace.lower().split(',')
upperList = strRemoveSpace.upper().split(',')
hexList = lowerList[:]

hexList[0] =  hex(ord(hexList[0]))
hexList[1] =  hex(ord(hexList[1]))
hexList[2] =  hex(ord(hexList[2]))

# print('lowerList', lowerList)
# print('upperList', upperList)
# print('hexList', hexList)

## -----------------------------------------------------
## Question 2
formatStr = 'The number {f0} of {f1} {f2} even'

a = 42
str1 = formatStr.format(f0=a, f1='a', f2='is' if a%2==0 else 'is not')
str11 = f'The number {a} of a {'is' if a%2==0 else 'is not'} even'

b = 31
str2 = formatStr.format(f0=b, f1='b', f2='is' if b%2==0 else 'is not')
str22 = f'The number {b} of b {'is' if b%2==0 else 'is not'} even'

print('str11', str11)
print('str22', str22)

## -----------------------------------------------------
## Question 3
a = 1
b = 3
formatStr2 = '{a} / {b} = {result:4f}'.format(a=a,b=b,result=(a/b))
formatStr3 = f'{a} / {b} = {(a/b):4f}'

# print('formatStr2', formatStr2)
# print('formatStr3', formatStr3)