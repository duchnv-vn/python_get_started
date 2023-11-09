## Custom function & Parameters/Arguments
def function_a(text_1 = '', text_2 = ''):
  print('text_1', text_1)
  print('text_2', text_2)
  return f'{text_1} {text_2}'

# str = function_a( text_2='hello 2', text_1='hello 1')

# print('str', str)
## ---------------------------------------------------------
# Star arguments
def star_agument(*values, end):
    print('values', values)
    print('end', end)

l = [*[3,4],5,*[6,7,*[8,9]]]

# print(l)

# star_agument( )
# star_agument(*l)
# star_agument('a', 3.14, end='b')
## ---------------------------------------------------------
# Default values
def function_b(arg, arg2=2, arg3=True):
  print('arg', arg)
  print('arg2', arg2)
  print('arg3', arg3)

# function_b(1, arg3=False)

def process_row(row, item_sep=','):
   row_str = item_sep.join(str(item)for item in row)
   return row_str

def process_data(data, item_sep=',', line_sep='\n'):
  row_strs = (process_row(row, item_sep) for row in data)
  output = line_sep.join(row_strs)
  return output

data = [
   [10, 20, 30],
   [100, 200, 300],
   [1000, 2000, 3000],
]

# data_str = process_data(data)

# print('START data_str')
# print(data_str)
# print('END data_str')
## ---------------------------------------------------------
# Keyword-only argument
def keyword_only_fuc(a, b, *args, **kwargs):
   print('a', a)
   print('b', b)
   print('args', args)
  #  print('c', c)
   print('kwargs', kwargs)

# keyword_only_fuc(1, 2, 3, 4, e=5, d=6)
