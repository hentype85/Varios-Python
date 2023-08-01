#!/usr/bin/python3

def roman_to_int(roman):
    """convertir números romanos a enteros"""

    if type(roman) != str:
        return 0

    d = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    res = 0
    for i in range(len(roman)):
        if i == len(roman) - 1 or d.get(roman[i]) >= d.get(roman[i + 1]):
            res += d.get(roman[i])
        else:
            res -= d.get(roman[i])
    return res


print(roman_to_int("VII"))
