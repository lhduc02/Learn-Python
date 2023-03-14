"""
Cho một danh sách các hình chữ nhật 1, 2,…, n. Hãy tìm diện tích hình chữ nhật nhỏ nhất bao tất cả các hình chữ nhật trong danh sách trên Dữ liệu
Input:
    + Dòng 1: chứa số nguyên dương n (1 <= n <= 1000)
    + Dòng i+1 (i=1,…,n): chứa 4 số nguyên dương x1, y1, x2, y2 trong đó (x1,y1) và (x2,y2) là tọa độ 2 đỉnh đối của hình chữ nhật thứ i (1 <= x1, y1, x2, y2 <= 100)
Output:
    Ghi ra diện tích của hình chữ nhật nhỏ nhất tìm được

Example
Input:
      3
      2 4 2 7
      3 2 4 7
      1 2 5 2
Output:
      20
"""

n = int(input())
x = []
y = []
for i in range(n):
    x1, y1, x2, y2 = [int(i) for i in input().split()]
    x.append(x1)
    x.append(x2)
    y.append(y1)
    y.append(y2)
print( (max(x) - min(x)) * (max(y) - min(y)) )
