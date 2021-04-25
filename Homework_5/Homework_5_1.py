#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------

# 1. Пользователь вводит данные о количестве предприятий,
# # их наименования и прибыль за четыре квартала для каждого предприятия.
# # Программа должна определить среднюю прибыль (за год для всех предприятий) и
# # отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

aa = []
alpha = 'a'
for i in range(0, 26):
    aa.append(alpha)
    alpha = chr(ord(alpha) + 1)

cc = int(input('Введите количество организаций'))

ii=0
while ii < cc:

    a = input('Наименование Предприятия')
    b = int(input('Прибыль Предприятия'))
    aa[ii] = Counter({'Предприятие': a ,'Прибыль':b})
    ii += 1

gg = 0

while gg < ii:
    for i,v in list(aa[gg].items()):
        if is_number(v) == False:
            h = v
        if is_number(v) == True:

            if v/4 > 1000 and v/4 <  10000:
                print(f'У предприятия{h} прибыль меньше среднего {v/4}')
            elif v / 4 > 10000:
                print(f'У предприятия{h} прибыль больше среднего {v / 4}')
            else:
                print(f'У предприятия{h} прибыль убыточная {v / 4}')
    gg += 1








