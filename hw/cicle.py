# 9 
# text = input("Enter your text: ")
# text = text.replace(',', ', ')
# while '  ' in text:
#     text = text.replace('  ', ' ')
# print(text)
# Оно работает, но я не понимаю как она распознает 2+ пробелов и в какой момент прерывается цикл

# 6 
# n = int(input("Введите число: "))
# nums = [1, 4, 9, 16, 25]
# for num in nums:
#     if n > num:
#         print(num, end=' ')

# 10
# n = int(input("Введите натуральное число(в диапазоне 1-1000): "))
# if n > 1000:
#     print("Вы не попали в заданный диапазон!!!")
# else:    
#     for cows in range(1, n + 1):
#         last_n = cows % 10
#         last_2_n = cows % 100
#         if last_n == 1 and last_2_n != 11:
#             end = 'корова'
#         elif 2 <= last_n <= 4 and not (12 <= last_2_n <= 14):
#             end = 'коровы'
#         else:
#             end = 'коров'
#         print(f"На лугу {cows} {end}")

# 11
# dna = input("Введите строку: ")
# result = ""
# letter = dna[0]
# count = 1
# for i in range(1, len(dna)):
#     if dna[i] == letter:
#         count += 1
#     else:
#         result += letter + str(count)
#         letter = dna[i]
#         count = 1
# result += letter + str(count)
# print(result)

# 12
# a = int(input("Введите кол-во биологов: "))
# b = int(input("Введите кол-во информатиков: "))
# x, y = a, b
# while y:
#     x, y = y, x % y
# nod = x
# d = (a * b) // nod
# print(d)