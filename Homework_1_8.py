#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------

#8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

m = a
if m > b < c:
    m = b
    print(f'Среднее число оказалось {m}')
elif m > c < b:
    m = c
    print(f'Среднее число оказалось {m}')
else:
    print(f'Среднее число оказалось {m}')
