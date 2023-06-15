#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    prev_val = 0

    for alpha in reversed(roman_string):
        value = roman_n.get(alpha, 0)

        if value >= prev_val:
            ans += value
        else:
            ans -= value

        prev_val = value

    return ans
