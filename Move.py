"""
Ngôi làng sinh viên của Bảo có n nhà trọ xếp thành hàng ngang được đánh số từ 1 tới n theo thứ tự từ trái qua phải.
Mỗi nhà trọ có sức chứa vô hạn người. Nhà trọ thứ i hiện đang chứa ai sinh viên.
Do tình hình dịch bệnh diễn biến phức tạp, chính phủ ra chỉ thị rằng hai ngôi nhà liên tiếp không được có tổng cộng quá d người.
Vì vậy, các bạn sinh viên phải sắp xếp lại chỗ ở để phòng chống lây lan dịch bệnh.
Bảo có thể yêu cầu mỗi bạn sinh viên di chuyển từ ngôi nhà ban đầu tới một ngôi nhà khác trong n − 1 ngôi nhà còn lại.
Tuy nhiên Bảo chỉ có thể đặt ra yêu cầu với mỗi bạn sinh viên không quá một lần mà thôi.
Lưu ý rằng sau khi thực hiện các yêu cầu chuyển nhà, một số ngôi nhà có thể bị bỏ trống không có ai ở.

Hãy giúp Bảo kiểm tra xem liệu có cách nào để tái phân bố chỗ ở cho các bạn sinh viên thoả mãn yêu cầu của chính phủ đưa ra hay không.

Input
      Dòng đầu tiên chứa số nguyên dương q — số truy vấn    (1 ≤ q ≤ 50)
      Trong mỗi truy vấn, dòng đầu tiên chứa hai số nguyên dương n,d    (2 ≤ n ≤ 10^3, 1 ≤ d ≤ 10^9)
      Dòng thứ hai chứa n số nguyên dương a1, a2, ..., an   (1 ≤ ai ≤ 100)
Output
      Với mỗi truy vấn, in kết quả trên một dòng riêng biệt:
      Nếu Bảo có thể tìm cách sắp xếp để thoả mãn yêu cầu của chính phủ, in ra YES, ngược lại in ra NO.

Sample Test
      Input
      4
      4 6
      3 6 1 2
      3 4
      1 2 3
      2 10
      6 9
      2 69
      6 9

      Output
      YES
      YES
      NO
      YES
"""

def move(n, d, p):
    if (n+1)//2*d>=sum(p):
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    n, d = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    print(move(n, d, p))
