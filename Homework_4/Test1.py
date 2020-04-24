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
    count = 1
    current_prime = 2


    while count < num:
        current_prime += 1
        #for i in range(2,int(current_prime**0.5)+1):
        for i in range(2,current_prime):
            if current_prime % i == 0:
                break
        else:
            count +=1
    return current_prime

    #####Так как примера лучше для теста небыло я тестирую на этом примере

# #Test cProfile

#cProfile.run('prime(5000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000   11.430   11.430 <string>:1(<module>)
# 1   11.430   11.430   11.430   11.430 Test1.py:13(prime)
# 1    0.000    0.000   11.430   11.430 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Test TimeIT

# python -m timeit -n 1000 -s "import Test1" "Test1.prime(10)"
# 1000 loops, best of 5: 14.5 usec per loop
#
#python -m timeit -n 1000 -s "import Test1" "Test1.prime(50)"
# 1000 loops, best of 5: 327 usec per loop

# python -m timeit -n 1000 -s "import Test1" "Test1.prime(100)"
# # 1000 loops, best of 5: 1.47 msec per loop

