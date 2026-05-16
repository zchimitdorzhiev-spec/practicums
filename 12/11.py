def ind_maxlist(a):
    if len(a) == 1:
        return 0
    m = ind_maxlist(a[1:]) + 1
    return 0 if a[0] >= a[m] else m