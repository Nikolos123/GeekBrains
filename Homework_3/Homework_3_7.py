#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------
#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random

array = [random.randint(1,1000) for _ in range(10)]
array.sort()
print(array)

print(f'Самый меленький элементы = {array[0]} следущий элементы = {array[1]}')