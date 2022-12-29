#. Вычислить число c заданной точностью d
import math
def accuracy(n, k):
    count = 0
    while k < 1:
        count +=1
        k *= 10
    return round(n, count)



n = float(input('Введите число N='))
a = float(input('Введите точность a='))
na = accuracy(n, a)
print(na)