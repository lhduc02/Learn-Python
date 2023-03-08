"""
Nhàn rỗi không có việc gì, An và Phương cùng nhau chơi game.Luật chơi rất đơn giản: Ban đầu họ có một tập gồm n số nguyên khác nhau.
Hai người thay phiên nhau thực hiện bước sau: đến lượt người nào thì người đó sẽ chọn 2 số nguyên x và y trong tập trên
sao cho trong tập đó không tồn tại số bằng giá trị tuyệt đối của hiệu |x - y|.

Khi đó người đó sẽ thêm số này vào tập đã có (lúc đó số lượng phần tử trong tập sẽ tăng lên một)
Nếu đến lượt người nào mà không thực hiện được bước trên thì coi như là thua cuộc.
Vậy ai sẽ là người chiến thắng nếu cho rằng An và Phương đều đi tối ưu nhất và An luôn là người đi trước.

Input:
      Dòng đầu tiên là số n (2 ≤ n ≤ 100) là số lượng các số trong tập.
      Dòng số hai chứa n số nguyên phân cách bởi dấu cách: a1, a2, ..., an (1 <= ai <= 10^9) là các phần tử trong tập.

Output:     In tên người thắng cuộc (An hoặc là Phuong)

Sample Test
Input:
      3
      5 6 7

Output:
      Phuong
"""

def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a%b)
 
n = int(input())
p = [int(i) for i in input().split()]
 
uc = ucln(p[0], p[1])
for i in range(2, n):
    uc = ucln(uc, p[i])
 
sub = max(p)/uc - n
if sub%2==0:
    print("Phuong")
else:
    print("An")
