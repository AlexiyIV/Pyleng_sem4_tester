#4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# многочлена, записать в файл полученный многочлен не менее 3-х раз.
import random

def polynomial(n):
    a1 = [int(i) for i in range(n, 0, -1)]
    a2 = [random.randint(-10, 10) for i in range(n)]
    with open('H:/обучение/Python_tester/Sem/Pyleng_sem4_tester/task4.txt', 'a') as f:
        if a2[0] !=0:
            f.write(f'{a2[0]}*x^{a1[0]}')
        for i in range(1, len(a1)):
            if 0 < a2[i]:
                f.write(f'+{a2[i]}*x^{a1[i]}')
            elif 0 > a2[i]:
                f.write(f'{a2[i]}*x^{a1[i]}')
        if 0 < a2[-1]:
            f.write(f'+{a2[-1]}=0\n')
        elif 0 > a2[-1]:
            f.write(f'{a2[-1]}=0\n')
        else:
            f.write(f'=0\n')

n = int(input('inter n='))
polynomial(n)
