## QUESTION 1
l = [10, 'abc', 3.14, True]

# for i in range(len(l)):
#   print(f'index = {i} | value = {l[i]}')

# for index, value in enumerate(l):
#   print(f'index = {index} | value = {value}')

# print('done')
## --------------------------------------------------------
## QUESTION 2
from time import perf_counter

ave_generator_execute_time = 0
ave_list_execute_time = 0
total_execute_time = 10

# for time in range(1, total_execute_time):
#   # Generator execution
#   start_g = perf_counter()
#   g1 = iter(range(1, 10_001))
#   g2 = (i**i for i in g1)
#   end_g = perf_counter()
#   elapsed_g = end_g - start_g
#   ave_generator_execute_time += elapsed_g
#   print(f'elapsed generator {time}: {elapsed_g}')

#   # List execution
#   start_l = perf_counter()
#   g11 = iter(range(1, 10_001))
#   g22 = [i**i for i in g11]
#   end_l = perf_counter()
#   elapsed_l = end_l - start_l
#   ave_list_execute_time += elapsed_l
#   print(f'elapsed list {time}: {elapsed_l}')

#   print('-' * 10)

# ave_generator_execute_time = ave_generator_execute_time / total_execute_time
# ave_list_execute_time = ave_list_execute_time / total_execute_time

# print('=' * 10)
# print(f'Average generator execution time: {ave_generator_execute_time}')
# print(f'Average list execution time: {ave_list_execute_time}')

## --------------------------------------------------------