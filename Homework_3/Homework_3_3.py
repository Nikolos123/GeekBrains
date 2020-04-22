#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------
#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

array = [random.randint(-100,100) for _ in range(10)]
array.sort()
spam = array[0]
array[0] = array[-1]
array[-1]=spam
print(array)

