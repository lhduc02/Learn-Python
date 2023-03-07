"""
An là một người kì cục, và cậu thích sự cô đơn. Cậu quyết định đi xem phim một mình, và đặt vé qua mạng.
An thích ngồi ở dãy hàng ghế F. Có tất cả A ghế ngồi ở hàng F, đánh số từ 1 đến A, tuy nhiên đã có một nhóm người gồm B−1 người đã đặt trước các ghế từ 2 đến B.
Vì không muốn ngồi gần người lạ, An nhất quyết không ngồi ghế số 1, và muốn ngồi xa mọi người nhất, tức là chọn ghế có chỉ số lớn nhất có thể.
Tuy nhiên, với bản tính kì cục của mình, An sẽ không chọn ngồi những ghế có chỉ số là bội số của ít nhất một trong B−1 số từ 2 đến B.

Yêu cầu: Hãy giúp An tìm được vị trí ghế phù hợp với yêu cầu của anh ấy.

Input:  Một dòng chứa hai số nguyên dương B và A (2 ≤ B ≤ A ≤ 10^9)

Output: Xuất ra chỉ số của chiếc ghế thỏa yêu cầu của An. Nếu không tìm được chiếc ghế thỏa yêu cầu, xuất ra −1.

Sample Test:
    Input: 51 76
    Output: 73
"""

import math
b, a = [int(i) for i in input().split()]
r = min(b, math.ceil(math.sqrt(a)))
for i in range(a, b, -1):
    c = 0
    for j in range(2, r+1):
        if i%j==0:
            break
        else:
            c+=1
    if c==r-1:
        print(i)
        break
if c!=r-1:
    print("-1")
