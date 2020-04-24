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
        #for i in range(2,current_prime):
            if current_prime % i == 0:
                break
        else:
            count +=1
    return current_prime


def test_prime(func):
    real = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]

    for i,item in enumerate(real,start=1):
        assert func(i) ==item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
prime(prime(1023))