#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------

#6. В программе генерируется случайное целое число от 0 до 100.
#Пользователь должен его отгадать не более чем за 10 попыток.
#После каждой неудачной попытки должно сообщаться,
#больше или меньше введенное пользователем число, чем то, что загадано.
#Если за 10 попыток число не отгадано, вывести ответ.

import random

a = random.randint(0,100)

i= 10

while i > 0:
    print(f'У вас {i} попыток что бы угадать загаданное число')
    b = int(input('Введите число '))
    if a == b:
        print(f'Поздравляем загаданное число было {a}')
    elif a > b:
        print(f'Ваше число {b} меньше загаданного')
    else:
        print(f'Ваще число {b} больше загаданного')
    i -= 1

