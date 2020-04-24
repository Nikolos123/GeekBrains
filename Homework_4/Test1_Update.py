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
        for i in range(2,int(current_prime**0.5)+1):
            if current_prime % i == 0:
                break
        else:
            count +=1
    return current_prime

    #####Так как примера лучше для теста небыло я тестирую на этом примере

# #Test cProfile

#cProfile.run('prime(5000)')

# 1    0.000    0.000    0.135    0.135 <string>:1(<module>)
# 1    0.000    0.000    0.135    0.135 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1    0.135    0.135    0.135    0.135 Без_Решета Эратосфена_Update.py:13(prime)

#Test TimeIT

# python -m timeit -n 1000 -s "import Test1_Update" "Test1_Update.prime(10)"
# 1000 loops, best of 5: 17.2 usec per loop

# python -m timeit -n 1000 -s "import Test1_Update" "Test1_Update.prime(50)"
# 1000 loops, best of 5: 161 usec per loop
#
# python -m timeit -n 1000 -s "import Test1_Update" "Test1_Update.prime(100)"
# 1000 loops, best of 5: 420 usec per loop