"""
An có một màn hình máy tính có tỉ lệ chiều rộng : chiều cao là a:b. An muốn xem một bộ phim có tỉ lệ chiều rộng khung hình : chiều cao khung hình là c:d.
An muốn phóng to hoặc thu nhỏ khung hình phim sao cho chiếm được nhiều nhất diện tích của màn hình và vừa khít nhưng vẫn đảm bảo được tỉ lệ gốc của khung hình gốc.
Hãy tính tỉ lệ diện tích của phần màn hình còn trống so với tổng diện tích của màn hình. In kết quả theo dạng phân số tối giản.

Input:
      Bốn số nguyên a, b, c, d (1 ≤ a, b, c, d ≤ 1000).

Output:
      In ra phân số tổi giản p/q là tỉ lệ diện tích của phần màn hình còn trống so với tổng diện tích của màn hình.

Sample Test 1
Input:
      4 3 2 2
Output:
      1/4

Sample Test 2
Input:
      3 4 2 3
Output:
      1/9
"""

from fractions import Fraction
a, b, c, d = [int(i) for i in input().split()]
if a/b < c/d:
    print(Fraction(b*c-a*d, b*c))
elif a/b == c/d:
    print("0/1")
else:
    print(Fraction(a*d-b*c, a*d))
