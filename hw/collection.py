# TUPLE
# 1
# tup = (1, 2, 3, 4, 5, 6)
# min_tup = min(tup)
# max_tup = max(tup)
# print(max_tup - min_tup)

# 2
# tup = (5, 2, -2, 7, -8, -9, 1)
# changes = 0
# for i in range(1, len(tup)):
#     if tup[i-1] * tup[i] < 0:
#         changes += 1
# print(changes)

# 3
# tup = (4, 5, 2, 8, 18, 22, 34, 6, 13, 15, 17, 19, 21, 23, 25)
# for i in tup:
#     if i % 2 != 0 or i == 2:
#         print(i)

# LIST
# 1
# lst_1 = [2, 4, 3, 9, 9, 6]
# lst_2 = [8, 1, 2, 4, 9, 7, 6]
# set_2 = set(lst_2)
# result = [x for x in lst_1 if x not in lst_2]
# if result:
#     print(min(result))
# else:
#     print("Нет такого элемента")

# 2
# lst = [13, 18, 15, 16, 12, 19, 24]
# lst_2 = []
# for num in lst:
#     lst_2.append(num)
#     if num % 2 == 0:
#         reversed_num = int(str(num)[::-1])
#         lst_2.append(reversed_num)
# print(lst_2)

# 3
# lst = [5,2,4,5,1,2]
# result = []
# for i in lst:
#     if i not in result:
#         result.append(i)
# for i in result:
#     count = lst.count(i)
#     print(f"{i} - {count}")

# 4
# lst = [5,2,0,-2,-7,1,8,0,-1]
# result = []
# for i in lst:
#     if i > 0:
#         result.append(i)
# for i in lst:
#     if i < 0:
#         result.append(i)
# for i in lst:
#     if i == 0:
#         result.append(i)
# print(result)

# 5
# lst = [5,2,7,3,8,2,4,1,6,5]
# result = []
# for i in lst:
#     if lst.count(i) > 1:
#         result.append(i)
#     else:
#         lst.append(i)
#         lst.append(i)
# print(result)
# Работает корректно, но не понимаю почему изменяет порядок чисел в списке

# SET
# 1
# lst = [5, 2, 7, 3, 8, 2, 4, 1, 6, 5]
# my_set = set()
# for num in lst:
#     if num in my_set:
#         print(num, end=" ")
#         print("Yes")
#     else:
#         print(num, end=" ")
#         print("No")
#         my_set.add(num)

# DICT
# 1
# school = {
#     '9а' : 21,
#     '9б' : 23,
#     '9в' : 19,
#     '9г' : 20,
#     '9д' : 25,
#     '9е' : 22
# }

# school['9ф'] = 22
# school['9а'] = 26
# del school['9г']
# students = sum(school.values())
# print(school)
# print(students)

# 2
# my_dict = {}
# while True:
#     my_str = input("Введите определение: ").strip()
#     if my_str == '.':
#         break
#     part = my_str.split(' – ', 1)   #При вводе запросов должен быть именно этот символ, тире которое вводится с клавиатуры не подойдёт!!!
#     if len(part) == 2:
#         key, value = part
#         my_dict[key.strip()] = value.strip()
# m = int(input("Введите количество запросов: "))
# for _ in range(m):
#     request = input("Введите ваш запрос: ").strip()
#     if request in my_dict:
#         print(my_dict[request])
#     else:
#         print("Не найдено")