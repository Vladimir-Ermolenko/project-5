

def ind_find_rec(lst, vl):

    if len(lst) == 0:
        return 'None'

    ml = len(lst) // 2

    if lst[ml] == vl:
        fa = 'Индекс искомого числа: ' + str(ml)
        return fa
    else:
        if vl < lst[ml]:
            return ind_find_rec(lst[:ml], vl)
        else:
            return ind_find_rec(lst[ml + 1:], vl)

