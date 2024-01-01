"""
Trong chuỗi ký tự, "tiền tố chung" là một chuỗi con mà tất cả các xâu trong một tập hợp cho trước đều bắt đầu bằng nó.
Nói cách khác, đây là một chuỗi các ký tự ở đầu mỗi xâu trong tập hợp mà mỗi xâu trong tập hợp đều có.

Yêu cầu: Cho một mảng các xâu ký tự, hãy viết một hàm để tìm và trả về tiền tố chung dài nhất của các xâu trong mảng

Ví dụ:
strs = ['flower', 'flow', 'flight'] ==> tiền tố chung dài nhất 'fl'
strs = ['age', 'agent, 'apple'] ==> tiền tố chung dài nhất 'a'
strs = ['flower', 'fake', 'cat'] ==> không có tiền tố chung

Input:   chuỗi chứa N xâu chỉ chứa ký tự in thường ngăn cách bởi dấu ,
Constraints:
    0≤N≤10^3
    0≤N[i]≤100
 
Output:  Một chuỗi ký tự, là tiền tố chung dài nhất của các xâu trong mảng
         Nếu không có tiền tố chung, trả về một chuỗi trống
"""

str = input()
arr = str.split(",")
 
tien_to = ""
for i in range(len(arr[0])):
    xet = 1
    for index_arr in range(1, len(arr)):
        if arr[0][i] != arr[index_arr][i]:
            xet = 0
    if xet == 1:
        tien_to += arr[0][i]
    else:
        break
if tien_to == "":
    print("nothing")
else:
    print(tien_to)
