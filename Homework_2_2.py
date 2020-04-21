#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------

#2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
#если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите целое число: '))
aa = ''
bb = ''
aanum = 0
bbnum = 0
print(f'Вы ввели число {num} ')
while num > 0:
    b = num%10
    if b%2 == 0:
        aa += str(b)
        aanum +=1
    else:
        bb += str(b)
        bbnum  +=1
    num//=10
print(f'В нем {aanum} четных чисел ({aa}) ,а не четны[ {bbnum} ({bb})')
