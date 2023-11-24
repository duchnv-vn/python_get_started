# file = open('./files/read.txt', mode='r')

# while True:
#     try:
#         line_content = file.readline()
#         print(line_content)
#         print('-' * 30)
#     except Exception as ex:
#         file.close()
#         break

with open('./files/read.txt', mode='r') as file:
    pass
