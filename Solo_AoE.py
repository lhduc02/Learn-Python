"""
Trong một buổi thi đấu giao hữu giữa 2 game thủ, Chimsedinang và Vanlove đã chơi với nhau rất nhiều “C đấu” (set game) đế chế.
Mỗi C bao gồm nhiều game đấu, mỗi game đấu chỉ có kết quả thắng thua (không có hoà),
khi người đầu tiên đạt đến số trận thắng trong C là k trận, thì C đấu kết thúc và C mới được bắt đầu.
Ví dụ, C đấu có k=3 thì C đấu sẽ kết thúc khi đạt đến một trong các tỉ số sau: 3-0, 3-1, 3-2 và ngược lại.

Sau buổi thi, Chimsedinang có tổng cộng x trận thắng, còn Vanelove có tổng cộng y trận thắng.
Bạn hãy tính thử xem có thể có tối đa bao nhiêu C đấu tất cả hay tình huống ban đầu là không thể xảy ra.

Chú ý: buổi giao hữu chỉ bao gồm nhiều C đấu đã hoàn thành.

Input
      Dòng đầu tiên là 3 số nguyên k, x, y với (1 ≤ k ≤ 10^9, 0 ≤ x,y ≤ 10^9, x+y > 0).

Output
      Nếu không thể xảy ra tình huống như đề bài, in ra -1, ngược lại, in ra số C đấu nhiều nhất có thể thoả mãn.
      
Sample Test 1
      Input:    2 3 3
      Output:   2

Sample Test 2
      Input:    123 456 789
      Output:   9
"""

k, x, y = [int(i) for i in input().split()]
x_tran = x//k
x_du = x%k
y_tran = y//k
y_du = y%k
if x_du > (k-1)*y_tran or y_du > (k-1)*x_tran:
    print(-1)
else:
    print(x_tran + y_tran)
