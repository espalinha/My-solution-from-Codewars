def keep_order(ary, val):
    i = 0
    cout = 0
    if len(ary ) == 0:
        return 0 
    while cout < len(ary):
        if val > ary[i]:
            i += 1
            cout += 1
        if cout == len(ary):
            return i 
        else:
            if val == ary[i]:
                return i
            if val < ary[i]:
                return i
        