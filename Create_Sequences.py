"""
Bi định nghĩa S(n) là số chữ số của 1 số nguyên dương n trong hệ thập phân.
Từ đó, Bi muốn tạo một dãy số nguyên liên tiếp bắt đầu từ số m(m,m+1,...) để phục vụ cho dự án.
Nhưng Bi cần phải trả S(n)⋅k chi phí để thêm số n vào dãy (với k là một hằng số có sẵn).
Bi có thể bỏ ra một khoản chi phí lên đến w và Bi muốn tạo ra một chuỗi càng dài càng tốt.
Giúp Bi tính độ dài tối đa của chuỗi để Bi còn chuẩn bị cho dự án nhé.

Yêu cầu: Tính độ dài tối đa của chuỗi.

Input:    Dòng duy nhất chứa 3 số w,m,k lần lượt là tổng chi phí Bi có, số khởi đầu và hằng số ban đầu mà Bi nhập vào.

Constraints
      1 ≤ w ≤ 10^16.
      1 ≤ m ≤ 10^16.
      1 ≤ k ≤ 10^9.

Output:   In ra độ dài tối đa của chuỗi tạo được.
"""

w, m, k = [int(i) for i in input().split()] #chi phi, khoi dau, hang so
c = len(str(m))
count = 0
while w>0:
    w-=c*k
    count+=1
print(count-1)
