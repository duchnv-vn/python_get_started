from csv import reader, writer, register_dialect, Error

store_folder_path_name = "section22-csv-module/files"

## QUESTION 1

FILE_1 = "file1.csv"
FILE_2 = "file2.csv"
FILE_3 = "file3.tsv"
FILE_4 = "file4.csv"

register_dialect("file3.tsv", delimiter="\t")
register_dialect("file4.csv", delimiter="|")


def find_extreme_data(file_name):
    with open(f"{store_folder_path_name}/{file_name}") as file:
        try:
            fileReader = reader(file, dialect=file_name)
        except Error:
            fileReader = reader(file)

        next(fileReader)

        min_number = 0
        max_number = 0
        index = 0
        for row in fileReader:
            if file_name == FILE_4:
                row = [float(item.replace("-", "")) for item in row]
            else:
                row = [float(item) for item in row]

            if index > 0:
                row += [min_number, max_number]

            asc_sorted_row = sorted(row)
            min_number = asc_sorted_row[0]
            max_number = asc_sorted_row[-1]
            index += 1

    return min_number, max_number


for name in (FILE_1, FILE_2, FILE_3, FILE_4):
    min_number, max_number = find_extreme_data(name)
    # print(name, min_number, max_number)

## -------------------------------------
## QUESTION 2
data = [
    {"a": "1_a", "b": "1_b", "c": "1_c"},
    {"c": "2_c", "d": "2_d"},
    {"a": "3_a", "c": "3_c", "e": "3_e"},
]

data[0].items()


def write_csv_file(data, file_name):
    headers = []
    write_data = []

    for row in data:
        for key, value in row.items():
            print(key)
            row_data = []

            if key in headers:
                index = headers.index(key)

                if len(row_data) < index + 1:
                    distance = index - len(row_data)
                    row_data[len(row_data)]  ## Need to fix

                row_data[index] = value

            else:
                headers += key
                row_data.append(value)
                write_data = [[*item, ""] for item in write_data]

    # with open(f"{store_folder_path_name}/{file_name}") as file:
    #     fileWriter = writer(file)


write_csv_file(data, "OUTPUT_QUESTION_2.csv")
