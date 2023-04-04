def sum_even_number(seq):
    even = []
    for i in range(0, len(seq)):
        if seq[i] % 2 == 0:
            even.append(seq[i])
    return sum(even)

sum_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
