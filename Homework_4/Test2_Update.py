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
    assert  num <= 5761455,'Слишком большой аргумент'
    func = { 4:10,
                25:10**2,
                168:10**33,
                1229:10**4,
                9592:10**5,
                78498:10**6,
                664579:10**7,
                5761455: 10**8
    }

    for key in func.keys():
        if num <= key:
            size = func[key]
            break


    array = [True for _ in range(size)]
    array[:2]=[False,False]
    c = 0

    for m in range(2,size):
        if array[m]:

            c +=1
            if c == num:
                return m

        for j in range (m **2, size,m):
            array[j] = False
    return None


            #####Так как примера лучше для теста небыло я тестирую на этом примере

# #Test cProfile
#cProfile.run('prime(5000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.338    0.338 <string>:1(<module>)
# 1    0.334    0.334    0.338    0.338 Test2.py:13(prime)
# 1    0.004    0.004    0.004    0.004 Test2.py:31(<listcomp>)
# 1    0.000    0.000    0.338    0.338 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}

#Test TimeIT

# python -m timeit -n 1000 -s "import Test2" "Test2.prime(10)"
# # 1000 loops, best of 5: 21.7 usec per loop
# #
# # python -m timeit -n 1000 -s "import Test2" "Test2.prime(20)"
# # 1000 loops, best of 5: 38.9 usec per loop
# #
# # python -m timeit -n 1000 -s "import Test2" "Test2.prime(25)"
# # 1000 loops, best of 5: 50.2 usec per loop
