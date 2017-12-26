#!/usr/bin/python3

T = int(input())

for _ in range(T):
    N = int(input())
    s = 2
    fib_1 = 1
    fib_2 = 2
    fib_3 = fib_1 + fib_2
    while fib_3 < N:
        s += (fib_3%2 == 0)*fib_3
        fib_1 = fib_2
        fib_2 = fib_3
        fib_3 = fib_1 + fib_2
    print(s)
