"""
Trong tủ của Bi có m cái bát sạch và k cái đĩa sạch.Bi đã lên kế hoạch ăn uống cho n ngày tiếp theo.
Vì Bi rất lười biếng nên anh ấy sẽ ăn đúng một món mỗi ngày. Tại thời điểm đó, để ăn một món ăn, anh ta cần đúng một đĩa hoặc bát sạch.
Ngoài ra, Bi chỉ có thể nấu hai loại món ăn: Loại 1 chỉ có thể ăn bằng bát và các món thuộc loại 2 có thể ăn bằng bát hoặc đĩa.
Khi Bi ăn xong, anh ta để lại một chiếc đĩa / bát bẩn. Dù rất lười nhưng Bi lại rất thích sạch sẽ, anh ấy không thể ăn bằng bát đĩa đã bị bẩn.
Vì vậy, thỉnh thoảng Bi vẫn cần rửa sạch đĩa / bát của mình trước khi ăn.
Yêu cầu: Tìm số lượng tối thiểu đĩa / bát Bi cần rửa, nếu Bi thực hiện một cách tối ưu.

Input:
      Dòng đầu tiên chứa 3 số n, m ,k lần lượt là số ngày, số bát sạch và số đĩa sạch mà Bi nhập vào  (1 ≤ n, m, k ≤ 1000).
      Dòng thứ hai chứa n số a1, a2, ..., an xác định xem ngày nào sẽ ăn loại nào (loại 1 và loại 2).

Output:
      In ra số lượng tối thiểu đĩa / bát Bi cần rửa.
"""

n, bat, bat_dia = [int(i) for i in input().split()]
p = input()
a = p.count('1')        # bat
b = p.count('2')        # bat_dia
c = 0
 
if bat < a:
    c += (a - bat)
 
if bat > a:
    bat_dia += (bat - a)
 
if bat_dia < b:
    c += (b - bat_dia)
print(c)
