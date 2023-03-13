"""
Given 2 positive integers k and n. Write a program tat generates all k-combinations of 1, 2, ..., n in a lexicographic order.

Example:
Input:
      2
      4
Output:
      1 2
      1 3
      1 4
      2 3
      2 4
      3 4
"""
from itertools import permutations
k, n = [int(i) for i in input().split()]
p = [i for i in range(1, n+1)]

perm = permutations(p, k)
for i in list(perm):
    if list(i) == sorted(i):
        for j in i:
            print(j, end = " ")
        print()
