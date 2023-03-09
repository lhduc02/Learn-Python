"""
An và Bình chơi 1 trò chơi như sau. An lấy ra một băng giấy gồm có 1 × n ô vuông được tô màu đen và trắng. Sau đó, Bình bắt đầu di chuyển.
Ở mỗi nước đi, Bình có thể chọn hai ô vuông cạnh nhau có cùng màu và tô màu lại tùy ý cho 2 ô này, có thể tô khác màu nhưng chỉ có thể là trắng hoặc đen.
Bình muốn tô lại sao cho không có 2 ô màu nào cạnh nhau có cùng một màu.
Hãy giúp Bình tìm số bước ít nhất để đạt được điều đó.

Input:
      Dòng đầu là số nguyên n (1 ≤ n ≤ 1000) — chiều dài của băng đấy.
      Dòng thứ hai là chuỗi n kí tự 0 và 1, là trạng thái lúc đầu của băng giấy. Trong đó: 0 là ô màu trắng, 1 là ô màu đen.
Output:
      In ra số bước ít nhất để đạt được điều đó. In ra -1 nếu không thể.
"""

n = int(input())
r = input()
r = [*r]
 
p = []
for i in range(n):
    if i%2==0:
        p.append('1')
    else:
        p.append('0')
 
q = []
for i in range(n):
    if i%2==0:
        q.append('0')
    else:
        q.append('1')
 
c1 = 0
for i in range(n):
    if r[i] != p[i]:
        c1 += 1
 
c2 = 0
for i in range(n):
    if r[i] != q[i]:
        c2 += 1
 
print(min(c1, c2))
