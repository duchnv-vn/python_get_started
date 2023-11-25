
store_folder_path_name = 'section19-text-files/files'

# file = open(f'section19-text-files/files/{file_name}', mode='r')
# for line in file:
#     print(line, end='')
# file.close()


def read_file_r(folder_path_name, file_name):
    file_to_read_headers = []
    file_to_read_data = []

    with open(f'{folder_path_name}/{file_name}', mode='r') as file_r:
        file_to_read_headers = next(file_r).strip().split(',')

        for line in file_r:
            date, value_str = line.strip().split(',')

            try:
                file_to_read_data.append((date, float(value_str)))
            except ValueError:
                pass
    return file_to_read_headers, file_to_read_data


file_to_read_name = "DEXUSEU.csv"
# read_file_r(store_folder_path_name, file_to_read_name)


def write_file_w(folder_path_name, file_name):
    file_to_write_w_headers = ('SKU', 'Name', 'Price')
    file_to_write_w_data = [
        ('111', 'Product 111', '200.500'),
        ('222', 'Product 222', '50.555'),
        ('333', 'Product 333', '1000.250'),
        ('444', 'Product 444', '1500'),
        ('555', 'Product 555', '999')
    ]

    with open(f'{folder_path_name}/{file_name}', mode='w') as file_w:
        file_w.write(f"{','.join(file_to_write_w_headers)}\n")
        file_w.writelines(
            "\n".join([
                ','.join(row) for row in file_to_write_w_data
            ])
        )


file_to_write_mode_w = 'write_w.csv'
# write_file_w(store_folder_path_name, file_to_write_mode_w)


def write_file_a(folder_path_name, file_name, *, headers=None, data):
    with open(f'{folder_path_name}/{file_name}', mode='a') as file_a:
        if headers:
            file_a.write(f"{','.join(headers)}\n")
        file_a.writelines([f"{','.join(row)}\n" for row in data])


file_to_write_a_headers = ('SKU', 'Name', 'Price')
file_to_write_a_data = [
    # ('111', 'Product 111', '200.500'),
    ('222', 'Product 222', '50.555'),
    # ('333', 'Product 333', '1000.250'),
    # ('444', 'Product 444', '1500'),
    # ('555', 'Product 555', '999')
]

file_to_write_mode_a = 'write_a.csv'
# write_file_a(
#     store_folder_path_name,
#     file_to_write_mode_a,
#     # headers=file_to_write_a_headers,
#     data=file_to_write_a_data
# )


def increment_id(id):
    id += 1
    return id


def transform_input_to_output(*, source_file, target_file):
    with open(source_file, mode='r') as source:
        source_headers = next(source).strip().split(',')
        source_headers.insert(0, 'ID')

        with open(target_file, mode='a') as target:
            target.write(f"{','.join(source_headers)}\n")
            id = 0
            for row in source:
                id += 1
                target.write(f"{id},{row}")


transform_input_to_output(source_file=f'{store_folder_path_name}/DEXUSEU.csv',
                          target_file=f'{store_folder_path_name}/DEXUSEU_OUTPUT.csv')
