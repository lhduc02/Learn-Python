"""
Bob chơi game rất nhiều. Mẹ bắt Bob phải giảm đi d phút chơi game mỗi ngày, thực hiện trong n ngày liên tiếp (coi như ngày đầu tiên vẫn chưa giảm). 
Bob đã thực hiện thành công quy trình trên và sau n ngày thực hiện, tổng thời gian chơi game của Bob chỉ là s phút
Yêu cầu: Hãy tìm thời gian chơi game của Bob ở ngày cuối cùng và ngày đầu tiên trong chuỗi n ngày thực hiện bỏ game?

Input:
      + Dòng đầu tiên ghi số nguyên dương n.
      + Dòng thứ hai ghi một chuỗi dạng hh:mm - tổng số giờ và số phút Bob chơi game trong n ngày.
      + Dòng thứ ba ghi một một chuỗi dạng hh:mm - thời gian d mà Bob giảm chơi game đi mỗi ngày.

Constrains:
      +  1 <= n <= 30
      + Tổng thời gian Bob chơi game không vượt quá ×n×24 giờ.
      + Tổng thời gian Bob giảm chơi game đi trong ngày không vượt quá 24 giờ.

Output:
      Trên hai dòng khác nhau, mỗi dòng đưa ra một chuỗi dạng hh:mm là tổng số giờ và số phút chơi game trong ngày cuối cùng
      và ngày đầu tiên của chuỗi n ngày Bob thực hiện bỏ game.

Sample Test
Input:
      7 
      01:59 
      00:04

Output:
      00:05
      00:29
"""

n = int(input())
s = str(input())
s = s.split(":")
s = 60*int(s[0])+int(s[1])
d = input()
d = d.split(":")
d = 60*int(d[0])+int(d[1])
 
u1 = int(s/n+(n-1)*d/2)
un = u1-(n-1)*d
 
a=un//60
b=un%60
if a<=9 and b<=9:
    print("0{}:0{}".format(a, b))
elif a>9 and b<=9:
    print("{}:0{}".format(a, b))
elif a<=9 and b>9:
    print("0{}:{}".format(a, b))
elif a>9 and b>9:
    print("{}:{}".format(a, b))
 
a=u1//60
b=u1%60
if a<=9 and b<=9:
    print("0{}:0{}".format(a, b))
elif a>9 and b<=9:
    print("{}:0{}".format(a, b))
elif a<=9 and b>9:
    print("0{}:{}".format(a, b))
elif a>9 and b>9:
    print("{}:{}".format(a, b))
