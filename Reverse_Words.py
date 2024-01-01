"""
Xét chuỗi Hello World, chúng ta có thể đảo ngược chuỗi trên (từng ký tự, kể cả dấu cách) thành: olleH dlroW.
Cho input là một chuỗi gồm các ký tự chữ cái, chữ số và ký tự đặc biệt (bao gồm cả dấu cách).

Yêu cầu: In ra chuỗi đảo ngược của nó.

Input:          Chuỗi S.
Constraints:    S có thể chứa bất kỳ ký tự nào, bao gồm chữ cái, số, ký tự đặc biệt.
                S.length < 1500.
Output:         Chuỗi S' sau khi đảo ngược.

Sample Test
    Input:    Nguyen Van An
    Output:   neyugN naV nA
"""

str = input()
arr = str.split(" ")
arr1 = []
for i in arr:
    i = list(i)
    i.reverse()
    arr1.append("".join(i))
print(" ".join(arr1))
