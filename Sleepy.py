"""
Bình tỉnh dậy và thấy thời gian hiển thị trên đồng hồ điện tử là s. Ngoài ra, Bình còn biết mình đã ngủ được khoảng thời gian là t.
Bạn hãy giúp anh Bình viết chương trình, nhập vào s và t sau đó đưa ra thời điểm p mà Bình lên giường đi ngủ.
Chú ý là Bình có thể đi ngủ từ tối hôm qua.

Input:
      Dòng đầu tiên là s - thời gian Bình tỉnh dậy theo format hh:mm.
      Dòng thứ hai là t- khoảng thời gian mà Bình đã ngủ cũng theo format hh:mm.
      Hai thời gian này được đảm bảo là đúng, và đúng theo format 24h: 00 ≤ hh ≤ 23, 00 ≤ mm ≤ 59.

Output:
      In ra thời điểm p mà Bình bắt đầu ngủ theo format như trên.
      
Sample Test 1
Input:
      05:50
      05:44
Output:
      00:06

Sample Test 2
Input:
      00:00
      01:00
Output:
      23:00
"""

s = input()
s1 = s.split(":")
t = input()
t1 = t.split(":")
a = int(s1[0])-int(t1[0])
b = int(s1[1])-int(t1[1])
if b==0:
    if a<10 and a>=0:
        print("0{}:00".format(a))
    elif a<0 and a+24<10:
        print("0{}:00".format(a+24))
    elif a<0 and a+24>=10:
        print("{}:00".format(a+24))
    else:
        print("{}:00".format(a))
elif a==0:
    if b<0 and b+60<10:
        print("23:0{}".format(b+60))
    elif b<0 and b+60>=10:
        print("23:{}".format(b+60))
    elif b>0 and b<10:
        print("00:0{}".format(b))
    else:
        print("00:{}".format(b))
 
elif a<0 and b<0:
    if a+23<10 and b+60<10:
        print("0{}:0{}".format(a+23, b+60))
    elif a+23<10 and b+60>=10:
        print("0{}:{}".format(a+23, b+60))
    elif a+23>=10 and b+60<10:
        print("{}:0{}".format(a+23, b+60))
    else:
        print("{}:{}".format(a+23, b+60))
 
elif a<0 and b>0:
    if a+24<10 and b<10:
        print("0{}:0{}".format(a+24, b))
    elif a+24<10 and b>=10:
        print("0{}:{}".format(a+24, b))
    elif a+24>=10 and b<10:
        print("{}:0{}".format(a+24, b))
    else:
        print("{}:{}".format(a+24, b))
 
elif a>0 and b<0:
    if a<10 and b+60<10:
        print("0{}:0{}".format(a-1, b+60))
    elif a<10 and b+60>=10:
        print("0{}:{}".format(a-1, b+60))
    elif a>=10 and b+60<10:
        print("{}:0{}".format(a-1, b+60))
    else:
        print("{}:{}".format(a-1, b+60))
else:
    if a<10 and b<10:
        print("0{}:0{}".format(a, b))
    elif a<10 and b>=10:
        print("0{}:{}".format(a, b))
    elif a>=10 and b<10:
        print("{}:0{}".format(a, b))
    else:
        print("{}:{}".format(a, b))
