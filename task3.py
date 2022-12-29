#3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности в том же порядке.
import random
def fillarray1(n, min, max):
    arr = [random.randint(min, max) for i in range(n)]
    return arr

def fillarray2(arr):
    a = []
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            a.append(arr[i])
    return a

n = int(input('Введите количество элементов n='))
min = int(input('Введите ограничение от '))
max = int(input('Введите ограничение до '))

array1 = fillarray1(n, min, max)
array2 = fillarray2(array1) 
print(array1)
print(array2)