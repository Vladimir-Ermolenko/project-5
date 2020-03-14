
import time
from itter import ind_find
from rec import ind_find_rec


fct_ch = input('\nВыберите способ решения: \n 1. Иттеративный \n 2. Рекурсивный \n')

if int(fct_ch) == 1:
    lst = list(map(int, input('Введите элементы списка через пробел: \n').split()))
    lst.sort()

    strt_tm = time.time()

    print(ind_find(lst))
    print('Время выполнения: ' + '~' + str(time.time() - strt_tm))

elif int(fct_ch) == 2:
    lst = list(map(int, input('Введите элементы списка через пробел: \n').split()))
    lst.sort()
    vl = int(input('Введите искомое число: '))
    lt = lst[0]
    rt = lst[-1]

    strt_tm = time.time()

    print(ind_find_rec(lst, vl, lt, rt))
    print('Время выполнения: ' + '~' + str(time.time() - strt_tm))

