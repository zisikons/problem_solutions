#!/usr/bin/python3

T = int(input())

for _ in range(T):
    N = int(input()) - 1

    N_3 = N - N%3
    N_5 = N - N%5
    N_15 = N - N%15

    l_3 = N//3
    l_5 = N//5
    l_15 = N//15

    sum_3 = l_3*(3 + N_3)//2
    sum_5 = l_5*(5 + N_5)//2
    sum_15 = l_15*(15 + N_15)//2
    print(sum_3 + sum_5 - sum_15)
