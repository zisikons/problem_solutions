#!/usr/bin/python3

def number_needed(a, b):
    sa = set(a)
    sb = set(b)
    fa = {k: a.count(k) for k in sa}
    fb = {k: b.count(k) for k in sb}

    ans = sum(abs(fa[i] - fb[i]) for i in sa & sb)
    ans += sum(fa[i] for i in sa - sb)
    ans += sum(fb[i] for i in sb - sa)
    return ans

a = input().strip()
b = input().strip()

print(number_needed(a, b))
