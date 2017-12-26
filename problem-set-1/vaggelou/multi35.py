#!/usr/bin/python3

from __future__ import print_function
import sys
import math


def calculateMultSum(n):

    whole_sum = 0

    i = 0
    while (i * 3) < n:
        whole_sum += i * 3
        i = i + 1

    i = 0
    while (i * 5) < n:
        if (i * 5) % 3:
            whole_sum += i * 5
        i = i + 1

    return whole_sum


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(calculateMultSum(n))
