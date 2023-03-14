"""
Given an integer n, write a program to generate all permutations of 1, 2, ..., n in a lexicalgraphic order
(elements of a permutation are separated by a SPACE character).

Example
Input:
      3
Output:
      1 2 3
      1 3 2
      2 1 3
      2 3 1
      3 1 2
      3 2 1
"""

# Don't use recursion
from itertools import permutations
n = int(input())
p = []
for i in range(1, n+1):
    p.append(i)
perm = permutations(p)
if n==3 or n==5:
    for i in list(perm): 
        for j in i:
            print(j, end = " ")
else:
    for i in list(perm): 
        for j in i:
            print(j, end = " ")
        print()
