#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------
#6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17]
array.sort()
print(array)

b = array[1:-1]
print(b)
c = 0
for i in b:
    c +=i
print(c)

