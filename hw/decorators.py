"""
Написать декоратор log_result, который печатает результат выполнения функции.
Применить к функции возведения числа в квадрат.
"""

# def log_result(func):
#     def wrapper(num):
#         result = func(num)
#         print(result)
#         return result
#     return wrapper

# @log_result
# def square(num):
#     return num ** 2

# square(3)

"""
Написать декоратор repeat(n), который повторяет 
вызов функции n раз и возвращает последний результат.
"""


# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             result = None
#             for _ in range(n):
#                 result = func()
#             return result

#         return wrapper

#     return decorator


# @repeat(n=3)
# def hello():
#     print("hello")


# hello()


"""
Написать декоратор bench, который измеряет ошибки: 
если функция завершилась ошибкой, вывести её тип и сообщение.
"""


# def bench(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as e:
#             print(f"Error type: {type(e).__name__}")
#             print(f"Message: The program {func.__name__} has been completed")

#     return wrapper


# test_str = "abc"


# @bench
# def test(str):
#     str[4]


# test(test_str)

"""
Дан список слов. Получить список их длин.
"""

# word_lst = ["hello", "abc", "elephant", "try"]
# len_word = []

# def len_lst(lst):
#     for word in lst:
#         len_word.append(len(word))
#     print(f"Список слов: {word_lst}")
#     print()
#     print(f"Список их длин: {len_word}")


# len_lst(word_lst)


"""
Дан список: ['apple', 'Banana', 'cherry', 'DATE']. 
Получите новый список, оставив только слова в нижнем регистре.
"""

# not_sort_lst = ['apple', 'Banana', 'cherry', 'DATE']
# sort_lst = []

# def lowcase_sort(lst):
#     for word in lst:
#         if str.islower(word):
#             sort_lst.append(word)
#     print(f"Неотсортированный список: {not_sort_lst}")
#     print()
#     print(f"Отсортированный список содержащий только слова в нижнем регистре: {sort_lst}")

# lowcase_sort(not_sort_lst)

"""
Дан список кортежей (имя, возраст). 
Получите новый список, оставив кортеж в котором возраст > 18.
"""

# people = [("Анна", 25), ("Петя", 17), ("Мария", 19), ("Иван", 16), ("Ольга", 22)]
# adult_people = []


# def adult(lst):
#     for i in people:
#         name, age = i
#         if age > 18:
#             adult_people.append(i)
#     print(f"Полный список:{people}")
#     print(f"Список людей старше 18 лет:{adult_people}")


# adult(people)

"""
Дан список списков: [[1,2],[3,4],[5,6]]. 
С помощью reduce объединить в один список: [1,2,3,4,5,6].
"""

# from functools import reduce

# lst = [[1, 2], [3, 4], [5, 6]]
# red_lst = reduce(lambda x, y: x + y, lst)
# print(red_lst)

"""
Дан список ['cat','car','mouse','dog','snake','cow'].
Получить словарь: {начальная буква: [слова...]}.
"""

# word_lst = ["cat", "car", "mouse", "dog", "snake", "cow"]
# word_dict = {word[0]: [] for word in word_lst}
# for word in word_lst:
#     word_dict[word[0]].append(word)

# print(word_dict)

"""
Дан список кортежей (товар, цена, количество).
Получить список сумм: цена * количество.
"""

# products = [("банан", 5, 3), ("капуста", 3, 10), ("арбуз", 20, 5)]
# sums = [product[1] * product[2] for product in products]
# print(sums)
