def fillarray(n):
    a = []
    with open(f'H:/обучение/Python_tester/Sem/Pyleng_sem4_tester/{n}', 'r') as f:
        for line in f:
            a.append(line)
    return a

def deln(d):
    for i in range(len(d)):
        d[i] = d[i].strip('\n')

def delzero(n):
    for i in range(len(n)):
        data = list(n[i])
        data[-1] = ""
        data[-2] = ""
        n[i] = "".join(data)

def sum_polynomial(a1, a2):
    with open('H:/обучение/Python_tester/Sem/Pyleng_sem4_tester/task5_sum.txt', 'w', encoding='utf-8') as f:
        for i in range(len(a1)):
            data = list(a2[i])
            if data[0] != '-':
                f.write(f'{a1[i]}+{a2[i]}\n')
            else:
                f.write(f'{a1[i]}{a2[i]}\n')


f1 = 'task5_1.txt'
f2 = 'task5_2.txt'
array1 = fillarray(f1)
array2 = fillarray(f2)
deln(array1)
deln(array2)
delzero(array1)
sum_polynomial(array1, array2)
print(array1)
print(array2)
