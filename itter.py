

def ind_find(lst):
    vl = int(input('Введите искомое число: '))

    lt = 0
    ml = len(lst) // 2
    rt = len(lst) - 1

    while lst[ml] != vl and lt <= rt:
        if vl > lst[ml]:
            lt = ml + 1
        else:
            rt = ml - 1

        ml = (lt + rt) // 2

    if lt > rt:
        return None
    else:
        fa = 'Индекс искомого числа: ' + str(ml)
        return fa
