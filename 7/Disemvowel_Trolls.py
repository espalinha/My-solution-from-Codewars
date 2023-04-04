def disemvowel(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newstring = ''
    for char in string:
        if char in vowel_list:
            continue
        else:
            newstring += char
    print(newstring)

