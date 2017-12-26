#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    N = n - 1
    
    last_3 = N - N % 3
    last_5 = N - N % 5
    last_15 = N - N % 15
    
    count_3 = N // 3
    count_5 = N // 5
    count_15 = N // 15
    
    sum_3 = count_3 * (3+last_3) // 2
    sum_5 = count_5 * (5+last_5) // 2
    sum_15 = count_15 * (15+last_15) // 2
    
    print(sum_3 + sum_5 - sum_15)
