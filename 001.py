#!/usr/bin/env python

"""
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples(below, divs):
    return sum(i for i in range(below) if any(i % div == 0 for div in divs))

print(sum_multiples(1000, [3, 5]))
