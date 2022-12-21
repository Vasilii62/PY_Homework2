# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# 1.
# import time

# current_time = time.time()
# print(current_time)

# rand_num = int(100 * current_time)
# print(rand_num %100)
# print(str(rand_num)[-5:])

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# import os
# os.system("clear")

# list = ['2', '43', '5', '331', '91', '35', '79', '53']
# x = input('Введите число: ')

# for i in list:
#     if x == i:
#         print(f'Число {i} присутствует в списке')
#         break
# else:
#     print('Заданное число отсутствует в списке')

# Вариант 2
# def check(stringlist: list, n: str) -> bool:
#     for i in stringlist:
#         if n == i:
#             return True
#     return False

# my_list = ["2", "3", "3425", "0", "-1"]
# x = input("Введите искомое число: ")
# if check(my_list, x):
#     print("Число есть в последовательности", my_list)
# else:
#     print("Числа нет в последовательности", my_list)


# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# my_list =["qwe", "asd", "zxc", "qwe", "ertqwe"]
# print(my_list)

# string_find = "123"
# count = 0
# for i in range(len(my_list)):
#     if string_find == my_list[i]:
#         count = count+1
#         if count == 2:
#             print(i)
#             break
# else:
#     print(-1)

# Вариант 2

# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# my_str = input('Введите строку')
# if my_str in my_list:
#     my_index = my_list.index(my_str)
#     if my_str in my_list[my_index + 1:]:
#         print(my_list[my_index + 1:].index(my_str))
#     else:
#         print(-1)
# else:
#     print(-1)

# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# my_str = input('Введите строку: ')

# if my_list.count(my_str) > 1:
#     first_index = my_list.index(my_str)
#     print(my_list.index(my_str, first_index + 1))
# else:
#     print(-1)

# Срезы

# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# print(list(range(-20,40,5)))
# # range(start=0, stop=?, step=1)
# range(5) # 5 - stop ->  range(start=0, stop=5, step=1)
# range(3,7) #  ->  range(start=3, stop=7, step=1)
# range(3,7, 2) #  ->  range(start=3, stop=7, step=2)

# my_list[start:stop:step]
# print(my_list[5]) #-> "йцу"
# print(my_list[1:4]) #-> [ "фыв", "ячс", "цук"]
# print(my_list[1:4:2]) #-> [ "фыв", "ячс", "цук"]


# Домраб
# 2.
# sum = 1
# print(sum, end= ' ')
# for n in range(2,5):
#     sum *= n 
#     print(sum, end= ' ')

# 3.

# Задача № 3.

# Задай список из n чисел последовтельности (1+1/n)^n
# Выведи на экран их сумму.
#
# Пример:
# Для n= 4 {1: 2, 2:2.25, 3: 2.34, 4: 2.44}
# Сумма: 9,06


# def subsec(num):

#     #num = float(num)
#     # print(type(num), num) # <class 'int'> 4

#     # сгенерировать ряд от 1 до ... num (от 1 до 4)
#     arrLst = [i * 1 for i in range(1, num + 1)]
#     #print(arrLst)  # [1, 2, 3, 4]


#     # сборщик итогов
#     accum = 0

#     for j in arrLst:
#         expr = (1+1/j)**j
#         #print(expr, type(expr) ) # число и <class 'float'>

#         accum += expr
#         #print(accum, type(accum) ) # нараст. итог и <class 'float'>

#     return round(accum, 3)

# # вызов ф-ции:
# print(subsec(4))


# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# #*Пример:*
#     - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

# print('Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')
# n = int(input('Введите число N:-> '))
# seq = dict()
# seq_sum = 0
# for i in range(1, n+1):
#     seq[i] = round((1+1/i)**i, 2)
# print(f'Для N={n} {seq}')
# print(f'Сумма {sum(seq.values())}')

# 3.

# import random

# num = int(input("Ведите число: "))  # = 5
# my_list = []
# for i in range(num):
#     my_list.append(random.randint(-num, num))
# print(my_list)
# # делали так на 1й задаче 2го семинара

# path = 'file.txt'
# data = open(path, 'w')
# data.write('2\n')
# data.write('4\n')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# mult = 1
# for line in data:
#     mult*=my_list[int(line)]
#     # print(line, end='')
# print(mult)

# 5.

import random

# Вариант 1:

# def list_shuffle(my_list: list):
#     shuffled_list = []
#     temp_list = my_list
#     print(temp_list)

#     for _ in range(len(my_list)):
#         position = random.randint(0, len(temp_list) - 1)
#         shuffled_list.append(temp_list.pop(position))
#     return shuffled_list


# print(list_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# Вариант 2:

my_list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
orig_list = my_list
print(orig_list)
random.shuffle(my_list)
print(my_list)