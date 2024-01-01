"""
Khi nói về việc “xoay phải N lần” đối với một mảng, nghĩa là ta di chuyển các phần tử của mảng sang phải N vị trí.
Cụ thể, sau mỗi lần di chuyển, phần tử cuối cùng của mảng sẽ chuyển về vị trí đầu tiên của mảng.

Ví dụ, giả sử ta có mảng [1,2,3,4,5] và muốn xoay phải 2 lần. Sau mỗi lần xoay, mảng sẽ thay đổi như sau:

Lần xoay đầu tiên:  [5,1,2,3,4]
Lần xoay thứ hai:   [4,5,1,2,3]
Yêu cầu: Cho một mảng A và một số nguyên N, hãy viết một hàm để xoay phải mảng A với N lần.

Input:          Một chuỗi chứa các phần tử của mảng Arr được ngăn cách bởi dấu ,
                Số nguyên N lần cần xoay

Constraints:    0 < Arr.length, Arr[i] ≤ 10^3
                0<N≤10^3

Output:         Chuỗi chứa các phần tử của mảng Arr (sau khi đã thực hiện N lần xoay phải) được ngăn cách bởi dấu ,

Sample Test:
Input:    1,2,3,4,5,6,7,8,9
          4
Output:   6,7,8,9,1,2,3,4,5
"""

str = input()
n = int(input())
arr = str.split(",")
n = n % len(arr)
arr1 = arr[-1*n : ] + arr[ : -1*n]
print(",".join(arr1))
