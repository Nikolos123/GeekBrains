#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------
#4. Определить, какое число в массиве встречается чаще всего.
import random
array = [1,43,-43,5,2,43,7,8,9,1,3,13,41,43,78,99,90,11,23,-14]
array.sort()
print(array)

i = 0
g = 0

for num in array:
    s = 0
    for c in array:
        if num == c:
            s+=1
    if s > i:
        i = s
        g = num
print(f'В нашем списке наибольшее количествол раз встретилась цифра {g}  {i} раза')

