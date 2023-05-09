"""
Input: Một dòng duy nhất là một số tự nhiên x biết (0≤x≤10).
Output: Một dòng duy nhất chứa kết quả bài toán theo định dạng chuỗi sau: {y} year(s), {d} day(s), {h} hour(s), {m} minutes and {s} sencond(s)

Trong đó:
    + {y} là số năm, {d} là số ngày, {h} là số giờ, {m} là số phút và {s} là số giây.
    + Nếu cô ấy đưa số 0 thì in ra “now”.
    + Một đơn vị thời gian sẽ không xuất hiện trong chuỗi nếu giá trị của nó bằng 0.
      Ví dụ “1 minute and 0 second” sẽ là không hợp lệ phải là “1 minute”.
      Nếu có 2 đơn vị trở lên thì 2 đơn vị cuối phải được nối bằng từ “and”, còn lại phân cách bằng dấu ‘,’ như đúng mẫu trên.
    + Thời gian trả về tối ưu.
      Ví dụ không trả về “61 seconds” mà là “1 minute and 1 second”.
    + Coi 1 năm có 12 tháng các tháng có thể có 28,29,30,31 ngày, tổng 1 năm có 365 ngày.
"""

n = int(input())
time0 = n
time = [0, 0, 0, 0, 0] #y, d, h, m, s
time[0] = n//31536000
n = n%31536000
time[1] = n//86400
n = n%86400
time[2] = n//3600
n = n%3600
time[3] = n//60
n = n%60
time[4] = n


dem_gio = []

if time[0] != 0:
    if time[0] == 1:
        dem_gio.append((str(time[0]) + ' year'))
    else:
        dem_gio.append((str(time[0]) + ' years'))

if time[1] != 0:
    if time[1] == 1:
        dem_gio.append((str(time[1]) + ' day'))
    else:
        dem_gio.append((str(time[1]) + ' days'))

if time[2] != 0:
    if time[2] == 1:
        dem_gio.append((str(time[2]) + ' hour'))
    else:
        dem_gio.append((str(time[2]) + ' hours'))

if time[3] != 0: 
    if time[3] == 1:
        dem_gio.append((str(time[3]) + ' minute'))
    else:
        dem_gio.append((str(time[3]) + ' minutes'))

if time[4] != 0:
    if time[4] == 1:
        dem_gio.append((str(time[4]) + ' second'))
    else:
        dem_gio.append((str(time[4]) + ' seconds'))


if time0==0:
    print("now")

elif len(dem_gio) == 1:
    print(dem_gio[0])

elif len(dem_gio) == 2:
    print(" and ".join(dem_gio))

else:
    print(", ".join(dem_gio[:-1]) + " and " + dem_gio[-1])
