from collections import Counter


def number_needed(a, b):
    letters_in_a = set(a)
    letters_in_b = set(b)
    letters_count_in_a = Counter(a)
    letters_count_in_b = Counter(b)

    s = 0
    for letter in letters_in_a:
        s = s + abs(letters_count_in_a[letter]-letters_count_in_b[letter])
    for letter in letters_in_b:
        if letters_count_in_a[letter] == 0:
            s = s + letters_count_in_b[letter]
    
    return s


a = input().strip()
b = input().strip()

print(number_needed(a, b))
