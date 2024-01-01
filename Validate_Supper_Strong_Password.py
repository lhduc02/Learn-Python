"""
Trên trang web test.vn, khi tạo tài khoản mới, một mật khẩu mạnh phải đảm bảo đầy đủ các yếu tố sau:
    Tối thiểu 8 ký tự.
    Ít nhất một ký tự latin viết thường.
    Ít nhất một ký tự latin viết hoa.
    Ít nhất một chữ số thập phân.
    Ít nhất một ký tự đặc biệt nằm trong danh sách: !@#$%^&*()_-=+/\';><,.>.
    Không có bất ký ký tự nào lặp lại 3 lần liên tiếp cạnh nhau
    Không có ký tự nào có mã Hexa nằm ngoài đoạn [0x20,0x7f] trong bảng mã ASCII.
    
Yêu cầu: Với một mật khẩu cho trước, hãy xác định xem nó có đủ mạnh hay không?

Input:        Một dòng duy nhất chứa xâu kí tự s - mật khẩu cần kiểm tra.
Constraints:  1≤∣s∣≤1000.
Output:       In ra Strong nếu s là mật khẩu mạnh, ngược lại in ra Weak.

Sample Test 1
Input:      mmm,%e54S+m
Output:     Weak

Sample Test 2
Input:      md&7DD2MT@H
Output:     Strong
"""

str = input()
a = len(str) >= 8
b, c, d, e, f, g = 0, 0, 0, 0, 1, 1
for i in str:
    if i == i.lower():
        b = 1
    if i == i.upper():
        c = 1
    if i.isnumeric():
        d = 1
    if i in "!@#$%^&*()_-=+/\';><,.>":
        e = 1
    if ord(i) not in range(32, 128):
        g = 0
 
for i in range(0, len(str)-2):
    if str[i] == str[i+1] and str[i] == str[i+2]:
        f = 0
 
if a and b and c and d and e and f and g:
    print("Strong")
else:
    print("Weak")
