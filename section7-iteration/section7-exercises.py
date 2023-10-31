## Question 1
row_start = 1
row_end = 4
column_start = 1
column_end = 5

# for row_index in range(row_start, row_end):
#     for column_index in range(column_start, column_end):
#         print(f'{row_index} x {column_index} = {row_index * column_index}')
#     print('-' * 10)
# print('done')

## -------------------------------
## Question 2
data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)

latest_greatest_value = data[0]

for row_index, row in enumerate(data):
    distance = abs(row[2] - row[1])

    row.append(distance)

    if row_index == 0:
        continue

    if row[0] > latest_greatest_value[0] and distance > latest_greatest_value[-1]:
        latest_greatest_value = row

data = list(data)

# print('latest_greatest_value', latest_greatest_value)
# print('data', data)

## -------------------------------
## Question 3
data3 = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]

for row_index, row in enumerate(data3):
    if(row_index == 0):
        row.append('')
    else:
        minus = (row[0] - data3[row_index -1][1])
        str = 'up' if minus > 0 else 'down' if minus < 0  else 'same'
        row.append(str)

print('data3', data3)