"""
Cho một bảng ô vuông có kích thước vô hạn.
Các dòng được đánh số từ 1 theo thứ tự từ trên xuống dưới, các cột được đánh số từ 1 theo thứ tự từ trái qua phải.
Ô vuông nằm trên giao của dòng thứ i và cột thứ j được gọi là ô (i, j), và tại ô vuông đó có ghi số nguyên i∗j.

Một con robot xuất phát tại ô (1, 1). Trong mỗi bước, con robot có thể đi đến một trong bốn ô kề cạnh với ô robot đang đứng.
Robot không được phép đi ra ngoài bảng ô vuông.

Hãy cho biết số bước ít nhất để robot đi đến một ô vuông bất kì được ghi số nguyên N.

Input:  Gồm một số nguyên N (1 ≤ N ≤ 10^12)

Output: In ra một số nguyên duy nhất là số bước ít nhất cần tìm.
Subtasks:
    Subtask 1 (50% số test): N ≤ 10^6
    Subtask 2 (50% số test): Không có ràng buộc gì thêm

Sample Test
    Input:  180
    Output: 25
"""

import math
n = int(input())
for i in range(math.ceil(math.sqrt(n))+1, -1, -1):
    if n%i==0:
        a = i+n//i-2
        print(a)
        break
