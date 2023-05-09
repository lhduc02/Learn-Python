"""
Có một chú thỏ tên là Freke rất thích ăn cà rốt. Chú thường hay đến trộm cà rốt ở một mảnh vườn, nhưng sau nhiều lần ăn trộm, chủ của mảnh vườn đó đã lắp đặt những con robot để bảo vệ khu vườn. Hãy giúp Freke lấy cà rốt một cách an toàn nhé.

Input
Mảng 2 chiều M hàng N cột:
  + Ô có giá trị 1: có robot tuần tra.
  + Ô có giá trị 0: không có robot tuần tra.

Output:
Số cà rốt có thể trộm. Biết những hàng và cột có robot tuần tra thì không thể trộm (tầm hoạt động của robot là hàng và cột mà nó đứng).

Sample Test
Input:
      3 5
      1 0 0 0 0
      0 0 1 0 0
      0 0 0 0 0

Output:
      3
"""

r, c = [int(i) for i in input().split()]
mt = []
for i in range(r):
    lst = [int(i) for i in input().split()]
    mt.append(lst)

#matrix = mt.copy()
row = []
column = []
for i in range(r):
    for j in range(c):
        if mt[i][j] == 1:
            row.append(i)
            column.append(j)
a = len(set(column))
b = len(set(row))
print(r*c-a*r-b*c+a*b)
