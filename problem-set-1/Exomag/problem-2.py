#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    f1 = 1
    f2 = 2
    sum_even = 2
    
    while True:
        f = f1 + f2
        if f >= n:
            break
        f1 = f2
        f2 = f
        if f % 2 == 0:
            sum_even = sum_even + f
    
    print(sum_even)
