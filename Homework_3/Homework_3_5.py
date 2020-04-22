#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------
#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

array = [random.randint(-100,100) for _ in range(50)]
array.sort()
print(array)
print(f'Макссимально отрицательный элемент в массиве яляется {array[0]} и позиция у него в списке 1 если брать индексы то 0')