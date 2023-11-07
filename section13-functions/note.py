## Custom function & Parameters/Arguments
def function_a(text_1 = '', text_2 = ''):
  print('text_1', text_1)
  print('text_2', text_2)
  return f'{text_1} {text_2}'

# str = function_a( text_2='hello 2', text_1='hello 1')

# print('str', str)
## ---------------------------------------------------------
# Star arguments
def star_agument(*values):
    print('values', values)

l = [*[3,4],5,*[6,7,*[8,9]]]

# print(l)

# star_agument( )
# star_agument(*l)
# star_agument('a', 3.14, 'b')
## ---------------------------------------------------------
# Default values
def function_b(arg, arg2=2):
  print('arg', arg)
  print('arg2', arg2)

# function_b(1)