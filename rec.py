

def ind_find_rec(lst, vl, lt, rt):

    if lt > rt:
        return 'None'
    else:
        ml = (lt + rt) // 2

        if lst[ml] == vl:
            fa = 'Индекс искомого числа: ' + str(ml)
            return fa
        elif vl < lst[ml]:
            return ind_find_rec(lst, vl, lt, rt - 1)
        else:
            return ind_find_rec(lst, vl, ml + 1, rt)

