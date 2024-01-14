import numpy as np
import csv
from dateutil import parser
from time import perf_counter
import random

l = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]

m = np.array(l)

# print(m)
# print(type(m))
# print(m.dtype)
# print(m.shape)

l_2 = np.zeros((3, 3), dtype=float)

# print(l_2)

l_3 = np.linspace(2, 20, 10, dtype=int)
l_4 = np.linspace(2, 20, num=10)

# print(l_3)
# print(l_4)

np.random.seed(123)
r_1 = np.random.random((3, 4))
r_2 = np.random.random(5)

# print(r_1)
# print(r_2)

# === RESHAPE ARRAY
init_arr_1 = np.arange(12)
reshaped_arr_1 = np.reshape(init_arr_1, (3, 4))
# OR: init_arr_1.reshape((3, 4))

# print(f'init_arr_1: {init_arr_1} - shape: {init_arr_1.shape}')
# print(f'reshaped_arr_1: {reshaped_arr_1}- shape: {reshaped_arr_1.shape}')

# === STACKING ARRAY
stack_arr_1 = np.arange(10).reshape((2, 5))
stack_arr_2 = np.arange(10, 20).reshape((2, 5))

stack_arr_3 = np.array([1.9, 2.2, 3.6], dtype=np.float64)

v_stack = np.vstack((stack_arr_1, stack_arr_2))
h_stack = np.hstack((stack_arr_1, stack_arr_2))

# print(f'stack_arr_1: {stack_arr_1}')
# print(f'stack_arr_2: {stack_arr_2}')
# print(f'v_stack: {v_stack}')
# print(f'h_stack: {h_stack}')
# print(f'stack_arr_3: {stack_arr_3.astype(np.uint16)}')

# === 4. INDEXING
arr_4 = np.arange(1, 26).reshape((5, 5))
slice_arr_4 = arr_4[::2, 1::2]

# print(arr_4)
# print("-" * 50)
# print(slice_arr_4)

# === 5. SLICING
arr_5 = np.arange(1, 31).reshape(5, 6)
slicing_arr_5 = arr_5[0:3, 2:5]

# print(arr_5)
# print("-" * 50)
# print(slicing_arr_5)

# === 6. FANCY INDEXING
arr_6 = np.arange(1, 26).reshape(5, 5)

fancy_arr_6_1 = arr_6[np.array([0, 1, 3, 4])]

fancy_arr_6_2 = arr_6[1, np.array([0, 1, 3])]

fancy_arr_6_3 = arr_6[np.array([0, 1, 3]), 1]

# print(arr_6)
# print("-" * 50)
# print(fancy_arr_6_1)
# print("-" * 50)
# print(fancy_arr_6_2)
# print("-" * 50)
# print(fancy_arr_6_3)

with open("section29-numPy/files/AAPL.csv") as file:
    reader = csv.reader(file, skipinitialspace=True)
    headers = next(reader)
    data = np.array(list(reader))
    dates = data[:, 1]
    open_and_close = data[:, [4, 2]].astype(float)
    diffs = open_and_close[:, 1] - open_and_close[:, 0]
    diff_percs = (diffs % open_and_close[:, 0]) * 100

# print(open_and_close)
# print(diffs)

# === 7. MASKING
arr_7 = np.arange(1, 11)

less_arr_7 = np.less(arr_7, 0)
less_arr_7_2 = arr_7 > 5

# print(arr_7)
# print(less_arr_7)
# print(less_arr_7_2)
# print(arr_7[less_arr_7_2])

with open("section29-numPy/files/AAPL.csv") as file:
    reader = csv.reader(file, skipinitialspace=True)
    headers = next(reader)
    data = np.array(list(reader))

    dates = np.array([parser.parse(date) for date in data[:, 1]])
    ohlc = data[:, [4, 5, 6, 2]].astype(float)

    highes_close_mask = ohlc[:, 3] > 116.0
    highes_close = ohlc[highes_close_mask]
    date_with_highes_close = dates[highes_close_mask]

    highes_close_with_date = np.hstack(
        (date_with_highes_close.reshape(11, 1), highes_close)
    )
    highes_close_with_date_2 = [
        [date, *row] for date, row in zip(date_with_highes_close, highes_close)
    ]

# print(date_with_highes_close)
# print(highes_close)
# print(highes_close_with_date)
# print(np.array(highes_close_with_date_2))

# === 8. UNIVERSAL FUNCTIONS
row_num = 1_000_000

# start = perf_counter()
# data = [
#     (
#         random.randint(120, 180),
#         random.randint(180, 200),
#         random.randint(300, 440),
#         random.randint(100, 150),
#     )
#     for _ in range(row_num)
# ]
# calc = [round((high - low) / close * 100) for (open, high, low, close) in data]
# end = perf_counter()

# print(f"Spent time used by vanila Python code: {end - start} seconds")

# start = perf_counter()
# data = np.array(
#     [
#         np.array(
#             [
#                 np.random.randint(120, 180),
#                 np.random.randint(180, 200),
#                 np.random.randint(300, 440),
#                 np.random.randint(100, 150),
#             ]
#         )
#         * row_num
#     ]
# )
# calc = np.array([np.round((data[:, 1] - data[:, 2]) / data[:, 3] * 100)])
# end = perf_counter()

# print(f"Spent time used by Numpy written by C code: {end - start} seconds")

# === 9. ADDITIONAL MATH AND STATS FUNCTIONS
