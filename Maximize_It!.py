"""
You are given a function f(X) = X^2. You are also given K lists. The i^th list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
  S = ( f(X1) + f(X2) + ... + f(Xk) ) % M
  Xi denotes the element picked from the i^th list. Find the maximized value S_max obtained.
  % denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element.
You add the squares of the chosen elements and perform the modulo operation.
The maximum value that you can obtain, will be the answer to the problem.

Input Format:
  The first line contains 2 space separated integers K and M.
  The next K lines each contains an integer Ni, denoting the number of elements
  in the  list, followed by Ni space separated integers denoting the elements in the list.

Constraints:
  1 <= K <= 7
  1 <= M <= 1000
  1 <= Ni <= 7
  1<= arr[i] <= 10^9

Output Format:
  Output a single integer denoting the value .


Sample Input:
  3 1000
  2 5 4
  3 7 8 9 
  5 5 7 8 9 10 
Sample Output
  206

Explanation:
  Picking 5 from the st list, 1st from the 2nd list and 10 from the 3rd list gives 
  the maximum S value equal to (5^2 + 9^2 + 10^2) % 1000 = 206.
"""

import itertools
k, m = [int(i) for i in input().split()]
a = []
for i in range(k):
    p = [int(i)*int(i) for i in input().split()]
    a.append(p[1:])

lst = []

if k==1:
    for r in itertools.product(a[0]):
        lst.append(sum(r) % m)

if k==2:
    for r in itertools.product(a[0], a[1]):
        lst.append(sum(r) % m)

if k==3:
    for r in itertools.product(a[0], a[1], a[2]):
        lst.append(sum(r) % m)

if k==4:
    for r in itertools.product(a[0], a[1], a[2], a[3]):
        lst.append(sum(r) % m)

if k==5:
    for r in itertools.product(a[0], a[1], a[2], a[3], a[4]):
        lst.append(sum(r) % m)

if k==6:
    for r in itertools.product(a[0], a[1], a[2], a[3], a[4], a[5]):
        lst.append(sum(r) % m)

if k==7:
    for r in itertools.product(a[0], a[1], a[2], a[3], a[4], a[5], a[6]):
        lst.append(sum(r) % m)

print(max(lst))
