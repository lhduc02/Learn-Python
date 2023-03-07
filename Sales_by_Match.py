"""
Có một đống tất lớn phải được ghép theo màu. Cho một mảng các số nguyên biểu thị màu của mỗi chiếc tất, hãy xác định xem có bao nhiêu đôi tất có màu phù hợp.
Thí dụ:
        n=7
        arr=[1,2,1,2,1,3,2]

Có một cặp màu của màu 1 và một cặp màu của màu 2 . Còn lại ba chiếc tất lẻ, mỗi chiếc một màu. Số cặp là 2.

Mô tả chức năng:  Hoàn thành hàm sockMerchant trong trình chỉnh sửa bên dưới.
                  sockMerchant có (các) tham số sau: int n: số lượng tất trong đống int ar[n]: màu sắc của mỗi chiếc tất
Input:
      Dòng đầu tiên chứa một số nguyên n, số lượng tất được thể hiện trong ar.
      Dòng thứ hai chứa số nguyên n được phân tách bằng dấu cách, ar[i] là màu sắc của tất trong đống.

Constraints:  1≤n≤100, 1≤ar[i]≤100
Output:       Số lượng cặp màu có kiểu dữ liệu int
"""

n = int(input())
p = [int(i) for i in input().split()]
s = 0
for i in range(1, 101):
    c = 0
    for j in p:
        if i==j:
            c += 1
    s += c//2
print(s)
