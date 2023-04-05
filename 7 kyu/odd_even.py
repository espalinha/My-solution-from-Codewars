def sort_my_string(s):
    lineeven = ''
    lineodd = ''
    for i in range(0, len(s)):
        if i % 2 == 0:
            lineeven = lineeven + s[i]
        else:
            lineodd += s[i]
    return lineeven + ' ' + lineodd

sort_my_string("CodeWars")