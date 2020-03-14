
import time
from itter import ind_find
from rec import ind_find_rec


fct_ch = input('\nВыберите способ решения: \n 1. Иттеративный \n 2. Рекурсивный \n')

if int(fct_ch) == 1:
    lst = list(map(int, input('Введите элементы списка через пробел: \n').split()))

    strt_tm  = time.time()

    print(ind_find(lst))
    print('Время выполнения: ' + '~' + str(round(time.time() - strt_tm, 2)))

elif int(fct_ch) == 2:
    lst = list(map(int, input('Введите элементы списка через пробел: \n').split()))
    vl = int(input('Введите искомое число: '))

    strt_tm = time.time()

    print(ind_find_rec(lst, vl))
    print('Время выполнения: ' + '~' + str(round(time.time() - strt_tm, 2)))

