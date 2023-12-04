import csv

store_folder_path_name = "section22-csv-module/files"
actors_file = "actors.pdv"
nasdaq_file = "nasdaq.csv"
st_2001est_file = "st-2001est-01.csv"

csv.register_dialect(
    "pdv",
    delimiter="|",
    quotechar="'",
    escapechar="\\",
    skipinitialspace=True,
)


def parse_nasdaq(file_name, dialect_name="excel"):
    result = []

    with open(f"{store_folder_path_name}/{file_name}") as file:
        reader = csv.reader(file, dialect=dialect_name)

        headers = next(reader)
        result.append(headers)

        for row in reader:
            row[-1] = float(row[-1])
            result.append(row)

    return result


def parse_st_2001_est(file_name, dialect_name="excel"):
    result = []

    with open(f"{store_folder_path_name}/{file_name}") as file:
        reader = csv.reader(file, dialect=dialect_name)

        headers = next(reader)
        result.append(headers)

        for row in reader:
            area_name = row[0]
            data = row[1:]
            data = [area_name] + [int(field.replace(",", "")) for field in data]
            result.append(data)

    return result


def read_file_csv(file_name, dialect_name="excel"):
    with open(f"{store_folder_path_name}/{file_name}") as file:
        reader = csv.reader(file, dialect=dialect_name)
        for row in reader:
            print(row)


# read_file_csv(actors_file, "pdv")

# nasdaq_data = parse_nasdaq(nasdaq_file)
# print(nasdaq_data)

# st_2001_est_data = parse_st_2001_est(st_2001est_file)
# print(st_2001_est_data[0])
# print(st_2001_est_data[1])


write_file_name = "OUTPUT.csv"


def write_csv_file(file_name, data):
    with open(f"{store_folder_path_name}/{file_name}", mode="a") as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)


data_to_write = [
    ["ID", "Company name", "Annual revenue"],
    [1, "AAA", 5_000_000_000],
    [2, "BBB", 100_000_000],
    [3, "CCC", 250_000_000],
    [4, "DDD", 10_000_000_000],
]

write_csv_file(write_file_name, data_to_write)
