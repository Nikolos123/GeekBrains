#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------

import random
import string

#3. Написать программу, которая генерирует в указанных пользователем границах :
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.

ans = input(' Для получение целого числа из заданых границ введите "a" \n Для получение вещественного числа "b" \n Для получение случайного символа "c"\n ВВЕДИТЕ КОМАНДУ ИЗ ВЫЩЕ ОПИСАННЫХ ')

if ans == "a":
    a = int(input('Ведите первое число для назначения начало границы для вывода рандомного число '))
    b = int(input('Ведите второе число для назначения конца границы для вывода рандомного число '))
    print(f'Рандомное число - {random.randint(a,b)}')
elif ans =="b":
    a = float(input('Ведите первое число для назначения начало границы для вывода рандомного число '))
    b = float(input('Ведите второе число для назначения конца границы для вывода рандомного число '))
    print(f'Рандомное число - {random.uniform(a, b)}')
elif ans == "c":
    k = list(string.punctuation)
    print(k)
    a = input('Введите символ с которого начнется поиск ')
    b = input('Введите символ на которой закончится поиск ')
    if a in k and b in k:
        a = k.index(a)
        b = k.index(b)
        rws = random.randint(a, b)
        print(f'Случайный символ из выбранного диапазона  {k[rws]}')
    else:
        print(f'Вы ввели символы которых нет в списе {a},{b} \n Символы которые разрещено вводить \n {k}')
else:
    print('Вы ввели не существующую команду')
