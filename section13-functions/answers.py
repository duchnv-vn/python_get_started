## QUESTION 1
def get_average(*numbers):
  average = 0

  try:
    average = sum(numbers) / len(numbers)
  except ZeroDivisionError:
    print('Error: Pass at least 1 number')

  return average

# average = get_average(1,2,3)

# print(f'average: {average}')

## ----------------------------------------------------------------
## QUESTION 2
def separator(character = '-', repeat_times = 10):
  output = character * repeat_times

  return output

# output_2_1 = separator()
# output_2_2 = separator('=', 20)

# print(f'output_2_1: {output_2_1}')
# print(f'output_2_2: {output_2_2}')

## ----------------------------------------------------------------
## QUESTION 3
filter_unique = lambda arg = (): len(set(arg)) if len(arg) > 0 else 0

# output_3_1 = filter_unique()
# output_3_2 = filter_unique((1,1,2,2,2,3,4))
# output_3_3 = filter_unique('aaabcdde')

# print(f'output_3_1: {output_3_1}')
# print(f'output_3_2: {output_3_2}')
# print(f'output_3_3: {output_3_3}')

## ----------------------------------------------------------------
## QUESTION 4
input_str = 'This is the first sentence. This is the scecond sentence. This is not the fourth sentence, it is the third sentence.'

def count_text_freq(str = ''):
  input_str_list =  [text.casefold() for text in str.replace(',', '').replace('.', '').split()]
  input_str_set = set(input_str_list)

  output = {}
  output = {
    unique_text: input_str_list.count(unique_text)
      for unique_text in input_str_set
  }

  return output

output_dict = count_text_freq(input_str)

# print(f'output_dict: {output_dict}')