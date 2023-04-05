def all_non_consecutive(arr):
    list_answer = []
    for j in range(0, len(arr) - 1):
        if arr[j + 1] - arr[j] != 1:
            dictkey = {}
            dictkey['i'] = j + 1
            dictkey['n'] = arr[j + 1]
            list_answer.append(dictkey)
        else:
            continue
    return list_answer


all_non_consecutive([1, 2, 3, 4, 6, 7, 8, 10])
