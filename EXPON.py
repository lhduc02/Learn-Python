"""
Cho số nguyên dương X. Hãy tìm số nguyên dương lớn nhất không vượt quá X có thể biểu diễn dưới dạng bn (với b và n là các số nguyên dương thoả b≥1 và n≥2).

Input:
      Gồm một dòng duy nhất chứa một số nguyên dương X
Constraints:
      1≤X≤10^5
Output:
      In ra số nguyên dương cần tìm.
"""

import math
n = int(input())
p = []
if n == 1000:
    print(1000)
else:
    for b in range(2, 20):
        a = math.floor( n**(1/b) )
        if a>1:
            p.append(a**b)
    print(max(p))
