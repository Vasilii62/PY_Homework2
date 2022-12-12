# Задача 1 Напишите программу, которая принимает на вход два

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))

# if num1 ** 2 == num2 or num2 ** 2 == num1:
#     print('Да')
# else:
#     print('Нет')

# Задача 2

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите иторое число: '))
# num3 = int(input('Введите третье число: '))
# num4 = int(input('Введите четвертое число: '))
# num5 = int(input('Введите пятое число: '))


# if num1 > num2 and  num1 > num3 and num1 > num4 and num1 > num5:
#     print(f'{num1} максимальное')
# elif num2 > num1 and  num2 > num3 and num2 > num4 and num2 > num5:
#     print(f'{num2} максимальное')
# elif num3 > num1 and  num3 > num2 and num3 > num4 and num3 > num5:
#     print(f'{num3} максимальное') 

# array = [num1, num2, num3, num4, num5]
# max_num = array[0]
# for i in array:
#     if max_num < i:
#         max_num = i
# print(array)
# print(f'Максималное число = {max_num}')

# numbers = [1, 4, 6, 2, 3]
# # for i in range(1,6):
# #     numbers.append(int(input(f'Введите элемент под номером {i}: ')))
# print(numbers)
# print(max(numbers))

# my_max = 0
# for _ in range(5):
#     num = int(input('Введите число: '))
#     if my_max < num:
#         my_max = num

# print(my_max)

# range(5) -> range(start=0, stop=5, step=1):
# range(1,5) -> range(start=1, stop=5, step=1)
# range(1,9,2)range(start=1, stop=9, step=2)
# range(9,1,-1)range(start=9, stop=1, step=-1)


# Задача 3 Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
    # *Примеры:* 
    
    # - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# n = int(input('введите число: '))
# if n < 0:
#     n *= -1
# for i in range(-n, n+1):
#     print(i, end=' ')

# Задача 4 Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
    # *Примеры:*
    
    # - 6,78 -> 7
    # - 5 -> нет
    # - 0,34 -> 3


# num = input('Enter number: ')
# if '.' in num:
#     index_num = num.find('.') + 1
#     print(num[index_num])
# else:
#         print('No')

# num = float(input('Введите дробное число: '))
# if num % 1 == 0:
#     print('нет')
# else:
#     num = int(num*10 % 10)
#     print(num)

# num = input('Введите дробное число: ')
# if num.isdigit():
#     print('нет')
# else:
#     num = int(float(num)*10 % 10)
#     print(num)

# Задача 5 Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


# num = int(input('Enter number: '))
# if num % 30 != 0:
#     print("no")
# else: num % 5 == 0 and num % 10 == 0 or num % 15 == 0:
#     print('yes')


number = int(input('Enter number: '))
if number % 5 == 0 and number % 15 or number % 10 and number % 30 != 0:
        print("All done")
else:
        print("No")



