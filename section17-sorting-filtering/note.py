from time import perf_counter


def log_time(f, predict_f):
    def inner(*args):
        start = perf_counter()
        result = f(predict_f, *args)
        end = perf_counter()
        print(f"elapsed time: {end - start}")
        return result

    return inner


## FILTERING FUNCTIONS
l = [
    ("AAA", 4.51, 6, 1_000),
    ("AAA", 4.51, 6, 2_000),
    ("AAA", 4.51, 1.3, 500),
    ("AAA", 4.51, 6, 200),
    ("AAA", 4.51, 10.44, 10_000),
    ("AAA", 4.51, -5.5, 5_000),
]


def is_desc(item):
    return item[2] > item[1]


def generator_func(predict_f, l):
    return (i for i in l if predict_f(i))


# exe_1 = log_time(filter, is_desc)
# result_1 = list(exe_1(l * 1_000_000))

# exe_2 = log_time(generator_func, is_desc)
# result_2 = list(exe_2(l * 1_000_000))

# print(f"result_1: {result_1}")
# print(f"result_2: {result_2}")

## SORTING FUNCTIONS
l_need_to_sort = [3, 1, -6, -2, -4, 5]

text_need_to_sort = "this is the paraph need to be sorted"

dict_list_need_to_sort = [
    {"name": "AAA", "sell_price": 100},
    {"name": "BBB", "sell_price": 50},
    {"name": "CCC", "sell_price": 30.5},
    {"name": "DDD", "sell_price": 500.05},
    {"name": "EEE", "sell_price": 1.55},
]

dict_need_to_sort = {
    "a": 5.5,
    "b": 1.25,
    "c": 1.3,
    "d": 5.55,
}


def sort_key_by_abs(x):
    return abs(x)


def sort_key_by_unicode(x):
    return ord(x)


def sort_key_by_sell_price(x):
    return x["sell_price"]


# sorted_l = sorted(l_need_to_sort, key=sort_key_by_abs)
# sorted_s = sorted(text_need_to_sort, key=sort_key_bu_unicode)
# sorted_dict_list = sorted(dict_list_need_to_sort, key=sort_key_by_sell_price, reverse=True)
sort_dict = sorted(dict_need_to_sort.keys(), key=lambda k: dict_need_to_sort[k])

# print(f"sorted_l: {sorted_l}")
# print(f"sorted_s: {sorted_s}")
# print(f"sorted_dict_list: {sorted_dict_list}")
print(f"sort_dict: {sort_dict}")
