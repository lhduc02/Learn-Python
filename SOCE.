"""
Một mạng xã hội có n người sử dụng tương ứng với n tài khoản X1, X2, ..., Xn, tài khoản thứ i có mật khẩu là Pi
Hôm nay, server ghi nhận k lượt đăng nhập, lượt thứ i có một người nhập vào tên đăng nhập là xi , mật khẩu là pi.
Một lượt đăng nhập (x,p) được gọi là thành công nếu tên đăng nhập trùng với một tên đăng nhập của một trong số những người sử dụng,
và mật khẩu trùng khớp với tên đăng nhập tương ứng, tức tồn tại i (1 ≤ i ≤ n) sao cho x = Xi và p = Pi.

Khi đó, ta tính người dùng thứ i có một lượt đăng nhập thành công.Hãy cho biết, mỗi người sử dụng đăng nhập thành công bao nhiêu lần?

Input:
      + Dòng đầu tiên chứa số n là số người sử dụng. Dữ liệu đảm bảo không có hai người sử dụng trùng tên đăng nhập.
      + n dòng tiếp theo, dòng thứ i chứa cặp xâu Xi, Pi lần lượt là tên đăng nhập và mật khẩu của người thứ i.
      + Dòng tiếp theo chứa số k là số lượt đăng nhập server ghi nhận hôm nay.
      + k dòng cuối cùng, dòng thứ i chứa cặp xâu xi, pi là tên đăng nhập và mật khẩu được nhập ở lượt đăng nhập thứ i.

Constraints:
      n ≤ 100, k ≤ 1000. Toàn bộ các xâu có độ dài không quá 20.
Output:
      k số trên một dòng, số thứ i là số lượt đăng nhập thành công của người thứ i.

Sample Test
Input:
      4
      tendangnhap matkhau
      username password
      nguoidung m4tkh4un4yr4tb40m4t
      user2 password
      6
      tendangnhap matkhau
      username matkhau
      bfc34 contest
      username password
      tendangnhap matkhau
      user2 password

Output:
      2 1 0 1
"""

n = int(input())
p = []
q = []
for i in range(n):
    a, b = input().split()
    p.append(a)
    q.append(a+b)
 
p1 = []
q1 = []
k = int(input())
for i in range(k):
    a, b = input().split()
    p1.append(a)
    q1.append(a+b)
 
for i in range(n):
    c = 0
    for j in range(k):
        if p[i]==p1[j] and q[i]==q1[j]:
            c+=1
    print(c, end = " ")
