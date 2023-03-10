"""
Do tình hình dịch bệnh diễn biến phức tạp, việc học tập và giáo dục ở đất nước ABC chuyển sang học online trên ứng dụng “adobe LOL”.
Tèo là một học sinh ở lớp X, trường Y, tỉnh Z. Thầy giáo của Tèo mà một người tinh tế, biết rõ việc học online dễ xao nhãng khó tập trung.
Vì thế, trước buổi học sẽ đố vui với học sinh nhằm tạo hứng thú cho học trò.
Hôm nay thầy giáo đưa ra 3 số nguyên a, b, c được viết trên bảng là |a _ b _ c|.
Các học sinh cần đặt các kí hiệu toán học +, -, * vào các vị trí trống, người thắng cuộc là người đạt được kết quả nhỏ nhất.
Hãy giúp Tèo tìm ra kết quả nhỏ nhất.

Input:
      Dòng đầu chứa số nguyên T là số lượng testcase.
      T dòng sau đó, mỗi dòng chứa 3 số nguyên a b c.
Constraints:
      1 ≤ T ≤ 10^4
      −10^6 < a, b, c < 10^6
Output:
      In ra T dòng, mỗi dòng chứa một số nguyên duy nhất là kết quả của bài toán.
"""

def exp(a, b, c):
    m = abs(a*b*c)
    n = abs(a+b+c)
    p = abs(a-b-c)
    q = abs(a*b+c)
    r = abs(a+b*c)
    s = abs(a*b-c)
    t = abs(a-b*c)
    x = abs(a+b-c)
    y = abs(a-b+c)
    o = [m, n, p, q, r, s, t, x, y]
    return min(o)
n = int(input())
for i in range(n):
    a, b, c = [int(i) for i in input().split()]
    print(exp(a, b, c))
