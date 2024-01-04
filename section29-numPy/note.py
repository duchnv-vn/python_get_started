import numpy as np

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

print(arr_5)
print("-" * 50)
print(slicing_arr_5)
