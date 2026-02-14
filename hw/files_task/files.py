import os
from pathlib import Path

# 1)Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.

# file = open(file="hw/files_task/text.txt", mode="w", encoding="Utf-8")

# lst_str = ["Hello", "world", "Python", "text", "append", "writemode"]

# for line in lst_str:
#     file.write(line + "\n")

# file.close()



# 2)В конец существующего текстового файла записать три новые
# строки текста. Записываемые строки вводятся с клавиатуры.

# lst_str = ["This", "Appended", "String"]
# path = "hw/files_task/text.txt"
# mode = "a"
# encode = "Utf-8"

# with open(file=path, mode=mode, encoding=encode) as file:
#     for line in lst_str:
#         file.write(line + "\n")



# 3)Дан текстовый файл. 
# Подсчитать количество символов в нем. Без \n

# path = "hw/files_task/text.txt"
# mode = "r"
# encode = "Utf-8"
# chars_len = 0

# with open(file=path, mode=mode, encoding=encode) as file:
#     for line in file:
#         chars_len += len(line.strip("\n"))

# print(chars_len)


# 4)Имеется текстовый файл, содержащий 5 строк. 
# Переписать каждую из его строк в список в том же порядке. 

# path = "hw/files_task/text.txt"
# mode = "r"
# encode = "Utf-8"
# file_lst = []
# with open(file=path, mode=mode, encoding=encode) as file:
#     for line in file:
#         file_lst.append(line.strip("\n"))

# print(file_lst)


# 5)Имеется текстовый файл. Получить текст, в котором в конце 
# каждой строки из заданного файла добавлен восклицательный знак. 

# path = "hw/files_task/text.txt"
# mode = "r"
# encode = "Utf-8"
# file_lst = []
# with open(file=path, mode=mode, encoding=encode) as file:
#     for line in file:
#         if line.endswith('\n'):
#             file_lst.append(line[:-1] + "!")
#         else:
#             file_lst.append(line + "!")

# print(file_lst)