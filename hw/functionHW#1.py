"""
Напишите функцию m(a, b), вычисляющую минимум двух чисел.
С помощью вашей функции найдите минимальное четырёх чисел.
"""

# def min_num(a, b):
#     return a if a < b else b
# user_num_1 = int(input("Введите первое число: "))
# user_num_2 = int(input("Введите второе число: "))
# user_num_3 = int(input("Введите третье число: "))
# user_num_4 = int(input("Введите четвертое число: "))
# min_1 = min_num(user_num_1, user_num_2)
# min_2 = min_num(min_1, user_num_3)
# min_3 = min_num(min_2, user_num_4)
# print(f"Ваши числа: {user_num_1}, {user_num_2}, {user_num_3}, {user_num_4}")
# print(f"Минимальное число: {min_3}")

"""
Дано натуральное число n > 1. Проверьте, является ли оно совершенным. 
Программа должна вывести слово YES, если число совершенное и NO, в противном случае.
"""
# def perf_num(n):
#     if n not in {6, 28, 496, 8128}:
#         print("No")
#     else:
#         print("Yes")
#     return
# n = int(input("Введите число которое хотите проверить: "))
# perf_num(n)

"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
Ищем число Фиббоначи через цикл! Рекурсию не использовать! 
"""
# print("Поиск числа Фибоначчи")
# def fib(n):
#     if n < 0:
#         raise ValueError("n должно быть неотрицательным")
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
# n = int(input("Введите неотрицательное число:"))
# result = fib(n)
# print(f"Для числа: {n} - число Фибоначчи: {result}")

"""
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое
маленькое целое число y, такое что:
-y больше или равно x                                                                                  
-y делится нацело на 5
"""
# def closest_mod_5(x):
#     div = x % 5
#     if div == 0:
#         return x
#     else:
#         return x + (5 - div)
# x = int(input())
# y = closest_mod_5(x)
# print(y)

"""
В языке Python есть некоторые ограничения на имена переменных. 
Имена переменных:
-могут состоять только из цифр, букв и знаков подчеркивания.          
-не могут начинаться с цифры. 
Программист вводит строки с именами переменных. Для каждой переменной нужно вывести "Можно использовать",
если ее имя корректно, или "Нельзя использовать", если это не так. 
Определив все нужные переменные, программист заканчивает ввод строкой "Поработали, и хватит".                                                                       
Для проверки каждой строки используйте функцию check_variable(v). 
Для простоты будем считать, что программист использует только латинские буквы.  
Не может содержать : ! @ # $ % ^ & * ()
"""

# def check_variable(var_name):
#     forbidden = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")"}
#     if not var_name:
#         return ("Нельзя использовать")
#     elif var_name[0].isdigit():
#         return ("Нельзя использовать")
#     for char in var_name:
#         if char in forbidden:
#             return ("Нельзя использовать")
#     return "Можно использовать"
# var_name = input()
# while True:
#     var_name = input()
#     if var_name == "Поработали, и хватит":
#         print("Работа завершена!")
#         break
#     result = check_variable(var_name)
#     print(result)

"""
Сгенерировать список нечётных двузначных  чисел.
"""
# def odd_num_generator():
#     odd_lst = []
#     for odd in range(11, 100, 2):
#         odd_lst.append(odd)
#     return odd_lst
# odd_num = odd_num_generator()
# print(odd_num)

"""
Сгенерировать список всех трёхзначных чисел кратных 5 и 3.
"""
# def three_dig_num(num_1=5,num_2=3):
#     num_lst = []
#     for num in range(100, 1000):
#         if num % num_1 == 0 and num % num_2 == 0:
#             num_lst.append(num)
#     return num_lst
# print(three_dig_num())

"""
Дан список, упорядоченный по не убыванию элементов в нем. 
Напишите функцию которая определяет количество в нем различных элементов. 
set функцию не использовать. 
"""
# def unique_el_lst(sort_list):
#     if not sort_list:
#         return 0
#     unique_el = 1
#     for i in range(1, len(sort_list)):
#         if sort_list[i] != sort_list[i-1]:
#             unique_el += 1
#     return unique_el
# sort_list = [1,2,2,2,3,3,4,4,5,6,7,7,8]
# result = unique_el_lst(sort_list)
# print(result)

"""
Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, 
находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же. 
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
"""
# def neighbours(num_lst):
#     if len(num_lst) == 1:
#         return num_lst[0]
#     result_lst = []
#     n = len(num_lst)
#     for i in range(n):
#         first = (i - 1) % n
#         last = (i + 1) % n
#         neighb_sum = num_lst[first] + num_lst[last]
#         result_lst.append(neighb_sum)
#     return result_lst
# num_lst = [1, 3, 5, 6, 10]
# result = neighbours(num_lst)
# print(result)

"""
Дан список, состоящий из строк. Отсортировать его по длине слов. Сначала должны идти длинные слова затем короткие. 
"""
lst = ["asdfadf", "dasfasdfasdf", "fdsfaf", "dsa", "as"]
lst.sort(key=len, reverse=True)
print(lst)

"""
Сгенерировать список всех простых чисел до  100 с помощью генератора.
"""
def prime_num_generator(num):
    prime_num = [2]
    for i in range(3, 100, 2):
        if i % 2 != 0:
            prime_num.append(i)
    return prime_num
