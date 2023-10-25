## UNICODE
a = "A"
ord = ord(a)
hex = hex(ord)

# print('ord', ord)
# print('hex', hex)

hex2 = '\u0041'
hex3 = '\u03b1'
character1 = 'α'
snakeIcon = '\U0001f40d'

# print('hex2', hex2)
# print('hex3', hex3)
# print('character1', character1)
# print('snakeIcon', snakeIcon)

## ---------------------------------------------------------
## COMMON STRING METHODS
m1 = "This is the test string for Python"
m2 = "abc"
m3 = "aBc"

m4 = 'a,1,b,c,1,2,3,1'
m41= m4.split(',')
m42 = '.'.join(m41)

m5='c,d,e'

# print('m41', m41)
# print('m42', m42)
# print('in', 'C'.casefold() in m4)
# print('upper', m1.upper())
# print('lower', m1.lower())
# print('lower', m1.title())
# print('compare', m2.casefold() == m3.casefold())

## ---------------------------------------------------------
## STRING INTERPOLATION
m9 = f'"{m4}"{m5}'

m10 = 'a:{a:6f},b:{b}'.format(b=2,a=3.333333333333333333333)

print('m9', m9)
print('m10', m10)
