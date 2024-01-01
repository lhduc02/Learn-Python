"""
Một số tự nhiên được gọi là số pow2num nếu nó có thể biểu diễn dưới dạng 2^k, với k là một số tự nhiên.
Cho số tự nhiên n, hãy kiểm tra n có phải số pow2num hay không.

Yêu cầu: in ra YES nếu số đã cho là số pow2num, ngược lại in ra NO.

Input:        Dòng duy nhất gồm số tự nhiên n
Constraints:  0≤n≤10^6
Output:       YES nếu n là số pow2num, NO nếu ngược lại.

Sample Test 1:
Input:  4
Output: YES

Sample Test 2
Input:  24222
Output: NO
"""

import math
 
n = int(input())
if n==0:
    print("NO")
else:
    a = math.log(n) / math.log(2)
    if a == round(a):
        print("YES")
    else:
        print("NO")

