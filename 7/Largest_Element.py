def largest(n, list):
    list_big = []
    new = sorted(list, reverse=True)
    while n > 0:
        n -= 1
        list_big.append(new[0])
        del (new[0])

    return sorted(list_big, reverse=False)


