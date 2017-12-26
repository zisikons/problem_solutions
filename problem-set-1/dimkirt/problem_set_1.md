# 1st Problem Set (Deadline 27/12/2017)

For the first problem set we have some easy problems to warm up. Below are the solutions.

## Project Euler #1: Multiples of 3 and 5

The task of this problem is to find the sum of all numbers up to a number 'n' that are multiples of the number 3 and 5. Instead of checking all numbers one by one up to number 'n' we can get all the multiples of 3 and 5 that are smaller to number 'n'. Moreover because some numbers are multiples of both 3 and 5 we count them two times so we have to subtract them one time to achieve this we subtract all multiples of 15 up to number 'n'.

```python
#!/bin/python3
import sys

def calculateMultiples(n):
    listA = []

    i = 0
    # Add multiples of 3
    while(i*3 < n):
        listA.append(i*3)
        i = i + 1

    i = 0
    # Add multiples of 5
    while(i*5 < n):
        listA.append(i*5)
        i = i + 1

    i = 0
    # subtract multiples of 15
    while(i*15 < n):
        listA.append(-i*15)
        i = i + 1

    return sum(listA)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(calculateMultiples(n))

```

Even though we only calculate the multiples of 3, 5 and 15 and thus we save lots of time in comparison with checking each number one by one, if the number 'n' is very large this solution also takes a lot of time. We can use [this math formula](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF) to get the sum of all natural numbers up to a number 'n'. Using this formula we can create a solution with O(1) time complexity instead  of O(n).

```python
#!/bin/python3
import sys

def calculateMultiples(n):
    # n1, n2, n3 is the n for the math formula for each of the three sums
    n1 = n // 3
    n2 = n // 5
    n3 = n // 15

    # We don't want to take into account the number 'n'
    if n % 3 == 0:
        n1 = n1 - 1
    if n % 5 == 0:
        n2 = n2 - 1
    if n % 15 == 0:
        n3 = n3 - 1

    # Because we have very large number if we divide it and then floor it we have error
    # we do integer division instead
    return ( 3*n1*(n1+1) + 5*n2*(n2+1) - 15*n3*(n3+1) ) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (calculateMultiples(n))

```

## Project Euler #2: Even Fibonacci numbers

The task of this problem is to sum all the even numbers of the fibonacci sequence up to the given number 'n'. In order to solve this problem we generate the fibonacci sequence up to the number 'n' and while we do that, in each step we check if the genrated number is even and if so we add it to the sum we return at the end.

```python
#!/bin/python3
import sys

def calculateEvenFiboSum(n):
    suma = 0
    f0 = 0
    f1 = 1
    fn = f0 + f1

    while fn < n:
        if fn % 2 == 0:
            suma += fn
        f0 = f1
        f1 = fn
        fn = f0 + f1
    return suma

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(calculateEvenFiboSum(n))

```

## CTCI Making Anagrams

The task of the problem is count the chars you have to remove from two given strings in order for the them become anagram of each other. To solve this problem I first created a frequency dictionary for the characters of each one of the two strings. Then using sets I find the chars that are only in one of the two dictionaries and sum their frequencies. In the end I also add possible differences in in frequency in characters that appear in both strings.

**Solution:**

```python

from collections import defaultdict

def number_needed(a, b):

    freq_a = defaultdict(int)
    freq_b = defaultdict(int)

    for char in a:
        freq_a[char] += 1

    for char in b:
        freq_b[char] += 1

    set_a = set(freq_a.keys())
    set_b = set(freq_b.keys())

    intersection = set_a & set_b
    union = set_a | set_b

    suma = 0

    to_remove = union - intersection

    for x in to_remove:
        if x in freq_a:
            suma += freq_a[x]
        else:
            suma += freq_b[x]

    for x in intersection:
        suma += abs(freq_a[x] - freq_b[x])

    return suma

a = input().strip()
b = input().strip()

print(number_needed(a, b))

```

## Irrelevant Hints

Suppose we have a list with numbers and we want to get the sum of all even numbers in the list, we can use reduce to do it one line:

```python
import functools as fnt
listA = [1,2,3,4,5,6,7,8,9,10]

# We define a lambda function and then we apply it on the listA
# reduce args: function to apply, list to transform, initial value of the accumulator
# the accumulator is the first arg of the lambda
sumEven = fnt.reduce((lambda accum,x: accum+x if x%2 == 0 else accum+0), listA, 0)
print (sumEven)  # output: 30
```

## Sources

- [Link to Project Euler #1](https://www.hackerrank.com/contests/projecteuler/challenges/euler001)
- [Link to Project Euler #2](https://www.hackerrank.com/contests/projecteuler/challenges/euler002)
- [Link to CTCI Making Anagrams](https://www.hackerrank.com/challenges/ctci-making-anagrams/problem)