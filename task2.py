#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def prime_factors(n):
    k = 2
    arr = []
    while n != 1:
        while n % k == 0:    
            arr.append(k)
            n = n/k
        k += 1
    return arr

n = int(input('Введите число N='))
pf = prime_factors(n)


print(pf)