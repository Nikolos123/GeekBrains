#------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

#------------------------------------------
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

def test_prime(func):
    real = [2,3,	5,	7,	11,	13,	17,	19,	23,	29,	31,	37,	41,	43,	47,	53,	59,	61,	67]

    for i,item in enumerate(real,start=1):
        assert func(i) ==item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')

test_prime(prime)
prime(prime(1023))