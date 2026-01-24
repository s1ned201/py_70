"""
Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали.
"""
# try:
#     x = (1, 2, 5, 7)
#     x = x / 2
#     print(x)
# except TypeError:
#     print("Нельзя делить кортеж на целое число")
"""
Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента, которого нет в списке.
"""
# user_lst = [1, 2, 3]
# try:
#     ind = user_lst[3]
# except IndexError:
#     print("IndexError: элемента под индексом 3 не существует")

"""
Напишите программу которая вычисляет площадь треугольника по формуле Герона,
однако если пользователь введёт длину хоть одной стороны треугольника равную 0,
то программа должна бросить исключение ArithmeticError.
"""
# import math

# try:
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     c = int(input("Введите сторону c: "))
#     if a == 0 or b == 0 or c == 0:
#         raise ArithmeticError("ArithmeticError: сторона треугольника не может быть равна 0")
#     if a < 0 or b < 0 or c < 0:
#         raise ValueError("ValueError: сторона треугольника не может быть отрицательным числом")
#     if a + b <= c or a + c <= b or b + c <= a:
#         raise ValueError("ValueError: такого треугольника не существует")
#     p = 0.5 * (a + b + c)
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print(f"Площадь треугольника: {s}")
# except ArithmeticError as e:
#     print(e)
# except ValueError as e:
#     print(e)

"""
Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError,
когда пользователь пытается удалить элемент которого нет в списке.
"""
# user_lst = [5, 89, 1, 13]
# a = int(input("Введите значение элемента который вы хотите удалить из списка: "))
# try:
#     if a not in user_lst:
#         raise TypeError("TypeError: этого элемента нет в списке")
#     user_lst.remove(a)
# except TypeError as e:
#     print(e)
# print(user_lst)

"""
Дан словарь, который содержит некоторые ключи и значения по этим ключам, 
пользователь не знает этих ключей. Бросьте ошибку KeyError в том случае когда пользователь 
пытается просмотреть значение по ключу, которого нет в словаре.
"""
# lang_ext = {
#     "Python" : ".py",
#     "JavaScript" : ".js"
# }
# lang = input("Введите язык програмирования, файловое расширение которого хотите узнать: ")
# try:
#     if lang in lang_ext:
#         print(lang_ext.get(lang))
#     else:
#         raise KeyError("KeyError: этого ключа нет в словаре")
# except KeyError as e:
#     print(e)

"""
Дана строка, содержащая числа, разделённые пробелами. 
Нужно вывести их сумму. Если хотя бы один элемент не является числом — перехватить 
исключение и пропустить его. "10 5 abc 3" → 18
"""
# user_str = input("Введите числа через пробел: ")
# user_lst = user_str.split()
# sum = 0
# for i in user_lst:
#     try:
#         sum += int(i) 
#     except Exception:
#         continue
# print(sum)

"""
Написать алгоритм, считающий частоту букв в строке. 
Если входные данные — не строка, выбросить TypeError.
"""
# letter_string = input()
# clean_string = letter_string.replace(' ', '')
# unique_letters = set(clean_string)
# for i in unique_letters:
#     count = clean_string.count(i)
#     print(f"{i} {count}")
# Не очень понял про TypeError, ведь через input всегда будет строка

"""
Реализовать алгоритм бинарного поиска. 
Если входной список не отсортирован, выбросить ValueError. 
Если искомого элемента нет, вернуть None. 
"""
inp = input("Введите отсортированный список чисел через пробел: ")
inp_lst = [int(x) for x in inp.split()]
target = int(input("Введите искомое число: "))
is_sorted = True
for i in range(len(inp_lst) - 1):
    if inp_lst[i] > inp_lst[i + 1]:
        is_sorted = False
        break
    if not is_sorted:
        raise ValueError("ValueError: список должен быть отсортирован")
low = 0
high = len(inp_lst) - 1
found_index = None
while low <= high:
    mid = (low + high) // 2
    if inp_lst[mid] == target:
        found_index = mid
        break
    elif inp_lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if found_index is not None:
    print("Искомое число найдено")
else:
    print("None: число не найдено")