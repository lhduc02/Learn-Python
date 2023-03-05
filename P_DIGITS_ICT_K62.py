"""
Write C program that reads an integer value N from stdin,
prints to stdout the number Q ways to assign values 1, 2, …, 9 to characters I, C, T, H, U, S, K (characters are assigned with different values)
such that: ICT - K62 + HUST = N

Input: Unique line contains an integer N (1 <= N <= 10 5 )
Output: Write the value Q

Example:
      Input: 2000
      Output: 28
"""

from itertools import permutations
import math
n = int(input())
comb = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
count = 0
for j in comb:
    i, c, t, k, h, u, s = j
    if 1000*h + 100*(i+u-k) + 10*(c+s-6) + 2*t-2 == n:
        count += 1
print(count)
