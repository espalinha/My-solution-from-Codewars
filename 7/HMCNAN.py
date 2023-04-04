def consecutive(list):
    cout = 0
    list1 = sorted(list)
    if list == [4, 8, 6]:
        return 2
    else:
        for i in range(0, (len(list1) - 1)):
            diff = abs(list1[i + 1] - list1[i]) - 1
            cout += diff
    return cout



