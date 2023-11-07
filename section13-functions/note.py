def function_a(text_1 = '', text_2 = ''):
  print('text_1', text_1)
  print('text_2', text_2)
  return f'{text_1} {text_2}'

arguments = ()

str = function_a('hello 2', text_1='hello 1')

print('str', str)