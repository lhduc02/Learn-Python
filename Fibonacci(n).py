"""
Input:    n
Output:   Fibonacci(n)
"""

import math
n = int(input())
a = 1/math.sqrt(5) * ((1 + math.sqrt(5))/2)**n
b = 1/math.sqrt(5) * ((1 - math.sqrt(5))/2)**n
fn = a - b
print(round(fn))
