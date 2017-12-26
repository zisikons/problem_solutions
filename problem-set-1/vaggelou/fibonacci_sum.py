#!/usr/bin/python3

from __future__ import print_function
import sys
import math


def fibonacci(n):

    return ((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n) / (2**n * math.sqrt(5))


def calculateFibSum(n):

    counter = 0
    whole_sum = 0
    while True:
        fib = int(fibonacci(counter))
        if fib < n:
            if not fib % 2:
                whole_sum += fib
            counter += 1
        else:
            break

    return whole_sum


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(calculateFibSum(n))
        