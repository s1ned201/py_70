"""
Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных,
и функцию которая находит наибольшее значение из этих двух переменных.
"""

# class Variables:
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b

#     def show(self):
#         print(f"a = {self.a}, b = {self.b}")

#     def change(self, new_a=None, new_b=None):
#         if new_a is not None:
#             self.a = new_a

#         if new_b is not None:
#             self.b = new_b

#         print(f"Новые значения для переменных: a = {new_a}, b = {new_b}")

#     def sum(self):
#         result = self.a + self.b
#         print(f"Cумма {self.a} + {self.b} = {result}")
#         return result

#     def max_value(self):
#         max_val = max(self.a, self.b)
#         print(f"Максимальное из: {self.a}, {self.b} -> {max_val}")
#         return max_val


# var = Variables(5,3)
# var.show()
# var.sum()
# var.max_value()
# var.change(10,11)
# var.show()
# var.sum()
# var.max_value()

"""
Описать класс, реализующий десятичный счетчик, который может увеличивать или 
уменьшать свое значение на единицу в заданном диапазоне. Предусмотреть инициализацию 
счетчика значениями по умолчанию и произвольными значениями. Счетчик имеет два метода: 
увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. 
Написать программу, демонстрирующую все возможности класса.
"""


# class Counter:
#     def __init__(self, min_value=0, max_value=0, current=None):
#         if min_value > max_value:
#             raise ValueError("Некорректный диапазон")

#         self.min = min_value
#         self.max = max_value

#         if current is not None:
#             self.current = current
#         else:
#             self.current = min_value

#         if self.current < self.min or self.current > self.max:
#             raise ValueError("Текущее значение вне диапазона")

#     def more(self):
#         if self.current < self.max:
#             self.current += 1
#         else:
#             raise ArithmeticError("Вы достигли максимального значения диапазона")

#     def less(self):
#         if self.current > self.min:
#             self.current -= 1
#         else:
#             raise ArithmeticError("Вы достигли минимального значения диапазона")

#     def cur_val(self):
#         print(f"Текущее значение: {self.current}")


# count = Counter(1, 10, 5)

# count.cur_val()
# count.more()
# count.less()

"""
Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, 
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
"""


# class Shop:
#     def __init__(self, name=""):
#         self.name = name
#         self.products = []

#     def add_product(self, product_name, price=0, quantity=1):
#         product = {
#             "Название товара": product_name,
#             "Цена": price,
#             "Количество": quantity
#             }
#         self.products.append(product)
#         print(f"Добавлен продукт: {product_name}, цена: {price}, количество: {quantity}")

#     def del_product(self, product_name):
#         count = 0
#         i = 0
#         while i<len(self.products):
#             if self.products[i]["Название товара"] == product_name:
#                 removed_product = self.products.pop(i)
#                 count += 1
#                 print(f"Удален продукт: {removed_product["Название товара"]}")
#             else:
#                 i += 1

#             if count == 0:
#                 print(f"Продукт '{product_name}' не найден")

#     def search_product(self, product_name):
#         found_products = []
#         for product in self.products:
#             if product_name.lower() in product["Название товара"].lower():
#                 found_products.append(product)
#             else:
#                 print(f"Товара с названием: {product_name}, в данный момент нет в наличии")
#         print(f"Товар с названием: {product_name}, в наличии")

#     def show_all(self):
#         if not self.products:
#             print("Магазин пуст, приходите завтра!")
#         else:
#             print(self.products)
#             print(f"Всего товаров: {len(self.products)}")


# magazine = Shop("Евроопт")
# magazine.show_all()
# magazine.add_product("Бананы", 10, 3)
# magazine.add_product("Колбаса", 20, 10)
# magazine.add_product("Сыр", 5, 6)
# magazine.add_product("Молоко", 3, 10)
# magazine.add_product("Кока-кола", 2, 5)
# magazine.add_product("Помидор", 5, 2)
# magazine.show_all()
# magazine.del_product("Кока-кола")
# magazine.show_all()

"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой. 
Каждая копилка имеет ограниченную вместимость, которая выражается целым 
числом – количеством монет(capacity -вместимость), которые можно положить в копилку. 
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность 
добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, 
не превышая ее вместимость. 

Класс должен иметь следующий вид:

class MoneyBox: 
    def__init__(self, capacity) :
    #конструктор с аргументом- вместимость копилки 
    def can_add(self,v)
    #True, если можно добавить v монет, False иначе
    def add(self,v)
    #положить v монет в копилку

При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
"""


# class MoneyBox:
#     def __init__(self, capacity=100):
#         self.capacity = capacity
#         self.current_count = 0

#     def can_add(self):
#         can_add_counter = self.capacity - self.current_count
#         print(f"В копилку можно добавить {can_add_counter} монет")

#     def can_add_v(self, v):
#         can_add_counter = self.capacity - self.current_count
#         if v <= can_add_counter:
#             self.can = True
#             return True
#         else:
#             self.can = False
#             print(f"Невозможно добавить {v} монет")
#             return False

#     def add(self, v):
#         if self.can_add_v(v) is True:
#             self.current_count += v
#             print(f"Добавлено {v} монет. В копилке {self.current_count} монет")
#         else:
#             print(f"Невозможно добавить {v} монет")

#     def show(self):
#         print(f"В копилке {self.current_count} монет")


# money = MoneyBox(50)
# money.show()
# money.can_add()
# money.can_add_v(51)
# money.add(25)
# money.show()
