#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------
import cProfile
def prime(num):
    func = { 4:10,
                25:10**2,
                168:10**33,
                1229:10**4,
                9592:10**5
    }

    for key in func.keys():
        if num <= key:
            size = func[key]
            break
    else:
        raise Exception('Слишком большой аргумент')


    array = [i for i in range(size)]
    array[1]=[0]

    for m in range(2,size):
        if array[m] != 0:

            j = m ** 2
            while j < size:
                array[j] = 0
                j+=m
    res = [i for i in array if i !=0]
    return res[num-1]


            #####Так как примера лучше для теста небыло я тестирую на этом примере

# #Test cProfile
#cProfile.run('prime(5000)')

# 1    0.000    0.000    0.037    0.037 <string>:1(<module>)
# 1    0.031    0.031    0.037    0.037 Test2.py:13(prime)
# 1    0.003    0.003    0.003    0.003 Test2.py:29(<listcomp>)
# 1    0.003    0.003    0.003    0.003 Test2.py:39(<listcomp>)
# 1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)



#Test TimeIT

# python -m timeit -n 1000 -s "import Test2" "Test2.prime(10)"
# 1000 loops, best of 5: 26.3 usec per loop

# python -m timeit -n 1000 -s "import Test2" "Test2.prime(20)"
# 1000 loops, best of 5: 27.1 usec per loop
#
# >python -m timeit -n 1000 -s "import Test2" "Test2.prime(25)"
# 1000 loops, best of 5: 26.5 usec per loop
