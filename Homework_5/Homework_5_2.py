#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------


#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
#При этом каждое число представляется как массив, элементы которого — цифры числа.
#Например, пользователь ввёл A2 и C4F.
#Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
#соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import namedtuple,Counter

def ABCDEF(i,p):

    for j, v in p.items():
        if i == j:
            return v
            #F += v
    return None
def FEDCBA(i,c):
    for k,s in c.items():
        if i == k:
            return s
            #f +=s
    return None
def ABCSIM(simv):
    kk = 0
    if simv == '-':
        if ff > f:
            kk = ff - f
        else:
            kk = f - ff
    elif simv == "+":
        kk = f + ff
    elif simv == "*":
        kk = f * ff
    elif simv == '/':
        if f == 0 or ff == 0:
            print('Число деление на 0 запрещено')
        else:
            kk = f / ff

    print(f'Вычет произведен {kk}')


d = namedtuple('d', 'A, B, C, D, E, F')
t = [10, 11, 12, 13, 14, 15]
g = d._make(t)
p = g._asdict()

c = Counter({'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9})


a = input('Введите число в шестнадцатеричной системе исчисления')
b = [i for i in a.upper()]

f = 0
for i in b:
    b = FEDCBA(i,p)
    if b !=None:
        f += b
    else:
        d = ABCDEF(i,c)
        if d !=None:
            f+=d

aa = input('Введите число в шестнадцатеричной системе исчисления')
bb = [i for i in aa.upper()]

ff = 0
for ii in bb:
    bb = FEDCBA(ii,p)
    if bb !=None:
        ff += bb
    else:
        dd = ABCDEF(ii,c)
        if dd !=None:
            ff+=dd

simv = input('Ведите символ для этих чисел из списка - + / *')
ABCSIM(simv)

