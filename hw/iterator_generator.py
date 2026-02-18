"""
Создайте класс RangeIterator, который реализует протокол итератора (__iter__, __next__).
Итератор должен возвращать числа в заданном диапазоне с указанным шагом.
После окончания итерации должно выбрасываться исключение StopIteration.
"""


# class RangeIterator:

#     def __init__(self, start_range: int, stop_range: int, step_range: int):
#         self.start_range = start_range
#         self.stop_range = stop_range
#         self.step_range = step_range

#     def __iter__(self):
#         return self

#     def __next__(self):
#         for i in range(self.start_range, self.stop_range, self.step_range):
#             print(i)
#         raise StopIteration

# iteration = RangeIterator(1, 10, 2)

# for value in iteration:
#     print(value)


"""
Напишите генераторную функцию fibonacci(limit),
которая возвращает последовательность Фибоначчи до заданного предела. 
Генерация должна останавливаться, когда значение превышает limit.
"""


# def fibonacci_generator(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b

# for num in fibonacci_generator(100):
#     print(num, end=" ")

"""
Создайте класс LogReader, который читает строки из источника данных и является итерируемым объектом.
Класс должен:
- поддерживать перебор через for
- пропускать пустые строки
- возвращать строки по одной без загрузки всех данных в память
"""

# class LogReader:
#     def __init__(self, src_data):
#         self.src_data = src_data

#     def __iter__(self):
#         for data in self.src_data:
#             if data.strip():
#                 yield data


# data_lst = ['', 'ga sdgf', 'as  dfa  dsf', 'gsaasdf', '  ', 'asdfaa', 'asdfasdf']

# loger = LogReader(data_lst)

# for log in loger:
#     print(log)


"""
Напишите генераторную функцию flatten(iterable),
которая принимает вложенную структуру (списки внутри списков) и возвращает элементы в плоском виде.
Решение должно корректно обрабатывать любую глубину вложенности.
Simple input:
[1, [2, 3], [[4], 5], 6]
Simple Output:
1 → 2 → 3 → 4 → 5 → 6
"""

# def flatten(iterable):
#     for item in iterable:
#         if isinstance(item, list):
#             yield from flatten(item)
#         else:
#             yield item


# test_lst = [1, [2, 3], [[4], 5], 6]


# flat = []

# for item in flatten(test_lst):
#     flat.append(str(item))

# print(" → ".join(flat))
