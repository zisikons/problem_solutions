#!/usr/bin/python3

from collections import Counter

def number_needed(a, b):

    set_a = set(a)
    set_b = set(b)
    freq_a = Counter(a)
    freq_b = Counter(b)

    remove_sum = 0
    for char in set_a:
        if char in set_b:
            remove_sum += abs(freq_a[char] - freq_b[char])
        else:
            remove_sum += freq_a[char]

    for char in set_b:
        if char not in set_a:
            remove_sum += freq_b[char]

    return remove_sum


a = input().strip()
b = input().strip()

print(number_needed(a, b))
